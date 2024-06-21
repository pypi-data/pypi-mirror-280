#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
# @Time    : 2024/6/3
# @Author  : yanxiaodong
# @File    : intput_output.py
"""
from pydantic import BaseModel

from gaea_operator.artifacts import Variable


class InferenceInput(BaseModel):
    """
    Transform eval input
    """
    model: Variable = Variable(type="model", name="input_model_uri", value="package.output_model_uri")
    dataset: Variable = Variable(type="dataset", name="input_dataset_uri", value="eval.output_dataset_uri")
