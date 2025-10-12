# ChampionAnalysisTool

## Overview

This tool simulates and analyzes champion skill cycles, damage, healing, shields, and buff/debuff uptime for Raid Shadow Legends champions.  
It reads champion JSON files, runs simulations for both single-target (boss) and multi-target (wave) scenarios, and outputs detailed markdown reports for each champion.

---

## Prerequisites

- Python 3.9+ installed
- Champion JSON files located in:  
  `../Champion Review and Comparison/Champions/`
- (Optional) VS Code for easier navigation and editing

---

## Folder Structure
ChampionAnalysisTool/
├── championAnalysis.py
├── cooldown_analysis/
│   └── [ChampionName].md

- `championAnalysis.py`: Main script for running skill cycle simulations and generating reports.
- `cooldown_analysis/`: Output folder for detailed markdown analysis files for each champion.

---

## Usage

1. Ensure your champion JSON files are up to date and located in  
   `../Champion Review and Comparison/Champions/`
2. Run the analysis script:
   ```sh
   python championAnalysis.py
   ```
3. Check the output in the `cooldown_analysis/` folder for detailed reports on each champion.

---

## Output

The tool generates detailed markdown files for each champion containing:
- Skill cycle analysis for single-target (boss) scenarios
- Skill cycle analysis for multi-target (wave) scenarios  
- Damage calculations over multiple turns
- Healing, shield, and buff/debuff uptime analysis
- Optimal skill rotation recommendations
