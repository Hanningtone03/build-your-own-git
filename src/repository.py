import os
import json

def init():
    if os.path.exists(".vgit"):
        print("Repository already exists.")
        return
    os.makedirs(".vgit/objects")
    os.makedirs(".vgit/refs/heads")
    with open(".vgit/HEAD", "w") as f:
        f.write("ref: refs/heads/main\n")
    with open(".vgit/config.json", "w") as f:
        json.dump({"branch": "main"}, f)
    print("Initialized empty vgit repository.")

def get_head():
    with open(".vgit/HEAD") as f:
        ref = f.read().strip()
    if ref.startswith("ref: "):
        ref_path = os.path.join(".vgit", ref[5:])
        if os.path.exists(ref_path):
            with open(ref_path) as f:
                return f.read().strip()
        return None
    return ref

def set_head(sha1):
    with open(".vgit/HEAD") as f:
        ref = f.read().strip()
    if ref.startswith("ref: "):
        ref_path = os.path.join(".vgit", ref[5:])
        os.makedirs(os.path.dirname(ref_path), exist_ok=True)
        with open(ref_path, "w") as f:
            f.write(sha1 + "\n")
    else:
        with open(".vgit/HEAD", "w") as f:
            f.write(sha1 + "\n")