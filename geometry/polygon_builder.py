from geometry.bearing_parser import bearing_to_angle
from geometry.coordinate_builder import next_coordinate

def build_vertices(segments):
    vertices = [(0, 0)]

    current_x = 0
    current_y = 0

    for segment in segments:

        angle = bearing_to_angle(
            segment["direction_ns"],
            segment["degrees"],
            segment["minutes"],
            segment["direction_ew"]
        )

        current_x, current_y = next_coordinate(
            current_x,
            current_y,
            angle,
            segment["distance"]
        )

        vertices.append(
            (
                current_x,
                current_y
            )
        )

    return vertices
