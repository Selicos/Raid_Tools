# Raid_Tools

# 🛡️ Champion Intake & Review System

## 📦 Overview

This system streamlines the intake, prompt generation, and review update process for Raid Shadow Legends champions. It supports single or batch processing, integrates with Copilot Chat, and auto-validates and timestamps each champion entry.

1. Run task for Champion Intake OR initiate pythin script Champ_Intake

---

## 🧰 Prerequisites

Before running the system, ensure you have:

- ✅ Python 3.9+ installed
- ✅ VS Code installed
- ✅ VS Code extensions:
  - Python
  - Copilot Chat (optional but recommended)
- ✅ Internet access for package installation

---

## 📁 Required Folder Structure

Create the following structure inside your working directory:

Champion Review and Comparison/ 
├── Champions/ │ 
|    ├── Owned Champions/
|    │ └── Owned_Champion_list.md 
|    │ └── [ChampionName].json 
|    ├── prompt/ 
|    │ └── [ChampionName].md 
|    ├── Tools/
|    | └── champ_intake.py 
|    | └── setup_environment.py 
|    | └── cleanup_duplicates.py



---

## 📄 Required Files

| File                        | Purpose                                                                 |
|-----------------------------|-------------------------------------------------------------------------|
| `champ_intake.py`           | Main script for champion intake, prompt generation, and review updates |
| `setup_environment.py`      | Ensures required Python packages and tools are installed               |
| `cleanup_duplicates.py`     | Detects and merges case-insensitive duplicates in JSON and prompt files|
| `Owned_Champion_list.md`    | Tracks owned champions and last update timestamps                      |
| `[ChampionName].json`       | Placeholder or completed champion log file                             |
| `[ChampionName].md`         | Prompt file for Copilot Chat to generate champion log                  |

---

## 🚀 Initialization Steps

1. **Clone or create your project folder**
2. **Open in VS Code**
3. **Ensure Python interpreter is selected**
4. **Run setup script once:**
    ```bash
    python setup_environment.py

5. **Run the champ_intake.py script to begin:**
    python champ_intake.py

    You’ll be prompted: Use smart batch mode from owned list? (y/n):
        y → Scans Owned_Champion_list.md and updates champions older than 30 days
        n → Prompts for a single champion name
    
6. **Copy and paste the output of the script into Copilot, or set it up to add to Chat in VSCode:**
    python cleanup_duplicates.py
        Detects duplicate .json and .md files (case-insensitive)
        Offers to merge them safely

## Scripts and Tool dir Summary
Module Summaries
champ_intake.py
    Adds champion to owned list
    Creates placeholder JSON
    Generates prompt .md file
    Validates both files
    Copies prompt to clipboard
    Opens in VS Code or Notepad
    Updates timestamp if successful
setup_environment.py
    Installs required Python packages (e.g. pyperclip)
    Checks for VS Code CLI availability
    Ensures environment is ready before intake
cleanup_duplicate_champions.py
    Scans for case-insensitive duplicates in Champions/ and prompt/
    Merges content into one file
    Deletes redundant copies
    Adds merge header for traceability
Champ_synergy_check.py
    WIP
    To use copilot to compare owned champions from json and identify synergy across attacks, buffs, debuffs, and rotations.
update_owned_champions.py
    Run through owned champ list and update all older than 30 days, or without a date stamp.
##