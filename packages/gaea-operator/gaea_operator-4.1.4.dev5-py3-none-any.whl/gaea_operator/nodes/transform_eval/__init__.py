#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
# @Time    : 2024/3/21
# @Author  : yanxiaodong
# @File    : __init__.py.py
"""
from paddleflow.pipeline import ContainerStep
from paddleflow.pipeline import Artifact

from .types import TransformEvalInput
from gaea_operator.utils import get_accelerator, modify_paddleflow_step


def transform_eval(transform_eval_skip: int = -1,
                   transform_eval_input: TransformEvalInput = None,
                   name_to_step: dict = None,
                   algorithm: str = "",
                   accelerator: str = "",
                   base_params: dict = None,
                   base_env: dict = None,
                   dataset_name: str = "",
                   transform_model_name: str = ""):
    """
    Transform eval step
    """
    transform_eval_params = {"transform_eval_skip": transform_eval_skip,
                             "accelerator": accelerator,
                             "dataset_name": dataset_name,
                             "model_name": transform_model_name,
                             "advanced_parameters": '{"conf_threshold":"0.5",'
                                                    '"iou_threshold":"0.5"}'}
    transform_eval_env = {"ACCELERATOR": "{{accelerator}}",
                          "DATASET_NAME": "{{dataset_name}}",
                          "MODEL_NAME": "{{model_name}}",
                          "ADVANCED_PARAMETERS": "{{advanced_parameters}}"}
    transform_eval_params.update(base_params)
    transform_eval_env.update(base_env)
    accelerator = get_accelerator(name=accelerator)
    # 增加set image接口，不在依赖streamlit获取推理镜像
    name_to_image = {accelerator.T4: "iregistry.baidu-int.com/windmill-public/inference/nvidia:v4.1.4-dev31",
                     accelerator.V100: "iregistry.baidu-int.com/windmill-public/inference/nvidia:v4.1.4-dev31",
                     accelerator.A100: "iregistry.baidu-int.com/windmill-public/inference/nvidia:v4.1.4-dev31",
                     accelerator.A10: "iregistry.baidu-int.com/windmill-public/inference/nvidia:v4.1.4-dev31",
                     accelerator.R200: "iregistry.baidu-int.com/windmill-public/inference/kunlun:v4.1.4-dev31"}
    accelerator.set_image(name_to_image=name_to_image)
    transform_eval_env.update(accelerator.suggest_env())

    transform_eval = ContainerStep(name="transform-eval",
                                   docker_env=accelerator.suggest_image(),
                                   env=transform_eval_env,
                                   parameters=transform_eval_params,
                                   outputs={"output_uri": Artifact(), "output_dataset_uri": Artifact()},
                                   command=f'python3 -m gaea_operator.components.transform_eval.transform_eval '
                                           f'--algorithm={algorithm} '
                                           f'--input-model-uri={{{{input_model_uri}}}} '
                                           f'--input-dataset-uri={{{{input_dataset_uri}}}} '
                                           f'--output-dataset-uri={{{{output_dataset_uri}}}} '
                                           f'--output-uri={{{{output_uri}}}}')
    modify_paddleflow_step(skip=transform_eval_skip,
                           step=transform_eval,
                           input=transform_eval_input,
                           input_spec=TransformEvalInput,
                           name_to_step=name_to_step)

    return transform_eval
