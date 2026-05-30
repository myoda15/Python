def secure_archive(
    filename: str,
    mode: str = "read",
    content: str = ""
) -> tuple[bool, str]:
    try:
        if mode == "write":
            with open(filename, 'w') as f:
                f.write(content)
            return (True, "Content successfully written to file")
        else:
            with open(filename, 'r') as f:
                data: str = f.read()
            return (True, data)
    except OSError as e:
        return (False, str(e))


def main() -> None:
    print("=== Cyber Archives Security ===")
    print()

    print("Using 'secure_archive' to read from a nonexistent file:")
    result: tuple[bool, str] = secure_archive('/not/existing/file')
    print(result)
    print()

    print("Using 'secure_archive' to read from an inaccessible file:")
    result = secure_archive('/etc/master.passwd')
    print(result)
    print()

    print("Using 'secure_archive' to read from a regular file:")
    result = secure_archive('ancient_fragment.txt')
    print(result)
    print()

    print(
        "Using 'secure_archive' to write previous content to a new file:"
    )
    if result[0]:
        write_result: tuple[bool, str] = secure_archive(
            'new_vault.txt', 'write', result[1]
        )
        print(write_result)


if __name__ == "__main__":
    main()
