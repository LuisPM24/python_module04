import sys
import typing


def main() -> None:
    new_text: str = ""
    count: int = 0

    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>")
        return
    print("=== Cyber Archives Recovery ===")
    try:
        print(f"Accessing file '{sys.argv[1]}'")
        fd: typing.TextIO = open(sys.argv[1], 'r')
        content = fd.read()
        print("---")
        print(content)
        print("---")
        fd.close()
        print(f"File '{sys.argv[1]}' closed.\n")
        while count < len(content):
            if content[count] == '\n':
                new_text += "#\n"
            else:
                new_text += content[count]
            count += 1
        print("Transform data:\n---\n")
        print(new_text)
        print("---")
        sys.stdout.write("Enter new file name (or empty): ")
        sys.stdout.flush()
        new_name: str = sys.stdin.readline().strip()
        if (new_name):
            print(f"Saving data to '{new_name}'")
            try:
                new_file: typing.TextIO = open(new_name, 'w')
                new_file.write(new_text + "\n")
                new_file.close()
                print(f"Data saved in file '{new_name}'")
            except OSError as e:
                print(f"Error generating file {new_name}: {e}")
        else:
            print("Data was not saved")
    except OSError as e:
        print(f"Error opening file '{sys.argv[1]}': {e}")


if __name__ == "__main__":
    main()
