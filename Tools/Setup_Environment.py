"""
Setup_Environment.py

Sets up the Python environment for Raid Tools project according to current requirements.

- Python 3.9+
- Installs all packages in requirements.txt
- Installs Black, flake8, pytest if missing
- Creates .venv if not present
- Creates .vscode/settings.json, tasks.json, extensions.json with recommended config
- Validates Makefile and README.md presence
- Prompts user to open workspace in VS Code and install recommended extensions
"""

import os
import sys
import subprocess
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
VENV_DIR = REPO_ROOT / ".venv"
REQUIREMENTS = REPO_ROOT / "requirements.txt"
VS_CODE_DIR = REPO_ROOT / ".vscode"
MAKEFILE = REPO_ROOT / "Makefile"
README = REPO_ROOT / "README.md"


RECOMMENDED_EXTENSIONS = [
    "ms-python.python",
    "ms-python.vscode-pylance",
    "ms-toolsai.jupyter"
]

SETTINGS_JSON = VS_CODE_DIR / "settings.json"
TASKS_JSON = VS_CODE_DIR / "tasks.json"
EXTENSIONS_JSON = VS_CODE_DIR / "extensions.json"


def run(cmd):
    print(f"Running: {cmd}")
    result = subprocess.run(cmd, shell=True)
    if result.returncode != 0:
        print(f"Error running: {cmd}")
        sys.exit(result.returncode)


def create_venv():
    if not VENV_DIR.exists():
        print("Creating virtual environment...")
        run(f"python -m venv {VENV_DIR}")
    else:
        print("Virtual environment already exists.")


def activate_venv():
    # On Windows, activate using Scripts\activate.bat
    # On Unix, activate using bin/activate
    if os.name == "nt":
        activate_script = VENV_DIR / "Scripts" / "activate.bat"
        if activate_script.exists():
            print(f"To activate the virtual environment, run:")
            print(f"    {activate_script}")
        else:
            print("activate.bat not found. Please check your venv setup.")
    else:
        activate_script = VENV_DIR / "bin" / "activate"
        if activate_script.exists():
            print(f"To activate the virtual environment, run:")
            print(f"    source {activate_script}")
        else:
            print("activate script not found. Please check your venv setup.")


def install_requirements():
    pip_path = (
        VENV_DIR / "Scripts" / "pip.exe"
        if os.name == "nt"
        else VENV_DIR / "bin" / "pip"
    )
    if not pip_path.exists():
        pip_path = "pip"
    # Ensure pip is upgraded before installing packages
    run(f"{pip_path} install --upgrade pip")
    # Install requirements and core dev tools (including jsonschema for schema validation)
    run(f"{pip_path} install -r {REQUIREMENTS}")
    run(f"{pip_path} install black flake8 pytest jsonschema")


def create_vscode_configs():
    VS_CODE_DIR.mkdir(exist_ok=True)
    if not SETTINGS_JSON.exists():
        interpreter_path = str(
            VENV_DIR / "Scripts" / "python.exe"
            if os.name == "nt"
            else VENV_DIR / "bin" / "python"
        )
        SETTINGS_JSON.write_text(
            f"""{{
  "python.defaultInterpreterPath": "{interpreter_path}",
  "python.linting.enabled": true,
  "python.linting.flake8Enabled": true,
  "python.formatting.provider": "black"
}}"""
        )
        # Always write the current tasks.json content
        TASKS_JSON.write_text(
                '{\n'
                '  "version": "2.0.0",\n'
                '  "tasks": [\n'
                '    {\n'
                '      "label": "Run Champion Intake",\n'
                '      "type": "shell",\n'
                '      "command": "python ChampionIntake/Champ_Intake.py",\n'
                '      "group": "build",\n'
                '      "presentation": { "reveal": "always" },\n'
                '      "problemMatcher": []\n'
                '    },\n'
                '    {\n'
                '      "label": "Run Champion Turn Analysis",\n'
                '      "type": "shell",\n'
                '      "command": "python ChampionTurnAnalysis/ChampionTurnAnalysis.py",\n'
                '      "group": "build",\n'
                '      "presentation": { "reveal": "always" },\n'
                '      "problemMatcher": []\n'
                '    },\n'
                '    {\n'
                '      "label": "Generate Champion Summaries",\n'
                '      "type": "shell",\n'
                '      "command": "python ChampionSummary/generateChampionSummaries.py",\n'
                '      "group": "build",\n'
                '      "presentation": { "reveal": "always" },\n'
                '      "problemMatcher": []\n'
                '    },\n'
                '    {\n'
                '      "label": "Setup Environment",\n'
                '      "type": "shell",\n'
                '      "command": "python Tools/Setup_Environment.py",\n'
                '      "group": { "kind": "build", "isDefault": false },\n'
                '      "presentation": { "reveal": "never" },\n'
                '      "problemMatcher": []\n'
                '    },\n'
                '    {\n'
                '      "label": "Validate JSON",\n'
                '      "type": "shell",\n'
                '      "command": "python Tools/validate_json.py",\n'
                '      "group": "build",\n'
                '      "presentation": { "reveal": "always" },\n'
                '      "problemMatcher": []\n'
                '    },\n'
                '    {\n'
                '      "label": "First Run: Setup & Activation Instructions",\n'
                '      "type": "shell",\n'
                '      "command": "echo To activate the virtual environment, run: .\\.venv\\Scripts\\Activate (Windows) or source .venv/bin/activate (macOS/Linux)",\n'
                '      "group": { "kind": "build", "isDefault": true },\n'
                '      "presentation": { "reveal": "always" },\n'
                '      "problemMatcher": [],\n'
                '      "dependsOn": [ "Setup Environment" ],\n'
                '      "dependsOrder": "sequence"\n'
                '    }\n'
                '  ],\n'
                '  "inputs": [\n'
                '    {\n'
                '      "id": "ChampName",\n'
                '      "type": "promptString",\n'
                '      "description": "Enter the champion name",\n'
                '      "default": "Brogni"\n'
                '    },\n'
                '    {\n'
                '      "id": "Rarity",\n'
                '      "type": "promptString",\n'
                '      "description": "Enter rarity (6/Mythic, 5/Legendary, 4/Epic, 3/Rare)",\n'
                '      "default": "5"\n'
                '    }\n'
                '  ]\n'
                '}\n'
        )
        if not EXTENSIONS_JSON.exists():
                EXTENSIONS_JSON.write_text(
                        """{
    "recommendations": [
        "ms-python.python",
        "ms-python.vscode-pylance",
        "ms-toolsai.jupyter"
    ]
}"""
                )


def validate_files():
    missing = []
    for f in [REQUIREMENTS, MAKEFILE, README]:
        if not f.exists():
            missing.append(str(f))
    if missing:
        print("Missing required files:", ", ".join(missing))
        sys.exit(1)


def main():
    print("Raid Tools Environment Setup")
    validate_files()
    create_venv()
    activate_venv()
    install_requirements()
    create_vscode_configs()
    print(
        "Setup complete. Open the workspace in VS Code and install all recommended extensions when prompted."
    )
    print("\n--- VS Code Integration ---")
    print(
        "If you open this folder in VS Code, it will detect the .venv and prompt you to use it as the Python interpreter."
    )
    print(
        "If not prompted, use Ctrl+Shift+P > 'Python: Select Interpreter' and choose the .venv Python."
    )
    print(
        "After selecting the interpreter, all VS Code terminals and tasks will use the virtual environment automatically."
    )
    print(
        "You can run all tools and tests from the VS Code terminal or using the provided tasks."
    )


if __name__ == "__main__":
    main()
