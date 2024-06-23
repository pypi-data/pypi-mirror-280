from compipe.utils.access import AccessHub
from cryptography.fernet import Fernet

DEFAULT_HASH_KEY_NAME = "mars"


def hash_encrypt(msg: str, key: bytes = None) -> str:
    if not key:
        key = AccessHub().get_credential(DEFAULT_HASH_KEY_NAME).encode('utf-8')
    fernet = Fernet(key)
    return fernet.encrypt(msg.encode()).decode("utf-8")


def hash_decrypt(hash: str, key: bytes = None) -> str:
    if not key:
        key = AccessHub().get_credential(DEFAULT_HASH_KEY_NAME).encode('utf-8')
    fernet = Fernet(key)
    return fernet.decrypt(hash.encode('utf-8')).decode()
