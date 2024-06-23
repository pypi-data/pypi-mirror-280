import os
import shutil
from collections import defaultdict
from posixpath import join
from typing import Dict, List

from compipe.utils.io_helper import (get_files, get_files_by_regex_basename,
                                     json_loader, json_writer, warm_up_path)
from compipe.utils.parameters import (ARG_CHANNEL_MAP, ARG_DIFFUSE_MAP,
                                      ARG_GUID, ARG_MODEL, ARG_NAME, ARG_PATH,
                                      ARG_SEGMENT)
from engine_grpc.engine_stub_interface import GRPCInterface
from engine_grpc.unity.engine_pipe_unity_impl import UnityEngineImpl as UEI

from ..synpusher_engine_interface import SynPusherInterface
from ...utils.const_key import ARG_BONE, ARG_MUSCLE, ARG_SKIN, ARG_TUMOR, ARG_BONE_CLIP, ARG_DEFAULT
# the models and materials are attached the "clip" extension to identify for
# 3d dicom viewer contents
CLIPPING_EXTENSION = "clip"


MODEL_MATERIAL_VARIANT = {
    "bone": [f"bone_{CLIPPING_EXTENSION}", "bone"]
}

TEXTURE_TYPES = [ARG_DIFFUSE_MAP, ARG_CHANNEL_MAP]

MODEL_FOLDER_NAME = "model"


def unity_integrate_model(name: str, source: str, target: str, material_mappings: Dict) -> List[str]:

    # represent the unity absolute path of "Assets"
    project_root = UEI().get_project_info().project_root

    # represent the relative unity asset path
    model_root_dir = join(target, MODEL_FOLDER_NAME)
    asset_path = join(model_root_dir, name)

    # represent the local path
    absolute_asset_path = os.path.join(project_root, asset_path)

    warm_up_path(path=absolute_asset_path)

    UEI().command_parser(cmd=GRPCInterface.method_editor_assetdatabase_refresh)

    children_prefabs = defaultdict(list)
    # get fbx files from the specified path
    for model_file in get_files([source], ext_patterns=['fbx']):
        model_base_name = os.path.basename(model_file)
        model_name = os.path.splitext(model_base_name)[0]
        model_asset_path = join(asset_path, model_base_name)
        # copy asset into unity project
        shutil.copy2(model_file, f"{absolute_asset_path}/{model_base_name}")

        UEI().command_parser(cmd=GRPCInterface.method_editor_import_asset,
                             params=[model_asset_path])

        texture_lists = []
        for texture_type in TEXTURE_TYPES:
            texture_basename = f"{model_name}_{texture_type}.tga"
            texture_file = os.path.join(source, texture_basename)
            texture_asset_path = join(asset_path, texture_basename)

            # integrate texture assets
            shutil.copy2(texture_file, os.path.join(
                absolute_asset_path, texture_basename))
            UEI().command_parser(cmd=GRPCInterface.method_editor_import_asset,
                                 params=[texture_asset_path])

            texture_lists.append(texture_asset_path)

        # generate prefab variant along with customized materials
        for mat_key in MODEL_MATERIAL_VARIANT.get(name, [name]):
            if (mat_template := material_mappings.get(mat_key, None)) is None:
                mat_template = material_mappings.get(ARG_DEFAULT)

            # create material
            material_path = join(asset_path, f"{model_name}_{mat_key}_Mat.mat")
            UEI().command_parser(cmd=GRPCInterface.method_editor_assetdatabase_copy_asset,
                                 params=[mat_template, material_path])

            # hook up textures
            UEI().command_parser(cmd=GRPCInterface.method_material_update_textures,
                                 params=[material_path,
                                         *texture_lists])
            # create prefab variant
            model_asset_prefab = join(
                asset_path, f"{model_name}_{mat_key}.prefab")
            UEI().command_parser(cmd=GRPCInterface.method_object_create,
                                 params=[model_asset_path,
                                         model_asset_prefab,
                                         True,
                                         material_path])

            children_prefabs[mat_key].append(model_asset_prefab)

    # create parent prefab
    output_prefabs = []

    for key, values in children_prefabs.items():

        root_asset_prefab = os.path.join(model_root_dir, f"{key}.prefab")

        UEI().command_parser(cmd=GRPCInterface.method_object_merge,
                             params=[
                                 values,
                                 root_asset_prefab
                             ])
        output_prefabs.append(root_asset_prefab)

    UEI().command_parser(cmd=GRPCInterface.method_editor_assetdatabase_refresh)

    return output_prefabs


