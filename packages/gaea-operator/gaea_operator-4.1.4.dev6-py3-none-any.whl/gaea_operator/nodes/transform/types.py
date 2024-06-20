#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
# @Time    : 2024/6/3
# @Author  : yanxiaodong
# @File    : intput_output.py
"""
from pydantic import BaseModel

from gaea_operator.artifacts import Variable


class TransformInput(BaseModel):
    """
    Transform input
    """
    model: Variable = Variable(type="model", name="input_model_uri", value="train.output_model_uri")


class TransformOutput(BaseModel):
    """
    Transform output
    """
    model: Variable = Variable(type="model",
                               name="output_model_uri",
                               displayName="模型转换后的模型",
                               value="transform.output_model_uri")
