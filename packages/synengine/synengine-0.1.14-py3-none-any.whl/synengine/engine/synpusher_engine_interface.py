from engine_grpc.engine_stub_interface import GRPCInterface, INTERFACE_MAPPINGS
from engine_grpc.engine_pipe_abstract import EnginePlatform
from enum import auto
from aenum import Enum, extend_enum


class SynPusherInterface(Enum):
    method_syngar_unittest = auto()
    method_syngar_integ_create_mesh_group = auto()
    method_syngar_integ_integrate_models = auto()
    method_syngar_integ_initialize_model_view_buttons = auto()
    method_syngar_integ_initialize_dicom_view_buttons = auto()
    method_syngar_integ_integrate_bottom_menu = auto()
    method_syngar_integ_initialize_dicom_viewer = auto()
    method_syngar_integ_integrate_dicom_viewer = auto()
    method_syngar_integ_initialize_dicom_widget = auto()
    method_syngar_integ_integrate_dicom_widget = auto()
    method_syngar_integ_integrate_update_alpha_and_color = auto()
    method_syngar_integ_integrate_create_near_interaction_grabbable = auto()
    method_syngar_integ_doc_texture = auto()
    method_syngar_integ_build_asset_bundle = auto()
    method_syngar_integ_application_version = auto()

    # scene commands
    method_syngar_integ_build_save_scene = auto()


def update_command_mappings():
    # for name, value in GRPCInterface.__members__.items():
    #     extend_enum(SynPusher, name, value)

    INTERFACE_MAPPINGS.update({
        SynPusherInterface.method_syngar_unittest: {
            EnginePlatform.unity: "SynPusherInterface.SyngarUnitTest.UnitTest"
        },
        # SyngarInteg utilities
        SynPusherInterface.method_syngar_integ_create_mesh_group: {
            EnginePlatform.unity: "SynPusherInterface.SyngarIntegUtils.CreateMeshGroup"
        },
        SynPusherInterface.method_syngar_integ_integrate_models: {
            EnginePlatform.unity: "SynPusherInterface.SyngarIntegUtils.IntegrateModels"
        },
        SynPusherInterface.method_syngar_integ_initialize_model_view_buttons: {
            EnginePlatform.unity: "SynPusherInterface.SyngarIntegUtils.InitializeModelViewButtons"
        },
        SynPusherInterface.method_syngar_integ_initialize_dicom_view_buttons: {
            EnginePlatform.unity: "SynPusherInterface.SyngarIntegUtils.InitializeDicomViewButtons"
        },
        SynPusherInterface.method_syngar_integ_integrate_bottom_menu: {
            EnginePlatform.unity: "SynPusherInterface.SyngarIntegUtils.IntegrateBottomMenu"
        },
        SynPusherInterface.method_syngar_integ_initialize_dicom_viewer: {
            EnginePlatform.unity: "SynPusherInterface.SyngarIntegUtils.InitializeDicomViews"
        },
        SynPusherInterface.method_syngar_integ_integrate_dicom_viewer: {
            EnginePlatform.unity: "SynPusherInterface.SyngarIntegUtils.IntegrateDicomViewer"
        },
        SynPusherInterface.method_syngar_integ_initialize_dicom_widget: {
            EnginePlatform.unity: "SynPusherInterface.SyngarIntegUtils.InitializeDicomWidget"
        },
        SynPusherInterface.method_syngar_integ_integrate_dicom_widget: {
            EnginePlatform.unity: "SynPusherInterface.SyngarIntegUtils.IntegrateDicomWidget"
        },
        SynPusherInterface.method_syngar_integ_integrate_update_alpha_and_color: {
            EnginePlatform.unity: "SynPusherInterface.SyngarIntegUtils.UpdateAlphaAndColor"
        },
        SynPusherInterface.method_syngar_integ_integrate_create_near_interaction_grabbable: {
            EnginePlatform.unity: "SynPusherInterface.SyngarIntegUtils.CreateNearInteractionGrabbable"
        },
        SynPusherInterface.method_syngar_integ_build_asset_bundle: {
            EnginePlatform.unity: "SynPusherInterface.SyngarIntegUtils.BuildAssetBundle"
        },
        SynPusherInterface.method_syngar_integ_doc_texture: {
            EnginePlatform.unity: "SynPusherInterface.SyngarIntegUtils.IntegrateDocTexture"
        },
        SynPusherInterface.method_syngar_integ_build_save_scene: {
            EnginePlatform.unity: "SynPusherInterface.SyngarIntegUtils.SaveCurrentScene"
        },
        SynPusherInterface.method_syngar_integ_application_version: {
            EnginePlatform.unity: "SynPusherInterface.SyngarIntegUtils.ApplicationVersion"
        }
    })
