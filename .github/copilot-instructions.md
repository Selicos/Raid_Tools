### 7. Commit Message Formatting
- Always wrap the entire commit message in double quotes ("...") and use single quotes (') within the message to avoid syntax issues with git commit commands.
- Example: git commit -m "Add affinity notes to Spider teams and update summary table"
# Copilot & AI Agent Instructions for Raid Tools (Unified, Markdown-First, Oct 2025)

> This file is the authoritative, codebase-specific guide for all AI coding agents. For universal project rules, see `.github/ai-assistant-instructions.md` (fallback for any ambiguity).
## Copilot & AI Agent Instructions (Consolidated, Oct 2025)

### 1. Markdown-First, Modular Workflow
- All boss/team guides must be written in Markdown, using the standard template.
- JSON is for internal data only; Markdown is the canonical output for all guides.

### 2. Affinity Safety/Risk Requirements
- Every boss/team Markdown file must:
  - Include explicit affinity information in the "Boss Mechanics & Stat Requirements" section.
  - For each team in the summary table and detailed section, add a clear "Affinity Safety/Risk" note.
  - Affinity notes must specify which affinities are safe, which are risky, and why (e.g., Spirit stun, weak affinity for key roles).
  - Avoid recommending weak affinity champions for key roles unless justified and explained.
- Example affinity note format for teams:
  ```
  **Affinity Safety/Risk:**
  - Void: Safe for all roles.
  - Force: Safe unless [specific champion] is Magic affinity.
  - Magic: Risk if [specific champion] is Force affinity.
  - Spirit: Risk if slowest champion is a key role (e.g., Geomancer, Brogni, main revive, etc.); Spirit stun can break team cycle.
  ```

### 3. Update & Staging Policy
- When the owned champion list changes, all boss/team Markdown files must be updated and staged in a new file (e.g., `_v2.md` or date-stamped).
- Never overwrite the original file directly; always preserve previous versions.
- All updates must be reviewed and compared before becoming canonical.


### 4. Section-by-Section Update & Guide Maintenance Workflow
- For each section in the Table of Contents (see `Notes/Boss_Guide_Template.md` for canonical structure and required sections):
   1. **Review and update the Table of Contents in each FINAL boss note file to match the actual sections present in the file.**
   2. Boss Mechanics & Stat Requirements: Re-validate mechanics, stat thresholds, affinity notes, and include a "Manual/Auto Play Notes" subsection.
   3. Teams by Estimated Damage/Clear Speed: Update table, add explicit, multi-line affinity column. All teams must use only unique, owned champions. If multiple teams use the same champion list, suggest variations based on boss mechanics or use case (e.g., manual vs auto, affinity risk, clear speed, etc.).
   4. Detailed Team Sections: Add/refresh explicit, multi-line affinity notes for each team; ensure all required subfields are present. If two teams use the same champion list, suggest variations based on boss mechanics, affinity, or playstyle.
   5. Best Champions & Team Participation: Update for new teams/champions.
   6. Direct Champion Comparisons by Role: Update for new roster. Only list owned champions in this section and include a note clarifying this.
   7. Ideal Champions to Pull: Remove now-owned, reprioritize. Only include champions not on the owned list (e.g., Yakarl if not owned).
   8. General Notes: Add or update actionable advice on gear, masteries, stat priorities, and manual/auto play.
   9. Validation & Simulation Notes: Document all validation and simulation steps, including number of test runs, clear time methodology, affinity risk observations, and data sources.

#### Guide Creation & Update Process
- **For new boss guides:**
   1. Copy the latest `Notes/Boss_Guide_Template.md` as the starting point.
   2. Populate each section with boss-specific and team-specific information, using only owned champions and validated data.
   3. Ensure all sections are present, numbered, and formatted per the template, including explicit affinity notes and validation/simulation documentation.

- **For updating existing FINAL boss guides:**
   1. Create a new draft file (e.g., `BossName_Team_Notes_DRAFT.md` or with a date-stamp) rather than editing the FINAL file directly.
   2. Compare the FINAL file section-by-section to the current template, adding or updating any missing or outdated sections (Manual/Auto Play Notes, General Notes, explicit Affinity Safety/Risk, Validation & Simulation Notes, etc.).
   3. Update all team recommendations and analysis based on the current owned champion list, verifying that all team data and analysis is correct for the boss and available options.
   4. Recommend additional teams if new champions have been added since the last update.
   5. Stage the draft for review and comparison before replacing the FINAL file.

- **For all guides:**
   - Use the template as the canonical reference for structure, content, and formatting.
   - Document all validation and simulation steps in the "Validation & Simulation Notes" section at the end of each guide.
   - Ensure all guides use consistent section numbering and explicit affinity notes.
   - Review and update guides regularly as the owned champion list or game mechanics change.

### 5. Validation & Documentation
- All champion and boss data must be cross-checked with at least two sources (Ayumilove, Hellhades, Wiki).
- Every boss/team Markdown file must include a **'Validation & Simulation Notes'** section at the end, or explicit documentation of simulation/validation steps for each team. This section should state:
   - Number of simulations or test runs performed (minimum 3 per team recommended)
   - How clear times and success rates were determined (average, fastest, manual/auto, etc.)
   - Affinity safety/risk notes are based on observed weak hit rates and debuff reliability
   - Data sources used for validation (e.g., Hellhades, Ayumilove, in-game testing)
- Document all validation and simulation steps in the Markdown file or commit message for transparency and reproducibility.
- Run at least 3 simulations for each team and summarize results.

### 6. No Deletion Policy
- Never delete files or folders as part of this workflow.
- For large changes, create a new file for review and comparison.
## Project Focus & Data Flow
- **Main workflow:** Use `input/Owned_Champions/Owned_champion_list.md` to generate boss-specific, actionable Markdown (`.md`) outputs for Raid Shadow Legends. Markdown is now the primary and canonical output format for all boss and team guides.
- **Boss context:** Default to Hard mode for all bosses; design for easy expansion to other difficulties and boss types.
- **Champion data:** Always validate skills/mechanics with at least two online sources (Ayumilove, Hellhades, etc). Document validation in Markdown or commit messages.
- **Output:** Modular, human-readable Markdown for each boss, using only owned champions. All outputs must follow the standard template and include boss mechanics, simulation summaries, and an indexed list of ideal champions to pull for upgrades.
- **No legacy workflows:** Remove or ignore all references to deprecated scripts, folders, or paths (e.g., `Champion Review and Comparison/`). Only use current, documented scripts and folder names.
## Essential Workflows
- **Setup:** `python Tools/Setup_Environment.py` or `make setup` (creates `.venv`, installs requirements, sets up VS Code config)
- **Champion list update:** Edit `input/Owned_Champions/Owned_champion_list.md` to reflect current roster.
- **Team generation:** For each boss, generate Markdown guides using only owned champions, referencing validated data and following the standard template.
- **Markdown output:** All team guides and summaries must be modular, actionable, and human-readable. Use clear headers, tables, and role separation. Save outputs in the appropriate `Notes/` or `output/` subfolder. JSON is optional and only for internal data, not for primary documentation.
- **Validation:** Cross-check all champion and boss data with at least two sources. Document validation in the Markdown file or commit message.
- **Large changes:** If a change requires more than 20 lines of edits to a Markdown file, create a new file (e.g., with `_v2.md` suffix) for review and comparison, rather than overwriting the original.
## Conventions & Methodology
- **Markdown-first:** All boss and team guides must be written in Markdown, following the standard template. JSON is for internal data only.
- **Standard Template:** Every boss/team Markdown file must include the sections and structure shown in `Notes/Boss_Guide_Template.md`. Use this template as the canonical reference for formatting, required sections, and placeholder data. The template includes:
   1. Table of Contents (with Boss Mechanics & Stat Requirements as section 1)
   2. Boss Mechanics & Stat Requirements (with Manual/Auto Play Notes)
   3. Teams by Estimated Damage/Clear Speed (table, with explicit, multi-line Affinity Safety/Risk column)
   4. Detailed Team Sections (each with: core roles, optimal combo, alternates, speed tuning, gear, masteries, manual/auto, strengths, weaknesses, simulated results, explicit affinity safety/risk)
   5. Best Champions & Team Participation (table)
   6. Direct Champion Comparisons by Role (table or summary)
   7. Ideal Champions to Pull (indexed, actionable list)
   8. General Notes (gear, masteries, stat priorities, manual/auto advice)
   9. Validation & Simulation Notes (test runs, clear time methodology, affinity risk, data sources)
- **No file/folder deletion:** AI agents must never delete files or folders—never run or suggest destructive operations. If a file must be replaced with a large change, create a new file instead.
- **Prompt/JSON overwrite policy:** Never overwrite a completed prompt in `output/completed_prompts/`. Prompts in `input/Prompt/` are always overwritten unless a completed prompt exists.
- **Validation:** All champion data must be cross-checked with at least two sources (Ayumilove, Hellhades, Wiki). Document validation in Markdown or commit.
- **No legacy paths:** Always use the latest folder/script names (e.g., `ChampionIntake/`, not `Champion Review and Comparison/`).
- **Testing:** All new features require pytest tests in `Tests/` or `root_Tests/`.
- **Formatting:** All Markdown files must use consistent header levels and section numbering. Use Black and flake8 for Python code. Use line-by-line edits for clarity and easier review. Prefer creating a new file for large changes.
- **Affinity review** All teams should be reviewed for affinity safety/risk. Include explicit affinity information in the Boss Mechanics & Stat Requirements section, and highlight affinity considerations in each team's detailed section using the multi-line format from the template.
- **Affinity Safety/Risk:**
   - Void: Safe for all roles.
   - Force: Safe unless [specific champion] is Magic affinity.
   - Magic: Risk if [specific champion] is Force affinity.
   - Spirit: Risk if slowest champion is a key role (e.g., Geomancer, Brogni, main revive, etc.); Spirit stun can break team cycle.


# Boss Guide Creation & Update Workflow

**Summary:**
All boss and team guides must use `Notes/Boss_Guide_Template.md` as the single source of truth for required sections, structure, and formatting. Always start from the template for new guides, and use it as the reference when updating existing guides. This ensures consistency, completeness, and actionable documentation across all bosses.

## For New Boss Guides
1. Copy the latest `Notes/Boss_Guide_Template.md` as the starting point, and name the new file using the format `BOSSNAME_Difficulty_Team_Notes.md` (e.g., `FireKnight_Hard_Team_Notes.md`).
2. Populate each section with boss-specific and team-specific information, using only owned champions and validated data.
3. Ensure all sections are present, numbered, and formatted per the template, including explicit affinity notes and validation/simulation documentation.

## For Updating Existing FINAL Boss Guides
1. Create a new draft file (e.g., `BOSSNAME_Difficulty_Team_Notes_DRAFT.md` or with a date-stamp, following the naming format) rather than editing the FINAL file directly.
2. Compare the FINAL file section-by-section to the current template, adding or updating any missing or outdated sections:
    - Manual/Auto Play Notes
    - General Notes
    - Explicit Affinity Safety/Risk (multi-line format)
    - Validation & Simulation Notes
    - Any other required template sections
3. Update all team recommendations and analysis based on the current owned champion list, verifying that all team data and analysis is correct for the boss and available options.
4. Recommend additional teams if new champions have been added since the last update.
5. Stage the draft for review and comparison before replacing the FINAL file.

## Checklist for Updating Existing Guides
- [ ] Use the template as the canonical reference for structure, content, and formatting
- [ ] Ensure all required sections are present and numbered
- [ ] Add/refresh explicit, multi-line affinity notes in all relevant sections
- [ ] Add/refresh Manual/Auto Play Notes and General Notes
- [ ] Document all validation and simulation steps in the "Validation & Simulation Notes" section
- [ ] Update teams and analysis for new champions or roster changes
- [ ] Stage changes for review before finalizing

## For All Guides
- Use the template as the canonical reference for structure, content, and formatting.
- Document all validation and simulation steps in the "Validation & Simulation Notes" section at the end of each guide.
- Ensure all guides use consistent section numbering and explicit affinity notes.
- Review and update guides regularly as the owned champion list or game mechanics change.
## AI Assistant Behavior
- **Markdown-first:** All outputs must be Markdown unless otherwise specified. Use the standard template for all boss/team guides.
- **Persistence:** Continue working on multi-step tasks for up to 4 cycles without asking for confirmation.
- **Proactivity:** Suggest better solutions, tools, or implementations when applicable.
- **Completeness:** Ensure full task completion before moving to next items.
- **Context Awareness:** Leverage conversation history and project context for informed decisions.
- **Tool Usage:** Prefer built-in tools over manual commands when available.
- **Code Generation:** Always include type hints and docstrings for new functions. Use pathlib for file operations. Implement proper error handling with try/except blocks. Update requirements.txt when adding new dependencies.
- **Formatting:** Use clear, modular, human-readable Markdown. Use consistent header levels, section numbering, and tables. Prefer line-by-line edits for small changes and new files for large changes.
- **No Deletion:** Never delete files or folders. For large changes, create a new file for review and comparison.

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
N+2. Ideal Champions to Pull, up to 50 per boss based on team setup.

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
# Copilot & AI Agent Instructions for Raid Tools (Oct 2025)

> This file is the authoritative, codebase-specific guide for all AI coding agents. For universal project rules, see `.github/ai-assistant-instructions.md` (fallback for any ambiguity).

## Project Focus & Data Flow

- **Primary workflow:** Process the canonical owned champion list (`input/Owned_Champions/Owned_champion_list.md`) to generate actionable, boss-specific team recommendations and summaries for Raid Shadow Legends.
- **Boss context:** Default to Hard mode for all bosses (e.g., Clan Boss, Spider, Dragon, Fire Knight, etc.), but design for easy expansion to other difficulties and boss types.
- **Champion data:** Always validate champion skills, stats, and mechanics using at least two authoritative online sources (Ayumilove, Hellhades, official Wiki). Document validation in prompts, commits, or logs.
- **Output:** Generate modular, human-readable markdown guides and JSON summaries for each boss situation, using only owned champions. All outputs must be actionable and suitable for both AI and human review.
- **No legacy workflows:** Remove or ignore all references to deprecated scripts, folders, or paths (e.g., `Champion Review and Comparison/`). Only use current, documented scripts and folder names.

## Essential Workflows

- **Environment setup:** `python Tools/Setup_Environment.py` or `make setup` (creates `.venv`, installs requirements, sets up VS Code config)
- **Champion list update:** Edit `input/Owned_Champions/Owned_champion_list.md` to reflect current roster. All downstream outputs are based on this file.
- **Boss team generation:** For each boss, generate teams and guides using only owned champions, referencing validated skill/mechanic data from online sources.
- **Markdown/JSON output:** All team guides and summaries must be modular, actionable, and human-readable. Use clear headers, tables, and role separation. Save outputs in the appropriate `Notes/` or `output/` subfolder.
- **Validation:** Cross-check all champion and boss data with at least two sources. Use `Tools/validate_json.py` for JSON validation if applicable.

## Project Conventions

- **Champion JSONs:** Use only allowed top-level keys (`champion`, `rarity`, `owned`, `modules`). All modules (e.g., `synergy`, `gear`, `summary`) are nested under `modules`.
- **No file/folder deletion** by AI agents—never run or suggest destructive operations.
- **Prompt/JSON overwrite policy:** Never overwrite a completed prompt in `output/completed_prompts/`. Prompts in `input/Prompt/` are always overwritten unless a completed prompt exists.
- **Validation:** All champion data must be cross-checked with at least two sources (Ayumilove, Hellhades, Wiki). Document validation in prompts or commits.
- **No legacy paths:** Always use the latest folder/script names (e.g., `ChampionIntake/`, not `Champion Review and Comparison/`).
- **Testing:** All new features require pytest tests in `Tests/` or `root_Tests/`.

## Example: Boss Team Markdown Output

```markdown
# Hard Spider Teams (Owned Champions Only)

## Table of Contents
1. Teams by Estimated Clear Speed & Consistency
2. Key Boss Mechanics & Stat Requirements
3. High-Damage Nuker Teams
...
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
}
```
## Safety & Fallback

- Never delete files/folders. For any ambiguous workflow, defer to `.github/ai-assistant-instructions.md`.


# (Retain style, AI power, and housekeeping sections below as relevant)


## Table of Contents
1. [Project Overview](#project-overview)
2. [Boss Guide Creation & Update Workflow](#boss-guide-creation--update-workflow)
3. [JSON Export Structure and Enforcement](#json-export-structure-and-enforcement)
4. [Validation and Cross-Source Verification](#validation-and-cross-source-verification)
8. [Modular, Human-Readable Outputs](#modular-human-readable-outputs)
9. [AI Model and Tooling Guidance](#ai-model-and-tooling-guidance)
11. [Contribution and Review Process](#contribution-and-review-process)
12. [Example Section for Common Tasks](#example-section-for-common-tasks)
13. [General Guidelines](#general-guidelines)
14. [Change Management & Documentation](#change-management--documentation)
15. [Testing & Validation](#testing--validation)
16. [AI Model & Prompting](#ai-model--prompting)
17. [Formatting & Style](#formatting--style)
18. [Simplicity & Maintainability](#simplicity--maintainability)
19. [Feedback & Review](#feedback--review)
20. [Core Technical Standards](#core-technical-standards)
22. [Data Flow and Processing](#data-flow-and-processing)
23. [AI Assistant Behavior Guidelines](#ai-assistant-behavior-guidelines)
24. [Common Task Patterns](#common-task-patterns)
25. [Automation and Workflow](#automation-and-workflow)
27. [Security and Best Practices](#security-and-best-practices)
28. [Integration Guidelines](#integration-guidelines)
29. [Troubleshooting Common Issues](#troubleshooting-common-issues)
30. [Recent Changes & Updates](#recent-changes--updates)
31. [Future Development Considerations](#future-development-considerations)
32. [Contact and Contribution](#contact-and-contribution)

---

## Project Overview
Raid Tools is a Python-based project for analyzing Raid Shadow Legends champion data. The project generates JSON champion profiles, performs skill cycle analysis, and creates human-readable markdown summaries. This project follows modern Python practices with comprehensive testing, automation, and documentation standards.

## JSON Export Structure and Enforcement
- All champion JSON exports must be strictly modular and nested.
- Each module (e.g., `synergy`, `gear`, `summary`) must be a sub-object under a `modules` dictionary.
- Only the allowed top-level keys (`champion`, `rarity`, `owned`, `modules`) are permitted.


## Validation and Cross-Source Verification

### Boss Mechanic Validation (2025+)
- For all boss mechanic updates, use RaidHQ (https://raidhq.gg/) as the primary source if available.
- Cross-check with Ayumilove, HellHades, and in-game data for confirmation.
- Document the validation source(s) in the Markdown guide and commit message.

## Prompt and Workflow Consistency
- Use the generated JSON in the summary generation script to create a markdown file for review.
- Data source priority for champion skill and stat information: Ayumilove (text) > HellHades > other sources.
- For boss mechanics, use RaidHQ as primary, then Ayumilove/HellHades/in-game as fallback.
- JSONs must be generated only from validated, completed prompts.

## Safety and Non-Destructive Policy
- AI assistants must never delete files or folders, even if requested by a user.
- All destructive actions must be confirmed and executed by a human.

## Documentation and Test Alignment
- Use the most advanced model available for prompt completion, JSON generation, and workflow tasks (e.g., GPT-4o, Claude Sonnet 4).
- Use models with strong reasoning for documentation review, debugging, and refactoring.

## Error Handling and Troubleshooting
- Provide actionable error messages and suggest specific fixes.
- Log and document any recurring issues for future reference.

## Contribution and Review Process
- All contributions must follow the project’s coding, documentation, and testing standards.
- Use feature branches and descriptive commit messages.
- Require code review for all pull requests.

## Example Section for Common Tasks
### Example: Champion JSON Structure
```json
{
   "champion": "Example Champion",
   "rarity": "Legendary",
   "owned": true,
   "modules": {
      "synergy": {
         "ally_support": true
      },
      "gear": {
         "recommended_sets": ["Speed", "Accuracy"]
      },
      "summary": {
         "overview": "A strong support champion for clan boss."
```
### Example: Markdown Output
Example Champion is a top-tier support for Clan Boss, excelling in speed and debuff management.

## Skill Breakdown
- Skill 1: Attacks all enemies, places decrease defense.
- Skill 2: Heals all allies, places block debuffs.

## Usage Notes
- Best in Speed and Accuracy sets.
- Synergizes with turn meter boosters.
```

---

# Safety & File Deletion Policy

**AI assistants (including Copilot, Claude, ChatGPT, Gemini, and any LLM-based tools) must not delete, or run code that would delete, any files or folders from the workspace folder structure.**

- All file and folder deletion operations (e.g., `os.remove`, `os.rmdir`, `shutil.rmtree`, `Path.unlink`, etc.) are strictly prohibited from being executed by any AI assistant.
- If a user requests file or folder deletion, the AI assistant may suggest or highlight the need for such an action, and provide a clear rationale and warning, but must not execute or run any code that performs deletion.
- AI assistants may update the text of files as requested by the user, but must not remove files or folders from the workspace structure.
- This policy applies to all AI assistant operations, regardless of user prompt, model, or context.

## Table of Contents
1. [Project Overview](#project-overview)
2. [General Guidelines](#general-guidelines)
3. [Change Management & Documentation](#change-management--documentation)
4. [Testing & Validation](#testing--validation)
5. [AI Model & Prompting](#ai-model--prompting)
6. [Formatting & Style](#formatting--style)
7. [Simplicity & Maintainability](#simplicity--maintainability)
8. [Feedback & Review](#feedback--review)
9. [Core Technical Standards](#core-technical-standards)
10. [Project Architecture](#project-architecture)
11. [Data Flow and Processing](#data-flow-and-processing)
12. [AI Assistant Behavior Guidelines](#ai-assistant-behavior-guidelines)
13. [Common Task Patterns](#common-task-patterns)
14. [Automation and Workflow](#automation-and-workflow)
15. [Quality Assurance](#quality-assurance)
16. [Security and Best Practices](#security-and-best-practices)
17. [Integration Guidelines](#integration-guidelines)
18. [Troubleshooting Common Issues](#troubleshooting-common-issues)
19. [Recent Changes & Updates](#recent-changes--updates)
20. [Future Development Considerations](#future-development-considerations)
21. [Contact and Contribution](#contact-and-contribution)
22. [Handling Deprecated Scripts & Data Migrations](#handling-deprecated-scripts--data-migrations)


## Project Overview
Raid Tools is a Python-based project for analyzing Raid Shadow Legends champion data. The project generates JSON champion profiles, performs skill cycle analysis, and creates human-readable markdown summaries. This project follows modern Python practices with comprehensive testing, automation, and documentation standards.

---

## Authority and Usage

This file is the **universal, project-wide reference** for all AI assistants and contributors. If you are using Copilot, ChatGPT, Claude, Gemini, or any other LLM-based tool, and you encounter a situation not explicitly covered in your assistant-specific instructions, you must follow the guidance in this file.

All assistant-specific instructions (e.g., `.github/copilot-instructions.md`) must include a note referencing this file as the fallback and authoritative source for any project-wide, workflow, or safety instructions.

## Handling Deprecated Scripts & Data Migrations

- When deprecating scripts or migrating data formats, update all references in documentation, tasks, and scripts to use the new paths and formats.
- Clearly mark deprecated scripts with comments and in the project tracking file.
- Provide migration scripts or instructions when possible.
- Remove or archive legacy files after migration is validated.
- Update the Index of Bad Ideas & Risky Features if deprecation or migration introduces risk.

**Optimized for:** Claude Sonnet 3.5/4.0, GPT-4, GPT-4o, ChatGPT, Gemini, and any advanced coding LLMs with strong Python and project comprehension capabilities.

---

## General Guidelines
- **Always use the latest folder and script names; do not reference legacy paths (e.g., `Champion Review and Comparison/`).**
If you find any legacy paths or references (such as `Champion Review and Comparison/`), update them to the new structure (e.g., `ChampionIntake/`, `ChampionSummary/`, `src/`, `data/`, `output/`).
- **Language:** Python 3.9+ with type hints and f-string formatting
- **Code Formatting:** Black formatter (line length 88 characters)
- **Linting:** flake8 for code quality enforcement
- **Testing Framework:** pytest with 90%+ coverage target
- **Documentation:** Google-style docstrings for all public functions/classes
- **File Naming:** snake_case.py for all Python files
- **No Emojis:** Avoid emojis in code, documentation, or output
- **Error Handling:** Use Python exceptions with clear, actionable messages
- **Imports:** Use pathlib for file operations, organize imports logically
- **Functions:** Keep functions focused and small, prefer composition over inheritance
- **Cross-Platform:** All scripts must work on Windows, macOS, and Linux
- **Virtual Environment:** Use .venv for isolation
- **Dependencies:** Minimal, well-documented in requirements.txt
- **Automation:** Makefile and VS Code tasks for common operations
- **Chat Behavior:** Provide concise, relevant code snippets; continue to work on larger tasks up to 4 cycles without asking for confirmation if needed
- **Positive but Realistic:** Stay positive but when there is a better solution, tool, implementation, or approach, suggest it. Note when something is not possible or not recommended.
- **Accessing external sites:** Always allow access to Raid Shadow Legends Wiki, Ayumilove, Hellhades, and other relevant sites for champion data verification and research.
- **File edits:** Directly edit files, but prefer line by line changes instead of text blocks to better compare versions/commits, and allow smaller overall changes in each save/commit/etc.

---

## Change Management & Documentation
- Use line-by-line edits for clarity and easier review.
- Commit messages must be clear, imperative, and reference the logical unit of work (see project tracking file for examples).
- If a change affects documentation, update the relevant README or tracking file in the same commit.
- When updating documentation, ensure all references to scripts, folders, and workflows are current. Remove or update legacy references.
- When updating the project tracking file, always update the Index of Bad Ideas & Risky Features and keep section numbers sequential.
- All markdown files should use consistent header levels and section numbering.
- When adding new features, update all relevant documentation, tracking, and index files. Cross-reference related sections for clarity.

---

## Testing & Validation
- All new features and bugfixes must include or update pytest tests.
- Run `pytest` before committing.
- If a change affects VS Code tasks or Makefile, validate with `test_tasks_json_and_scripts.py`.

---

## AI Model & Prompting
- These instructions apply to all AI assistants (Copilot, Claude, ChatGPT, Gemini, etc.) and all human contributors.
- When generating code or documentation, prefer clarity and simplicity.
- Avoid overengineering or adding unnecessary complexity.
- For LLM/AI integration, only proceed if there is a clear, valuable use case.
- Reference the project tracking file for current status and risks.

---

## Formatting & Style
- Use Black and flake8 for all Python code. Run formatting and linting before committing.
- All markdown files should use consistent header levels and section numbering.

---

## Simplicity & Maintainability
- Favor simple, maintainable solutions. Avoid duplicating functionality already provided by external tools or libraries.

---

## Feedback & Review
- When reviewing or updating planning files, consolidate repeated feedback and clarify section purposes.
- If a change affects documentation, update all relevant files and cross-reference related sections.

---

## Core Technical Standards

### Development Environment
- **Cross-Platform:** All scripts must work on Windows, macOS, and Linux
- **Virtual Environment:** Use .venv for isolation
- **Dependencies:** Minimal, well-documented in requirements.txt
- **Automation:** Makefile and VS Code tasks for common operations

### Dependencies
Current requirements include:
- **colorama** — Cross-platform colored terminal text
- **pyperclip** — Clipboard access for copy/paste functionality
- **pytest** — Testing framework
- **black** — Code formatter
- Additional packages as needed (always update `requirements.txt`)

### Environment Setup Process
1. Clone the repository
2. Run `make setup` or manually create and activate virtual environment
3. Install dependencies from `requirements.txt`
4. Copy `.env.example` to `.env` and configure any secrets
5. Run `make test` or `pytest` to verify setup
6. Start with a small feature or bugfix branch

### Code Style Guidelines
- **No Emojis:** Avoid emojis in code, documentation, or output
- **Error Handling:** Use Python exceptions with clear, actionable messages
- **Imports:** Use pathlib for file operations, organize imports logically
- **Functions:** Keep functions focused and small, prefer composition over inheritance

---

## Project Architecture

### Directory Structure
```
Raid_Tools/
├── ChampionIntake/
│   ├── Champ_Intake.py  # Champion data intake script
│   ├── Tools/           # Data management and cleanup utilities
│   ├── Champions/       # JSON champion data files
│   ├── Comparisons/     # Champion comparison scripts
│   └── Tests/           # Module-specific tests
├── ChampionAnalysisTool/
│   ├── championAnalysis.py    # Skill cycle simulation
│   └── cooldown_analysis/     # Analysis output files
├── ChampionSummary/
│   ├── generateChampionSummaries.py  # Markdown generation
│   └── Summary/               # Human-readable summaries
├── root_Tests/          # Project-wide test cases
├── templates/           # JSON templates for new champions
├── .github/            # GitHub workflows and configuration
└── .vscode/            # VS Code tasks and settings
```

### Key Scripts and Their Purposes
- **Champ_Intake.py** — Main champion intake and prompt generation (located in `ChampionIntake/`)
- **championAnalysis.py** — Skill cycle simulation and cooldown analysis
- **generateChampionSummaries.py** — Convert analysis to readable markdown
- **Setup_Environment.py** — Automated environment setup
- **cleanup_duplicate_champions.py** — Merge duplicate champion files (located in `Tools/`)
- **Makefile** — Build automation and task management

---

## Data Flow and Processing

### Champion Data Pipeline
1. **Data Intake** (`Champ_Intake.py`)
   - Collect champion information from game sources
   - Generate structured JSON using templates/logTemplate.json
   - Validate against Raid Shadow Legends official data
   - Cross-reference with Ayumilove and Hellhades for accuracy

2. **Analysis Processing** (`championAnalysis.py`)
   - Parse champion skills and stats from JSON
   - Simulate skill rotation cycles
   - Calculate cooldown timings and optimal sequences
   - Generate analysis data for summary creation

3. **Summary Generation** (`generateChampionSummaries.py`)
   - Transform analysis into human-readable markdown
   - Structure: Executive summary, skill breakdown, notes
   - Output to ChampionSummary/Summary/ directory

### Data Validation Standards
- All champion JSONs must conform to the template structure
- Cross-reference multiple sources for data accuracy
- Implement schema validation for new champion fields
- Maintain data consistency across all output formats

---

## AI Assistant Behavior Guidelines

### Task Approach
- **Persistence:** Continue working on multi-step tasks for up to 4 cycles without asking for confirmation
- **Proactivity:** Suggest better solutions, tools, or implementations when applicable
- **Realism:** Clearly indicate when something is not possible or not recommended
- **Completeness:** Ensure full task completion before moving to next items
- **Context Awareness:** Leverage conversation history and project context for informed decisions
- **Tool Usage:** Prefer built-in tools over manual commands when available

### Code Generation Standards
- Always include type hints and docstrings for new functions
- Use pathlib for file operations instead of os.path
- Implement proper error handling with try/except blocks
- Follow the established naming conventions and file organization
- Update requirements.txt when adding new dependencies
- **JSON Processing:** Use GPT-4o for JSON file creation, modification, and structural updates
- **Template Compliance:** Ensure all champion JSONs follow the logTemplate.json structure
- Use pathlib for file operations instead of os.path
- Implement proper error handling with try/except blocks
- Follow the established naming conventions and file organization
- Update requirements.txt when adding new dependencies

### Testing Requirements
- Write pytest tests for all new features and bug fixes
- Place tests in appropriate directories (Tests/ or root_Tests/)
- Use descriptive test names and include docstrings
- Aim for 90%+ code coverage on core functionality
- Include schema validation tests for JSON data structures

---

## Common Task Patterns

### Champion JSON Creation
```python
# Use templates/logTemplate.json as the base structure
# Validate against multiple sources: Raid Shadow Legends, Ayumilove, Hellhades
# Ensure all required fields are present and correctly formatted
# Save to ChampionIntake/Champions/
# Use Tools/validate_json.py to verify JSON structure after creation
```

### JSON Validation and Fixing
```python
# Use Tools/validate_json.py for individual file validation
# Run with --all flag to validate all champion JSON files
# For corrupted files: identify specific line/column errors
# Apply targeted fixes rather than full file replacement when possible
```

### Summary Generation
```python
# Read from Champions/ directory
# Process through championAnalysis.py if needed
# Generate markdown with clear structure:
#   - Executive Summary
#   - Skill Breakdown
#   - Usage Notes
#   - Statistical Analysis
# Output to ChampionSummary/Summary/
```

### Script Enhancement
```python
# Add type hints to all function parameters and returns
# Include comprehensive docstrings with Args/Returns/Raises
# Implement proper error handling
# Add corresponding test cases
# Update documentation and README files
```

---

## Automation and Workflow

### Makefile Commands
- `make setup` — Environment setup and dependency installation
- `make test` — Run complete test suite with pytest
- `make lint` — Code quality check with flake8
- `make format` — Code formatting with Black
- `make intake` — Run champion data intake process
- `make analysis` — Execute champion analysis pipeline
- `make summary` — Generate markdown summaries
- `make clean` — Clean up build artifacts and cache

### VS Code & AI Assistant Integration
Available tasks via Command Palette, task runner, or AI assistant interface:
- "Run Champion Intake" — Execute data collection workflow
- "Run Champion Comparison Tracker" — Compare owned champions
- "Cleanup Duplicate Champions" — Remove duplicate entries
- "Run Champion Analysis Tool" — Perform skill cycle analysis
- "Generate Champion Summaries" — Create readable summaries

### LLM/AI Optimization
- **File Reading Strategy:** Read large meaningful chunks rather than small sections
- **Tool Usage:** Use semantic_search for project understanding, file_search for specific patterns
- **Code Generation:** Always include full context in code examples
- **Multi-step Tasks:** Break complex requests into logical sub-tasks
- **Error Handling:** Provide specific, actionable error messages and solutions

---

## Quality Assurance

### Code Review Checklist
- [ ] Type hints on all function signatures
- [ ] Google-style docstrings for public functions
- [ ] Proper error handling with meaningful messages
- [ ] Cross-platform compatibility (Windows/macOS/Linux)
- [ ] Test coverage for new functionality
- [ ] Updated documentation and README files
- [ ] Dependencies added to requirements.txt
- [ ] Black formatting applied
- [ ] flake8 linting passes

### Documentation Standards
- Use clear, concise language without emojis
- Include code examples for complex functions
- Document expected file formats and data structures
- Provide troubleshooting information for common issues
- Keep README files current with actual script behavior

---

## Security and Best Practices

### Data Handling
- Never commit secrets or API keys to the repository
- Use environment variables for sensitive configuration
- Validate all input data before processing
- Implement proper file permissions for output files

### Development Workflow
- Use feature branches for all changes
- Write descriptive commit messages (imperative mood)
- Test thoroughly before merging to main branch
- Follow semantic versioning for releases
- Document breaking changes clearly

---

## Integration Guidelines

### External Data Sources
- **Primary:** Raid Shadow Legends official game data
- **Secondary:** Ayumilove champion database
- **Tertiary:** Hellhades champion information
- **Resolution:** When sources conflict, use consensus of majority

### File Formats
- **Input:** JSON for structured champion data
- **Output:** Markdown for human-readable summaries
- **Templates:** JSON templates in templates/ directory
- **Logs:** Plain text with timestamps for debugging

---

## Troubleshooting Common Issues

### Path Resolution
- Always use absolute paths when possible
- Use pathlib.Path for cross-platform compatibility
- Check file existence before attempting operations
- Handle permission errors gracefully

### Data Consistency
- Validate JSON structure against templates
- Check for required fields before processing
- Handle missing or malformed data appropriately
- Log data quality issues for manual review

### Environment Issues
- Ensure Python 3.9+ is installed and accessible
- Verify virtual environment activation
- Check that all dependencies are installed
- Confirm cross-platform script execution

---

## Recent Changes & Updates

### Directory Structure Changes
- **ChampionSummary/** — Renamed from "Summarize Champion Results"
- **generateChampionSummaries.py** — Renamed from "jsonToMdPerChamp.py"
- All documentation updated to reflect new structure

### Tool Improvements
- Added comprehensive Makefile for automation
- Enhanced error handling and type hints in scripts
- Standardized docstrings and code formatting
- Updated VS Code tasks to match new directory structure

### Documentation Updates
- Consistent README files across all directories
- Updated script references and folder structures
- Improved onboarding instructions

---

## Future Development Considerations

### Planned Features
- Enhanced LLM integration for automated analysis
- Web interface for champion data management
- API endpoints for external tool integration
- Advanced statistical analysis capabilities

### Architecture Notes
- Keep AI/LLM components modular and configurable
- Design for extensibility in data source integration
- Maintain backward compatibility for existing data files
- Plan for scalable processing of large champion datasets

---

## Contact and Contribution
- Open issues for bugs or feature requests
- Follow the CC BY-NC 4.0 license for all contributions
- Attribute original authors in significant modifications
- Maintain project coding standards and documentation quality

---


# Champion Prompt Workflow (Updated Oct 2025)

## Workflow for Processing Champion Prompts

1. **Prompt Generation**:
   - Use the template in `ChampionIntake/templates/Prompt_Template.md`.
   - Skip JSON generation if a validated prompt already exists in `output/completed_prompts/`.

2. **Prompt Completion**:
   - Ensure all fields are human-readable and validated.
   - Validate skills, stats, multipliers, and cooldowns using authoritative sources in this order: Ayumilove (text), then HellHades, then other sources.

3. **JSON Generation**:
   - Generate the JSON response first, using the template structure.
   - Ignore the completed prompt file and directory for now.
   - Use the generated JSON in the summary generation script to create a markdown file for review.
   - Ensure the structure is modular and adheres to the template.

4. **Validation**:
   - Use `Tools/validate_json.py` to validate JSON files.
   - Confirm data accuracy and suitability for downstream tools.

5. **Output Organization**:
   - Ensure all outputs are human-readable and modular.
   - Completed prompt files are JSON, not markdown, and reside in `output/completed_prompts/`.

---