![CI](https://github.com/Hanningtone03/build-your-own-git/actions/workflows/ci.yml/badge.svg)

# Build Your Own Git

A Git version control system in Python; init, add, commit, log, diff.

## How it works

Every file is SHA1-hashed and stored as a compressed blob. Directories become tree objects. Commits point to trees and parent commits. The log walks the commit chain. Diff compares working files against stored blobs.

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

## Tech

- Python 3
- `hashlib`, `zlib` modules
- No external dependencies
