def garden_operations(operation_number: int) -> None:
    if operation_number == 0:
        raise ValueError("Invalid garden operation")
    elif operation_number == 1:
        result = 10 / 0
        print(result)
    elif operation_number == 2:
        with open("nonexistent_plant.txt") as f:
            print(f.read())
    elif operation_number == 3:
        result = "plant" + 42  # type: ignore
        print(result)


def test_error_types() -> None:
    for i in range(4):
        try:
            garden_operations(i)
        except (
            ValueError, ZeroDivisionError, FileNotFoundError, TypeError
        ) as e:
            print(f"Caught {type(e).__name__}: {e}")


if __name__ == "__main__":
    print("=== Garden Error Types ===")
    test_error_types()
