import json

from llm.extractor import extract_segments
from geometry.polygon_builder import build_vertices
from visualization.polygon_plotter import plot_polygon
from pdf.pdf_converter import pdf_to_images


file_path = input("Enter file path: ")

if file_path.lower().endswith(".pdf"):

    image_paths = pdf_to_images(file_path)

    print("Converted pages:")
    print(image_paths)

    segments = extract_segments(image_paths)

else:

    segments = extract_segments(file_path)

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

print("\nVertices:")

for vertex in vertices:
    print(vertex)

plot_polygon(vertices)