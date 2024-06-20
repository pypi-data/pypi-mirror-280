#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
# @Time    : 2024/6/3
# @Author  : yanxiaodong
# @File    : intput_output.py
"""
from pydantic import BaseModel

from gaea_operator.artifacts import Variable


class PackageInput(BaseModel):
    """
    Transform eval input
    """
    model: Variable = Variable(type="model", name="input_model_uri", value="transform.output_model_uri")


class PackageOutput(BaseModel):
    """
    Transform eval output
    """
    model: Variable = Variable(type="model",
                               name="output_model_uri",
                               displayName="模型组装后的模型",
                               value="package.output_model_uri")
