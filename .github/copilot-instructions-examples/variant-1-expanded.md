
# Copilot & AI Agent Instructions (Variant 1 - Expanded)

> Authoritative guide for AI coding agents. For universal rules, see `.github/ai-assistant-instructions.md`.

## Quick Reference: Markdown-First Boss/Team Guide Workflow

- **Primary Output:** All boss and team guides must be written in Markdown, following the standard template below. JSON is for internal data only.
- **Template:** Every boss/team Markdown file must include:
  1. Table of Contents (with Boss Mechanics & Stat Requirements as section 1)
  2. Boss Mechanics & Stat Requirements (section 1)
  3. Teams by Estimated Damage/Clear Speed (table)
  4. Detailed Team Sections (each with: core roles, optimal combo, alternates, speed tuning, gear, masteries, manual/auto, strengths, weaknesses, simulated results)
  5. Best Champions & Team Participation (table)
  6. Direct Champion Comparisons by Role (table or summary)
  7. Ideal Champions to Pull (indexed, actionable list)
- **Validation:** All champion and boss data must be cross-checked with at least two sources (Ayumilove, Hellhades, Wiki). Document validation in Markdown or commit.
- **Simulation:** Run at least 3 simulations for each team and summarize results in the Markdown file.
- **File Handling:** Completed Markdown files are authoritative and must be preserved in `Notes/` or `output/`.
- **No Deletion:** Never delete files or folders as part of this workflow.



## Project Focus & Data Flow
- **Main workflow:** Use `input/Owned_Champions/Owned_champion_list.md` to generate boss-specific, actionable Markdown (`.md`) outputs for Raid Shadow Legends. Markdown is now the primary and canonical output format for all boss and team guides.
- **Boss context:** Default to Hard mode for all bosses; design for easy expansion to other difficulties and boss types.
- **Champion data:** Always validate skills/mechanics with at least two online sources (Ayumilove, Hellhades, Wiki). Document validation in prompts, commits, or logs.
- **Output:** Modular, human-readable Markdown for each boss, using only owned champions. All outputs must follow the standard template (see below) and include boss mechanics, simulation summaries, and an indexed list of ideal champions to pull for upgrades.


## Essential Workflows
- **Setup:** `python Tools/Setup_Environment.py` or `make setup` (creates `.venv`, installs requirements, sets up VS Code config)
- **Champion list update:** Edit `input/Owned_Champions/Owned_champion_list.md` to reflect current roster.
- **Team generation:** For each boss, generate Markdown guides using only owned champions, referencing validated data and following the standard template.
- **Markdown output:** All team guides and summaries must be modular, actionable, and human-readable. Use clear headers, tables, and role separation. Save outputs in the appropriate `Notes/` or `output/` subfolder. JSON is optional and only for internal data, not for primary documentation.
- **Validation:** Cross-check all champion and boss data with at least two sources. Document validation in the Markdown file or commit message.


## Conventions & Methodology
- **Markdown-first:** All boss and team guides must be written in Markdown, following the standard template below. JSON is for internal data only.
- **Standard Template:** Every boss/team Markdown file must include:
  1. Table of Contents (with Boss Mechanics & Stat Requirements as section 1)
  2. Boss Mechanics & Stat Requirements (section 1)
  3. Teams by Estimated Damage/Clear Speed (table)
  4. Detailed Team Sections (each with: core roles, optimal combo, alternates, speed tuning, gear, masteries, manual/auto, strengths, weaknesses, simulated results)
  5. Best Champions & Team Participation (table)
  6. Direct Champion Comparisons by Role (table or summary)
  7. Ideal Champions to Pull (indexed, actionable list)
- **No file/folder deletion** by AI agents—never run or suggest destructive operations.
- **Prompt/JSON overwrite policy:** Never overwrite a completed prompt in `output/completed_prompts/`. Prompts in `input/Prompt/` are always overwritten unless a completed prompt exists.
- **Validation:** All champion data must be cross-checked with at least two sources (Ayumilove, Hellhades, Wiki). Document validation in Markdown or commit.
- **No legacy paths:** Always use the latest folder/script names (e.g., `ChampionIntake/`, not `Champion Review and Comparison/`).
- **Testing:** All new features require pytest tests in `Tests/` or `root_Tests/`.
- **Formatting:** All Markdown files must use consistent header levels and section numbering. Use Black and flake8 for Python code.
- **Error Handling:** Use Python exceptions with clear, actionable messages. Prefer line-by-line edits for clarity and easier review.
- **Documentation:** Update README and internal docs to reflect current workflow and file structure. Use clear, concise language without emojis.
- **Automation:** Use Makefile and VS Code tasks for all core operations. Keep these in sync with scripts.
- **Cross-Platform:** All scripts must work on Windows, macOS, and Linux. Use `.venv` for isolation.
- **Dependencies:** Only add to `requirements.txt` if used in codebase. Remove unused packages after refactor.


## AI Assistant Behavior
- **Markdown-first:** All outputs must be Markdown unless otherwise specified. Use the standard template for all boss/team guides.
- **Persistence:** Continue working on multi-step tasks for up to 4 cycles without asking for confirmation.
- **Proactivity:** Suggest better solutions, tools, or implementations when applicable.
- **Completeness:** Ensure full task completion before moving to next items.
- **Context Awareness:** Leverage conversation history and project context for informed decisions.
- **Tool Usage:** Prefer built-in tools over manual commands when available.
- **Code Generation:** Always include type hints and docstrings for new functions. Use pathlib for file operations. Implement proper error handling with try/except blocks. Update requirements.txt when adding new dependencies.


## Example: Boss Team Markdown Output
```markdown
# [Boss Name] Teams (Owned Champions Only)

## Table of Contents
1. Boss Mechanics & Stat Requirements
2. Teams by Estimated Damage/Clear Speed
3. [Team Type 1]
4. [Team Type 2]
...
N. Best Champions & Team Participation
N+1. Direct Champion Comparisons by Role
N+2. Ideal Champions to Pull

---

## Boss Mechanics & Stat Requirements
- [Boss mechanics, immunities, stat thresholds, unique challenges, etc.]

---

## Teams by Estimated Damage/Clear Speed
| Team Name | Simulated Damage/Clear Time | Core Champions | Key Mechanics & Notes |
|---|:---:|---|---|
| ... | ... | ... | ... |

---

## [Team Type Section]
### Team: [Team Name]
**Core Roles:** ...
**Optimal Combo:** ...
**Alternates:** ...
**Speed Tuning:** ...
**Gear:** ...
**Masteries:** ...
**Manual/Auto:** ...
**Strengths:** ...
**Weaknesses:** ...
**Simulated Damage/Clear Time:** ...

---

## Best Champions & Team Participation
| Champion | Role(s) | Best Teams | Notes |
|---|---|---|---|

---

## Direct Champion Comparisons by Role
...

---

## Ideal Champions to Pull
- [List and rationale for each boss/team]
```

## Example: Champion JSON Structure
```json
{
  "champion": "Example Champion",
  "rarity": "Legendary",
  "owned": true,
  "modules": {
    "synergy": {"ally_support": true},
    "gear": {"recommended_sets": ["Speed", "Accuracy"]},
    "summary": {"overview": "A strong support champion for clan boss."}
  }
}
```

## Safety & Fallback
- Never delete files/folders. For ambiguous workflows, defer to `.github/ai-assistant-instructions.md`.

---

# (Retain style, AI power, and housekeeping sections below as relevant)
