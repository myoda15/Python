import sys
import typing


def read_file(filename: str) -> typing.Optional[str]:
    print("=== Cyber Archives Recovery & Preservation ===")
    print(f"Accessing file '{filename}'")
    file: typing.IO[str]
    try:
        file = open(filename, 'r')
    except OSError as e:
        print(f"Error opening file '{filename}': {e}")
        return None
    content: str = file.read()
    file.close()
    print("---")
    print(content, end='')
    print("---")
    print(f"File '{filename}' closed.")
    return content


def transform_content(content: str) -> str:
    lines: list[str] = content.splitlines()
    new_lines: list[str] = [line + '#' for line in lines]
    return '\n'.join(new_lines) + '\n'


def save_content(new_content: str) -> None:
    print()
    print("Transform data:")
    print("---")
    print(new_content, end='')
    print("---")
    new_filename: str = input("Enter new file name (or empty): ")
    if not new_filename:
        print("Not saving data.")
        return
    file: typing.IO[str]
    print(f"Saving data to '{new_filename}'")
    try:
        file = open(new_filename, 'w')
    except OSError as e:
        print(f"Error opening file '{new_filename}': {e}")
        print("Data not saved.")
        return
    file.write(new_content)
    file.close()
    print(f"Data saved in file '{new_filename}'.")


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_archive_creation.py <file>")
        return
    content: typing.Optional[str] = read_file(sys.argv[1])
    if content is not None:
        new_content: str = transform_content(content)
        save_content(new_content)


if __name__ == "__main__":
    main()
