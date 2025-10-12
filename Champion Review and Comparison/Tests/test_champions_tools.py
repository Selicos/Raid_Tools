import os
import json
import glob
import pytest

# Directories
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "Champion Review and Comparison"))
CHAMPIONS_DIR = os.path.join(BASE_DIR, "Champions")
PROMPT_DIR = os.path.join(BASE_DIR, "prompt")
MODULES_DIR = os.path.join(BASE_DIR, "modules")
OWNED_LIST = os.path.join(CHAMPIONS_DIR, "Owned_Champions", "Owned_Champion_list.md")
ALL_MODULES_MD = os.path.join(MODULES_DIR, "ALL_MODULES.md")

# 1. Champion JSON Schema Validation (basic required fields)
REQUIRED_FIELDS = [
    "champion", "owned", "overview", "skills", "team_inputs", "mastery_simulation",
    "clan_boss", "synergy", "investment", "intelligence", "turn_meter",
    "utility_comparison", "ratings", "final_summary", "synergy_engine"
]

def get_champion_json_files():
    return glob.glob(os.path.join(CHAMPIONS_DIR, "*.json"))

def get_prompt_files():
    return glob.glob(os.path.join(PROMPT_DIR, "*.md"))

def test_champion_json_schema():
    """Test that all champion JSON files have required fields."""
    for path in get_champion_json_files():
        with open(path, encoding="utf-8") as f:
            data = json.load(f)
        for field in REQUIRED_FIELDS:
            assert field in data, f"{os.path.basename(path)} missing field: {field}"

def test_no_duplicate_champion_files():
    """Test that there are no duplicate champion files (case-insensitive)."""
    files = [os.path.basename(f).lower() for f in get_champion_json_files()]
    assert len(files) == len(set(files)), "Duplicate champion JSON files found (case-insensitive)"

def test_prompt_file_consistency():
    """Test that every champion JSON has a corresponding prompt file."""
    champion_names = {os.path.splitext(os.path.basename(f))[0].lower() for f in get_champion_json_files()}
    prompt_names = {os.path.splitext(os.path.basename(f))[0].lower() for f in get_prompt_files()}
    missing_prompts = champion_names - prompt_names
    assert not missing_prompts, f"Missing prompt files for: {missing_prompts}"

def test_module_merge_integrity():
    """Test that ALL_MODULES.md contains all module headers."""
    if not os.path.exists(ALL_MODULES_MD):
        pytest.skip("ALL_MODULES.md not found")
    with open(ALL_MODULES_MD, encoding="utf-8") as f:
        content = f.read()
    for i in range(14):
        assert f"Module {i}" in content, f"Module {i} missing from ALL_MODULES.md"

def test_owned_champion_list_sync():
    """Test that all champions in Owned_Champion_list.md exist as JSON files."""
    if not os.path.exists(OWNED_LIST):
        pytest.skip("Owned_Champion_list.md not found")
    with open(OWNED_LIST, encoding="utf-8") as f:
        lines = f.readlines()
    owned = {line.strip('- \n').split(' (')[0].lower() for line in lines if line.strip().startswith('-')}
    champion_files = {os.path.splitext(os.path.basename(f))[0].lower() for f in get_champion_json_files()}
    missing = owned - champion_files
    assert not missing, f"Owned champions missing JSON files: {missing}"