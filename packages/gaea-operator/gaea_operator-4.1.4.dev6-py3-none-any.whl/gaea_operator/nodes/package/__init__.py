#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
# @Time    : 2024/3/21
# @Author  : yanxiaodong
# @File    : __init__.py.py
"""
from paddleflow.pipeline import ContainerStep
from paddleflow.pipeline import Artifact

from .types import PackageInput
from gaea_operator.utils import get_accelerator, modify_paddleflow_step


def package(package_skip: int = -1,
            package_input: PackageInput = None,
            name_to_step: dict = None,
            algorithm: str = "",
            accelerator: str = "",
            base_params: dict = None,
            base_env: dict = None,
            transform_model_name: str = "",
            ensemble_model_name: str = "",
            sub_extra_models: str = "",
            ensemble_model_display_name: str = ""):
    """
    Package step
    """
    package_params = {"package_skip": package_skip,
                      "accelerator": accelerator,
                      "transform_model_name": transform_model_name,
                      "ensemble_model_name": ensemble_model_name,
                      "sub_extra_models": sub_extra_models,
                      "ensemble_model_display_name": ensemble_model_display_name}
    package_env = {"ACCELERATOR": "{{accelerator}}",
                   "TRANSFORM_MODEL_NAME": "{{transform_model_name}}",
                   "ENSEMBLE_MODEL_NAME": "{{ensemble_model_name}}",
                   "SUB_EXTRA_MODELS": "{{sub_extra_models}}",
                   "ENSEMBLE_MODEL_DISPLAY_NAME": "{{ensemble_model_display_name}}"}
    package_params.update(base_params)
    package_env.update(base_env)
    accelerator = get_accelerator(name=accelerator)
    # 增加set image接口，不在依赖streamlit获取推理镜像
    name_to_image = {accelerator.T4: "iregistry.baidu-int.com/windmill-public/inference/nvidia:v4.1.4-dev31",
                     accelerator.V100: "iregistry.baidu-int.com/windmill-public/inference/nvidia:v4.1.4-dev31",
                     accelerator.A100: "iregistry.baidu-int.com/windmill-public/inference/nvidia:v4.1.4-dev31",
                     accelerator.A10: "iregistry.baidu-int.com/windmill-public/inference/nvidia:v4.1.4-dev31",
                     accelerator.R200: "iregistry.baidu-int.com/windmill-public/inference/kunlun:v4.1.4-dev31"}
    accelerator.set_image(name_to_image=name_to_image)

    package = ContainerStep(name="package",
                            docker_env=accelerator.suggest_image(),
                            env=package_env,
                            parameters=package_params,
                            outputs={"output_model_uri": Artifact(), "output_uri": Artifact()},
                            command=f'python3 -m gaea_operator.nodes.package.package '
                                    f'--algorithm={algorithm} '
                                    f'--input-model-uri={{{{input_model_uri}}}} '
                                    f'--output-uri={{{{output_uri}}}} '
                                    f'--output-model-uri={{{{output_model_uri}}}}')
    modify_paddleflow_step(skip=package_skip,
                           step=package,
                           input=package_input,
                           input_spec=PackageInput,
                           name_to_step=name_to_step)

    return package
