import math


def next_coordinate(x, y, angle_degrees, distance):
    angle_radians = math.radians(angle_degrees)

    dx = distance * math.cos(angle_radians)
    dy = distance * math.sin(angle_radians)

    new_x = x + dx
    new_y = y + dy

    return new_x, new_y

if __name__ == "__main__":
    x, y = next_coordinate(
        0,
        0,
        54.75,
        150
    )

    print(x, y)