import os
import hashlib
import zlib

def hash_object(data, obj_type="blob", write=True):
    if isinstance(data, str):
        data = data.encode()
    header = f"{obj_type} {len(data)}\0".encode()
    full = header + data
    sha1 = hashlib.sha1(full).hexdigest()
    if write:
        path = os.path.join(".vgit", "objects", sha1[:2], sha1[2:])
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "wb") as f:
            f.write(zlib.compress(full))
    return sha1

def read_object(sha1):
    path = os.path.join(".vgit", "objects", sha1[:2], sha1[2:])
    with open(path, "rb") as f:
        raw = zlib.decompress(f.read())
    null = raw.index(b"\0")
    header = raw[:null].decode()
    obj_type, _ = header.split(" ")
    data = raw[null + 1:]
    return obj_type, data

def hash_tree(entries):
    tree_data = b""
    for name, sha1, mode in sorted(entries, key=lambda x: x[0]):
        tree_data += f"{mode} {name}\0".encode() + bytes.fromhex(sha1)
    return hash_object(tree_data, obj_type="tree")