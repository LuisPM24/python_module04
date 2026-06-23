import sys


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>")
        return
    try:
        fd = open(sys.argv[1], 'r')
        print(f"Accessing file '{sys.argv[1]}'")
        content = fd.read()
        print("---")
        print(content)
        print("---")
        fd.close()
        print(f"File {sys.argv[1]} closed.")
    except Exception as e:
        print(f"Error opening file '{sys.argv[1]}': {e}")


if __name__ == "__main__":
    main()
