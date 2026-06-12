from ollama import chat
from llm.prompts import EXTRACTION_PROMPT
import json

response = chat(
    model="qwen2.5vl:latest",
    messages=[
        {
            "role": "user",
            "content": EXTRACTION_PROMPT,
            "images": ["sample_data/test.png"]
        }
    ]
)

content = response["message"]["content"]

# Remove markdown wrappers if the model returns them
content = content.replace("```json", "")
content = content.replace("```", "")
content = content.strip()

# Convert JSON string -> Python object
data = json.loads(content)

# Save JSON to file
with open("output.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4, ensure_ascii=False)

print("Parsed successfully!")
print("Type:", type(data))
print("Number of segments:", len(data))
print()

# Print each extracted segment
for i, segment in enumerate(data, start=1):
    print(f"Segment {i}")
    print(segment)
    print()