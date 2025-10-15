# Housekeeping & Repo Maintenance Checklist

Use this checklist after any major code, process, or path update to ensure the repo remains clean, consistent, and maintainable.

## Housekeeping Steps

- [ ] Confirm all VS Code tasks in `.vscode/tasks.json` point to current, existing scripts. Update or remove any tasks for missing or deprecated scripts.
- [ ] Confirm `.github/ai-assistant-instructions.md` and `.github/copilot-instructions.md` are up to date with the current, advised workflow and guidelines as described in this file and in project chat/documentation.
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

# Universal AI Assistant Instructions for Raid Tools Project

> **Note:** This file is the authoritative, universal reference for all AI assistants (including Copilot, ChatGPT, Claude, Gemini, and any LLM-based tools) and all human contributors. For any project-wide, workflow, or safety instructions not explicitly covered in an assistant-specific file (e.g., `.github/copilot-instructions.md`), this file must be used as the source of truth.

---

## Core Reference for All AI Assistants

This file serves as the **core reference** for all AI assistants contributing to the Raid Tools project. It supersedes `.github/ai-assistant-instructions.md` and any other assistant-specific guidelines. All contributors, whether human or AI, must adhere to the instructions outlined here.

- **Scope**: Applies to Copilot, ChatGPT, Claude, Gemini, and any other AI tools.
- **Fallback**: If any ambiguity arises, this file takes precedence over other documentation.
- **Updates**: Ensure this file is updated alongside any major changes to workflows, scripts, or project structure.

---

## Table of Contents
1. [Project Overview](#project-overview)
2. [JSON Export Structure and Enforcement](#json-export-structure-and-enforcement)
3. [Validation and Cross-Source Verification](#validation-and-cross-source-verification)
4. [Prompt and Workflow Consistency](#prompt-and-workflow-consistency)
5. [Safety and Non-Destructive Policy](#safety-and-non-destructive-policy)
6. [Documentation and Test Alignment](#documentation-and-test-alignment)
7. [Modular, Human-Readable Outputs](#modular-human-readable-outputs)
8. [AI Model and Tooling Guidance](#ai-model-and-tooling-guidance)
9. [Error Handling and Troubleshooting](#error-handling-and-troubleshooting)
10. [Contribution and Review Process](#contribution-and-review-process)
11. [Example Section for Common Tasks](#example-section-for-common-tasks)
12. [General Guidelines](#general-guidelines)
13. [Change Management & Documentation](#change-management--documentation)
14. [Testing & Validation](#testing--validation)
15. [AI Model & Prompting](#ai-model--prompting)
16. [Formatting & Style](#formatting--style)
17. [Simplicity & Maintainability](#simplicity--maintainability)
18. [Feedback & Review](#feedback--review)
19. [Core Technical Standards](#core-technical-standards)
20. [Project Architecture](#project-architecture)
21. [Data Flow and Processing](#data-flow-and-processing)
22. [AI Assistant Behavior Guidelines](#ai-assistant-behavior-guidelines)
23. [Common Task Patterns](#common-task-patterns)
24. [Automation and Workflow](#automation-and-workflow)
25. [Quality Assurance](#quality-assurance)
26. [Security and Best Practices](#security-and-best-practices)
27. [Integration Guidelines](#integration-guidelines)
28. [Troubleshooting Common Issues](#troubleshooting-common-issues)
29. [Recent Changes & Updates](#recent-changes--updates)
30. [Future Development Considerations](#future-development-considerations)
31. [Contact and Contribution](#contact-and-contribution)
32. [Handling Deprecated Scripts & Data Migrations](#handling-deprecated-scripts--data-migrations)

---

## Project Overview
Raid Tools is a Python-based project for analyzing Raid Shadow Legends champion data. The project generates JSON champion profiles, performs skill cycle analysis, and creates human-readable markdown summaries. This project follows modern Python practices with comprehensive testing, automation, and documentation standards.

---

## JSON Export Structure and Enforcement
- All champion JSON exports must be strictly modular and nested.
- Each module (e.g., `synergy`, `gear`, `summary`) must be a sub-object under a `modules` dictionary.
- Only the allowed top-level keys (`champion`, `rarity`, `owned`, `modules`) are permitted.
- Keys like `relentless_viability` and `mastery_impact_of_gear` must only appear within their relevant module object, never at the top level.
- Reference the template in `ChampionIntake/templates/logTemplate.json` as the canonical structure.

## Validation and Cross-Source Verification
- All champion data (skills, stats, multipliers, cooldowns, etc.) must be validated against at least two authoritative sources (Raid Shadow Legends Wiki, Ayumilove, Hellhades).
- Document the validation process in prompts, commit messages, or workflow logs.

## Prompt and Workflow Consistency
- All prompt completions must use the template in `ChampionIntake/templates/Prompt_Template.md`.
- Completed prompts must be moved to `output/completed_prompts/` and not overwritten unless re-validated.
- JSONs must be generated only from validated, completed prompts.

## Safety and Non-Destructive Policy
- AI assistants must never delete files or folders, even if requested by a user.
- All destructive actions must be confirmed and executed by a human.

## Documentation and Test Alignment
- Any new feature, script, or workflow change must be accompanied by updates to documentation and tests.
- README and internal docs must always reflect the current workflow and file structure.

## Modular, Human-Readable Outputs
- All outputs (JSON, markdown, analysis) must be human-readable, modular, and suitable for both AI and human review.
- Use clear headers, bullet points, and tables in markdown outputs.

## AI Model and Tooling Guidance
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
      }
   }
}
```
### Example: Validation Log
```
Validated skills and multipliers against Raid Shadow Legends Wiki and Ayumilove. Both sources agree on cooldowns and multipliers. No discrepancies found.
```
### Example: Markdown Output
```
# Example Champion Summary

## Executive Summary
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