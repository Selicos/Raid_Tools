1. ![Python](https://img.shields.io/badge/python-3.10%2B-blue)
2. ![Python](https://img.shields.io/badge/python-3.10%2B-blue)
3. ![License: CC BY-NC 4.0](https://img.shields.io/badge/License-CC%20BY--NC%204.0-lightgrey.svg)
4. ![Platform](https://img.shields.io/badge/platform-windows%20%7C%20linux%20%7C%20macos-blue)

5. [Quick Start & VS Code Integration](#quick-start--vs-code-integration)
6. [Makefile: Simplified Commands & Environment Test](#makefile-simplified-commands--environment-test)
7. [Folder Structure & VS Code Config](#folder-structure--vs-code-config)
8. [VS Code Extensions (Recommended)](#vs-code-extensions-recommended)
9. [Tools and Scripts](#tools-and-scripts)
10. [Workflow: How the Tools Are Linked](#workflow-how-the-tools-are-linked)
11. [Completed Markdown Output](#completed-markdown-output)
12. [VS Code Task Runner](#vs-code-task-runner)
13. [Troubleshooting](#troubleshooting)

# Raid Tools: Champion Review, Analysis, and Summary System

## Onboarding & Environment Setup (2025)

**Quick Start:**
1. Run `python Tools/Setup_Environment.py` (or `make setup`) in the repo root.
2. Open the folder in VS Code. Select the `.venv` Python interpreter if prompted.
3. Install all recommended extensions when prompted.
4. Activate the virtual environment before running tests or scripts (see below).
5. Use the Makefile or VS Code tasks for all core operations (intake, analysis, summary, test, lint, format).

**Environment Test:**
Run `make test` or `python -m pytest` to validate your environment, dependencies, and project structure. This checks Python version, virtualenv, required packages, Makefile, VS Code configs, and more.

**VS Code Integration:**
- The `.vscode` folder configures interpreter, linting, formatting, and tasks for all users.
- Use the Source Control panel for git operations and the Run/Debug panel for tasks.

**Activation:**
- Windows: `.venv\Scripts\activate`
- macOS/Linux: `source .venv/bin/activate`

See the rest of this README for details on tools, folder structure, and troubleshooting.

## Overview

This repository provides a complete workflow for reviewing, analyzing, and summarizing Raid Shadow Legends champions.
It includes tools for champion intake, prompt generation, review, skill cycle simulation, and summary report generation.

---



## Quick Start & VS Code Integration

### 1. Environment Setup

Open a terminal in the repo root and run:
```sh
python Tools/Setup_Environment.py
```
This will:
- Create a `.venv` virtual environment if it doesn't exist
- Install all required Python packages (see `requirements.txt`)
- Create VS Code config files in `.vscode/`
- Print instructions for activating the virtual environment

### 2. VS Code Integration

- Open the folder in VS Code. You will be prompted to select the `.venv` Python interpreter.
- If not prompted, use `Ctrl+Shift+P` > `Python: Select Interpreter` and choose the `.venv` Python.
- VS Code terminals and tasks will now use the virtual environment automatically.
- Install all recommended extensions when prompted.

### 3. Activate the Virtual Environment (CLI)

- On Windows:
  ```sh
  .\.venv\Scripts\Activate
  ```
- On macOS/Linux:
  ```sh
  source .venv/bin/activate
  ```

### 4. Run Tools and Tests

You can run all core operations using either the Makefile or direct Python commands:

```sh
make intake    # Intake a new champion
make analysis  # Run cooldown analysis
make summary   # Generate summary markdowns
make test      # Run all tests
```

**Or with Python directly:**
```sh
python Tools/champIntake.py
python ChampionAnalysisTool/championAnalysis.py
python ChampionSummary/generateChampionSummaries.py
python -m pytest
```


**With Makefile (recommended):**
```sh
make intake    # Intake a new champion
make analysis  # Run cooldown analysis
make summary   # Generate summary markdowns
make test      # Run all tests
make organize-completed  # Move all *_prompt.completed.md files to output/completed_prompts/
```

**Or with Python directly:**
```sh
python Tools/import_owned_champions.py --from-owned-list  # Bulk import and batch prompt generation
python ChampionIntake/Champ_Intake.py  # Single champion intake
python ChampionAnalysisTool/championAnalysis.py
python ChampionSummary/generateChampionSummaries.py
python -m pytest
```

---


### Troubleshooting
- If tests fail with "Not running inside a virtual environment", activate `.venv` before running tests.
- If you see import errors for packages (e.g., `Pygments` vs `pygments`), check that package names in `requirements.txt` match their import names (usually lowercase).
- For best experience, always use VS Code with the `.venv` interpreter selected.

---


## Makefile: Simplified Commands & Environment Test


You can use the provided `Makefile` to automate common tasks. This makes setup, testing, and running tools easier and more consistent.

### Environment & Project Health Test

Run `make test` or `python -m pytest` to check:
- All required Python packages are installed
- All key project files and folders exist (including .vscode configs, Makefile, README)
- The Python virtual environment is active
- All packages in requirements.txt are importable

If any check fails, review the error message and update your environment or project files as needed.

### Common Commands

```sh
# Set up the environment (venv, requirements)
make setup

# Run all tests
make test

# Lint code with flake8
make lint

# Format code with Black
make format

# Intake a new champion
make intake

# Run cooldown analysis
make analysis

# Generate summary markdowns
make summary

# Clean up venv and cache files
make clean
```

Run `make help` to see all available commands.

---

## Folder Structure & VS Code Config

Raid_Tools/
├── Champion Review and Comparison/
│   ├── Champions/
│   ├── prompt/
│   ├── Tools/
│   ├── Summary/
│   ├── templates/
│   └── README.md
├── ChampionAnalysisTool/
│   ├── championAnalysis.py
│   ├── cooldown_analysis/
│   └── README.md
├── ChampionSummary/
│   ├── generateChampionSummaries.py
│   ├── readme.md
│   └── Summary/
│       └── [ChampionName].md
├── Tests/
│   ├── testChampionReviewAndComparison.py
│   └── test_script_paths.py
├── .vscode/
│   ├── settings.json   # Python interpreter, linting, formatting
│   ├── tasks.json      # VS Code tasks for all core operations
│   └── extensions.json # Recommended extensions
└── README.md (this file)

**VS Code Workspace Setup:**
- The `.vscode` folder ensures all users have the same Python interpreter, linting, formatting, and task setup.
- To save your workspace state (open files, layout, etc.), use `File > Save Workspace As...` in VS Code to create a `.code-workspace` file.
- To reopen, double-click the `.code-workspace` file or open the folder in VS Code. VS Code will restore your environment, tasks, and recommended extensions.


---

## VS Code Extensions (Recommended)

The following extensions are recommended for best experience:
- Python (ms-python.python)
- Pylance (ms-python.vscode-pylance)
- Jupyter (ms-toolsai.jupyter)
- Docker (ms-azuretools.vscode-docker)

Open the workspace in VS Code and install all recommended extensions when prompted.

---


## Tools and Scripts

### 1. Champion Management & Review Tools

- **Purpose:** Intake new champions, generate prompts, maintain champion logs, validate data, and perform bulk import and batch prompt generation.

- **Key Scripts:**
  - `Tools/import_owned_champions.py` — Authoritative CLI for champion management, bulk import, and batch prompt generation from the owned list.
  - `ChampionIntake/Champ_Intake.py` — Add a new champion, generate prompt, and create a placeholder JSON (single champion intake).
  - `Tools/Setup_Environment.py` — Install required Python packages and check VS Code CLI.
  - `Tools/cleanup_duplicate_champions.py` — Merge and clean up duplicate champion files.
  - `ChampionIntake/Comparisons/Champ_Comparison_Track_owned.py` — Compare owned champions.

- **Other Files:**
  - `ChampionIntake/templates/logTemplate.json` — Template for new champion JSON files.
  - `ChampionIntake/Prompt/` — Prompt files for Copilot Chat.
  - `ChampionIntake/Champions/Owned_Champions/Owned_champion_list.md` — List of owned champions and timestamps.

#### Champion Management CLI Usage

Use `Tools/import_owned_champions.py` for all champion management, bulk import, and batch prompt generation workflows:

```sh
# Import owned champions from a file (default: ChampionIntake/Champions/Owned_Champions/Owned_champion_list.md)
python Tools/import_owned_champions.py --from-owned-list

# Trigger champion intake and prompt generation for all owned champions
python Tools/import_owned_champions.py --from-owned-list --trigger-intake

# Import a single champion by name and rarity
python Tools/import_owned_champions.py --name "Arbiter" --rarity "Legendary"
```

See the script's help for all options:

```sh
python Tools/import_owned_champions.py --help
```

Do **not** use or reference `manage_champions.py` (this script does not exist) or any legacy paths.

---

## Completed Markdown Output



All completed prompt markdown files (e.g., `[champion]_prompt.completed.md`) **must** be placed in the `output/completed_prompts/` directory. Use the Makefile target `make organize-completed` or the VS Code task “Organize Completed Prompts” to move all completed files automatically.

**Prompt File Handling:**
- Incomplete or in-progress prompts are kept in `input/Prompt/`.
- Once a prompt is fully validated and used to generate a JSON, the markdown file is moved to `output/completed_prompts/`.
- Completed prompts in `output/completed_prompts/` are the authoritative, human-readable record for each champion and are used for review, notes, and as the source for JSON generation and all downstream tools (summary, cooldown analysis, etc.).
- If a completed prompt already exists in `output/completed_prompts/` for a champion, prompt and JSON generation for that champion is skipped. This prevents unnecessary overwrites and ensures completed prompts are not regenerated.
- Prompt files in `input/Prompt/` are always overwritten when generating prompts for a champion, unless a completed prompt already exists.

---

## Champion JSON Creation & Update Workflow (Authoritative)


1. **Champion Intake (Prompt Generation)**
  - If a champion name (and optionally rarity) is provided, generate or overwrite the prompt file in `input/Prompt/` using the template, unless a completed prompt already exists in `output/completed_prompts/` for that champion. If a completed prompt exists, skip prompt and JSON generation for that champion.
  - In batch mode (no champion provided), process all champions in the owned list, generating/overwriting prompt files in `input/Prompt/` for each, unless a completed prompt already exists for that champion.
  - Prompt files are always overwritten unless a completed prompt exists.

2. **Complete the Prompt**
  - Fill out the prompt markdown file in `input/Prompt/`, ensuring all modules (0–20) are completed in the required JSON structure.
  - Do not proceed unless the prompt is 100% complete and accurate.

3. **Manual Validation of Champion Data**
  - Manually validate all champion data (name, skills, multipliers, cooldowns, stat priorities, etc.) using authoritative sources (Raid Shadow Legends Wiki, Ayumilove, Hellhades, etc.).
  - Only proceed if all data is correct and up to date. Document the validation step in the workflow log or commit message.

4. **Move Completed Prompt**
  - After the prompt is fully completed and validated, move the markdown file to `output/completed_prompts/` as `[champion]_prompt.completed.md`. This file is the authoritative, human-readable record for the champion.

5. **Generate the JSON Log**
  - Use the content of the completed prompt markdown to generate a single JSON object, following the template and module keys provided in the prompt (`data/templates/logTemplate.json`), including modules 0–20.
  - The JSON must reflect the validated champion name and data exactly.
  - Save the JSON to `output/Champions/[champion].json`.

6. **Validation**
  - Run validation with:
    ```sh
    python Tools/validate_json.py output/Champions/[champion].json
    ```
  - Confirm the script prints the champion name and rarity, and that the JSON is valid.
  - Only mark the champion as updated when the JSON passes all validation and matches the authoritative sources.

7. **Repeat for All Champions**
  - Continue this process for each champion as needed, especially after prompt updates, new information, or game changes. All new modules (14–20) are required for a complete prompt/JSON.

**Important:**
- Never generate or overwrite a prompt or JSON for a champion if a completed prompt already exists in `output/completed_prompts/` for that champion. This prevents unnecessary overwrites and ensures completed prompts are not regenerated.
- Prompt files in `input/Prompt/` are always overwritten unless a completed prompt exists.
- Never delete files or folders as part of this workflow.
- Completed prompts in `output/completed_prompts/` are the authoritative, human-readable record for each champion and should always be preserved for review, notes, and as the source for all downstream tools.
- As of October 2025, all prompts and JSON logs must include modules 0–20 (see expanded template and module files for details).

---

## VS Code Task Runner

You can run all core operations using the VS Code UI:
- Open the Command Palette (`Ctrl+Shift+P`)
- Select “Tasks: Run Task”
- Choose any of the following tasks:
  - Run Champion Intake
  - Bulk Import Owned Champions
  - Batch Prompt Generation (All Owned)
  - Run Champion Comparison Tracker
  - Cleanup Duplicate Champions
  - Run Champion Analysis Tool
  - Generate Champion Summaries
  - Setup Environment
  - Validate Champion JSON
  - Test Environment Setup and Requirements
  - First Run: Setup & Activation Instructions
  - Organize Completed Prompts

This ensures all completed markdowns and outputs are consistently organized and all workflows are accessible from the UI.

---

### 2. Cooldown Analysis Tool

- **Purpose:** Simulate champion skill cycles, calculate damage, healing, shield, and buff/debuff uptime.

- **Key Script (in `ChampionAnalysisTool/`):**
  - `championAnalysis.py` — Standalone script to analyze all champion JSONs and output markdown reports.

- **Output:**
  - `cooldown_analysis/` — Contains detailed markdown analysis for each champion.

---

### 3. Champion Summary Tool
- **Purpose:** Generate readable summary markdowns for each champion, including skill order and expected damage from the cooldown analysis.

- **Key Script (in `ChampionSummary/`):**
  - `generateChampionSummaries.py` — Generates summary markdowns for each champion.

- **Output:**
  - `ChampionSummary/Summary/` — Contains summary markdowns for each champion.

---

### 4. Testing and Validation

- **Purpose:** Ensure all champion JSONs and prompts are consistent and valid, and that all referenced paths exist.

- **Key Scripts (in `Tests/`):**
  - `testChampionReviewAndComparison.py` — Validates champion JSON and prompt consistency.
  - `test_script_paths.py` — Checks all Python scripts for valid referenced paths.

---

## Workflow: How the Tools Are Linked

1. **Champion Intake & Review**
   - Run `champIntake.py` to add a new champion and generate a prompt.
   - Use Copilot Chat (optional) to help fill out the champion JSON.
   - Update and review champion data as needed.

2. **Cooldown Analysis**
   - Run `championAnalysis.py` in `ChampionAnalysisTool/` to simulate skill cycles and generate detailed markdown reports in `cooldown_analysis/`.

3. **Summary Generation**
   - Run `generateChampionSummaries.py` in `ChampionSummary/` to generate readable summaries for each champion, including skill order and expected damage.



