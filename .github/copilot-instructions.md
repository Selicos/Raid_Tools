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
- **Data Files:** Champion data is stored as JSON in `Champion Review and Comparison/Champions/`
- **Markdown Output:** All summaries and reports should be in Markdown, placed in `ChampionSummary/Summary/` or `cooldown_analysis/` folders
- **Environment:** Scripts must work cross-platform (Windows, macOS, Linux)
- **Dependencies:** List all dependencies in `requirements.txt`; avoid unnecessary packages
- **Chat Behavior:** Provide concise, relevant code snippets; continue to work on larger tasks up to 4 cycles without asking for confirmation if needed
- **No Emojis:** Do not use emojis in code, documentation, markdown, or output
- **Positive but Realistic:** Stay positive but when there is a better solution, tool, implementation, or approach, suggest it. Note when something is not possible or not recommended.
- **Accessing external sites** Always allow access to Raid Shadow Legends Wiki, Ayumilove, Hellhades, and other relevant sites for champion data verification and research.
- **File edits** directly edit files, but prefer line by line changes instead of text blocks to better compare versions/commits, and allow smaller overall changes in each save/commit/etc.

---

## Project Structure
- `Champion Review and Comparison/` — Contains main intake script and data management tools
  - `Champ_Intake.py` — Main champion intake and prompt generation
  - `Tools/` — Data management and cleanup utilities
  - `Champions/` — JSON champion data files
  - `Comparisons/` — Champion comparison scripts
  - `Tests/` — Module-specific tests
- `ChampionAnalysisTool/` — Skill cycle and cooldown analysis
- `ChampionSummary/` — Markdown summary generation (renamed from "Summarize Champion Results")
- `root_Tests/` — Project-wide test cases
- `templates/` — JSON templates for new champions
- `.github/` — GitHub configuration, workflows, and this instructions file
- `.vscode/` — VS Code tasks and settings

### Key Scripts and Files
- **Champ_Intake.py** — Main champion intake and prompt generation (located in `Champion Review and Comparison/`)
- **championAnalysis.py** — Skill cycle simulation and analysis
- **generateChampionSummaries.py** — Generate readable summaries (renamed from jsonToMdPerChamp.py)
- **Setup_Environment.py** — Environment setup and dependency installation
- **cleanup_duplicate_champions.py** — Merge duplicate champion files (located in `Champion Review and Comparison/Tools/`)
- **Makefile** — Automated tasks for setup, testing, formatting, and running tools

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
- When asked to generate a new champion JSON, use the template in `templates/logTemplate.json`. Ignore examples or presets and focus on the template structure.
  - Confirm the champion skills and stats are correct before finalizing any outputs.
  - Reference the Raid Shadow Legends Site then check against Ayumilove and Hellhades for accuracy. If something contradicts, use whichever sites agree. 
- When asked to generate a summary, use the structure and style found in `ChampionSummary/Summary/`. Ensure it is human readable and organized with an executive summary, skill breakdown, and notes. Update the summary with the latest analysis results.
- When asked to add a new tool or script, follow the folder conventions above and update the README if needed. Check if a task should be added for VS Code tasks or Makefile.
- When asked to validate or test, use pytest and ensure all paths are valid (see `test_script_paths.py`).
- When asked about project priorities or what to work on next, reference `Project tracking and new ideas.md` for the current roadmap and implementation order.

### Example Prompts
- "Generate a new champion JSON for 'Arbiter' using the template." (GPT-4o)
- "Add a pytest to validate all champion JSONs in the Champions folder." (GPT-4o)
- "Create a script to batch-generate summaries for all champions." (GPT-4o)
- "Refactor championAnalysis.py to use pathlib and add type hints." (Claude Sonnet 4)
- "Add a test for the LLM integration module." (GPT-4o)
- "Show an example of error handling for missing champion fields." (GPT-4o)
- "Update the README to include the new ChampionSummary tool." (Claude Sonnet 4)
- "What should I work on next according to the project tracking file?" (Claude Sonnet 4)
- "Create a new feature branch for the next section in project tracking." (GPT-4o)
- "Fix JSON formatting issues in Alice the Wanderer champion file." (GPT-4o)
- "Generate new champion JSON for Artak using the template." (GPT-4o)

---

## Contribution Workflow

### Git Workflow and Feature Branches
- **Feature Branches:** Use descriptive feature branches for all changes (e.g., `feature/schema-validation`, `feature/llm-integration`)
- **Branch Creation:** Create a new feature branch when starting work on a new section from `Project tracking and new ideas.md`
- **Single Focus:** Each branch should focus on one logical feature or improvement area
- **Testing:** Ensure all tests pass before merging to main

### Commit Strategy
- **Commit Frequency:** Make commits when you complete a logical unit of work (single function, test, or file)
- **Commit Messages:** Use imperative mood with clear, descriptive messages:
  - ✅ "Add schema validation for champion JSON files"
  - ✅ "Implement batch processing for champion intake"
  - ✅ "Fix path resolution in championAnalysis.py"
  - ❌ "Update stuff" or "Fix bug"

### When to Create a New Feature Branch
Reference the `Project tracking and new ideas.md` file for guidance:

1. **Starting a New Section:** When moving from one numbered section to another (e.g., Section 2 → Section 3)
2. **Major Focus Shift:** When switching between different types of work:
   - Testing & Validation → Champion Data Enhancements
   - Data Import/Export → LLM Integration
   - Champion Analysis → Database System
3. **Scope Change:** When the current work extends beyond the original branch purpose

