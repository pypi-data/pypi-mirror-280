#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
# @Time    : 2024/3/21
# @Author  : yanxiaodong
# @File    : __init__.py.py
"""
from paddleflow.pipeline import ContainerStep
from paddleflow.pipeline import Artifact

from .types import InferenceInput
from gaea_operator.utils import get_accelerator, modify_paddleflow_step


def inference(inference_skip: int = -1,
              inference_input: InferenceInput = None,
              name_to_step: dict = None,
              accelerator: str = "",
              base_params: dict = None,
              base_env: dict = None,
              ensemble_model_name: str = "",
              dataset_name: str = ""):
    """
    Inference step
    """
    inference_params = {"inference_skip": inference_skip,
                        "accelerator": accelerator,
                        "model_name": ensemble_model_name,
                        "dataset_name": dataset_name,
                        "advanced_parameters": '{"conf_threshold":"0.5"}'}
    inference_env = {"ACCELERATOR": "{{accelerator}}",
                     "MODEL_NAME": "{{model_name}}",
                     "DATASET_NAME": "{{dataset_name}}",
                     "ADVANCED_PARAMETERS": "{{advanced_parameters}}"}
    inference_params.update(base_params)
    inference_env.update(base_env)
    accelerator = get_accelerator(name=accelerator)
    # 增加set image接口，不在依赖streamlit获取推理镜像
    name_to_image = {accelerator.T4: "iregistry.baidu-int.com/windmill-public/inference/nvidia:v4.1.4-dev31",
                     accelerator.V100: "iregistry.baidu-int.com/windmill-public/inference/nvidia:v4.1.4-dev31",
                     accelerator.A100: "iregistry.baidu-int.com/windmill-public/inference/nvidia:v4.1.4-dev31",
                     accelerator.A10: "iregistry.baidu-int.com/windmill-public/inference/nvidia:v4.1.4-dev31",
                     accelerator.R200: "iregistry.baidu-int.com/windmill-public/inference/kunlun:v4.1.4-dev31"}
    accelerator.set_image(name_to_image=name_to_image)
    inference_env.update(accelerator.suggest_env())

    inference = ContainerStep(name="inference",
                              docker_env=accelerator.suggest_image(),
                              env=inference_env,
                              parameters=inference_params,
                              outputs={"output_uri": Artifact()},
                              command=f'python3 -m gaea_operator.nodes.inference.ppyoloe_plus '
                                      f'--input-model-uri={{{{input_model_uri}}}} '
                                      f'--input-dataset-uri={{{{input_dataset_uri}}}} '
                                      f'--output-uri={{{{output_uri}}}}')
    modify_paddleflow_step(skip=inference_skip,
                           step=inference,
                           input=inference_input,
                           input_spec=InferenceInput,
                           name_to_step=name_to_step)

    return inference
