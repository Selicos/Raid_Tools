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
   python Comparisons/Champ_Comparison_Track_owned.py
   ```

## Data Structure

- Champion JSON files: `Champions/`
- Comparison scripts: `Comparisons/`
- Prompt files: `Prompt/`
- Templates: `templates/`

## Testing & Makefile

- All tests for this module are in `Tests/`
- Run with `pytest` or `make test` from the repo root
- Use the Makefile for common tasks (setup, test, format, intake)

## VS Code & Environment Setup

1. Clone the repository
2. Run `python Tools/Setup_Environment.py` or `make setup` from the root
3. Open the workspace in VS Code for best experience
4. Ensure `.vscode/settings.json`, `.vscode/tasks.json`, and `.vscode/extensions.json` exist (see root README)
5. Install all recommended extensions when prompted
6. Run `make test` to validate your environment and project health

See the root README for full environment and onboarding details, including the environment test and VS Code configuration.

2. **Champion Review & Update**
   - Edit the champion JSON as needed.
   - Run `updateOwnedChampions.py` to refresh outdated entries.
   - Use `cleanupDuplicateChampions.py` to merge duplicate files.

3. **Skill Cycle Analysis**
   - Run `championAnalysis.py` in `ChampionAnalysisTool/` to simulate skill cycles and generate detailed markdown reports in `cooldown_analysis/`.

4. **Summary Generation**
   - Run `generateChampionSummaries.py` in `ChampionSummary/` to generate readable summaries for each champion, including skill order and expected damage from the analysis tool.

5. **Testing & Validation**
   - Run tests in `Tests/` to ensure all champion JSONs and prompts are consistent and valid.

---

## Example Usage

```sh
# Setup environment
python "Champion Review and Comparison/Setup_Environment.py"

# Intake a new champion
python "Champion Review and Comparison/Tools/champIntake.py"

# Run skill cycle analysis
python ChampionAnalysisTool/championAnalysis.py

# Generate summary markdowns
python ChampionSummary/generateChampionSummaries.py
```