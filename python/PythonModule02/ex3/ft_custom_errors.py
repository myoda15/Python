class GardenError(Exception):
    def __init__(self, message: str = "Unknown garden error") -> None:
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message: str = "Unknown plant error") -> None:
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message: str = "Unknown water error") -> None:
        super().__init__(message)


def check_plant(name: str) -> None:
    if not name:
        raise PlantError("Plant name cannot be empty")


def check_water(level: int) -> None:
    if level <= 0:
        raise WaterError("Water level must be positive")


def test_custom_errors() -> None:
    print("--- Testing PlantError ---")
    try:
        check_plant("")
    except GardenError as e:
        print(f"Caught GardenError: {e}")

    print("--- Testing WaterError ---")
    try:
        check_water(0)
    except GardenError as e:
        print(f"Caught GardenError: {e}")

    print("--- Testing default messages ---")
    try:
        raise PlantError()
    except PlantError as e:
        print(f"PlantError default: {e}")

    try:
        raise WaterError()
    except WaterError as e:
        print(f"WaterError default: {e}")


if __name__ == "__main__":
    print("=== Custom Garden Errors ===")
    test_custom_errors()
