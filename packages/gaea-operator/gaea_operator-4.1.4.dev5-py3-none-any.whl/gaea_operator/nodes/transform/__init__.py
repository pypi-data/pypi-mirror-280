#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
# @Time    : 2024/3/12
# @Author  : yanxiaodong
# @File    : __init__.py.py
"""
from paddleflow.pipeline import ContainerStep
from paddleflow.pipeline import Artifact

from .types import TransformInput
from gaea_operator.utils import modify_paddleflow_step


def transform(transform_skip: int = -1,
              transform_input: TransformInput = None,
              name_to_step: dict = None,
              algorithm: str = "",
              category: str = "",
              accelerator: str = "",
              base_params: dict = None,
              base_env: dict = None,
              train_model_name: str = "",
              transform_model_name: str = "",
              transform_model_display_name: str = "",
              advanced_parameters: str = ""):
    """
    Transform step
    """
    transform_params = {"transform_skip": transform_skip,
                        "train_model_name": train_model_name,
                        "transform_model_name": transform_model_name,
                        "transform_model_display_name": transform_model_display_name,
                        "accelerator": accelerator,
                        "advanced_parameters": advanced_parameters}
    transform_env = {"TRAIN_MODEL_NAME": "{{train_model_name}}",
                     "TRANSFORM_MODEL_NAME": "{{transform_model_name}}",
                     "TRANSFORM_MODEL_DISPLAY_NAME": "{{transform_model_display_name}}",
                     "ACCELERATOR": "{{accelerator}}",
                     "ADVANCED_PARAMETERS": "{{advanced_parameters}}"}
    transform_env.update(base_env)
    transform_params.update(base_params)

    transform = ContainerStep(name="transform",
                              docker_env="iregistry.baidu-int.com/windmill-public/transform:v4.1.4-dev31",
                              env=transform_env,
                              parameters=transform_params,
                              outputs={"output_model_uri": Artifact(), "output_uri": Artifact()},
                              command=f'python3 -m gaea_operator.components.transform.transform '
                                      f'--algorithm={algorithm} '
                                      f'--category={category} '
                                      f'--input-model-uri={{{{input_model_uri}}}} '
                                      f'--output-uri={{{{output_uri}}}} '
                                      f'--output-model-uri={{{{output_model_uri}}}}')
    modify_paddleflow_step(skip=transform_skip,
                           step=transform,
                           input=transform_input,
                           input_spec=TransformInput,
                           name_to_step=name_to_step)

    return transform
