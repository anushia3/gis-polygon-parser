import json
import os
import tempfile

import streamlit as st

from llm.extractor import extract_segments
from geometry.polygon_builder import build_vertices
from visualization.polygon_plotter import plot_polygon
from pdf.pdf_converter import pdf_to_images
from export.shapefile_exporter import export_shapefile


st.set_page_config(page_title="GIS Survey Geometry Extractor")

st.title("GIS Survey Geometry Extractor")

uploaded_file = st.file_uploader(
    "Upload a PDF or image",
    type=["pdf", "png", "jpg", "jpeg"]
)

if uploaded_file is not None:

    if st.button("Process File"):

        with tempfile.NamedTemporaryFile(
            delete=False,
            suffix=os.path.splitext(uploaded_file.name)[1]
        ) as tmp:

            tmp.write(uploaded_file.getbuffer())

            file_path = tmp.name

        if file_path.lower().endswith(".pdf"):

            image_paths = pdf_to_images(file_path)

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

        export_shapefile(vertices)

        st.success("Extraction Complete!")

        st.subheader("Extracted JSON")

        st.json(segments)

        st.subheader("Vertices")

        st.write(vertices)

        st.info(
            "The plot window will open separately."
        )