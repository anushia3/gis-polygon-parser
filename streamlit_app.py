import json
import os
import tempfile

import streamlit as st

from llm.extractor import extract_segments
from geometry.polygon_builder import build_vertices
from visualization.polygon_plotter import plot_polygon
from pdf.pdf_converter import pdf_to_images
from export.shapefile_exporter import export_shapefile


st.set_page_config(
    page_title="GIS Survey Geometry Extractor",
    page_icon="🗺️",
    layout="wide"
)

st.title("🗺️ GIS Survey Geometry Extractor")

st.write(
    "Upload a scanned survey PDF or image to extract boundary "
    "descriptions, generate geometry, and create a shapefile."
)

uploaded_file = st.file_uploader(
    "Upload a PDF or image",
    type=["pdf", "png", "jpg", "jpeg"]
)

if uploaded_file is not None:

    st.success(f"Uploaded: {uploaded_file.name}")

    if st.button("🚀 Process File"):

        status = st.empty()

        with st.spinner("Processing..."):

            status.info("📄 Preparing file...")

            with tempfile.NamedTemporaryFile(
                delete=False,
                suffix=os.path.splitext(uploaded_file.name)[1]
            ) as tmp:

                tmp.write(uploaded_file.getbuffer())

                file_path = tmp.name

            if file_path.lower().endswith(".pdf"):

                status.info("📄 Converting PDF into images...")

                image_paths = pdf_to_images(file_path)

                status.info("🤖 Extracting survey information...")

                segments = extract_segments(image_paths)

            else:

                status.info("🤖 Extracting survey information...")

                segments = extract_segments(file_path)

            status.info("💾 Saving JSON...")

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

            status.info("📐 Building geometry...")

            vertices = build_vertices(segments)

            status.info("🗂️ Generating shapefile...")

            export_shapefile(vertices)

        status.success("✅ Extraction Complete!")

        st.subheader("Extracted JSON")
        st.json(segments)

        st.subheader("Vertices")
        st.write(vertices)

        st.subheader("📈 Geometry Plot")

        fig = plot_polygon(vertices, show=False)

        st.pyplot(fig)