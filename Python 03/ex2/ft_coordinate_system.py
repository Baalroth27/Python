import math


def measure_distance(
        a: tuple[float, ...], b: tuple[float, ...] = (0.0, 0.0, 0.0)
        ) -> float:
    x1, y1, z1 = a
    x2, y2, z2 = b
    return math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)


def get_player_pos() -> tuple[float, ...]:
    while True:
        line = input("Enter new coordinates as floats in format 'x,y,z': ")
        parts = line.split(",")
        if len(parts) == 3:
            coords: tuple[float, ...] = ()
            try:
                for part in parts:
                    coords += (float(part),)
                return coords
            except ValueError as e:
                print(f"Error on parameter '{part}': {e}")
        else:
            print("Invalid syntax")


if __name__ == "__main__":
    try:
        print("=== Game Coordinate System ===")
        print("")
        print("Get a first set of coordinates")
        pos_1 = get_player_pos()
        print(f"Got a first tuple: {pos_1}")
        print(f"It includes: X={pos_1[0]}, Y={pos_1[1]}, Z={pos_1[2]}")
        print(f"Distance to center: {round(measure_distance(pos_1), 4)}")
        print("")
        print("Get a second set of coordinates")
        pos_2 = get_player_pos()
        print(f"Distance between the 2 sets of coordinates:"
              f" {round(measure_distance(pos_1, pos_2), 4)}")
    except EOFError:
        print()
