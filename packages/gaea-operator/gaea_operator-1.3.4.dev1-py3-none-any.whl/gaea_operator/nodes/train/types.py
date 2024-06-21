#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
# @Time    : 2024/6/3
# @Author  : yanxiaodong
# @File    : input_output.py
"""
from pydantic import BaseModel

from gaea_operator.artifacts import Variable


class TrainOutput(BaseModel):
    """
    Train output
    """
    model: Variable = Variable(type="model",
                               name="output_model_uri",
                               displayName="模型训练后的模型",
                               value="train.output_model_uri")
