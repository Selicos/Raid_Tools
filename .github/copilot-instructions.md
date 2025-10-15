# Housekeeping & Repo Maintenance Checklist (Copilot)

Use this checklist after any major code, process, or path update to ensure the repo remains clean, consistent, and maintainable.

## Housekeeping Steps (Copilot)

- [ ] Confirm all VS Code tasks in `.vscode/tasks.json` point to current, existing scripts. Update or remove any tasks for missing or deprecated scripts.
- [ ] Confirm `.github/ai-assistant-instructions.md` and `.github/copilot-instructions.md` are up to date with the current, advised workflow and guidelines as described in `.github/ai-assistant-instructions.md` and project chat/documentation.
- [ ] Run the "Cleanup Test Output Directories" task to ensure no test output directories contain stale or unnecessary files.
- [ ] Remove orphaned or deprecated scripts and files (not referenced in tasks, tests, or docs)
- [ ] Remove unused or empty folders (except required workflow folders)
- [ ] Clean up `requirements.txt` to include only packages actually used in the codebase
- [ ] Remove any leftover dependencies from previous features (e.g., clipboard/pyperclip)
- [ ] Run `pytest` and ensure all tests pass
- [ ] Run the “Organize Completed Prompts” task to tidy prompt files
- [ ] Confirm `.vscode/tasks.json` only references valid, existing scripts
- [ ] Remove or update any tasks for deleted/missing scripts
- [ ] Check for and remove any commented-out legacy code in scripts
# Housekeeping & Repo Maintenance Checklist

Use this checklist after any major code, process, or path update to ensure the repo remains clean, consistent, and maintainable. Update this section as new best practices or requirements emerge.

## Housekeeping Steps

- [ ] Remove orphaned or deprecated scripts and files (not referenced in tasks, tests, or docs)
- [ ] Remove unused or empty folders (except required workflow folders)
- [ ] Clean up `requirements.txt` to include only packages actually used in the codebase
- [ ] Remove any leftover dependencies from previous features (e.g., clipboard/pyperclip)
- [ ] Run `pytest` and ensure all tests pass
- [ ] Run the “Organize Completed Prompts” task to tidy prompt files
- [ ] Confirm `.vscode/tasks.json` only references valid, existing scripts
- [ ] Remove or update any tasks for deleted/missing scripts
- [ ] Check for and remove any commented-out legacy code in scripts

## Documentation & Test Updates

- [ ] Update `README.md` to match current repo structure, scripts, and workflow
- [ ] Update `.github/copilot-instructions.md` and internal docs to reference only current scripts, folders, and steps
- [ ] Remove any mention of deprecated workflows, scripts, or clipboard logic
- [ ] Add or update tests for any new scripts or features
- [ ] Periodically review and update test lists to match tasks and scripts

## General Best Practices

- [ ] Run all tests before every commit
- [ ] Keep documentation and tests tightly aligned with code and workflow
- [ ] Regularly review for any remaining legacy references or unused code

---





# AI Assistant Instructions for Raid Tools (Universal, Verbose, and Project-Focused)

## Project Goals

Raid Tools is a modular, maintainable, and human-readable system for managing, analyzing, and documenting Raid Shadow Legends champion data. The project’s primary goals are:

- To generate, validate, and maintain champion JSONs that are strictly modular and nested, supporting downstream tools and analysis.
- To ensure all champion data is accurate, up-to-date, and validated against authoritative sources (e.g., Raid Shadow Legends Wiki, Ayumilove, Hellhades).
- To provide a clear, auditable workflow for prompt completion, JSON generation, and champion analysis.
- To keep all outputs (JSON, markdown, analysis) human-readable, modular, and suitable for both AI and human review.
- To maintain a safe, non-destructive environment—no file or folder deletion by AI assistants.

## Workflow Overview

1. **Prompt Generation**
   - Generate or update a prompt in `input/Prompt/` using the provided template (`prompt_template.md`).
   - If a completed prompt already exists in `output/completed_prompts/`, skip prompt and JSON generation for that champion to avoid overwriting validated work.

2. **Prompt Completion**
   - Complete all modules in the prompt template, using the required JSON structure and ensuring all fields are filled in a human-readable format.
   - Validate all champion data (skills, stats, multipliers, cooldowns, etc.) using at least two authoritative sources.
   - If JSON formatting issues are found, identify and suggest the change, but do not loop through making changes without prompting.

