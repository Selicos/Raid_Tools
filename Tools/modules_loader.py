import os
import json
from pathlib import Path

# Load all module templates from a single JSON file for prompt generation
MODULES_JSON = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "data", "templates", "modules.json"))

def load_modules_from_json():
    if not os.path.exists(MODULES_JSON):
        raise FileNotFoundError(f"Module JSON not found: {MODULES_JSON}\nRun combine_modules_to_json.py to generate it.")
    with open(MODULES_JSON, encoding="utf-8") as f:
        return json.load(f)
