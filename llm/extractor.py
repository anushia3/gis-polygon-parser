from ollama import chat
from llm.prompts import EXTRACTION_PROMPT
import json


def extract_segments(image_path):

    response = chat(
        model="qwen2.5vl:latest",
        messages=[
            {
                "role": "user",
                "content": EXTRACTION_PROMPT,
                "images": [image_path]
            }
        ]
    )

    content = response["message"]["content"]

    content = content.replace("```json", "")
    content = content.replace("```", "")
    content = content.strip()

    print("\n=== RAW MODEL OUTPUT ===\n")
    print(content)
    print("\n========================\n")
    
    content = content.replace('"minutes": 00', '"minutes": 0')
    data = json.loads(content)

    return data