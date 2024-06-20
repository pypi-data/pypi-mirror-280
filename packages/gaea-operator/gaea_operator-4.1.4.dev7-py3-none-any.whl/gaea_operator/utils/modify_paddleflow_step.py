#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
# @Time    : 2024/6/19
# @Author  : yanxiaodong
# @File    : modify_paddleflow_step.py
"""
from typing import Dict, Type
from paddleflow.pipeline import ContainerStep
from pydantic import BaseModel


def modify_paddleflow_step(skip: int,
                           skip_name: str,
                           step: ContainerStep,
                           input: BaseModel,
                           input_spec: Type[BaseModel],
                           name_to_step: Dict[str, ContainerStep]):
    """
    modify paddleflow step
    """
    if skip > 0:
        step.condition = f"{step.parameters[skip_name]} < 0"
    if isinstance(input, input_spec):
        for attr, _ in input.dict().items():
            variable = getattr(input, attr)
            if variable.value != "":
                name, value = variable.value.split(".")
                step.inputs[variable.name] = getattr(name_to_step[name], "outputs")[value]
            else:
                step.parameters[variable.name] = ""
    else:
        for attr, _ in input_spec().dict().items():
            variable = getattr(input_spec(), attr)
            step.parameters[variable.name] = ""