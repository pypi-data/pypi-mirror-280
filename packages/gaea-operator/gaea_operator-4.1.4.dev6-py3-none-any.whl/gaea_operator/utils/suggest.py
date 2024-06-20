#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
# @Time    : 2024/6/18
# @Author  : yanxiaodong
# @File    : suggest.py
"""
from .accelerator import Accelerator, get_accelerator


def suggest_compute(component_kind: str, accelerator_name: str = Accelerator.T4):
    """
    suggest compute name
    """
    nvidia_accelerator = get_accelerator(kind=Accelerator.NVIDIA)
    accelerator = get_accelerator(name=accelerator_name)
    # 训练只支持gpu
    if component_kind in ["train", "eval"]:
        return ["training", "tags.usage=train"] + nvidia_accelerator.suggest_resource_tips()
    elif component_kind == "package":
        return ["training", "tags.usage=train"]
    elif component_kind == "transform":
        # 模型转换 nvidia需要gpu，其他不需要xpu
        if accelerator.get_kind == Accelerator.NVIDIA:
            return ["training", "tags.usage=train"] + nvidia_accelerator.suggest_resource_tips()
        return ["training", "tags.usage=train"]
    else:
        return ["training", "tags.usage=train"] + accelerator.suggest_resource_tips()


def suggest_flavours(component_kind: str, accelerator_name: str = Accelerator.T4):
    """
    suggest flavour name
    """
    nvidia_accelerator = get_accelerator(kind=Accelerator.NVIDIA)
    accelerator = get_accelerator(name=accelerator_name)
    # 训练只支持gpu
    if component_kind in ["train", "eval"]:
        return nvidia_accelerator.suggest_flavours()
    elif component_kind == "package":
        return [{"name": "c4m16", "display_name": "CPU: 4核 内存: 16Gi"}]
    elif component_kind == "transform":
        # 模型转换 nvidia需要gpu，其他不需要xpu
        if accelerator.get_kind == Accelerator.NVIDIA:
            return [nvidia_accelerator.suggest_flavours()[0]]
        return [{"name": "c4m16", "display_name": "CPU: 4核 内存: 16Gi"}]
    else:
        return [accelerator.suggest_flavours()[0]]