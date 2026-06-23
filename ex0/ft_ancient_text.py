import sys
import typing


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>")
        return
    print("=== Cyber Archives Recovery ===")
    try:
        print(f"Accessing file '{sys.argv[1]}'")
        fd: typing.TextIO = open(sys.argv[1], 'r')
        content = fd.read()
        print("---")
        print(content, end="")
        print("---")
        fd.close()
        print(f"File '{sys.argv[1]}' closed.")
    except OSError as e:
        print(f"Error opening file '{sys.argv[1]}': {e}")


if __name__ == "__main__":
    main()
