![Python](https://img.shields.io/badge/python-3.10%2B-blue)
![Python](https://img.shields.io/badge/python-3.10%2B-blue)
![License: CC BY-NC 4.0](https://img.shields.io/badge/License-CC%20BY--NC%204.0-lightgrey.svg)
![Platform](https://img.shields.io/badge/platform-windows%20%7C%20linux%20%7C%20macos-blue)
2. [Quick Start & VS Code Integration](#quick-start--vs-code-integration)
3. [Makefile: Simplified Commands & Environment Test](#makefile-simplified-commands--environment-test)

4. [Folder Structure & VS Code Config](#folder-structure--vs-code-config)
5. [VS Code Extensions (Recommended)](#vs-code-extensions-recommended)
6. [Tools and Scripts](#tools-and-scripts)
7. [Workflow: How the Tools Are Linked](#workflow-how-the-tools-are-linked)
8. [Getting Started Fast](#getting-started-fast)
9. [Example Usage](#example-usage)
10. [Troubleshooting](#troubleshooting)

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

**With Makefile (recommended):**
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

### 1. Champion Review and Comparison Tools

- **Purpose:** Intake new champions, generate prompts, maintain champion logs, and validate data.

- **Key Scripts (in `Champion Review and Comparison/Tools/`):**
  - `champIntake.py` — Add a new champion, generate prompt, and create a placeholder JSON.
  - `Setup_Environment.py` — Install required Python packages and check VS Code CLI.
  - `cleanupDuplicateChampions.py` — Merge and clean up duplicate champion files.
  - `updateOwnedChampions.py` — Update champions missing timestamps or older than 30 days.
  - `champSynergyCheck.py` — (WIP) Analyze synergy between owned champions.

- **Other Files:**
  - `templates/logTemplate.json` — Template for new champion JSON files.
  - `prompt/` — Prompt files for Copilot Chat.
  - `Champions/Owned Champions/Owned_Champion_list.md` — List of owned champions and timestamps.

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



