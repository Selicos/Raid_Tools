![Python](https://img.shields.io/badge/python-3.10%2B-blue)
![License: CC BY-NC 4.0](https://img.shields.io/badge/License-CC%20BY--NC%204.0-lightgrey.svg)
![Platform](https://img.shields.io/badge/platform-windows%20%7C%20linux%20%7C%20macos-blue)

# Raid Tools: Automation-Ready Boss & Team Guide System

> **Source of truth:** All workflows, templates, and best practices are in `.github/copilot-instructions.md` and `input/Templates/`.

## Onboarding

1. Read this README for a high-level overview and quick start.
2. For all details, workflows, and canonical templates, see `.github/copilot-instructions.md`.
3. Use the template files in `input/Templates/` for all new entries.

## Quick Start

1. Open a terminal in the repo root and run:
   ```sh
   python Tools/Setup_Environment.py
   ```
   - Creates `.venv`, installs requirements, and sets up VS Code configs.
2. Open the folder in VS Code. Select the `.venv` Python interpreter if prompted.
3. Install all recommended extensions when prompted.
4. Activate the virtual environment before running tests or scripts:
   - Windows: `.venv\Scripts\activate`
   - macOS/Linux: `source .venv/bin/activate`

## Core Workflows

### Champion Intake (4-Source Validation)
```sh
# Add new champion with owned count
python Tools/champion_scraper/champion_scraper.py "Champion Name" --owned 1

# Add champion (owned count defaults to existing value in table or 0)
python Tools/champion_scraper/champion_scraper.py "Champion Name"
```
- Scrapes Fandom table → Ayumilove (OCR) → HellHades
- Auto-validates and updates `Champion_stats.md` table
- Creates JSON in `input/Champion_Dictionary/`
- `--owned N` updates Owned column in Champion_stats.md

### Table Sync
```sh
# Sync Champion_stats.md with all JSON files
python Tools/champion_scraper/scripts/sync_table_from_json.py
```

### JSON Validation
```sh
python Tools/Validate/validate_json.py --schema
```

## Champion Dictionary Completion Workflow

**Standard Process: Option C (User Stats + AI Research)**

This is the canonical workflow for completing champion dictionary entries:

1. **User provides screenshot** of champion base stats (100% accurate)
2. **AI parses skills** from scraped data and populates:
   - `effects[]` arrays with damage multipliers, debuff/buff details
   - `mechanics_tags[]` for indexing
   - `book_value` and skill-specific `notes`
3. **Clean skill descriptions** (remove level-up info and multipliers)
4. **Meta research** from authoritative sources (HellHades, Ayumilove, RaidHQ)
5. **Cross-reference** with user's content priorities
6. **Validate and document** all sources

**Time estimate:** 2-3 minutes per champion

> For complete details, see `.github/copilot-instructions.md` → "Champion Dictionary Entry Completion Process"

## Directory Drop Points

| Entry Type                | Directory Path (relative to repo root)                | Notes |
|--------------------------|------------------------------------------------------|--------|
| Champion Dictionary      | input/Champion_Dictionary/                           | JSON files for completed champions |
| Champion Intake Queue    | input/Champion_Intake_list.md                        | List of champions to process (intake queue) |
| Champion Stats Table     | input/Champion_Dictionary/Champion_stats.md          | Reference table with all champion base stats + Owned column |
| Mechanic Dictionary      | input/Mechanic_Dictionary/                           | Mechanic reference files |
| Templates                | input/Templates/                                     | Canonical templates for all entry types |
| Prompts                  | input/Prompts/                                       | Automation prompts |
| Boss Guides              | Output/Boss_Guides/                                  | Generated boss guides |
| Build Evaluations        | Output/Build_Evaluations/                            | Champion build analysis |
| Mechanic Dictionary (Out)| Output/Mechanic_Dictionary/                          | Output mechanic files |

## Where to Find Templates

| Entry Type         | Template File (relative to repo root)           |
|--------------------|------------------------------------------------|
| Champion           | input/Templates/Champion_Dictionary_Template.json|
| Boss Guide         | input/Templates/Boss_Guide_Template.md          |
| Mechanic           | input/Templates/Mechanic_Entry_Template.json    |
| Team               | input/Templates/Team_Entry_Template.md          |
| Build Evaluation   | input/Templates/Build_Evaluation_Template.md    |

> For the latest and most detailed instructions, always refer to `.github/copilot-instructions.md`.

## Essential Commands

- `make setup` — Set up environment (venv, requirements)
- `make test` — Run all tests
- `make intake` — Intake a new champion
- `make analysis` — Run cooldown analysis
- `make summary` — Generate summary markdowns
- `make validate` — Validate all JSON files

Or use VS Code tasks (`Ctrl+Shift+P` → "Tasks: Run Task") or run scripts directly.

**Note:** Schema validation for champion JSONs uses the `jsonschema` package. Web scraping requires `requests`, `beautifulsoup4`, and `lxml`. OCR-based stat extraction (optional) requires `pillow`, `pytesseract`, and the [Tesseract OCR binary](https://github.com/UB-Mannheim/tesseract/wiki). The setup script installs all Python dependencies automatically.

## Best Practices

- Always use the canonical templates in `input/Templates/` for new entries
- For champion completion, use **Option C workflow** (user stats + AI research)
- Validate all entries with at least 2 authoritative sources
- Use DRAFT-to-FINAL workflow for major updates
- Document all sources in citations and commit messages

> For all other guidance, workflows, and standards, see `.github/copilot-instructions.md`.

---
Open the Command Palette (`Ctrl+Shift+P`), select “Tasks: Run Task”, and choose the desired operation.
