#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
# @Time    : 2024/2/23
# @Author  : yanxiaodong
# @File    : transform_component.py
"""
import os
import json
from argparse import ArgumentParser
import base64

import bcelogger
from gaea_tracker import ExperimentTracker
from bcelogger.base_logger import setup_logger
from windmillmodelv1.client.model_api_model import parse_model_name
from windmillclient.client.windmill_client import WindmillClient
from gaea_operator.transform import Transform

from gaea_operator.config import Config
from gaea_operator.utils import write_file, read_file, ModelTemplate, get_accelerator, is_base64
from gaea_operator.config.generate_transform_config import KEY_ACCELERATOR


def parse_args():
    """
    Parse arguments.
    """
    parser = ArgumentParser()
    parser.add_argument("--windmill-ak", type=str, default=os.environ.get("WINDMILL_AK"))
    parser.add_argument("--windmill-sk", type=str, default=os.environ.get("WINDMILL_SK"))
    parser.add_argument("--windmill-endpoint", type=str, default=os.environ.get("WINDMILL_ENDPOINT"))
    parser.add_argument("--project-name", type=str, default=os.environ.get("PROJECT_NAME"))
    parser.add_argument("--scene", type=str, default=os.environ.get("SCENE"))
    parser.add_argument("--public-model-store",
                        type=str,
                        default=os.environ.get("PUBLIC_MODEL_STORE", "workspaces/public/modelstores/default"))
    parser.add_argument("--tracking-uri", type=str, default=os.environ.get("TRACKING_URI"))
    parser.add_argument("--experiment-name", type=str, default=os.environ.get("EXPERIMENT_NAME"))
    parser.add_argument("--experiment-kind", type=str, default=os.environ.get("EXPERIMENT_KIND"))
    parser.add_argument("--train-model-name",
                        type=str,
                        default=os.environ.get("TRAIN_MODEL_NAME"))
    parser.add_argument("--transform-model-name",
                        type=str,
                        default=os.environ.get("TRANSFORM_MODEL_NAME"))
    parser.add_argument("--transform-model-display-name",
                        type=str,
                        default=os.environ.get("TRANSFORM_MODEL_DISPLAY_NAME"))
    parser.add_argument("--accelerator", type=str, default=os.environ.get("ACCELERATOR", "t4"))
    parser.add_argument("--advanced-parameters",
                        type=str,
                        default=os.environ.get("ADVANCED_PARAMETERS", "{}"))
    parser.add_argument("--category", type=str, default=os.environ.get("CATEGORY", "Image/ObjectDetection"))
    parser.add_argument("--algorithm", type=str, default=os.environ.get("ALGORITHM", ModelTemplate.PPYOLOE_PLUS_NAME))

    parser.add_argument("--input-model-uri", type=str, default=os.environ.get("INPUT_MODEL_URI"))
    parser.add_argument("--output-model-uri", type=str, default=os.environ.get("OUTPUT_MODEL_URI"))
    parser.add_argument("--output-uri", type=str, default=os.environ.get("OUTPUT_URI"))

    args, _ = parser.parse_known_args()

    return args


def transform(args):
    """
    Transform component for model.
    """
    windmill_client = WindmillClient(ak=args.windmill_ak,
                                     sk=args.windmill_sk,
                                     endpoint=args.windmill_endpoint)
    tracker_client = ExperimentTracker(windmill_client=windmill_client,
                                       tracking_uri=args.tracking_uri,
                                       experiment_name=args.experiment_name,
                                       experiment_kind=args.experiment_kind,
                                       project_name=args.project_name)
    setup_logger(config=dict(file_name=os.path.join(args.output_uri, "worker.log")))

    if args.input_model_uri is not None and len(args.input_model_uri) > 0:
        bcelogger.info(f"Model artifact input uri is {args.input_model_uri}")
        response = read_file(input_dir=args.input_model_uri)
    else:
        args.input_model_uri = "/home/windmill/tmp/model"
        bcelogger.info(f"Model artifact name is {args.train_model_name}")
        assert args.train_model_name is not None and len(args.train_model_name) > 0, "Model artifact name is None"
        response = windmill_client.get_artifact(name=args.train_model_name)
        response = json.loads(response.raw_data)
        windmill_client.download_artifact(object_name=response["objectName"],
                                          version=str(response["version"]),
                                          output_uri=args.input_model_uri)
    bcelogger.info(f"Model artifact is {response}")
    metadata = response["metadata"]

    # 1. 生成转换配置文件，固定名称 transform_config.yaml 保存在 output_model_uri
    if is_base64(args.advanced_parameters):
        transform_advanced_parameters = json.loads(base64.b64decode(args.advanced_parameters))
    else:
        transform_advanced_parameters = json.loads(args.advanced_parameters)
    transform_advanced_parameters.update({KEY_ACCELERATOR: args.accelerator})
    config = Config(windmill_client=windmill_client, tracker_client=tracker_client, metadata=metadata)
    config.write_transform_config(model_uri=args.output_model_uri, advanced_parameters=transform_advanced_parameters)

    # 2. 下载模板模型
    model_template = ModelTemplate(windmill_client=windmill_client,
                                   scene=args.scene,
                                   accelerator=args.accelerator,
                                   model_store_name=args.public_model_store,
                                   algorithm=args.algorithm)
    model = model_template.suggest_template_model()
    windmill_client.download_artifact(object_name=model, version="latest", output_uri=args.output_model_uri)

    # 3. 修改config.pbtxt配置文件
    config.write_model_config(transform_model_uri=args.output_model_uri)

    # 4. 转换
    Transform(windmill_client=windmill_client).transform(transform_config_dir=args.output_model_uri,
                                                         src_model_uri=args.input_model_uri,
                                                         dst_model_uri=args.output_model_uri)

    # 5. 上传转换后的模型
    accelerator = get_accelerator(name=args.accelerator)
    model_name_instance = parse_model_name(name=args.transform_model_name)
    workspace_id = model_name_instance.workspace_id
    model_store_name = model_name_instance.model_store_name
    local_name = model_name_instance.local_name
    response = windmill_client.create_model(
        artifact_uri=args.output_model_uri,
        workspace_id=workspace_id,
        model_store_name=model_store_name,
        local_name=local_name,
        display_name=args.transform_model_display_name,
        prefer_model_server_parameters=accelerator.suggest_model_server_parameters(),
        category=args.category,
        artifact_metadata=config.metadata,
        model_formats=[
            Config.accelerator2model_format[args.accelerator]])
    bcelogger.info(f"Model {args.transform_model_name} created response: {response}")

    # 6. 输出文件
    write_file(obj=json.loads(response.raw_data)["artifact"], output_dir=args.output_model_uri)


if __name__ == "__main__":
    args = parse_args()
    transform(args=args)
