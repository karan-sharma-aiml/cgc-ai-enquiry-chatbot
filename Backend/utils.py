import json

# Load JSON file
def load_json(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)


# Format response nicely
def format_response(text):
    return text.strip().capitalize()