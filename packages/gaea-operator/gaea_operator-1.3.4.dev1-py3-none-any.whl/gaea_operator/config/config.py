#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
# @Time    : 2024/2/26
# @Author  : yanxiaodong
# @File    : config.py
"""
from typing import Dict
import os
from abc import ABCMeta
import bcelogger

from gaea_tracker import ExperimentTracker
from windmillclient.client.windmill_client import WindmillClient
from windmillmodelv1.client.model_api_model import ModelMetadata, InputSize

from gaea_operator.utils import DEFAULT_TRANSFORM_CONFIG_FILE_NAME, Accelerator
from .generate_transform_config import generate_transform_config
from .modify_package_files import ModifyPackageFiles
from .generate_transform_config import KEY_EVAL_SIZE, \
    KEY_EVAL_WIDTH, \
    KEY_EVAL_HEIGHT, \
    KEY_MAX_BATCH_SIZE, \
    KEY_MAX_BOX_NUM

KEY_MODEL_TYPE = 'model_type'


class Config(metaclass=ABCMeta):
    """
    Config write for train, transform and package.
    """
    accelerator2model_format = {Accelerator.T4: "TensorRT",
                                Accelerator.A100: "TensorRT",
                                Accelerator.V100: "TensorRT",
                                Accelerator.R200: "PaddleLite"}

    def __init__(self, windmill_client: WindmillClient, tracker_client: ExperimentTracker, metadata: Dict = {}):
        self.windmill_client = windmill_client
        self.tracker_client = tracker_client
        self._metadata = metadata

    @property
    def metadata(self):
        """
        Get metadata.
        """
        return self._metadata

    @metadata.setter
    def metadata(self, value: dict):
        """
        Set metadata.
        """
        self._metadata = ModelMetadata(**value).dict()

    def write_train_config(self,
                           dataset_uri: str,
                           model_uri: str,
                           advanced_parameters: dict,
                           pretrain_model_uri: str):
        """
        Config write for train.
        """
        pass

    def write_eval_config(self, dataset_uri: str, model_uri: str, ):
        """
        Config write for eval.
        """
        pass

    def write_transform_config(self, model_uri: str, advanced_parameters: dict):
        """
        Config write for transform.
        """
        cfg_path = os.path.join(model_uri, DEFAULT_TRANSFORM_CONFIG_FILE_NAME)
        self._update_transform_metadata(advanced_parameters)

        generate_transform_config(advanced_parameters, cfg_path, self.metadata)

    def write_model_config(self, transform_model_uri: str):
        """
        Config write for transform model.
        """
        model_type = self.metadata["algorithmParameters"].get("modelType", "")
        bcelogger.info('model type: {}'.format(model_type))
        cfg = ModifyPackageFiles(metadata=self.metadata, transform_model_uri=transform_model_uri)
        cfg.modify_model_config(model_type=model_type)

    def write_connect_config(self,
                             model_repo: str,
                             model_display_name: str,
                             template_ensemble_name: str,
                             template_ensemble_version: str,
                             ensemble_name: str,
                             sub_models: dict,
                             model_name: str,
                             template_model_name: str,
                             extra_models: dict = None):
        """
        Config write for connect model.
        """
        model_type = self.metadata["algorithmParameters"].get("modelType", "")
        bcelogger.info('model type: {}'.format(model_type))
        cfg = ModifyPackageFiles(sub_models=sub_models,
                                 extra_models=extra_models,
                                 metadata=self.metadata,
                                 model_repo=model_repo,
                                 template_ensemble_name=template_ensemble_name,
                                 template_ensemble_version=template_ensemble_version)
        return cfg.modify_connect_config(model_name=model_name,
                                         ensemble_name=ensemble_name,
                                         template_model_name=template_model_name,
                                         model_display_name=model_display_name,
                                         model_type=model_type)

    def write_ensemble_config(self,
                              model_repo: str,
                              sub_models: dict,
                              model_name_pairs: dict,
                              ensemble_name: str,
                              ensemble_version: str,
                              extra_models: dict = None):
        """
        Config write for ensemble.
        """
        cfg = ModifyPackageFiles(sub_models=sub_models,
                                 extra_models=extra_models,
                                 metadata=self.metadata,
                                 model_repo=model_repo,
                                 template_ensemble_name=ensemble_name,
                                 template_ensemble_version=ensemble_version)
        return cfg.modify_ensemble_config(model_name_pairs=model_name_pairs)

    def _update_train_metadata(self, advanced_parameters: Dict):
        meta_data = ModelMetadata(experimentName=self.tracker_client.experiment_name,
                                  algorithmParameters={'modelType': str(advanced_parameters[KEY_MODEL_TYPE])},
                                  experimentRunID=self.tracker_client.run_id)
        self._metadata.update(meta_data.dict())

    def _update_transform_metadata(self, advanced_parameters: Dict):
        if KEY_EVAL_SIZE in advanced_parameters:
            width, height = advanced_parameters.pop(KEY_EVAL_SIZE).split('*')
            advanced_parameters[KEY_EVAL_WIDTH] = width
            advanced_parameters[KEY_EVAL_HEIGHT] = height

        input_size = InputSize(width=int(advanced_parameters[KEY_EVAL_WIDTH]),
                               height=int(advanced_parameters[KEY_EVAL_HEIGHT]))

        meta_data = ModelMetadata(**self._metadata)
        meta_data.inputSize = input_size
        maxBoxNum = int(advanced_parameters[KEY_MAX_BOX_NUM]) \
            if KEY_MAX_BOX_NUM in advanced_parameters else 1
        meta_data.maxBoxNum = maxBoxNum
        advanced_parameters = {
            'inferenceMaxBatchSize': str(advanced_parameters[KEY_MAX_BATCH_SIZE]),
            'modelType': str(advanced_parameters[KEY_MODEL_TYPE]),
            'maxBoxNum': str(maxBoxNum)}

        if meta_data.algorithmParameters is None:
            meta_data.algorithmParameters = advanced_parameters
        else:
            meta_data.algorithmParameters.update(advanced_parameters)

        self._metadata = meta_data.dict()
