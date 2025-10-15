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



# GitHub Copilot Instructions for Raid Tools


## Champion JSON Creation & Update Workflow (Authoritative)


This is the only approved workflow for creating or updating champion JSON logs in the Raid Tools project. All previous, parallel, or batch/automated alternatives are deprecated. Follow these steps for every champion update:

**Prompt File Handling:**
- All in-progress or incomplete prompts are kept in `input/Prompt/`.
- Once a prompt is fully validated and used to generate a JSON, the markdown file is moved to `output/completed_prompts/`.
- Completed prompts in `output/completed_prompts/` serve as the authoritative, human-readable record for each champion and are used for review, notes, and as the source for JSON generation and downstream tools (summary, cooldown analysis, etc.).
- If a completed prompt already exists in `output/completed_prompts/` for a champion, prompt and JSON generation for that champion is skipped. This prevents unnecessary overwrites and ensures completed prompts are not regenerated.
- Prompt files in `input/Prompt/` are always overwritten when generating prompts for a champion, unless a completed prompt already exists.

### Steps


1. **Champion Intake (Prompt Generation)**
   - If a champion name (and optionally rarity) is provided, generate or overwrite the prompt file in `input/Prompt/` using the template, unless a completed prompt already exists in `output/completed_prompts/` for that champion. If a completed prompt exists, skip prompt and JSON generation for that champion.
   - In batch mode (no champion provided), process all champions in the owned list, generating/overwriting prompt files in `input/Prompt/` for each, unless a completed prompt already exists for that champion.
   - Prompt files are always overwritten unless a completed prompt exists.
   - No clipboard or copy-to-clipboard logic is used. In single champion mode, the prompt file may be opened in the editor; in batch mode, prompt files are not opened.

2. **Complete the Prompt**
   - Fill out the prompt markdown file in `input/Prompt/`, ensuring all modules (0–20) are completed in the required JSON structure.
   - Do not proceed unless the prompt is 100% complete and accurate.

3. **Manual Validation of Champion Data**
   - Manually validate all champion data (name, skills, multipliers, cooldowns, stat priorities, etc.) using authoritative sources (Raid Shadow Legends Wiki, Ayumilove, Hellhades, etc.).
   - Only proceed if all data is correct and up to date. Document the validation step in the workflow log or commit message.

4. **Move Completed Prompt**
   - After the prompt is fully completed and validated, move the markdown file to `output/completed_prompts/` as `[champion]_prompt.completed.md`. This file is the authoritative, human-readable record for the champion.

5. **Generate the JSON Log**
   - Use the content of the completed prompt markdown to generate a single JSON object, following the template and module keys provided in the prompt (`data/templates/logTemplate.json`), including modules 0–20.
   - The JSON must reflect the validated champion name and data exactly.
   - Save the JSON to `output/Champions/[champion].json`.

6. **Validation**
   - Run validation with:
     ```sh
     python Tools/validate_json.py output/Champions/[champion].json
     ```
   - Confirm the script prints the champion name and rarity, and that the JSON is valid.
   - Only mark the champion as updated when the JSON passes all validation and matches the authoritative sources.

7. **Repeat for All Champions**
   - Continue this process for each champion as needed, especially after prompt updates, new information, or game changes. All new modules (14–20) are required for a complete prompt/JSON.

**Important:**
- Never generate or overwrite a prompt or JSON for a champion if a completed prompt already exists in `output/completed_prompts/` for that champion. This prevents unnecessary overwrites and ensures completed prompts are not regenerated.
- Prompt files in `input/Prompt/` are always overwritten unless a completed prompt exists.
- Never delete files or folders as part of this workflow.
- Completed prompts in `output/completed_prompts/` are the authoritative, human-readable record for each champion and should always be preserved for review, notes, and as the source for all downstream tools.
- As of October 2025, all prompts and JSON logs must include modules 0–20 (see expanded template and module files for details).

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

