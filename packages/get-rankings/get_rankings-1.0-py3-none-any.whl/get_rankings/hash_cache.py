import json
import os

def default_cache():
    return os.environ["HOME"] + "/.local/state/pyrank"

def list_to_hash(content):
    return {tuple(elem[0]): elem[1] for elem in content}

def hash_to_list(content):
    return [[a, content[a]] for a in content]


def load_hash_caches(basename, cache_dir=None):
    if cache_dir is None:
        cache_dir = default_cache()
    core = "%s/%s.json" % (cache_dir, basename)
    if os.path.exists(core):
        with open(core, "r") as fid:
            # for elem in
            return list_to_hash(json.load(fid))
    return {}

def save_hash_caches(cache, basename, cache_dir=None):
    if cache_dir is None:
        cache_dir = default_cache()
    os.makedirs(cache_dir, exist_ok=True)
    core = "%s/%s.json" % (cache_dir, basename)
    with open(core, "w") as fid:
        json.dump(hash_to_list(cache), fid)