### Commit Message Examples by Work Type
- **Features:** `feat: add gear recommendations to champion schema`
- **Bug Fixes:** `fix: correct cooldown calculation in skill analysis`
- **Documentation:** `docs: update README with new batch processing workflow`
- **Tests:** `test: add schema validation tests for champion JSONs`
- **Refactoring:** `refactor: extract common file operations to utility module`
- **Chores:** `chore: update dependencies and clean up imports`

### Branch Transition Workflow
1. **Complete Current Work:** Finish and commit all changes in current branch
2. **Create Commit:** `git commit -m "Complete [current feature description]"`
3. **Merge to Main:** Merge current branch after testing
4. **New Branch:** Create new branch for next project tracking item
5. **Notify:** Inform that work focus has shifted to new feature area

### Code Review and Merge Process
- Merge changes to main once fully tested and reviewed
- Recommend expanding tests for any new features or bug fixes before moving to the next feature branch
- Follow code review feedback and resolve merge conflicts promptly
- Document any breaking changes in commit messages

---

## Testing Standards

- All new features and bugfixes must include or update pytest tests in the `Tests/` or `root_Tests/` folders.
- Target 90%+ code coverage for core modules.
- Run `pytest` locally before pushing changes.
- Use descriptive test names and docstrings.
- Add schema validation tests for new champion JSON fields.
- Use the Makefile (`make test`) for consistent test execution.

---

## Error Handling & Logging

- Use Python exceptions for error handling; provide clear error messages.
- Log errors and warnings to the console or a log file as appropriate.
- Use try/except blocks for file I/O, JSON parsing, and external API calls.
- Document expected error cases in function docstrings.

---

## Style Guide & Naming Conventions

- Use Black for code formatting and flake8 for linting (available via Makefile: `make format` and `make lint`).
- Use snake_case for files, functions, and variables; PascalCase for classes.
- Write Google-style docstrings for all public functions/classes.
- Keep functions small and focused; prefer composition over inheritance.

---

## Automation & Build Tools

### Makefile Commands
The project includes a Makefile for common tasks:
- `make setup` — Set up environment and install dependencies
- `make test` — Run all tests with pytest
- `make lint` — Run flake8 linter
- `make format` — Run Black code formatter
- `make intake` — Run champion intake tool
- `make analysis` — Run champion analysis tool
- `make summary` — Generate champion summaries
- `make clean` — Remove .venv and cache files

### VS Code Tasks
Available tasks in `.vscode/tasks.json`:
- "Run Champion Intake" — Execute data collection workflow
- "Run Champion Comparison Tracker" — Compare owned champions
- "Cleanup Duplicate Champions" — Remove duplicate entries
- "Run Champion Analysis Tool" — Perform skill cycle analysis
- "Generate Champion Summaries" — Create readable summaries

### GitHub Copilot Integration
- Use Copilot Chat for complex multi-step tasks
- Leverage Copilot suggestions for boilerplate code generation
- Use inline completions for repetitive patterns
- Reference these instructions via `@workspace` in Copilot Chat

---

## Environment Setup

1. Clone the repository.
2. Run `make setup` or manually:
   - Create and activate a virtual environment
   - Install dependencies from `requirements.txt`
3. Copy `.env.example` to `.env` and set any required secrets.
4. Run `make test` or `pytest` to verify setup.
5. Review the README and these Copilot instructions.
6. Start with a small feature or bugfix branch.

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

## Documentation & Commenting Standards

- **No emojis:** Do not use emojis in code, documentation, markdown, or output.
- **Script/process flow:** For complex scripts, include a high-level docstring or markdown section outlining the main steps and logic. Use lists or simple ASCII diagrams if helpful.
- **Commenting:** Add comments explaining the purpose and flow of each function, especially for non-obvious or multi-step logic.
- **Example docstring:**
	```python
	def example_function(x: int) -> int:
		"""
		Brief description of what the function does.

		Args:
			x (int): Description of parameter x.

		Returns:
			int: Description of the return value.

		Flow:
			1. Step one description
			2. Step two description
			3. ...
		"""
		# ...function code...
	```
- **Example flow documentation (Markdown):**
	```markdown
	### Script Flow
	1. Load champion JSON
	2. Parse skills and stats
	3. Run cooldown analysis
	4. Generate markdown summary
	5. Save output to ChampionSummary/Summary/
	```

---

## Markdown Planning/Tracking File Standards

For all future project planning, roadmap, or tracking markdown files (e.g., project tracking, feature breakdowns):

- **Section Structure:**
	- Use unique numbered headings for all main sections (e.g., `### 1. Main Feature`)
	- Use lettered sub-sections for sub-features (e.g., `#### a. Sub-feature`)
	- Each section and sub-section should follow this template:
		- **Purpose:** Briefly describe the goal of the feature or task.
		- **Files/Paths:** List new or updated files/directories.
		- **Scripts to Edit:** List scripts/modules to be created or modified.
		- **Dependencies:** Note any dependencies or prerequisites.
		- **Tests:** Describe required or updated tests.
		- **README Updates:** Specify documentation changes.
- **Consistency:**
	- Ensure all sections use the same heading levels and order of fields.
	- Remove duplicates and keep sections uniquely numbered and sorted.
	- Use horizontal rules (`---`) to separate main sections.
- **Example Section:**
	```markdown
	### 2. Testing & Validation

	#### a. Implement Schema Validation
	- **Purpose:** Enforce JSON schema for champion files.
	- **Files/Paths:** `schemas/` directory for JSON schemas.
	- **Scripts to Edit:** Update test scripts to use schema validation.
	- **Dependencies:** Foundational files in place.
	- **Tests:** Add schema validation tests.
	- **README Updates:** Document schema validation.
	```

Follow this format for all new and updated planning markdown files to ensure clarity, maintainability, and easy sorting.

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

## Contact
For questions, open an issue or contact the repository owner.