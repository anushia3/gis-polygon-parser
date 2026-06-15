from pdf2image import convert_from_path


def pdf_to_images(pdf_path):

    pages = convert_from_path(
        pdf_path,
        dpi=100,
        poppler_path=r"C:\Users\anushi.aggarwal\Downloads\Release-26.02.0-0\poppler-26.02.0\Library\bin"
    )

    image_paths = []

    for i, page in enumerate(pages):

        output_path = f"temp_page_{i+1}.png"

        page.save(
            output_path,
            "PNG"
        )

        image_paths.append(output_path)

    return image_paths


if __name__ == "__main__":

    images = pdf_to_images(
        "sample_data/test_survey_description.pdf"
    )

    print(images)