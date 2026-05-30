def garden_operations(operation_number: int) -> None:
    if operation_number == 0:
        int("abc")
    elif operation_number == 1:
        result = 10 / 0
        print(result)
    elif operation_number == 2:
        with open("/non/existent/file") as f:
            print(f.read())
    elif operation_number == 3:
        result = "plant" + 42  # type: ignore
        print(result)


def test_error_types() -> None:
    for i in range(5):
        print(f"Testing operation {i}...")
        try:
            garden_operations(i)
            print("Operation completed successfully")
        except (
            ValueError, ZeroDivisionError, FileNotFoundError, TypeError
        ) as e:
            print(f"Caught {type(e).__name__}: {e}")
    print("All error types tested successfully!")


if __name__ == "__main__":
    print("=== Garden Error Types Demo ===")
    test_error_types()
