# Raid Tools: Champion Review, Analysis, and Summary System

## Overview

This repository provides a complete workflow for reviewing, analyzing, and summarizing Raid Shadow Legends champions.
It includes tools for champion intake, prompt generation, review, skill cycle simulation, and summary report generation.

---

## Folder Structure
Raid_Tools/
├── Champion Review and Comparison/
│ ├── Champions/
│ ├── prompt/
│ ├── Tools/
│ ├── Summary/
│ ├── templates/
│ └── README.md
├── ChampionAnalysisTool/
│ ├── championAnalysis.py
│ ├── cooldown_analysis/
│ └── README.md
├── Summarize Champion Results/
│ ├── jsonToMdPerChamp.py
│ └── README.md
├── Tests/
│ ├── testChampionReviewAndComparison.py
│ └── test_script_paths.py
└── README.md (this file)

---

## Tools and Scripts

### 1. Champion Review and Comparison Tools

- **Purpose:** Intake new champions, generate prompts, maintain champion logs, and validate data.

- **Key Scripts (in `Champion Review and Comparison/Tools/`):**
  - `champIntake.py` — Add a new champion, generate prompt, and create a placeholder JSON.
  - `setupEnvironment.py` — Install required Python packages and check VS Code CLI.
  - `cleanupDuplicateChampions.py` — Merge and clean up duplicate champion files.
  - `updateOwnedChampions.py` — Update champions missing timestamps or older than 30 days.
  - `champSynergyCheck.py` — (WIP) Analyze synergy between owned champions.

- **Other Files:**
  - `templates/logTemplate.json` — Template for new champion JSON files.
  - `Summary/` — Human-readable markdown summaries for each champion.
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

### 3. Summarize Champion Results Tool

- **Purpose:** Generate readable summary markdowns for each champion, including skill order and expected damage from the cooldown analysis.

- **Key Script (in `Summarize Champion Results/`):**
  - `jsonToMdPerChamp.py` — Generates summary markdowns for each champion.

- **Output:**
  - `Champion Review and Comparison/Summary/` — Contains summary markdowns for each champion.

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
   - Run `jsonToMdPerChamp.py` in `Summarize Champion Results/` to generate readable summaries for each champion, including skill order and expected damage.

4. **Testing**
   - Run `pytest` or execute the scripts in `Tests/` to validate data and paths.

---

## Example Usage

```sh
# 1. Setup environment (if needed)
python "Champion Review and Comparison/Tools/setupEnvironment.py"

# 2. Intake a new champion
python "Champion Review and Comparison/Tools/champIntake.py"

# 3. Run cooldown analysis
python "ChampionAnalysisTool/championAnalysis.py"

# 4. Generate summary markdowns
python "Summarize Champion Results/jsonToMdPerChamp.py"

# 5. Run tests
pytest
# or
python [test_script_paths.py](http://_vscodecontentref_/5)
```