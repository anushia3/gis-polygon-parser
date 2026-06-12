def bearing_to_decimal(degrees, minutes):
    return degrees + minutes / 60

def bearing_to_angle(
    direction_ns,
    degrees,
    minutes,
    direction_ew
):
    angle = bearing_to_decimal(degrees, minutes)

    if direction_ns == "N" and direction_ew == "E":
        return 90 - angle

    if direction_ns == "N" and direction_ew == "W":
        return 90 + angle

    if direction_ns == "S" and direction_ew == "E":
        return 270 + angle

    if direction_ns == "S" and direction_ew == "W":
        return 270 - angle

if __name__ == "__main__":
    print(
        bearing_to_angle(
            "N",
            35,
            15,
            "E"
        )
    )