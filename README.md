![Python](https://img.shields.io/badge/python-3.10%2B-blue)
![License: CC BY-NC 4.0](https://img.shields.io/badge/License-CC%20BY--NC%204.0-lightgrey.svg)
![Platform](https://img.shields.io/badge/platform-windows%20%7C%20linux%20%7C%20macos-blue)

# Raid Tools: Automation-Ready Boss & Team Guide System

> **Project instructions:** See `.github/copilot-instructions.md` for canonical workflows, templates, and best practices.

## Quick Start

1. Open a terminal in the repo root and run:
   ```sh
   python Tools/Setup_Environment.py
   ```
   - Creates `.venv`, installs requirements, and sets up VS Code configs.
2. Open the folder in VS Code. Select the `.venv` Python interpreter if prompted.
3. Install all recommended extensions when prompted.
4. Activate the virtual environment before running tests or scripts:
   - Windows: `.venv\Scripts\activate`
   - macOS/Linux: `source .venv/bin/activate`
5. Use the Makefile or VS Code tasks for all core operations (intake, analysis, summary, test, lint, format).

## Directory Structure and Drop Points

All major entry types and templates are stored in standardized directories for automation and onboarding. Use these exact paths for all intake, output, and reference operations:

| Entry Type                | Directory Path (relative to repo root)                | Format/Notes                                  |
|--------------------------|------------------------------------------------------|------------------------------------------------|
| Champion Dictionary      | input/Champion_Dictionary/                           | JSON, one file per champion                   |
| Mechanic Dictionary      | input/Mechanic_Dictionary/                           | JSON, one file per mechanic (input, WIP)      |


![Python](https://img.shields.io/badge/python-3.10%2B-blue)
![License: CC BY-NC 4.0](https://img.shields.io/badge/License-CC%20BY--NC%204.0-lightgrey.svg)
![Platform](https://img.shields.io/badge/platform-windows%20%7C%20linux%20%7C%20macos-blue)

# Raid Tools: Automation-Ready Boss & Team Guide System

> **Source of truth:** All workflows, templates, and best practices are in `.github/copilot-instructions.md` and `input/Templates/`.

## Onboarding

1. Read this README for a high-level overview and quick start.
2. For all details, workflows, and canonical templates, see `.github/copilot-instructions.md`.
3. Use the template files in `input/Templates/` for all new entries.

## Quick Start

1. Open a terminal in the repo root and run:
   ```sh
   python Tools/Setup_Environment.py
   ```
2. Open the folder in VS Code. Select the `.venv` Python interpreter if prompted.
3. Install all recommended extensions when prompted.
4. Activate the virtual environment before running tests or scripts:
   - Windows: `.venv\Scripts\activate`
   - macOS/Linux: `source .venv/bin/activate`
5. Use the Makefile or VS Code tasks for all core operations (intake, analysis, summary, test, lint, format).

## Directory Drop Points

| Entry Type                | Directory Path (relative to repo root)                |
|--------------------------|------------------------------------------------------|
| Champion Dictionary      | input/Champion_Dictionary/                           |
| Mechanic Dictionary      | input/Mechanic_Dictionary/                           |
| Templates                | input/Templates/                                     |
| Prompts                  | input/Prompts/                                       |
| Boss Guides              | Output/Boss_Guides/                                  |
| Build Evaluations        | Output/Build_Evaluations/                            |
| Mechanic Dictionary (Out)| Output/Mechanic_Dictionary/                          |

## Where to Find Templates

| Entry Type         | Template File (relative to repo root)           |
|--------------------|------------------------------------------------|
| Champion           | input/Templates/Champion_Dictionary_Template.json|
| Boss Guide         | input/Templates/Boss_Guide_Template.md          |
| Mechanic           | input/Templates/Mechanic_Entry_Template.json    |
| Team               | input/Templates/Team_Entry_Template.md          |
| Build Evaluation   | input/Templates/Build_Evaluation_Template.md    |

> For the latest and most detailed instructions, always refer to `.github/copilot-instructions.md`.

## Essential Commands

- `make setup` — Set up environment (venv, requirements)
- `make test` — Run all tests
- `make intake` — Intake a new champion
- `make analysis` — Run cooldown analysis
- `make summary` — Generate summary markdowns

Note: schema validation for champion JSONs uses the `jsonschema` package. The setup script installs this dependency automatically, or install it manually with `pip install jsonschema`.

Or use the corresponding Python scripts directly (see `.github/copilot-instructions.md`).

## Best Practices

- Always use the canonical templates in `input/Templates/` for new entries. For all other guidance, see `.github/copilot-instructions.md`.

---
- Validate JSON

- Organize Completed Prompts



Open the Command Palette (`Ctrl+Shift+P`), select “Tasks: Run Task”, and choose the desired operation.
