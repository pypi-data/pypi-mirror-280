#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
# @Time    : 2024/2/23
# @Author  : yanxiaodong
# @File    : eval_component.py
"""
import os
from argparse import ArgumentParser
import json

import bcelogger
from gaea_tracker import ExperimentTracker
from bcelogger.base_logger import setup_logger
from windmilltrainingv1.client.training_api_job import parse_job_name
from windmillclient.client.windmill_client import WindmillClient

from gaea_operator.dataset import CocoDataset
from gaea_operator.trainer import Trainer
from gaea_operator.metric import update_metric_file
from gaea_operator.utils import read_file, write_file
from gaea_operator.config import PPYOLOEPLUSMConfig


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
    parser.add_argument("--tracking-uri", type=str, default=os.environ.get("TRACKING_URI"))
    parser.add_argument("--experiment-name", type=str, default=os.environ.get("EXPERIMENT_NAME"))
    parser.add_argument("--experiment-kind", type=str, default=os.environ.get("EXPERIMENT_KIND"))
    parser.add_argument("--dataset-name", type=str, default=os.environ.get("DATASET_NAME"))
    parser.add_argument("--model-name", type=str, default=os.environ.get("MODEL_NAME"))
    parser.add_argument("--advanced-parameters",
                        type=str,
                        default=os.environ.get("ADVANCED_PARAMETERS", "{}"))

    parser.add_argument("--input-model-uri", type=str, default=os.environ.get("INPUT_MODEL_URI"))
    parser.add_argument("--output-dataset-uri", type=str, default=os.environ.get("OUTPUT_DATASET_URI"))
    parser.add_argument("--output-model-uri", type=str, default=os.environ.get("OUTPUT_MODEL_URI"))
    parser.add_argument("--output-uri", type=str, default=os.environ.get("OUTPUT_URI"))

    args, _ = parser.parse_known_args()

    return args


def ppyoloe_plus_eval(args):
    """
    Eval component for ppyoloe_plus_m model.
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
        bcelogger.info(f"Model artifact name is {args.model_name}")
        assert args.model_name is not None and len(args.model_name) > 0, "Model artifact name is None"
        response = windmill_client.get_artifact(name=args.model_name)
        response = json.loads(response.raw_data)
    bcelogger.info(f"Model artifact is {response}")

    coco_dataset = CocoDataset(windmill_client=windmill_client, work_dir=tracker_client.work_dir)
    # 1. 合并分片数据集
    coco_dataset.concat_dataset(dataset_name=args.dataset_name,
                                output_dir=args.output_dataset_uri,
                                usage=CocoDataset.usages[1])

    # 2. 下载模型文件
    windmill_client.download_artifact(object_name=response["objectName"],
                                      version=str(response["version"]),
                                      output_uri=args.output_model_uri)
    write_file(obj=response, output_dir=args.output_model_uri)

    # 3. 生成评估配置文件
    PPYOLOEPLUSMConfig(windmill_client=windmill_client, tracker_client=tracker_client).write_eval_config(
        dataset_uri=args.output_dataset_uri,
        model_uri=args.output_model_uri)

    # 4. 评估
    trainer = Trainer(framework="PaddlePaddle", tracker_client=tracker_client)
    trainer.track_train_log(output_uri=args.output_uri)
    trainer.launch()

    # 5. 更新指标文件
    update_metric_file(windmill_client=windmill_client,
                       tracker_client=tracker_client,
                       dataset_name=args.dataset_name,
                       model_object_name=response["objectName"],
                       model_artifact_name=response["name"])

    # 6. 更新job tags
    tags = {"artifactName": response["name"], "datasetName": args.dataset_name}
    job_name = parse_job_name(tracker_client.job_name)
    workspace_id, project_name, local_name = job_name.workspace_id, job_name.project_name, job_name.local_name
    windmill_client.update_job(workspace_id=workspace_id, project_name=project_name, local_name=local_name, tags=tags)


if __name__ == "__main__":
    args = parse_args()
    ppyoloe_plus_eval(args=args)
