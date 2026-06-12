import json

from llm.extractor import extract_segments
from geometry.polygon_builder import build_vertices
from visualization.polygon_plotter import plot_polygon


IMAGE_PATH = input("Enter image path:")


segments = extract_segments(IMAGE_PATH)

with open(
    "output.json",
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        segments,
        f,
        indent=4,
        ensure_ascii=False
    )

vertices = build_vertices(segments)

print("Vertices:")

for vertex in vertices:
    print(vertex)

plot_polygon(vertices)