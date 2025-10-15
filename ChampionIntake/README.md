
> **For all project-wide, workflow, and safety instructions, see `.github/ai-assistant-instructions.md` (universal, authoritative).**


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
   - If a completed prompt already exists in `output/completed_prompts/` for a champion, prompt and JSON generation for that champion is skipped. This prevents unnecessary overwrites and ensures completed prompts are not regenerated.
   - Prompt files in `input/Prompt/` are always overwritten unless a completed prompt exists.
   - No clipboard or copy-to-clipboard logic is used. In single champion mode, the prompt file may be opened in the editor; in batch mode, prompt files are not opened.

4. Complete the prompt markdown file in `input/Prompt/`, ensuring all modules (0–20) are completed in the required JSON structure.
5. Manually validate all champion data (name, skills, multipliers, cooldowns, stat priorities, etc.) using authoritative sources (Raid Shadow Legends Wiki, Ayumilove, Hellhades, etc.).
6. Only proceed if the prompt is 100% complete and accurate.
7. After the prompt is fully completed and validated, move the markdown file to `output/completed_prompts/` as `[champion]_prompt.completed.md`. This file is the authoritative, human-readable record for the champion.
8. Use the content of the completed prompt markdown to generate a single JSON object, following the template and module keys provided in the prompt (`data/templates/logTemplate.json`), including modules 0–20. Save the JSON to `output/Champions/[champion].json`.
9. Run validation with:
  ```sh
  python Tools/validate_json.py output/Champions/[champion].json
  ```
  Confirm the script prints the champion name and rarity, and that the JSON is valid.
10. Never delete files or folders as part of this workflow.

**Prompt File Handling:**
- Incomplete or in-progress prompts are kept in `input/Prompt/`.
- Once a prompt is fully validated and used to generate a JSON, the markdown file is moved to `output/completed_prompts/`.
- Completed prompts in `output/completed_prompts/` are the authoritative, human-readable record for each champion and are used for review, notes, and as the source for JSON generation and all downstream tools (summary, cooldown analysis, etc.).
- If a completed prompt already exists in `output/completed_prompts/` for a champion, prompt and JSON generation for that champion is skipped. This prevents unnecessary overwrites and ensures completed prompts are not regenerated.
- Prompt files in `input/Prompt/` are always overwritten unless a completed prompt exists.

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

## Module System (0–20)

Champion prompts and JSON logs now use modules 0–20:
- 0–13: Core champion review, skills, synergy, investment, etc.
- 14: Base stats (HP, ATK, DEF, SPD, C.RATE, C.DMG, RES, ACC)
- 15: Skill book requirements and effects
- 16: Aura details
- 17: AI behavior and skill logic
- 18: Dungeon/content-specific breakdowns
- 19: Mastery tree recommendations (visual/JSON)
- 20: Community ratings/notes

All prompt markdowns and JSON logs must include these modules for full compatibility.


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