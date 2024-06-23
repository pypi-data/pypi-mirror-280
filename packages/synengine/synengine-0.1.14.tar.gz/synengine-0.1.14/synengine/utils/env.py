from contextlib import contextmanager
from compipe.runtime_env import Environment as env
from compipe.utils.logging import logger
from compipe.utils.task_queue_helper import TQHelper
from compipe.response.command_result import MSGStatusCodes


# TODO config below values through runtime_config json
DEFAULT_GRPC_CHANNEL = "localhost:50051"
LOCAL_ENCRYPTED_CRED_FILE_PATH = "credential/cred.txt"
LOCAL_ENCRYPTED_CRED_KEY_FILE_PATH = "credential/cred_key.txt"
LOCAL_SOURCE_CRED_FILE_PATH = "credential/keys.json"
ENVIRONMENT_VAR_CRED_KEY = "CRED_KEY"
LOCAL_RUNTIME_CONFIG_FILE = "runtime_config.json"


@contextmanager
def inject_env_variables(**kwarg):
    try:
        if kwarg:
            env().param.update(kwarg)

            TQHelper.post(payload=kwarg,
                          message='Injected runtime environment',
                          msg_statue=MSGStatusCodes.warning)
        yield
    finally:
        env().reset()
