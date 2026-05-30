import sys
import typing


def read_file(filename: str) -> None:
    print("=== Cyber Archives Recovery ===")
    print(f"Accessing file '{filename}'")
    file: typing.IO[str]
    try:
        file = open(filename, 'r')
    except OSError as e:
        print(f"Error opening file '{filename}': {e}")
        return
    content: str = file.read()
    file.close()
    print("---")
    print(content, end='')
    print("---")
    print(f"File '{filename}' closed.")


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>")
        return
    read_file(sys.argv[1])


if __name__ == "__main__":
    main()
