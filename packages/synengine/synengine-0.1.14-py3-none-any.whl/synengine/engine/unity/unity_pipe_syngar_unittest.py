import os
import re
import shutil
import struct
from collections import defaultdict
from posixpath import join
from typing import Dict, List

from compipe.utils.decorators import validate_collection_parameter
from compipe.utils.io_helper import (get_files, get_files_by_regex_basename,
                                     json_loader, json_writer, warm_up_path)
from compipe.utils.logging import logger
from engine_grpc.engine_stub_interface import GRPCInterface
from engine_grpc.unity.engine_pipe_unity_impl import UnityEngineImpl as UEI
from ...utils.const_key import ARG_MODE
from ...utils.grpc_convert_utils import parse_int_from_str

from ..synpusher_engine_interface import SynPusherInterface


def syngar_unittest() -> bool:

    resp = UEI().command_parser(cmd=SynPusherInterface.method_syngar_unittest,
                                params=[])
    value = parse_int_from_str(resp.payload.value)
    print(value)
