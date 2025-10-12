# Raid_Tools

# Champion Intake & Review System

## Overview

This system streamlines the intake, prompt generation, review, analysis, and summary process for Raid Shadow Legends champions.  
It supports single or batch processing, integrates with Copilot Chat, auto-validates and timestamps each champion entry, and provides skill cycle analysis and summary reports.

1. Run task for Champion Intake OR initiate pythin script Champ_Intake. 
    This will generate and open a prompt md file and also generate a json for the champion.
2. Ask Copilot Chat (Ctrl+Shift+I) to: “Based on the open prompt file, generate the champion JSON for [champion].”
3. Copy the output json into the champion.json file generated in step 1.
4. Run tests or cleanup as needed.

---

## Prerequisites

Before running the system, ensure you have:

- ✅ Python 3.9+ installed
- ✅ VS Code installed
- ✅ VS Code extensions:
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
│   │   └── [ChampionName].md
│   ├── Tools/
│   │   ├── champ_intake.py
│   │   ├── setup_environment.py
│   │   ├── cleanup_duplicate_champions.py
│   │   ├── update_owned_champions.py
│   │   └── champ_synergy_check.py
│   └── Summary/
│       └── [ChampionName].md
├── Tests/
│   └── test_champion_review_and_comparison.py
├── templates/
│   └── log_template.json
├── README.md
Summarize Champion Results/
├── JSON_to_MD_Per_Champ.py
ChampionAnalysisTool/
├── champion_analysis.py
├── cooldown_analysis/
│   └── [ChampionName].md

---

## Required Files

| File                        | Purpose                                                                 |
|-----------------------------|-------------------------------------------------------------------------|
| `champ_intake.py`           | Main script for champion intake, prompt generation, and review updates |
| `setup_environment.py`      | Ensures required Python packages and tools are installed               |
| `cleanup_duplicates.py`     | Detects and merges case-insensitive duplicates in JSON and prompt files|
| `Owned_Champion_list.md`    | Tracks owned champions and last update timestamps                      |
| `[ChampionName].json`       | Placeholder or completed champion log file                             |
| `[ChampionName].md`         | Prompt file for Copilot Chat to generate champion log                  |

---

## Key Files & Scripts

| File/Folder                                 | Purpose                                                                 |
|----------------------------------------------|-------------------------------------------------------------------------|
| `champ_intake.py`                             | Main script for champion intake, prompt generation, and review updates  |
| `setup_environment.py`                        | Ensures required Python packages and tools are installed                |
| `cleanup_duplicate_champions.py`              | Detects and merges case-insensitive duplicates in JSON and prompt files |
| `update_owned_champions.py`                   | Updates all champions older than 30 days or missing a timestamp         |
| `champ_synergy_check.py`                      | (WIP) Analyze synergy across owned champions                            |
| `Owned_Champion_list.md`                      | Tracks owned champions and last update timestamps                       |
| `[ChampionName].json`                         | Champion log file (with rarity, overview, skills, etc.)                 |
| `[ChampionName].md` (prompt/)                 | Prompt file for Copilot Chat to generate champion log                   |
| `Summary/[ChampionName].md`                   | Human-readable summary for each champion                                |
| `test_champion_review_and_comparison.py`      | Tests for champion JSON and prompt consistency                          |
| `log_template.json` (templates/)              | Template for new champion JSON files                                    |
| `champion_analysis.py` (ChampionAnalysisTool) | Standalone script for skill cycle simulation and analysis               |
| `cooldown_analysis/[ChampionName].md`         | Detailed skill cycle analysis output                                    |
| `JSON_to_MD_Per_Champ.py` (Summarize Champion Results) | Generates summary markdowns for each champion                  |

---

## Workflow

1. **Champion Intake & Prompt Generation**
   - Run `champ_intake.py` (from Tools or via VS Code task).
   - Generates a prompt `.md` and a placeholder `.json` for the champion.
   - Use Copilot Chat to generate or update the champion JSON based on the prompt.

2. **Champion Review & Update**
   - Edit the champion JSON as needed.
   - Run `update_owned_champions.py` to refresh outdated entries.
   - Use `cleanup_duplicate_champions.py` to merge duplicate files.

3. **Skill Cycle Analysis**
   - Run `champion_analysis.py` in `ChampionAnalysisTool/` to simulate skill cycles and generate detailed markdown reports in `cooldown_analysis/`.

4. **Summary Generation**
   - Run `JSON_to_MD_Per_Champ.py` in `Summarize Champion Results/` to generate readable summaries for each champion, including skill order and expected damage from the analysis tool.

5. **Testing & Validation**
   - Run tests in `Tests/` to ensure all champion JSONs and prompts are consistent and valid.

---

## Example Usage

```sh
# Setup environment
python Champion Review and Comparison/Champions/Tools/setup_environment.py

# Intake a new champion
python Champion Review and Comparison/Champions/Tools/champ_intake.py

# Run skill cycle analysis
python [champion_analysis.py](http://_vscodecontentref_/1)

# Generate summary markdowns
python Summarize\ Champion\ Results/JSON_to_MD_Per_Champ.py
```