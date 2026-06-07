import sys
from .repository import init
from .index import add
from .commits import commit, log
from .diff import diff

def main():
    args = sys.argv[1:]

    if not args:
        print("Usage: python -m src.cli <command>")
        print("Commands: init, add, commit, log, diff")
        return

    command = args[0]

    if command == "init":
        init()

    elif command == "add":
        if len(args) < 2:
            print("Usage: python -m src.cli add <file> or .")
            return
        add(args[1:])

    elif command == "commit":
        if len(args) < 2:
            print("Usage: python -m src.cli commit <message>")
            return
        message = " ".join(args[1:])
        commit(message)

    elif command == "log":
        log()

    elif command == "diff":
        diff()

    else:
        print(f"Unknown command: {command}")

if __name__ == "__main__":
    main()