## Purpose
This file provides clear, project-specific instructions for GitHub Copilot and Copilot Chat to ensure high-quality, consistent, and maintainable code contributions to the Raid Tools project.

**Note for GitHub Copilot**: This file is the authoritative reference for GitHub Copilot and Copilot Chat. When working in VS Code, prioritize these instructions over other similar files in the repository.

## AI Model Recommendations
- **GPT-4.1**: Use for script development, code generation, project architecture, feature implementation, and general programming tasks
- **Claude Sonnet 4**: Use for documentation review, file analysis, debugging complex issues, code refactoring, and comprehensive project evaluation

---

## General Guidelines
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

## Project Structure
- `src/` — All main scripts and modules
- `data/` — Champion JSONs, templates, and input files
- `output/` — Markdown summaries, analysis, and logs
- `Tests/` and `root_Tests/` — All test files
- `.github/` — GitHub configuration, workflows, and this instructions file
- `.vscode/` — VS Code tasks and settings
- `Makefile` — Automated tasks for setup, testing, formatting, and running tools

### Key Scripts and Files
- **import_owned_champions.py** — Bulk import and update of owned champions
- **Champ_Intake.py** — Main champion intake and prompt generation
- **championAnalysis.py** — Skill cycle simulation and analysis
- **generateChampionSummaries.py** — Generate readable summaries
- **Setup_Environment.py** — Environment setup and dependency installation
- **cleanup_duplicate_champions.py** — Merge duplicate champion files

---

## Copilot Chat Prompts & Example Usage

### Model Selection Guidelines
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

### Task-Specific Guidance
- When asked to generate a new champion JSON, use the template in `data/templates/logTemplate.json`. Ignore examples or presets and focus on the template structure.
  - Confirm the champion skills and stats are correct before finalizing any outputs.
  - Reference the Raid Shadow Legends Site then check against Ayumilove and Hellhades for accuracy. If something contradicts, use whichever sites agree. 
- When asked to generate a summary, use the structure and style found in `output/ChampionSummary/`. Ensure it is human readable and organized with an executive summary, skill breakdown, and notes. Update the summary with the latest analysis results.
- When asked to add a new tool or script, follow the folder conventions above and update the README if needed. Check if a task should be added for VS Code tasks or Makefile.
- When asked to validate or test, use pytest and ensure all paths are valid (see `root_Tests/test_script_paths.py`).

---

## Best Practices
- Keep functions small and focused; prefer composition over inheritance
- Use pathlib for file paths when possible
- Use environment variables for secrets/config (see `.env.example`)
- Always update `requirements.txt` if new dependencies are added
- Add comments for non-obvious logic
- Prefer explicit over implicit (see Zen of Python)
- Use the Makefile for consistent task execution
- Test thoroughly before committing

---

## Data Privacy & Security
- Never commit secrets or credentials to the repository.
- Use environment variables for all sensitive config (see `.env.example`).
- Review third-party dependencies for security risks.
- The `.gitignore` file excludes sensitive files like `.env`, `.vscode/`, cache files, and virtual environments.

---

## LLM/AI Integration (Planned)
- If integrating LLMs, use modular design and keep API keys/secrets out of source code
- Place LLM-related scripts in a dedicated folder (e.g., `LLMTools/`)
- Document all prompts and expected outputs

---

## Issue & Feature Request Templates
- Use the provided markdown templates for bug reports and feature requests (see `.github/ISSUE_TEMPLATE/`).
- Include steps to reproduce, expected/actual behavior, and relevant logs for bugs.
- For features, describe the use case, requirements, and acceptance criteria.

---

## Attribution & License
- All contributions must comply with the CC BY-NC 4.0 license
- Attribute original authors in significant new files or modules

---

## Recent Changes & Updates
- All documentation, script references, and folder structures are up to date as of October 2025.
- The project tracking file is the authoritative source for priorities, risks, and roadmap.