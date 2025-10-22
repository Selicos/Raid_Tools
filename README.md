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


# Raid Tools: Boss & Team Markdown Guide System

> **Project-wide, workflow, and safety instructions:** See `.github/ai-assistant-instructions.md` (universal, authoritative).
> 
> **Copilot-specific quick reference:** See `.github/copilot-instructions.md` (always defers to the universal file for project-wide guidance).

## Major Workflow Update (October 2025)

**Markdown is now the primary and canonical output format for all boss and team guides.**
All new content, recommendations, and team breakdowns must be delivered as modular, human-readable Markdown files, following the standard template below. JSON is for internal data only.

### Standard Boss/Team Markdown Template

```markdown
# [Boss Name] Teams (Owned Champions Only)

## Table of Contents
1. Boss Mechanics & Stat Requirements
2. Teams by Estimated Damage/Clear Speed
3. [Team Type 1]
4. [Team Type 2]
...
N. Best Champions & Team Participation
N+1. Direct Champion Comparisons by Role
N+2. Ideal Champions to Pull

---

## Boss Mechanics & Stat Requirements
- [Boss mechanics, immunities, stat thresholds, unique challenges, etc.]

---

## Teams by Estimated Damage/Clear Speed
| Team Name | Simulated Damage/Clear Time | Core Champions | Key Mechanics & Notes |
|---|:---:|---|---|
| ... | ... | ... | ... |

---

## [Team Type Section]
### Team: [Team Name]
**Core Roles:** ...
**Optimal Combo:** ...
**Alternates:** ...
**Speed Tuning:** ...
**Gear:** ...
**Masteries:** ...
**Manual/Auto:** ...
**Strengths:** ...
**Weaknesses:** ...
**Simulated Damage/Clear Time:** ...

---

## Best Champions & Team Participation
| Champion | Role(s) | Best Teams | Notes |
|---|---|---|---|

---

## Direct Champion Comparisons by Role
...

---

## Ideal Champions to Pull
- [List and rationale for each boss/team]
```


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


This repository now provides a complete workflow for reviewing, analyzing, and summarizing Raid Shadow Legends boss teams and champion usage, with a focus on actionable Markdown guides for each boss and level. All new guides must follow the template above and include:
- Boss mechanics & stat requirements
- Teams by estimated damage/clear speed (with simulation summaries)
- Detailed team breakdowns (roles, speed tuning, gear, masteries, manual/auto, strengths/weaknesses)
- Best champions & team participation
- Direct champion comparisons by role
- Indexed list of ideal champions to pull for upgrades

JSON and Python scripts are still supported for internal data and automation, but Markdown is the primary output for all human and AI review.

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

WIP

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

- **Purpose:** Intake champions by building a dictionary entry in json of it's stats, skills, etc. USes those and boss information to create team recommendations for content like bosses, clan boss, and other areas of the game. 


- **Other Files:**
  - `ChampionIntake/templates/logTemplate.json` — Template for new champion JSON files.
  - `ChampionIntake/Prompt/` — Prompt files for Copilot Chat.
  - `ChampionIntake/Champions/Input/Owned_champion_list.md` — List of owned champions and timestamps.

#### Champion Management CLI Usage

Use `Tools/import_owned_champions.py` for all champion management, bulk import, and batch prompt generation workflows:

```sh
# Import owned champions from a file (default: ChampionIntake/Champions/Input/Owned_champion_list.md)
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

All completed boss/team Markdown files (e.g., `UltraNightmare_ClanBoss_Teams_OWNED_ONLY.md`, `Hard_Spider_Team_Notes.md`) **must** be placed in the `Notes/` or `output/` directory. These Markdown files are the authoritative, human-readable record for each boss and are used for review, team planning, and as the source for all downstream tools.

**File Handling:**
- Incomplete or in-progress Markdown files can be staged in a working directory or with a `_v2.md` suffix for review.
- Once a Markdown file is fully validated and follows the template, move it to `Notes/` or `output/` as the canonical version.
- Completed Markdown files are the authoritative record for each boss and should always be preserved for review, notes, and as the source for all downstream tools.

---


## Boss/Team Markdown Creation & Update Workflow (Authoritative)

1. **Boss/Team Markdown Creation**
  - For each boss or dungeon, create a Markdown file in `Notes/` or `output/` using the standard template above.
  - All teams, recommendations, and summaries must be based on the current owned champion list and validated with at least two authoritative sources (Ayumilove, Hellhades, Wiki).

2. **Simulation & Validation**
  - Run at least 3 simulations for each team (if possible) and summarize results in the Markdown file.
  - Manually validate all boss mechanics, stat requirements, and team recommendations.
  - Document validation in the Markdown file or commit message.

3. **Review & Finalization**
  - Once the Markdown file is complete and validated, move it to `Notes/` or `output/` as the canonical version.
  - Do not overwrite or delete completed Markdown files unless updating for new game content or major changes.

**Important:**
- Never delete files or folders as part of this workflow.
- Completed Markdown files are the authoritative, human-readable record for each boss and should always be preserved for review, notes, and as the source for all downstream tools.

---


## VS Code Task Runner

You can run all core operations using the VS Code UI:
- Open the Command Palette (`Ctrl+Shift+P`)
- Select “Tasks: Run Task”
- Choose any of the following tasks (all tasks are tightly aligned with the current scripts and workflow):
  - Run Champion Intake: `ChampionIntake/Champ_Intake.py` (single champion prompt/JSON)
  - Run Champion Turn Analysis: `ChampionTurnAnalysis/ChampionTurnAnalysis.py` (cooldown analysis)
  - Generate Champion Summaries: `ChampionSummary/generateChampionSummaries.py` (summary markdowns)
  - Setup Environment: `Tools/Setup_Environment.py` (environment and config)
  - Validate Champion JSON: `Tools/validate_json.py` (JSON validation)
  - First Run: Setup & Activation Instructions
  - Organize Completed Prompts: Moves completed prompt files to `output/completed_prompts/`

This ensures all completed markdowns and outputs are consistently organized and all workflows are accessible from the UI. Periodically validate that all VS Code tasks match the actual scripts in the repo.

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

1. **Boss/Team Markdown Creation**
  - Use the owned champion list and validated boss/champion data to create a Markdown file for each boss or dungeon, following the standard template.
  - Summarize all team recommendations, mechanics, and simulation results in Markdown.

2. **(Optional) Champion Intake & Review**
  - Use `ChampionIntake/Champ_Intake.py` and related scripts for internal champion data management and JSON generation, if needed for automation or analysis.

3. **(Optional) Cooldown Analysis & Summary Generation**
  - Use `ChampionTurnAnalysis/ChampionTurnAnalysis.py` and `ChampionSummary/generateChampionSummaries.py` for detailed skill cycle analysis and champion summaries, if needed.

**Note:** Markdown is the primary output for all human and AI review. JSON and Python scripts are for internal data and automation only.

---

## Recent Changes & Updates
- All documentation, script references, and folder structures are up to date as of October 2025.
- Batch intake now always processes all owned champions, regardless of last updated date.
- All scripts, tasks, and documentation are now tightly aligned and validated. Legacy scripts, clipboard logic, and deprecated workflows have been removed.
- The project tracking file is the authoritative source for priorities, risks, and roadmap.



