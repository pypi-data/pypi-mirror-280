import os
import re
import shutil
from collections import defaultdict
from typing import Dict, List
import math

from compipe.utils.decorators import validate_collection_parameter
from compipe.utils.io_helper import (get_files, get_files_by_regex_basename,
                                     json_loader, json_writer, warm_up_path)
from compipe.utils.logging import logger
from engine_grpc.engine_stub_interface import GRPCInterface
from engine_grpc.unity.engine_pipe_unity_impl import UnityEngineImpl as UEI
from ...utils.const_key import ARG_MODE

from ..synpusher_engine_interface import SynPusherInterface


def clone_scene(source: str, target: str) -> bool:
    project_root = UEI().get_project_info().project_root
    scene_path = os.path.join(project_root, target)
    warm_up_path(path=scene_path)

    UEI().command_parser(cmd=GRPCInterface.method_editor_assetdatabase_copy_asset,
                         params=[
                             source,
                             target
                         ])
    if not os.path.exists(scene_path):
        raise FileNotFoundError(f"Failed to clone new scene: {target}")

    logger.debug(f"Cloned scene and saved on path: {target}")
    return True


@validate_collection_parameter(ARG_MODE, ['Single', 'Additive', 'AdditiveWithoutLoading'])
def open_scene(path: str, mode: str):
    UEI().command_parser(cmd=GRPCInterface.method_editor_scenemanager_open,
                         params=[path, "Single"])
    logger.debug(f"Opened scene in editor: {path}")


def create_bottom_menu_asset(source: str, target: str):
    UEI().command_parser(cmd=GRPCInterface.method_editor_assetdatabase_copy_asset,
                         params=[source, target])


def initialize_model_buttons(container_path: str, config_path: str, button_template: str, button_root_path: str):
    UEI().command_parser(cmd=GRPCInterface.method_editor_assetdatabase_refresh)

    UEI().command_parser(cmd=SynPusherInterface.method_syngar_integ_initialize_model_view_buttons,
                         params=[
                             container_path,
                             config_path,
                             button_template,
                             button_root_path
                         ])


def integrate_sprite_assets(source: str, config_target: str) -> str:

    SPRITE_SUFFIX = "sprmap"
    # initialize target directories
    target = os.path.splitext(config_target)[0]

    project_root = UEI().get_project_info().project_root
    target_abs_path = os.path.join(project_root, os.path.normpath(target))

    output_config = {"sprites": [], "volume": []}

    sprite_index = -1
    for root, _, files in os.walk(source, topdown=True):
        if files:
            folder_name = os.path.basename(root)
            asset_cfg = {
                'name': folder_name,
                'modalities': [],
                'priority': (sprite_index := sprite_index+1)
            }

            for modality in ['sagittal', 'coronal', 'axial']:
                modality_asset = {
                    'name': modality,
                    'texture': [f'{target}/{folder_name}/{asset}' for asset in files if asset.endswith(f'{modality}_{SPRITE_SUFFIX}.png')][0],
                    'metadata': [f'{target}/{folder_name}/{asset}' for asset in files if asset.endswith(f'{modality}_{SPRITE_SUFFIX}.json')][0]
                }
                asset_cfg['modalities'].append(modality_asset)

            for asset in files:

                if not output_config['volume'] and asset.endswith(F'axial_{SPRITE_SUFFIX}.json'):
                    metadata = json_loader(path=os.path.join(root, asset))
                    output_config['volume'] = [metadata['count'],
                                               metadata['width'], metadata['height']]

                asset_abs_path = os.path.join(
                    target_abs_path, folder_name, os.path.basename(asset))
                warm_up_path(asset_abs_path)
                shutil.copy2(os.path.join(root, asset), asset_abs_path)
            output_config["sprites"].append(asset_cfg)

    json_writer(os.path.join(
        project_root, os.path.normpath(config_target)), output_config)
    UEI().command_parser(cmd=GRPCInterface.method_editor_assetdatabase_refresh)


def initialize_dicom_buttons(container_path: str, config_path: str, button_template: str, button_root_path: str):

    UEI().command_parser(cmd=SynPusherInterface.method_syngar_integ_initialize_dicom_view_buttons,
                         params=[
                             container_path,
                             config_path,
                             button_template,
                             button_root_path
                         ])


def integrate_bottom_menu(source: str,
                          root_path: str,
                          model_button_root: str,
                          dicom_button_root: str,
                          state_machine_path: str,
                          hub_controller_path: str):

    UEI().command_parser(cmd=SynPusherInterface.method_syngar_integ_integrate_bottom_menu,
                         params=[
                             source,
                             root_path,
                             model_button_root,
                             dicom_button_root,
                             state_machine_path,
                             hub_controller_path
                         ])


def integrate_models(source: str, config_path: str, root: str, state_machine_path: str):
    UEI().command_parser(cmd=SynPusherInterface.method_syngar_integ_integrate_models,
                         params=[
                             source,
                             config_path,
                             root,
                             state_machine_path
                         ])


def initialize_dicom_viewer(source: str, target: str, sprite_config: str, model_path: str, model_root: str,
                            plane_path: str):

    UEI().command_parser(cmd=SynPusherInterface.method_syngar_integ_initialize_dicom_viewer,
                         params=[
                             source,
                             target,
                             sprite_config,
                             model_path,
                             model_root,
                             plane_path
                         ])


def integrate_dicom_viewer(source: str, root: str, state_machine_path: str):
    UEI().command_parser(cmd=SynPusherInterface.method_syngar_integ_integrate_dicom_viewer,
                         params=[
                             source,
                             root,
                             state_machine_path
                         ])


def initialize_dicom_widget(source: str, target: str, sprite_config: str, button_template: str, button_root_path: str):
    UEI().command_parser(cmd=SynPusherInterface.method_syngar_integ_initialize_dicom_widget,
                         params=[
                             source,
                             target,
                             sprite_config,
                             button_template,
                             button_root_path
                         ])


def integrate_dicom_widget(source: str, root: str, setting_config: str):
    UEI().command_parser(cmd=SynPusherInterface.method_syngar_integ_integrate_dicom_widget,
                         params=[
                             source,
                             os.path.basename(os.path.splitext(source)[0]),
                             root,
                             setting_config
                         ])


def integrate_doc_texture(source: str, root: str, pages: int):
    UEI().command_parser(cmd=GRPCInterface.method_editor_import_asset,
                         params=[source])

    # calculate column numbers
    column_size = math.ceil(pages**0.5)
    # calculate raw numbers
    raw_size = 0
    for _ in range(0, pages, column_size):
        raw_size += 1

    UEI().command_parser(cmd=SynPusherInterface.method_syngar_integ_doc_texture,
                         params=[
                             source,
                             root,
                             raw_size,
                             column_size,
                             pages
                         ])
