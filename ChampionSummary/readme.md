# Champion Summary

## Overview

This tool generates human-readable summary markdown files for each champion, consolidating key information from champion JSON files and including skill order and expected damage results from the cooldown analysis tool. All output is written to `ChampionSummary/Summary/`.

---

## Prerequisites
  `../Champion Review and Comparison/Champions/`
  `../ChampionAnalysisTool/cooldown_analysis/`
## Folder Structure
ChampionSummary/
├── generateChampionSummaries.py

├── readme.md
    └── [ChampionName].md
- `generateChampionSummaries.py`: Script for generating summary markdowns for each champion, including analysis results.
---
## Usage

1. Ensure your champion JSON files are up to date and located in  
   `../Champion Review and Comparison/Champions/`
2. Ensure cooldown analysis markdowns exist in  
   `../ChampionAnalysisTool/cooldown_analysis/`
3. Run the summary script:
   ```sh
   python generateChampionSummaries.py
   ```