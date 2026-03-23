import math


def parse_coord(s: str) -> tuple[float, float, float] | None:
    s = s.strip()
    parts = s.split(",")
    if len(parts) != 3:
        print("Invalid syntax")
        return None

    parsed: list[float] = []
    for val in parts:
        try:
            parsed.append(float(val))
        except ValueError:
            print(
                f"Error on parameter '{val}': "
                f"could not convert string to float: '{val}'"
            )
            return None

    return tuple(parsed)


def get_player_pos():
    coord: tuple[float, float, float] = None
    coord2: tuple[float, float, float] = None
    print("=== Game Coordinate System ===\n")
    print("Get a first set of coordinates")
    while coord is None:
        coord = parse_coord(
            input("Enter new coordinates as floats in format 'x,y,z': ")
        )
    print(f"Got a first tuple: {coord}")
    x, y, z = coord[0], coord[1], coord[2]
    print(f"It includes: X={x}, Y={y}, Z={z}")
    dist = math.sqrt((x - 0) ** 2 + (y - 0) ** 2 + (z - 0) ** 2)
    print(f"Distance to center: {round(dist, 4)}\n")

    print("Get a second set of coordinates")
    while coord2 is None:
        coord2 = parse_coord(
            input("Enter new coordinates as floats in format 'x,y,z': ")
        )
    x2, y2, z2 = coord2[0], coord2[1], coord2[2]
    dist = math.sqrt((x - x2) ** 2 + (y - y2) ** 2 + (z - z2) ** 2)
    print(f"Distance between the 2 sets of coordinates: {round(dist, 4)}")


if __name__ == "__main__":
    get_player_pos()
