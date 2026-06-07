import os
import json
import time
from .objects import hash_object, hash_tree, read_object
from .repository import get_head, set_head
from .index import get_index

def commit(message, author="Hanningtone"):
    index = get_index()
    if not index:
        print("Nothing to commit.")
        return

    entries = [(name, sha1, "100644") for name, sha1 in index.items()]
    tree_sha1 = hash_tree(entries)

    parent = get_head()
    commit_data = {
        "tree": tree_sha1,
        "parent": parent,
        "author": author,
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
        "message": message
    }
    commit_json = json.dumps(commit_data, indent=2)
    commit_sha1 = hash_object(commit_json, obj_type="commit")
    set_head(commit_sha1)
    print(f"Committed {commit_sha1[:7]} — {message}")
    return commit_sha1

def log():
    sha1 = get_head()
    if not sha1:
        print("No commits yet.")
        return
    while sha1:
        try:
            obj_type, data = read_object(sha1)
            commit_data = json.loads(data.decode())
            print(f"commit {sha1}")
            print(f"Author: {commit_data['author']}")
            print(f"Date:   {commit_data['timestamp']}")
            print(f"\n    {commit_data['message']}\n")
            sha1 = commit_data.get("parent")
        except Exception as e:
            print(f"Error reading commit: {e}")
            break