from ollama import chat
from llm.prompts import EXTRACTION_PROMPT
import json


def extract_segments(image_paths):

    if isinstance(image_paths, str):
        image_paths = [image_paths]

    response = chat(
        model="qwen2.5vl:latest",
        messages=[
            {
                "role": "user",
                "content": EXTRACTION_PROMPT,
                "images": image_paths
            }
        ]
    )

    content = response["message"]["content"]

    print("\n=== RAW MODEL OUTPUT ===\n")
    print(content)
    print("\n========================\n")

    content = content.replace("```json", "")
    content = content.replace("```", "")
    content = content.replace('"minutes": 00', '"minutes": 0')
    content = content.strip()

    data = json.loads(content)

    return data