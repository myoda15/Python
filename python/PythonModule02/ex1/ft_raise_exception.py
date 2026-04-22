def input_temperature(temp_str: str) -> int:
    temp = int(temp_str)
    if temp < 0:
        raise ValueError(f"Temperature {temp}°C is too cold (below 0°C)")
    if temp > 40:
        raise ValueError(f"Temperature {temp}°C is too hot (above 40°C)")
    return temp


def test_temperature() -> None:
    for temp in ["25", "abc", "100", "-50"]:
        try:
            result = input_temperature(temp)
            print(f"Temperature: {result}°C")
        except ValueError as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    print("=== Temperature Validation System ===")
    test_temperature()
