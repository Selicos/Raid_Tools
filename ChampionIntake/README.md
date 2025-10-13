# Raid_Tools

# Champion Intake & Review System


It supports single or batch processing, integrates with Copilot Chat, auto-validates and timestamps each champion entry, and provides skill cycle analysis and summary reports.

1. Run environment setup:
    - **After setup, activate the virtual environment before running any other Python scripts:**
       - On Windows: `./.venv/Scripts/Activate`
       - On macOS/Linux: `source .venv/bin/activate`
    - For details, see the main README.md environment setup section.
2. (Recommended) Run duplicate cleanup to ensure no case-insensitive duplicate champion or prompt files:
   - `python Tools/cleanup_duplicate_champions.py`
   - Review and merge any duplicates as prompted.
3. Run task for Champion Intake OR initiate python script champIntake.py. 
   - This will generate and open a prompt md file and also generate a json for the champion.
4. Ask Copilot Chat (Ctrl+Shift+I) to: “Based on the open prompt file, generate the champion JSON for [champion].”
5. Copy the output json into the champion.json file generated in step 3.
6. Run tests or cleanup as needed.

---


## Prerequisites

Before running the system, ensure you have:

- ✅ Python 3.9+ installed
- ✅ VS Code installed
  - Python
  - Copilot Chat (optional but recommended)
- ✅ Internet access for package installation

---

## Required Folder Structure

Create the following structure inside your working directory:

Champion Review and Comparison/
├── Champions/
│   ├── Owned Champions/
│   │   └── Owned_Champion_list.md
│   │   └── [ChampionName].json
│   ├── prompt/
│   ├── Tools/
│   │   ├── champIntake.py
│   │   ├── Setup_Environment.py
│   │   ├── cleanupDuplicateChampions.py
│   │   ├── updateOwnedChampions.py
│   │   └── champSynergyCheck.py
│   └── Summary/
│       └── [ChampionName].md
├── Tests/
│   └── test_champion_review_and_comparison.py
├── templates/
│   └── logTemplate.json
├── README.md

# Champion Intake & Review

This module handles champion data intake, prompt generation, and review workflows for Raid Tools.

## Key Scripts

- `Champ_Intake.py`: Main champion intake and prompt generator
- `Tools/cleanup_duplicate_champions.py`: Remove duplicate champion files
- `Comparisons/Champ_Comparison_Track_owned.py`: Compare owned champions

## Usage

1. **Intake a new champion**
   ```sh
   python Tools/champIntake.py
   ```

2. **Cleanup duplicate champions**
   ```sh
   python Tools/cleanup_duplicate_champions.py
   ```

3. **Compare owned champions**
   ```sh

   # Champion Intake & Review System

   This module streamlines champion intake, prompt generation, review, and summary for Raid Tools.

   ## Onboarding & Environment Setup

   1. Run `python Tools/Setup_Environment.py` or `make setup` in the repo root.
   2. Open the folder in VS Code and select the `.venv` Python interpreter if prompted.
   3. Install all recommended extensions when prompted.
   4. Activate the virtual environment before running scripts or tests.
   5. Use the Makefile or VS Code tasks for all core operations (intake, cleanup, compare, test, etc.).

   ## Usage

   - **Intake a new champion:**
     - `python Tools/champIntake.py` or use the "Run Champion Intake" VS Code task.
   - **Cleanup duplicate champions:**
     - `python Tools/cleanup_duplicate_champions.py` or use the "Cleanup Duplicate Champions" task.
   - **Compare owned champions:**
     - `python ChampionIntake/Comparisons/Champ_Comparison_Track_owned.py` or use the "Run Champion Comparison Tracker" task.
   - **Run all tests:**
     - `pytest` or `make test` or use the "Test Environment Setup and Requirements" task.

   ## Data Structure

   - Champion JSON files: `Champions/`
   - Comparison scripts: `Comparisons/`
   - Prompt files: `Prompt/`
   - Templates: `templates/`

   ## VS Code & Makefile

   - The `.vscode` folder configures interpreter, linting, formatting, and tasks for all users.
   - Use the Makefile for setup, test, lint, format, and all core operations.
   - See the root README for full onboarding and troubleshooting details.