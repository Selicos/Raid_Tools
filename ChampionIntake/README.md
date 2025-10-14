


It supports single or batch processing, integrates with Copilot Chat, auto-validates and timestamps each champion entry, and provides skill cycle analysis and summary reports.

1. Run environment setup:
    - **After setup, activate the virtual environment before running any other Python scripts:**
       - On Windows: `./.venv/Scripts/Activate`
       - On macOS/Linux: `source .venv/bin/activate`
    - For details, see the main README.md environment setup section.
2. (Recommended) Run duplicate cleanup to ensure no case-insensitive duplicate champion or prompt files:
   - `python Tools/cleanup_duplicate_champions.py`
   - Review and merge any duplicates as prompted.
3. Run task for Champion Intake (single champion) OR use the CLI for bulk import:
   - For single champion intake: run the "Run Champion Intake" VS Code task or `python ChampionIntake/Champ_Intake.py`.
   - For bulk import, batch prompt generation, or owned list management, use `python Tools/import_owned_champions.py` (see below).
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

- `ChampionIntake/Champ_Intake.py`: Main champion intake and prompt generator (single champion)
- `Tools/import_owned_champions.py`: Bulk import, batch prompt generation, and owned list management (authoritative CLI)
- `Tools/cleanup_duplicate_champions.py`: Remove duplicate champion files
- `ChampionIntake/Comparisons/Champ_Comparison_Track_owned.py`: Compare owned champions

## Usage


### Champion Management CLI Usage

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