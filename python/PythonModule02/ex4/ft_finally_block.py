class PlantError(Exception):
    def __init__(self, message: str = "Unknown plant error") -> None:
        super().__init__(message)


def water_plant(plant_name: str) -> None:
    if not plant_name[0].isupper():
        raise PlantError(
            f"Plant name '{plant_name}' must start with a capital letter"
        )
    print(f"Watering {plant_name}...")


def test_watering_system(plants: list[str]) -> None:
    for plant in plants:
        try:
            water_plant(plant)
            print(f"{plant} watered successfully")
        except PlantError as e:
            print(f"Error: {e}")
            return
        finally:
            print(f"Watering attempt for '{plant}' completed")


if __name__ == "__main__":
    print("=== Garden Watering System ===")
    print("--- Valid plants ---")
    test_watering_system(["Rose", "Oak", "Sunflower"])
    print()
    print("--- Invalid plant in list ---")
    test_watering_system(["Rose", "sunflower", "Oak"])