def integrate_model_from_config(model_names: List[str], config_path: str, target: str, material_mappings: Dict):

    config_content = json_loader(path=config_path)

    model_full_name = config_content.get(ARG_NAME)

    output_path = join(target, config_content.get(ARG_GUID))

    segment_name = config_content.get(ARG_SEGMENT)

    # represent the unity absolute path of "Assets"
    project_root = UEI().get_project_info().project_root

    # represent the relative unity asset path
    model_root_dir = join(output_path, MODEL_FOLDER_NAME)

    asset_path = join(model_root_dir, segment_name)

    # represent the local path
    absolute_asset_path = os.path.join(project_root, asset_path)

    warm_up_path(path=absolute_asset_path)

    UEI().command_parser(cmd=GRPCInterface.method_editor_assetdatabase_refresh)

    model_collection = [v for k, v in config_content.get(
        ARG_MODEL).items() if k in model_names]

    children_prefabs = defaultdict(list)

    for model_content in model_collection:

        model_file_basename = model_content.get(ARG_MODEL)
        model_file = join(config_content.get(ARG_PATH), model_file_basename)
        model_name = os.path.splitext(model_file_basename)[0]
        model_asset_abs_path = os.path.join(
            absolute_asset_path, model_file_basename)
        model_asset_path = join(asset_path, model_file_basename)
        # copy fbx model to the assetbundle folder
        shutil.copy2(model_file, model_asset_abs_path)
        UEI().command_parser(cmd=GRPCInterface.method_editor_import_asset,
                             params=[model_asset_path])

        texture_list = []
        for texture_type in TEXTURE_TYPES:

            texture_file_basename = model_content.get(texture_type)
            texture_file = join(config_content.get(
                ARG_PATH), texture_file_basename)
            texture_asset_abs_path = os.path.join(
                absolute_asset_path, texture_file_basename)
            texture_asset_path = join(asset_path, texture_file_basename)
            texture_list.append(texture_asset_path)
            shutil.copy2(texture_file, texture_asset_abs_path)
            UEI().command_parser(cmd=GRPCInterface.method_editor_import_asset,
                                 params=[texture_asset_path])

        # generate prefab variant along with customized materials
        for mat_key in MODEL_MATERIAL_VARIANT.get(segment_name, [segment_name]):
            if (mat_template := material_mappings.get(mat_key, None)) is None:
                mat_template = material_mappings.get(ARG_DEFAULT)

            # create material
            material_path = join(asset_path, f"{model_name}_{mat_key}_mat.mat")
            UEI().command_parser(cmd=GRPCInterface.method_editor_assetdatabase_copy_asset,
                                 params=[mat_template, material_path])

            # hook up textures
            UEI().command_parser(cmd=GRPCInterface.method_material_update_textures,
                                 params=[material_path,
                                         *texture_list])
            # create prefab variant
            model_asset_prefab = join(
                asset_path, f"{model_name}_{mat_key}.prefab")
            UEI().command_parser(cmd=GRPCInterface.method_object_create,
                                 params=[model_asset_path,
                                         model_asset_prefab,
                                         True,
                                         material_path])

            children_prefabs[mat_key].append(model_asset_prefab)

   # create parent prefab
    output_prefabs = []

    for key, values in children_prefabs.items():

        root_asset_prefab = join(model_root_dir, f"{key}.prefab")

        UEI().command_parser(cmd=GRPCInterface.method_object_merge,
                             params=[
                                 values,
                                 root_asset_prefab
                             ])
        output_prefabs.append(root_asset_prefab)

    UEI().command_parser(cmd=GRPCInterface.method_editor_assetdatabase_refresh)

    return output_prefabs


def integrate_mesh_collider(collider_mesh: str, output: str, add_interactable_component: bool = True):
    UEI().command_parser(cmd=SynPusherInterface.method_syngar_integ_integrate_create_near_interaction_grabbable,
                         params=[
                             collider_mesh,
                             output,
                             add_interactable_component
                         ])


def integrate_mesh_group(assets: List[str], target: str, collider_asset: str):

    UEI().command_parser(cmd=SynPusherInterface.method_syngar_integ_create_mesh_group,
                         params=[
                             collider_asset,
                             assets,
                             target
                         ])


def get_model_asset_lists(path: str, reg_pattern: str):
    """Load the model prefab asset lists from the specified path.

    Args:
        path (str): Represent the folder for searching.

    Returns:
        List[str]: Represent the asset path lists
    """
    # assets = get_files([path], ext_patterns=['prefab'], recursive=False)

    assets = get_files_by_regex_basename(
        [path], reg_pattern=reg_pattern, recursive=False)

    proj_root = UEI().get_project_info().project_root

    return [asset[len(proj_root):].replace('\\', '/') for asset in assets]


def integrate_model_views(target: str, data: Dict):

    proj_root = UEI().get_project_info().project_root

    json_writer(os.path.join(proj_root, os.path.normpath(target)), data=data)

    UEI().command_parser(cmd=GRPCInterface.method_editor_import_asset,
                         params=[target])


def get_application_version():
    return UEI().command_parser(cmd=SynPusherInterface.method_syngar_integ_application_version,
                                params=[])