3. **Move Completed Prompt**
   - Once the prompt is fully completed and validated, move it to `output/completed_prompts/`. Overwrite existing files if needed to ensure the latest validated data is available.

4. **JSON Generation**
   - Generate a single JSON file for the completed prompt, following all current JSON guidelines:
     - The JSON must be modular and strictly nested, with each module as a sub-object under a `modules` dictionary.
     - Only the allowed top-level keys (`champion`, `rarity`, `owned`, `modules`) are permitted.
     - Keys like `relentless_viability` and `mastery_impact_of_gear` must only appear within their relevant module object, not at the top level.
   - Save the JSON to `output/Champions/[champion].json`.

5. **Validation**
   - Run the validation script: `python Tools/validate_json.py output/Champions/[champion].json`
   - Confirm the JSON is valid, matches authoritative sources, and is suitable for downstream tools.

6. **Repeat for All Champions**
   - Repeat the above steps for all champions, ensuring all modules in the template are included and up to date.

## Script & Tooling Guidelines

- Use Python 3.9+ and ensure all scripts are formatted with Black and linted with flake8.
- All public functions/classes must have Google-style docstrings for clarity and maintainability.
- All new features and bugfixes must include or update pytest tests in the `Tests/` or `root_Tests/` folders.
- Never delete files or folders as part of any AI assistant workflow.
- Always use the latest folder and script names; do not reference legacy paths or clipboard logic.
- Use the Makefile and VS Code tasks for consistent task execution and validation.

## Formatting & Output Standards

- Use clear, numbered sections and headers in all markdown and documentation.
- Use fenced code blocks for JSON and code examples.
- Use bullet points and tables for options, requirements, and value explanations.
- Keep all outputs concise, explicit, and human-readable.

## Data Validation & Safety

- Always cross-check champion data with at least two authoritative sources.
- Document validation steps in the prompt, commit message, or workflow log.
- Never run or suggest file/folder deletion code. All destructive actions must be confirmed by a human.

## Model & Assistant Guidance

- These instructions are universal: they apply to any AI assistant (Copilot, Claude, ChatGPT, etc.) and all human contributors.
- For prompt completion, JSON generation, and workflow tasks, use the most advanced model available (e.g., GPT-4o, Claude Sonnet 4, or equivalent).
- For documentation review, file analysis, debugging, and large-scale refactoring, use models with strong reasoning and context capabilities.

---

## Safety & File Deletion Policy

**Copilot and Copilot Chat must not delete, or run code that would delete, any files or folders from the workspace folder structure.**

- All file and folder deletion operations (e.g., `os.remove`, `os.rmdir`, `shutil.rmtree`, `Path.unlink`, etc.) are strictly prohibited from being executed by Copilot or Copilot Chat.
- If a user requests file or folder deletion, Copilot may suggest or highlight the need for such an action, and provide a clear rationale and warning, but must not execute or run any code that performs deletion.
- Copilot may update the text of files as requested by the user, but must not remove files or folders from the workspace structure.
- This policy applies to all Copilot and AI assistant operations, regardless of user prompt or context.

---

## Handling Deprecated Scripts & Data Migrations

...existing code...
# GitHub Copilot Instructions for Raid Tools

> **Note:** This file provides Copilot-specific highlights and quick references. For all project-wide, workflow, or safety instructions not explicitly covered here, Copilot and Copilot Chat must reference `.github/ai-assistant-instructions.md` as the authoritative source.

---

