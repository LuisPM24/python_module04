def secure_archive(file_name: str, action: str = "r", content: str = ""
                   ) -> tuple[bool, str]:
    try:
        if (action == "w"):
            with open(file_name, 'w') as fd:
                fd.write(content)
            return (True, "Content succesfully written to file")
        else:
            with open(file_name, 'r') as fd:
                res = fd.read()
            return (True, res)
    except OSError as e:
        return (False, str(e))


def main() -> None:
    print("=== Cyber Archives Security ===\n")
    print("Using 'secure_archive' to read from a nonexistent file:")
    print(secure_archive("/non/existing/file"), end="\n\n")
    print("Using 'secure_archive' to read from an inaccessible file:")
    print(secure_archive("hola.txt"), end="\n\n")
    print("Using 'secure_archive' to read from a regular file:")
    print(secure_archive("/ex0/ft_ancient_text.py"), end="\n\n")
    print("Using 'secure_archive' to write previous content to a new file:")
    print(secure_archive("hola.txt", "w", "Esto es un hola"))


if __name__ == "__main__":
    main()
