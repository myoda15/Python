def input_temperature(temp_str: str) -> int:
    return int(temp_str)


def test_temperature() -> None:
    for temp in ["25", "abc"]:
        try:
            result = input_temperature(temp)
            print(f"Temperature: {result}°C")
        except ValueError as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    print("=== Temperature Input System ===")
    test_temperature()
