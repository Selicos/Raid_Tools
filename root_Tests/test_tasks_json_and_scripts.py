"""
Test that all VS Code tasks in .vscode/tasks.json reference valid script paths and that those scripts exist in the workspace.
"""
import json
import os
import pytest

WORKSPACE_ROOT = os.path.dirname(os.path.dirname(__file__))
TASKS_PATH = os.path.join(WORKSPACE_ROOT, ".vscode", "tasks.json")

@pytest.mark.parametrize("task_label, script_path", [
    ("Run Champion Intake", "ChampionIntake/Champ_Intake.py"),
    ("Run Champion Comparison Tracker", "ChampionIntake/Comparisons/Champ_Comparison_Track_owned.py"),
    ("Cleanup Duplicate Champions", "Tools/cleanup_duplicate_champions.py"),
    ("Run Champion Analysis Tool", "ChampionAnalysisTool/championAnalysis.py"),
    ("Generate Champion Summaries", "ChampionSummary/generateChampionSummaries.py"),
    ("Setup Environment", "Tools/Setup_Environment.py"),
    ("Validate Champion JSON", "Tools/validate_json.py"),
    ("Test Environment Setup and Requirements", "root_Tests/test_env_setup_and_requirements.py"),
])
def test_task_script_exists(task_label, script_path):
    script_abs = os.path.join(WORKSPACE_ROOT, script_path)
    assert os.path.exists(script_abs), f"Task '{task_label}' references missing script: {script_path}"

def test_tasks_json_valid():
    with open(TASKS_PATH, encoding="utf-8") as f:
        data = json.load(f)
    assert "tasks" in data, ".vscode/tasks.json missing 'tasks' key"
    assert isinstance(data["tasks"], list), "'tasks' should be a list"
