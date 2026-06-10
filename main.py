from ollama import chat

response = chat(
    model="qwen2.5vl:latest",
    messages=[
        {
            "role": "user",
            "content": """
Read this image.

Extract all bearings and distances.

Return ONLY JSON.
""",
            "images": ["sample_data/test.png"]
        }
    ]
)

print(response["message"]["content"])