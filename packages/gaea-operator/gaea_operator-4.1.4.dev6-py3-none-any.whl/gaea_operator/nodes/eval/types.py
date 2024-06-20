#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
# @Time    : 2024/6/3
# @Author  : yanxiaodong
# @File    : intput_output.py
"""
from pydantic import BaseModel

from gaea_operator.artifacts import Variable


class EvalInput(BaseModel):
    """
    Eval input
    """
    model: Variable = Variable(type="model", name="input_model_uri", value="train.output_model_uri")


class EvalOutput(BaseModel):
    """
    Eval output
    """
    dataset: Variable = Variable(type="dataset",
                                 name="output_dataset_uri",
                                 displayName="模型评估的数据集",
                                 value="eval.output_dataset_uri")
    model: Variable = Variable(type="model",
                               name="output_model_uri",
                               displayName="模型评估后的模型",
                               value="eval.output_model_uri")
