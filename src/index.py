import os
import json
from .objects import hash_object

INDEX_FILE = ".vgit/index.json"

def load_index():
    if os.path.exists(INDEX_FILE):
        with open(INDEX_FILE) as f:
            return json.load(f)
    return {}

def save_index(index):
    with open(INDEX_FILE, "w") as f:
        json.dump(index, f, indent=2)

def add(paths):
    index = load_index()
    for path in paths:
        if path == ".":
            for root, dirs, files in os.walk("."):
                dirs[:] = [d for d in dirs if d not in [".vgit", ".git", "__pycache__"]]
                for file in files:
                    filepath = os.path.join(root, file).replace("\\", "/").lstrip("./")
                    if filepath:
                        with open(os.path.join(root, file), "rb") as f:
                            data = f.read()
                        sha1 = hash_object(data)
                        index[filepath] = sha1
        else:
            if os.path.exists(path):
                with open(path, "rb") as f:
                    data = f.read()
                sha1 = hash_object(data)
                index[path] = sha1
                print(f"Added {path}")
            else:
                print(f"File not found: {path}")
    save_index(index)

def get_index():
    return load_index()