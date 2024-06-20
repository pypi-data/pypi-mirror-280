#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
# @Time    : 2024/6/3
# @Author  : yanxiaodong
# @File    : intput_output.py
"""
from pydantic import BaseModel

from gaea_operator.artifacts import Variable


class TransformEvalInput(BaseModel):
    """
    Transform eval input
    """
    model: Variable = Variable(type="model", name="input_model_uri", value="transform.output_model_uri")
    dataset: Variable = Variable(type="dataset", name="input_dataset_uri", value="eval.output_dataset_uri")


class TransformEvalOutput(BaseModel):
    """
    Transform eval output
    """
    dataset: Variable = Variable(type="dataset",
                                 name="output_dataset_uri",
                                 displayName="模型转换评估的数据",
                                 value="transform-eval.output_dataset_uri", )
