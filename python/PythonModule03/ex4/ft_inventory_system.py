import sys


if __name__ == "__main__":
    print("=== Inventory System Analysis ===")
    inventory: dict[str, int] = {}

    for arg in sys.argv[1:]:
        parts: list[str] = arg.split(":")
        if len(parts) != 2 or not parts[0] or not parts[1]:
            print(f"Error - invalid parameter '{arg}'")
            continue
        item: str = parts[0]
        qty_str: str = parts[1]
        if item in inventory:
            print(f"Redundant item '{item}' - discarding")
            continue
        try:
            qty: int = int(qty_str)
            inventory[item] = qty
        except ValueError as e:
            print(f"Quantity error for '{item}': {e}")

    if len(inventory) == 0:
        print("Inventory is empty.")
    else:
        print(f"Got inventory: {inventory}")

        item_list: list[str] = list(inventory.keys())
        print(f"Item list: {item_list}")

        total: int = sum(inventory.values())
        print(f"Total quantity of the {len(inventory)} items: {total}")

        for item_name, qty_val in inventory.items():
            pct: float = round(qty_val / total * 100, 1)
            print(f"Item {item_name} represents {pct}%")

        most: str = item_list[0]
        least: str = item_list[0]
        for item_name in item_list:
            if inventory[item_name] > inventory[most]:
                most = item_name
            if inventory[item_name] < inventory[least]:
                least = item_name
        print(f"Item most abundant: {most} with quantity {inventory[most]}")
        print(
            f"Item least abundant: {least} with quantity {inventory[least]}"
        )

        inventory.update({"magic_item": 1})
        print(f"Updated inventory: {inventory}")
