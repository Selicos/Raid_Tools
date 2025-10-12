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
├── champion_analysis.py
├── cooldown_analysis/
│ └── [ChampionName].md

- `champion_analysis.py`: Main script for running skill cycle simulations and generating reports.
- `cooldown_analysis/`: Output folder for detailed markdown analysis files for each champion.

---

## Usage

1. Ensure your champion JSON files are up to date and located in  
   `../Champion Review and Comparison/Champions/`
2. Run the analysis script:
   ```sh
   python champion_analysis.py
