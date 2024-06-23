import os
import re
import requests
from posixpath import join
from typing import Dict
from compipe.utils.io_helper import (warm_up_path)
from compipe.utils.logging import logger
from engine_grpc.unity.engine_pipe_unity_impl import UnityEngineImpl as UEI

from ..synpusher_engine_interface import SynPusherInterface
from synengine.engine.unity.unity_pipe_syngar_utils import \
    get_application_version
from pydantic import BaseModel


class AssetBundleManifestItem(BaseModel):
    hash: str
    guid: str
    version: str


def is_md5_string(s):
    # Define the regular expression pattern for an MD5 hash
    md5_pattern = re.compile(r'^[a-fA-F0-9]{32}$')

    # Check if the string matches the MD5 pattern
    return bool(md5_pattern.match(s))


def build_single_asset_bundle(name: str, source: str, target: str, url: str = None) -> Dict:
    """It's aimed to build unity assetbundle for a specific case.

    Args:
        name (str): represent the case guid (uuid) hash.
        source (str): represent the relative folder path of unity project.
        target (str): represent the assetbundle path on server.
        url (str, optional): represent the url for updating assetbundle manifest config. Defaults to None.

    Returns:
        Dict: represent the assetbundle context
    """
    project_root = UEI().get_project_info().project_root

    if not os.path.isabs(target):
        target = os.path.join(project_root, target)

    if not os.path.isabs(source):
        source = os.path.join(project_root, source)

    warm_up_path(path=target)
    bundle_name = f"{name}.bundle"
    resp = UEI().command_parser(cmd=SynPusherInterface.method_syngar_integ_build_asset_bundle,
                                params=[
                                    bundle_name,
                                    source,
                                    target
                                ])

    hash_code = resp.payload

    asset_bundle_path = join(target, bundle_name)

    # validate assetbundle path exists. if not exists, raise error
    if not is_md5_string(str(hash_code)):
        raise FileNotFoundError(
            f"Failed to create assetbundle: {asset_bundle_path}")

    logger.debug(
        f"Created assetbundle: {asset_bundle_path}, hash: {hash_code}")

    # assemble the assetbundle context
    assetbundle_ctx = AssetBundleManifestItem(
        hash=hash_code,
        guid=name,
        version=get_application_version().payload
    )

    # update the manifest config if the url is specified
    if url:
        response = requests.post(
            url="http://localhost:5000/api/v1/assetbundle/manifest",
            json=assetbundle_ctx.dict(),
            timeout=180)

    response.raise_for_status()

    logger.debug(f"updated assetbundle manifest: {response.json()}")

    return assetbundle_ctx.dict()
