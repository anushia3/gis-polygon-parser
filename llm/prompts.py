EXTRACTION_PROMPT = """
You are a GIS land description parser.

Analyze the image.

Extract:

- bearings
- distances
- coordinates
- polygon descriptions

Return ONLY valid JSON.

Example:

{
  "segments": [
    {
      "bearing": "N35E",
      "distance": 150
    }
  ]
}
"""