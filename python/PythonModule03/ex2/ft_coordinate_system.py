import math


def get_player_pos() -> tuple[float, float, float]:
    while True:
        raw: str = input("Enter new coordinates as floats in format 'x,y,z': ")
        parts: list[str] = raw.split(",")
        if len(parts) != 3:
            print("Invalid syntax")
            continue
        try:
            x: float = float(parts[0].strip())
            y: float = float(parts[1].strip())
            z: float = float(parts[2].strip())
            return (x, y, z)
        except ValueError as e:
            for part in parts:
                try:
                    float(part.strip())
                except ValueError:
                    print(
                        f"Error on parameter '{part.strip()}': {e}"
                    )
                    break


if __name__ == "__main__":
    print("=== Game Coordinate System ===")

    print("Get a first set of coordinates")
    pos1: tuple[float, float, float] = get_player_pos()
    print(f"Got a first tuple: {pos1}")
    print(f"It includes: X={pos1[0]}, Y={pos1[1]}, Z={pos1[2]}")
    dist1: float = round(
        math.sqrt(pos1[0] ** 2 + pos1[1] ** 2 + pos1[2] ** 2), 4
    )
    print(f"Distance to center: {dist1}")

    print("Get a second set of coordinates")
    pos2: tuple[float, float, float] = get_player_pos()
    dist2: float = round(
        math.sqrt(
            (pos2[0] - pos1[0]) ** 2
            + (pos2[1] - pos1[1]) ** 2
            + (pos2[2] - pos1[2]) ** 2
        ),
        4,
    )
    print(f"Distance between the 2 sets of coordinates: {dist2}")
