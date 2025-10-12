# Raid_Tools

# Champion Intake & Review System

## Overview

This system streamlines the intake, prompt generation, review, analysis, and summary process for Raid Shadow Legends champions.  
It supports single or batch processing, integrates with Copilot Chat, auto-validates and timestamps each champion entry, and provides skill cycle analysis and summary reports.

1. Run task for Champion Intake OR initiate python script champIntake.py. 
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
ChampionSummary/
├── generateChampionSummaries.py
├── readme.md
└── Summary/
    └── [ChampionName].md
ChampionAnalysisTool/
├── championAnalysis.py
├── cooldown_analysis/
│   └── [ChampionName].md

---

## Required Files

| File                        | Purpose                                                                 |
|-----------------------------|-------------------------------------------------------------------------|
| `champIntake.py`           | Main script for champion intake, prompt generation, and review updates |
| `Setup_Environment.py`      | Ensures required Python packages and tools are installed               |
| `cleanupDuplicateChampions.py`     | Detects and merges case-insensitive duplicates in JSON and prompt files|
| `Owned_Champion_list.md`    | Tracks owned champions and last update timestamps                      |
| `[ChampionName].json`       | Placeholder or completed champion log file                             |
| `[ChampionName].md`         | Prompt file for Copilot Chat to generate champion log                  |

---

## Key Files & Scripts

| File/Folder                                 | Purpose                                                                 |
|----------------------------------------------|-------------------------------------------------------------------------|
| `champIntake.py`                             | Main script for champion intake, prompt generation, and review updates  |
| `Setup_Environment.py`                        | Ensures required Python packages and tools are installed                |
| `cleanupDuplicateChampions.py`              | Detects and merges case-insensitive duplicates in JSON and prompt files |
| `updateOwnedChampions.py`                   | Updates all champions older than 30 days or missing a timestamp         |
| `champSynergyCheck.py`                      | (WIP) Analyze synergy across owned champions                            |
| `Owned_Champion_list.md`                      | Tracks owned champions and last update timestamps                       |
| `[ChampionName].json`                         | Champion log file (with rarity, overview, skills, etc.)                 |
| `[ChampionName].md` (prompt/)                 | Prompt file for Copilot Chat to generate champion log                   |
| `Summary/[ChampionName].md`                   | Human-readable summary for each champion                                |
| `testChampionReviewAndComparison.py`      | Tests for champion JSON and prompt consistency                          |
| `logTemplate.json` (templates/)              | Template for new champion JSON files                                    |
| `championAnalysis.py` (ChampionAnalysisTool) | Standalone script for skill cycle simulation and analysis               |
| `cooldown_analysis/[ChampionName].md`         | Detailed skill cycle analysis output                                    |
| `generateChampionSummaries.py` (ChampionSummary) | Generates summary markdowns for each champion                  |

---

## Workflow

1. **Champion Intake & Prompt Generation**
   - Run `champIntake.py` (from Tools or via VS Code task).
   - Generates a prompt `.md` and a placeholder `.json` for the champion.
   - Use Copilot Chat to generate or update the champion JSON based on the prompt.

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