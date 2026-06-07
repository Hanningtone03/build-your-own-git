# Build Your Own Git

A Git version control system built from scratch in Python; supports init, add, commit, log and diff.

## How it works

Git stores every file as a content-addressed object identified by its SHA1 hash. This project implements that from scratch:

- Initializes a `.vgit` repository with an object store and HEAD reference
- Hashes file contents and stores them as compressed blob objects
- Builds tree objects representing directory snapshots
- Creates commit objects pointing to trees and parent commits
- Traverses commit history for the log command
- Compares current files against stored objects for diff

## Project structure

```
src/
├── cli.py
├── repository.py
├── objects.py
├── index.py
├── commits.py
└── diff.py
```

## Running locally

```bash
python -m src.cli init
python -m src.cli add .
python -m src.cli commit "your message"
python -m src.cli log
python -m src.cli diff
```

## Example

```bash
python -m src.cli init
echo "hello" > test.txt
python -m src.cli add test.txt
python -m src.cli commit "initial commit"
python -m src.cli log
echo "hello updated" > test.txt
python -m src.cli diff
```

## Tech

- Python 3
- `hashlib` module (SHA1 hashing)
- `zlib` module (object compression)
- No external dependencies