## Table of Contents
1. [Copilot-Specific Highlights](#copilot-specific-highlights)
2. [Quick Reference: JSON Export Structure](#quick-reference-json-export-structure)
3. [Quick Reference: Prompt and Workflow](#quick-reference-prompt-and-workflow)
4. [General Guidelines (Copilot)](#general-guidelines-copilot)
5. [Contribution and Review Process (Copilot)](#contribution-and-review-process-copilot)
6. [Example Section for Common Tasks](#example-section-for-common-tasks)
7. [Further Project Guidance](#further-project-guidance)

---

## Copilot-Specific Highlights
- Use Python 3.9+ with type hints and f-strings
- Format code with Black, lint with flake8
- All public functions/classes must have Google-style docstrings
- All new features and bugfixes must include or update pytest tests
- Never delete files or folders as part of any Copilot workflow (see Safety in `.github/ai-assistant-instructions.md`)
- Always use the latest folder and script names; do not reference legacy paths or clipboard logic
- For any project-wide, workflow, or safety instructions, defer to `.github/ai-assistant-instructions.md`

---

## Quick Reference: JSON Export Structure
- All champion JSON exports must use a nested/module-based structure.
- Each module (e.g., `synergy`, `gear`, `summary`) must be a sub-object under a `modules` dictionary.
- Only the allowed top-level keys (`champion`, `rarity`, `owned`, `modules`) are permitted.
- Keys like `relentless_viability` and `mastery_impact_of_gear` must only appear within their relevant module object, not at the top level.
- Reference the template in `ChampionIntake/templates/logTemplate.json` as the canonical structure.
- For full details, see [JSON Export Structure and Enforcement](./ai-assistant-instructions.md#json-export-structure-and-enforcement)

---

## Quick Reference: Prompt and Workflow
- All prompt completions must use the template in `ChampionIntake/templates/Prompt_Template.md`.
- Completed prompts must be moved to `output/completed_prompts/` and not overwritten unless re-validated.
- JSONs must be generated only from validated, completed prompts.
- For full workflow, see [Prompt and Workflow Consistency](./ai-assistant-instructions.md#prompt-and-workflow-consistency)

---

## General Guidelines (Copilot)
- See [General Guidelines](./ai-assistant-instructions.md#general-guidelines) for universal project standards
- Use concise, relevant code snippets; continue to work on larger tasks up to 4 cycles without asking for confirmation if needed
- Stay positive but realistic; suggest better solutions when possible
- Directly edit files, prefer line-by-line changes for clarity
- For all other standards, see `.github/ai-assistant-instructions.md`

---

## Contribution and Review Process (Copilot)
- All contributions must follow the project’s coding, documentation, and testing standards (see [Contribution and Review Process](./ai-assistant-instructions.md#contribution-and-review-process))
- Use feature branches and descriptive commit messages
- Require code review for all pull requests

---

## Example Section for Common Tasks
See [Example Section for Common Tasks](./ai-assistant-instructions.md#example-section-for-common-tasks) for JSON, validation, and markdown output examples.

---

## Further Project Guidance
For all other project-wide, workflow, or safety instructions, always defer to `.github/ai-assistant-instructions.md` as the master reference.
If in doubt, follow the universal instructions.



## Handling Deprecated Scripts & Data Migrations

- When deprecating scripts or migrating data formats, update all references in documentation, tasks, and scripts to use the new paths and formats.
- Clearly mark deprecated scripts with comments and in the project tracking file.
- Provide migration scripts or instructions when possible.
- Remove or archive legacy files after migration is validated.
- Update the Index of Bad Ideas & Risky Features if deprecation or migration introduces risk.

## Champion Management CLI Tool


**The authoritative CLI tool for champion management, bulk import, and batch prompt generation is:**

  Tools/import_owned_champions.py

All documentation, tasks, and workflows must reference this script for champion intake, prompt generation, and owned list management. Do **not** reference `manage_champions.py` (this script does not exist) or any legacy paths.

### Sample Usage

```sh
# Import owned champions from a file (default: ChampionIntake/Champions/Owned_Champions/Owned_champion_list.md)
python Tools/import_owned_champions.py --from-owned-list

# Trigger champion intake and prompt generation for all owned champions
python Tools/import_owned_champions.py --from-owned-list --trigger-intake
# Import owned champions from a file (default: input/Owned_Champions/Owned_champion_list.md)
python Tools/import_owned_champions.py --from-owned-list
# Import a single champion by name and rarity
python Tools/import_owned_champions.py --name "Arbiter" --rarity "Legendary"
```

See the script's help for all options:

```sh
python Tools/import_owned_champions.py --help
```

Update all documentation and tasks to use this script for champion management workflows.

---

## Completed Markdown Output

All completed prompt markdown files (e.g., `[champion]_prompt.completed.md`) **must** be placed in the `output/completed_prompts/` directory. Use the Makefile target `make organize-completed` or the VS Code task “Organize Completed Prompts” to move all completed files automatically.

## Issue & Feature Request Templates

Use the provided markdown templates for bug reports and feature requests (see `.github/ISSUE_TEMPLATE/`).
Include steps to reproduce, expected/actual behavior, and relevant logs for bugs.
For features, describe the use case, requirements, and acceptance criteria.

# GitHub Copilot Instructions for Raid Tools

> **Note:** For any project-wide, workflow, or safety instructions not explicitly covered in this file, Copilot and Copilot Chat must reference `.github/ai-assistant-instructions.md` as the authoritative source.

## Purpose
This file provides clear, project-specific instructions for GitHub Copilot and Copilot Chat to ensure high-quality, consistent, and maintainable code contributions to the Raid Tools project.


**Note for GitHub Copilot**: This file is the authoritative reference for Copilot-specific behavior. For all project-wide, workflow, or safety instructions not directly covered here, Copilot and Copilot Chat must reference `.github/ai-assistant-instructions.md`.

## AI Model Recommendations
- **GPT-4.1**: Use for script development, code generation, project architecture, feature implementation, and general programming tasks
- **Claude Sonnet 4**: Use for documentation review, file analysis, debugging complex issues, code refactoring, and comprehensive project evaluation

---

## General Guidelines (Copilot-Specific)
- **Language:** Python 3.9+ (use type hints and f-strings)
- **Formatting:** Use Black for code formatting and flake8 for linting
- **Testing:** Use pytest for all tests; place tests in the `Tests/` and `root_Tests/` folders
- **Documentation:** All public functions/classes must have docstrings (Google style preferred)
- **File Naming:** Use `snake_case.py` for scripts and modules
- **Data Files:** Champion data is stored as JSON in `data/champions/`
- **Markdown Output:** All summaries and reports should be in Markdown, placed in `output/ChampionSummary/` or `output/cooldown_analysis/` folders
- **Environment:** Scripts must work cross-platform (Windows, macOS, Linux)
- **Dependencies:** List all dependencies in `requirements.txt`; avoid unnecessary packages
- **Chat Behavior:** Provide concise, relevant code snippets; continue to work on larger tasks up to 4 cycles without asking for confirmation if needed
- **No Emojis:** Do not use emojis in code, documentation, markdown, or output
- **Positive but Realistic:** Stay positive but when there is a better solution, tool, implementation, or approach, suggest it. Note when something is not possible or not recommended.
- **Accessing external sites:** Always allow access to Raid Shadow Legends Wiki, Ayumilove, Hellhades, and other relevant sites for champion data verification and research.
- **File edits:** Directly edit files, but prefer line by line changes instead of text blocks to better compare versions/commits, and allow smaller overall changes in each save/commit/etc.
- **Always use the latest folder and script names; do not reference legacy paths or clipboard logic.**

---

## Change Management & Documentation (Copilot-Specific)
- Use line-by-line edits for clarity and easier review.
- Commit messages must be clear, imperative, and reference the logical unit of work (see project tracking file for examples).
- If a change affects documentation, update the relevant README or tracking file in the same commit.
- When updating documentation, ensure all references to scripts, folders, and workflows are current. Remove or update legacy references.
- When updating the project tracking file, always update the Index of Bad Ideas & Risky Features and keep section numbers sequential.
- All markdown files should use consistent header levels and section numbering.
- When adding new features, update all relevant documentation, tracking, and index files. Cross-reference related sections for clarity.

---

## Testing & Validation (Copilot-Specific)
- All new features and bugfixes must include or update pytest tests.
- Run `pytest` before committing.
- If a change affects VS Code tasks or Makefile, validate with `test_tasks_json_and_scripts.py`.

---

## AI Model & Prompting (Copilot-Specific)
- When generating code or documentation, prefer clarity and simplicity.
- Avoid overengineering or adding unnecessary complexity.
- For LLM/AI integration, only proceed if there is a clear, valuable use case.
- Reference the project tracking file for current status and risks.

---

## Formatting & Style (Copilot-Specific)
- Use Black and flake8 for all Python code. Run formatting and linting before committing.
- All markdown files should use consistent header levels and section numbering.

---

## Simplicity & Maintainability (Copilot-Specific)
- Favor simple, maintainable solutions. Avoid duplicating functionality already provided by external tools or libraries.

---

## Feedback & Review (Copilot-Specific)
- When reviewing or updating planning files, consolidate repeated feedback and clarify section purposes.
- If a change affects documentation, update all relevant files and cross-reference related sections.

---

## Project Structure (Copilot-Specific)
- `src/` — All main scripts and modules
- `data/` — Champion JSONs, templates, and input files
- `output/` — Markdown summaries, analysis, and logs
- `Tests/` and `root_Tests/` — All test files
- `.github/` — GitHub configuration, workflows, and this instructions file
- `.vscode/` — VS Code tasks and settings
- `Makefile` — Automated tasks for setup, testing, formatting, and running tools

### Key Scripts and Files (Copilot-Specific)
- **import_owned_champions.py** — Bulk import and update of owned champions
- **Champ_Intake.py** — Main champion intake and prompt generation
- **championAnalysis.py** — Skill cycle simulation and analysis
- **generateChampionSummaries.py** — Generate readable summaries
- **Setup_Environment.py** — Environment setup and dependency installation
- **cleanup_duplicate_champions.py** — Merge duplicate champion files

---

## Copilot Chat Prompts & Example Usage (Copilot-Specific)

### Model Selection Guidelines (Copilot-Specific)
- **Use GPT-4o for:**
  - Script development and code generation
  - Feature implementation and new functionality
  - Project architecture decisions
  - Performance optimization
  - Algorithm implementation
  - JSON file creation and modification
  - Champion data structure updates
- **Use Claude Sonnet 4 for:**
  - Documentation review and improvement
  - File analysis and code structure evaluation
  - Debugging complex issues and error investigation
  - Code refactoring and cleanup
  - Comprehensive project evaluation

### Task-Specific Guidance (Copilot-Specific)
- When asked to generate a new champion JSON, use the template in `data/templates/logTemplate.json`. Ignore examples or presets and focus on the template structure.
  - Confirm the champion skills and stats are correct before finalizing any outputs.
  - Reference the Raid Shadow Legends Site then check against Ayumilove and Hellhades for accuracy. If something contradicts, use whichever sites agree. 
- When asked to generate a summary, use the structure and style found in `output/ChampionSummary/`. Ensure it is human readable and organized with an executive summary, skill breakdown, and notes. Update the summary with the latest analysis results.
- When asked to add a new tool or script, follow the folder conventions above and update the README if needed. Check if a task should be added for VS Code tasks or Makefile.
- When asked to validate or test, use pytest and ensure all paths are valid (see `root_Tests/test_script_paths.py`).

---

## Best Practices (Copilot-Specific)
- Keep functions small and focused; prefer composition over inheritance
- Use pathlib for file paths when possible
- Use environment variables for secrets/config (see `.env.example`)
- Always update `requirements.txt` if new dependencies are added
- Add comments for non-obvious logic
- Prefer explicit over implicit (see Zen of Python)
- Use the Makefile for consistent task execution
- Test thoroughly before committing

---

## Data Privacy & Security (Copilot-Specific)
- Never commit secrets or credentials to the repository.
- Use environment variables for all sensitive config (see `.env.example`).
- Review third-party dependencies for security risks.
- The `.gitignore` file excludes sensitive files like `.env`, `.vscode/`, cache files, and virtual environments.

---

## LLM/AI Integration (Copilot-Specific)
- If integrating LLMs, use modular design and keep API keys/secrets out of source code
- Place LLM-related scripts in a dedicated folder (e.g., `LLMTools/`)
- Document all prompts and expected outputs

---

## Issue & Feature Request Templates (Copilot-Specific)
- Use the provided markdown templates for bug reports and feature requests (see `.github/ISSUE_TEMPLATE/`).
- Include steps to reproduce, expected/actual behavior, and relevant logs for bugs.
- For features, describe the use case, requirements, and acceptance criteria.

---

## Attribution & License (Copilot-Specific)
- All contributions must comply with the CC BY-NC 4.0 license
- Attribute original authors in significant new files or modules

---

## Recent Changes & Updates (Copilot-Specific)
- All documentation, script references, and folder structures are up to date as of October 2025.
- The project tracking file is the authoritative source for priorities, risks, and roadmap.