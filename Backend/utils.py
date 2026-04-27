#reusable helper functions ko store karna hota hai, jisse code clean aur modular rehta hai.”
import json

# Load JSON file
def load_json(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)


# Format response nicely
def format_response(text):
    return text.strip().capitalize()