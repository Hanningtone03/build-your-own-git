import os
from .index import get_index
from .objects import read_object

def diff():
    index = get_index()
    changes = []

    for filepath, sha1 in index.items():
        if os.path.exists(filepath):
            with open(filepath, "rb") as f:
                current = f.read()
            try:
                obj_type, stored = read_object(sha1)
                if current != stored:
                    changes.append((filepath, stored, current))
            except:
                changes.append((filepath, b"", current))
        else:
            changes.append((filepath, b"", b"(deleted)"))

    if not changes:
        print("No changes.")
        return

    for filepath, old, new in changes:
        print(f"--- {filepath}")
        old_lines = old.decode(errors="replace").splitlines()
        new_lines = new.decode(errors="replace").splitlines()
        old_set = set(old_lines)
        new_set = set(new_lines)
        for line in old_lines:
            if line not in new_set:
                print(f"- {line}")
        for line in new_lines:
            if line not in old_set:
                print(f"+ {line}")