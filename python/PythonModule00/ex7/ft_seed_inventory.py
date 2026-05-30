def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    name = seed_type.capitalize()
    if unit == "packets":
        print(f"{name} seeds: {quantity} packets available")
    elif unit == "grams":
        print(f"{name} seeds: {quantity} grams total")
    elif unit == "area":
        print(f"{name} seeds: covers {quantity} square meters")
    else:
        print("Unknown unit type")

if __name__ == "__main__":
    ft_seed_inventory("tomato", 5, "packets")
    ft_seed_inventory("wheat", 200, "grams")
    ft_seed_inventory("sunflower", 10, "area")
    ft_seed_inventory("rose", 3, "boxes")