import inspect
import hashlib

def get_source_code_hash(func):
    source_code = inspect.getsource(func)
    hasher = hashlib.sha256()
    hasher.update(source_code.encode('utf-8'))
    hash_digest = hasher.hexdigest()
    return source_code, hash_digest