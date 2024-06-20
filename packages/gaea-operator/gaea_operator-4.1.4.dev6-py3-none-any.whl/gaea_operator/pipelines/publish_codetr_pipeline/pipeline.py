#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
# @Time    : 2024/4/12
# @Author  : liyinggang
# @File    : codetr_pipeline.py
"""
from paddleflow.pipeline import Pipeline
from paddleflow.pipeline import CacheOptions
from paddleflow.pipeline import ContainerStep
from paddleflow.pipeline import Artifact
from paddleflow.pipeline import ExtraFS
from paddleflow.pipeline import FailureOptions

from gaea_operator.utils import DEFAULT_TRAIN_CONFIG_FILE_NAME, \
    DEFAULT_PYTORCH_MODEL_FILE_NAME, \
    ModelTemplate, \
    Accelerator, \
    modify_paddleflow_step
from gaea_operator.nodes import EvalInput, \
    TransformInput, \
    TransformEvalInput, \
    PackageInput, \
    InferenceInput
from gaea_operator.nodes import transform, transform_eval, package, inference


@Pipeline(
    name="codetr",
    cache_options=CacheOptions(enable=True, max_expired_time=604800),
    parallelism=6,
    failure_options=FailureOptions(strategy="continue"),
)
def pipeline(accelerator: str = "T4",
             transform_accelerator: str = None,
             transform_eval_accelerator: str = None,
             package_accelerator: str = None,
             inference_accelerator: str = None,
             train_skip: int = -1,
             eval_skip: int = -1,
             transform_skip: int = -1,
             transform_eval_skip: int = -1,
             package_skip: int = -1,
             inference_skip: int = -1,
             eval_input: EvalInput = EvalInput(),
             transform_input: TransformInput = TransformInput(),
             transform_eval_input: TransformEvalInput = TransformEvalInput(),
             package_input: PackageInput = PackageInput(),
             inference_input: InferenceInput = InferenceInput(),
             extra_fs_name: str = "vistudio",
             extra_fs_mount_path: str = "/home/paddleflow/storage/mnt/fs-root-vistudio",
             windmill_ak: str = "",
             windmill_sk: str = "",
             windmill_endpoint: str = "",
             experiment_kind: str = "",
             experiment_name: str = "",
             modelstore_name: str = "",
             tracking_uri: str = "",
             project_name: str = "",
             scene: str = "",
             train_dataset_name: str = "",
             val_dataset_name: str = "",
             base_train_dataset_name: str = "",
             base_val_dataset_name: str = "",
             train_model_name: str = "",
             train_model_display_name: str = "",
             eval_dataset_name: str = "",
             eval_model_name: str = "",
             transform_input_model_name: str = "",
             transform_model_name: str = "",
             transform_model_display_name: str = "",
             transform_eval_input_model_name: str = "",
             transform_advanced_parameters: str = "",
             ensemble_model_name: str = "",
             ensemble_model_display_name: str = "",
             inference_input_model_name: str = ""):
    """
    Pipeline for change ppyoloe_plus training eval transform transform-eval package inference.
    """
    base_params = {"flavour": "c4m16gpu1",
                   "queue": "qtrain",
                   "windmill_ak": windmill_ak,
                   "windmill_sk": windmill_sk,
                   "windmill_endpoint": windmill_endpoint,
                   "experiment_name": experiment_name,
                   "experiment_kind": experiment_kind,
                   "tracking_uri": tracking_uri,
                   "project_name": project_name,
                   "model_store_name": modelstore_name,
                   "scene": scene,
                   "is_step_run": "false"}
    base_env = {"PF_JOB_FLAVOUR": "{{flavour}}",
                "PF_JOB_QUEUE_NAME": "{{queue}}",
                "WINDMILL_AK": "{{windmill_ak}}",
                "WINDMILL_SK": "{{windmill_sk}}",
                "WINDMILL_ENDPOINT": "{{windmill_endpoint}}",
                "EXPERIMENT_KIND": "{{experiment_kind}}",
                "EXPERIMENT_NAME": "{{experiment_name}}",
                "TRACKING_URI": "{{tracking_uri}}",
                "PROJECT_NAME": "{{project_name}}",
                "SCENE": "{{scene}}",
                "PIPELINE_ROLE": "windmill"}

    name_to_step = {}
    if accelerator is None:
        accelerator = Accelerator.T4

    train_step = train(train_skip=train_skip,
                       base_params=base_params,
                       base_env=base_env,
                       extra_fs_name=extra_fs_name,
                       extra_fs_mount_path=extra_fs_mount_path,
                       train_dataset_name=train_dataset_name,
                       val_dataset_name=val_dataset_name,
                       base_train_dataset_name=base_train_dataset_name,
                       base_val_dataset_name=base_val_dataset_name,
                       train_model_name=train_model_name,
                       train_model_display_name=train_model_display_name)
    name_to_step[train_step.name] = train_step

    eval_step = eval(eval_skip=eval_skip,
                     eval_input=eval_input,
                     name_to_step=name_to_step,
                     base_params=base_params,
                     base_env=base_env,
                     eval_dataset_name=eval_dataset_name,
                     eval_model_name=eval_model_name)
    name_to_step[eval_step.name] = eval_step

    if transform_accelerator is None:
        transform_accelerator = accelerator
    transform_step = transform(transform_skip=transform_skip,
                               transform_input=transform_input,
                               name_to_step=name_to_step,
                               algorithm=ModelTemplate.CODETR_NAME,
                               category="Image/ObjectDetection",
                               accelerator=transform_accelerator,
                               base_params=base_params,
                               base_env=base_env,
                               train_model_name=transform_input_model_name,
                               transform_model_name=transform_model_name,
                               transform_model_display_name=transform_model_display_name,
                               advanced_parameters=transform_advanced_parameters)
    name_to_step[transform_step.name] = transform_step

    if transform_eval_accelerator is None:
        transform_eval_accelerator = accelerator
    transform_eval_step = transform_eval(transform_eval_skip=transform_eval_skip,
                                         algorithm=ModelTemplate.CODETR_NAME,
                                         transform_eval_input=transform_eval_input,
                                         name_to_step=name_to_step,
                                         base_params=base_params,
                                         base_env=base_env,
                                         accelerator=transform_eval_accelerator,
                                         dataset_name=eval_dataset_name,
                                         transform_model_name=transform_eval_input_model_name)
    name_to_step[transform_eval_step.name] = transform_eval_step

    if package_accelerator is None:
        package_accelerator = accelerator
    package_step = package(package_skip=package_skip,
                           algorithm=ModelTemplate.CODETR_NAME,
                           package_input=package_input,
                           name_to_step=name_to_step,
                           base_params=base_params,
                           base_env=base_env,
                           accelerator=package_accelerator,
                           transform_model_name=transform_eval_input_model_name,
                           ensemble_model_name=ensemble_model_name,
                           sub_extra_models="",
                           ensemble_model_display_name=ensemble_model_display_name)
    name_to_step[package_step.name] = package_step

    if inference_accelerator is None:
        inference_accelerator = accelerator
    inference_step = inference(inference_skip=inference_skip,
                               inference_input=inference_input,
                               name_to_step=name_to_step,
                               accelerator=inference_accelerator,
                               base_params=base_params,
                               base_env=base_env,
                               ensemble_model_name=inference_input_model_name,
                               dataset_name=eval_dataset_name)
    name_to_step[inference_step.name] = inference_step


def train(train_skip: int = -1,
          base_params: dict = None,
          base_env: dict = None,
          extra_fs_name: str = "vistudio",
          extra_fs_mount_path: str = "/home/paddleflow/storage/mnt/fs-root-vistudio",
          train_dataset_name: str = "",
          val_dataset_name: str = "",
          base_train_dataset_name: str = "",
          base_val_dataset_name: str = "",
          train_model_name: str = "",
          train_model_display_name: str = ""):
    """
    Train step
    """
    train_params = {"train_skip": train_skip,
                    "train_dataset_name": train_dataset_name,
                    "val_dataset_name": val_dataset_name,
                    "base_train_dataset_name": base_train_dataset_name,
                    "base_val_dataset_name": base_val_dataset_name,
                    "model_name": train_model_name,
                    "model_display_name": train_model_display_name,
                    "advanced_parameters": '{"max_epochs":"1",'
                                           '"eval_height":"224",'
                                           '"eval_width":"224",'
                                           '"batch_size":"2",'
                                           '"score_thresh":"0.05",'
                                           '"iou_thresh":"0.5",'
                                           '"model_type":"codetr"}'}
    train_env = {"TRAIN_DATASET_NAME": "{{train_dataset_name}}",
                 "VAL_DATASET_NAME": "{{val_dataset_name}}",
                 "BASE_TRAIN_DATASET_NAME": "{{base_train_dataset_name}}",
                 "BASE_VAL_DATASET_NAME": "{{base_val_dataset_name}}",
                 "MODEL_NAME": "{{model_name}}",
                 "MODEL_DISPLAY_NAME": "{{model_display_name}}",
                 "ADVANCED_PARAMETERS": "{{advanced_parameters}}",
                 "PF_EXTRA_WORK_DIR": extra_fs_mount_path}
    train_env.update(base_env)
    train_params.update(base_params)

    train = ContainerStep(name="train",
                          docker_env="iregistry.baidu-int.com/windmill-public/pytorch/pytorch::v4.1.4-dev31",
                          parameters=train_params,
                          env=train_env,
                          extra_fs=[ExtraFS(name=extra_fs_name, mount_path=extra_fs_mount_path)],
                          outputs={"output_model_uri": Artifact(), "output_uri": Artifact()},
                          command=f'cd /root && '
                                  f'package_path=$(python3 -c "import site; print(site.getsitepackages()[0])") && '
                                  f'python3 -m gaea_operator.nodes.train.codetr '
                                  f'--output-model-uri={{{{output_model_uri}}}} '
                                  f'--output-uri={{{{output_uri}}}} '
                                  f'$package_path/mmdet/tools/train.py '
                                  f'{{{{output_model_uri}}}}/{DEFAULT_TRAIN_CONFIG_FILE_NAME} '
                                  f'--work-dir={{{{output_model_uri}}}}')
    if train_skip > 0:
        train.condition = f"{train.parameters['train_skip']} < 0"

    return train


def eval(eval_skip: int = -1,
         eval_input: EvalInput = None,
         name_to_step: dict = None,
         base_params: dict = None,
         base_env: dict = None,
         eval_dataset_name: str = "",
         eval_model_name: str = ""):
    """
    Eval step
    """
    eval_params = {"eval_skip": eval_skip,
                   "dataset_name": eval_dataset_name,
                   "model_name": eval_model_name,
                   "advanced_parameters": '{"conf_threshold":"0.5",'
                                          '"iou_threshold":"0.5"}'}
    eval_env = {"DATASET_NAME": "{{dataset_name}}",
                "MODEL_NAME": "{{model_name}}",
                "ADVANCED_PARAMETERS": "{{advanced_parameters}}"}
    eval_env.update(base_env)
    eval_params.update(base_params)

    eval = ContainerStep(name="eval",
                         docker_env="iregistry.baidu-int.com/windmill-public/train/paddlepaddle:v4.1.4-dev31",
                         parameters=eval_params,
                         env=eval_env,
                         outputs={"output_uri": Artifact(),
                                  "output_dataset_uri": Artifact(),
                                  "output_model_uri": Artifact()},
                         command=f'cd /root && '
                                 f'package_path=$(python3 -c "import site; print(site.getsitepackages()[0])") && '
                                 f'python3 -m gaea_operator.nodes.eval.codetr '
                                 f'--input-model-uri={{{{input_model_uri}}}} '
                                 f'--output-uri={{{{output_uri}}}} '
                                 f'--output-dataset-uri={{{{output_dataset_uri}}}} '
                                 f'--output-model-uri={{{{output_model_uri}}}} '
                                 f'$package_path/mmdet/tools/test.py '
                                 f'{{{{input_model_uri}}}}/{DEFAULT_TRAIN_CONFIG_FILE_NAME} '
                                 f'{{{{input_model_uri}}}}/{DEFAULT_PYTORCH_MODEL_FILE_NAME} '
                                 f'--work-dir={{{{input_model_uri}}}}')
    modify_paddleflow_step(skip=eval_skip, step=eval, input=eval_input, input_spec=EvalInput, name_to_step=name_to_step)

    return eval


if __name__ == "__main__":
    pipeline_client = pipeline(
        accelerator="T4",
        windmill_ak="a1a9069e2b154b2aa1a83ed12316d163",
        windmill_sk="eefac23d2660404e93855197ce60efb3",
        windmill_endpoint="http://10.27.240.5:8340",
        experiment_kind="Aim",
        experiment_name="codetr",
        tracking_uri="aim://10.27.240.5:8329",
        project_name="workspaces/internal/projects/lyg_proj",
        train_dataset_name="workspaces/internal/projects/lyg_proj/datasets/wgisd/versions/1",
        val_dataset_name="workspaces/internal/projects/lyg_proj/datasets/wgisd/versions/1",
        eval_dataset_name="workspaces/internal/projects/lyg_proj/datasets/wgisd/versions/1",
        train_model_name="workspaces/internal/modelstores/ms-6TDGY7Hv/models/codetr",
        train_model_display_name="codetr",
        eval_model_name="workspaces/internal/modelstores/ms-6TDGY7Hv/models/codetr/versions/latest",
        transform_input_model_name="workspaces/internal/modelstores/ms-6TDGY7Hv/models/codetr/versions/latest",
        transform_model_name="workspaces/internal/modelstores/ms-6TDGY7Hv/models/codetr-t4",
        transform_model_display_name="codetr-t4",
        transform_eval_input_model_name="workspaces/internal/modelstores/ms-6TDGY7Hv/models/codetr-t4/versions/latest",
        ensemble_model_name="workspaces/internal/modelstores/ms-6TDGY7Hv/models/codetr-ensemble",
        ensemble_model_display_name="codetr-ensemble",
        inference_input_model_name="workspaces/internal/modelstores/ms-6TDGY7Hv/models/codetr-ensemble/versions/latest"
    )
    pipeline_client.compile(save_path="./codetr_pipeline.yaml")
    _, run_id = pipeline_client.run(fs_name="vistudio")
