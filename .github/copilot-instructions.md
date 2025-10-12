# GitHub Copilot Instructions for Raid Tools

## Purpose
This file provides clear, project-specific instructions for GitHub Copilot and Copilot Chat to ensure high-quality, consistent, and maintainable code contributions to the Raid Tools project.

---

## General Guidelines
- **Language:** Python 3.9+ (use type hints and f-strings)
- **Formatting:** Use Black for code formatting and flake8 for linting
- **Testing:** Use pytest for all tests; place tests in the `Tests/` folder
- **Documentation:** All public functions/classes must have docstrings (Google style preferred)
- **File Naming:** Use `snake_case.py` for scripts and modules
- **Data Files:** Champion data is stored as JSON in `Champion Review and Comparison/Champions/`
- **Markdown Output:** All summaries and reports should be in Markdown, placed in the appropriate `Summary/` or `cooldown_analysis/` folder
- **Environment:** Scripts must work cross-platform (Windows, macOS, Linux)
- **Dependencies:** List all dependencies in `requirements.txt`; avoid unnecessary packages
- **Chat Behavior:** Provide concise, relevant code snippets; continue to work on larger tasks up to 4 cycles without asking for confirmation if needed
- **No Emojis:** Do not use emojis in code, documentation, markdown, or output
- 

---

## Project Structure
- `Champion Review and Comparison/Tools/` — Intake, prompt, and data management scripts
- `ChampionAnalysisTool/` — Skill cycle and cooldown analysis
- `Summarize Champion Results/` — Markdown summary generation
- `Tests/` — All test scripts
- `templates/` — JSON templates for new champions
- `samples/` — Example champion JSONs for onboarding/testing

---


## Copilot Chat Prompts & Example Usage

- When asked to generate a new champion JSON, use the template in `templates/logTemplate.json`. Ignore examples or presets and focus on the template structure.
  - Confirm the champion skills and stats are correct before finalizing any outputs.
  - Reference the Raid Shadow Legends Site then check against Ayumilove and Hellhades for accuracy.  If something contradicts, use whichever sites to agree. 
- When asked to generate a summary, use the structure and style found in `Summarize Champion Results/Summary/`. Ensure it is human readable and organized with an executive summary, skill breakdown, and notes.
- When asked to add a new tool or script, follow the folder conventions above and update the README if needed. Check if a task should be added for vscode tasks or Makefile.
- When asked to validate or test, use pytest and ensure all paths are valid (see `test_script_paths.py`).

### Example Prompts
- "Generate a new champion JSON for 'Arbiter' using the template."
- "Add a pytest to validate all champion JSONs in the Champions folder."
- "Create a script to batch-generate summaries for all champions."
- "Refactor championAnalysis.py to use pathlib and add type hints."
- "Add a test for the LLM integration module."
- "Show an example of error handling for missing champion fields."

---

## Contribution Workflow

- Use feature branches for all changes (e.g., `feature/short-description`).
- Write clear, descriptive commit messages (imperative mood, e.g., "Add champion batch processing script").
- Commit and push to a feature branch and advise when the current work item has changed and a new branch should be created.
- Merge changes to main once fully tested and reviewed.
- Recommend expanding tests for any new features or bug fixes before moving to the next branch of feature.
- Follow code review feedback and resolve merge conflicts promptly.

---

## Testing Standards

- All new features and bugfixes must include or update pytest tests in the `Tests/` folder.
- Target 90%+ code coverage for core modules.
- Run `pytest` locally before pushing changes.
- Use descriptive test names and docstrings.
- Add schema validation tests for new champion JSON fields.

---

## Error Handling & Logging

- Use Python exceptions for error handling; provide clear error messages.
- Log errors and warnings to the console or a log file as appropriate.
- Use try/except blocks for file I/O, JSON parsing, and external API calls.
- Document expected error cases in function docstrings.

---

## Style Guide & Naming Conventions

- Use Black for code formatting and flake8 for linting.
- Use snake_case for files, functions, and variables; PascalCase for classes.
- Write Google-style docstrings for all public functions/classes.
- Keep functions small and focused; prefer composition over inheritance.

---

## Onboarding Checklist

1. Clone the repository.
2. Create and activate a virtual environment.
3. Install dependencies from `requirements.txt`.
4. Copy `.env.example` to `.env` and set any required secrets.
5. Run `pytest` to verify setup.
6. Review the README and Copilot instructions.
7. Start with a small feature or bugfix branch.

---

## LLM/AI Prompt Engineering Guidelines

- Write clear, concise prompts for LLM modules.
- Version and document all prompt templates in `llm/prompts/`.
- Test prompts for expected output and edge cases.
- Avoid leaking secrets or sensitive data in prompts.

---

## Data Privacy & Security

- Never commit secrets or credentials to the repository.
- Use environment variables for all sensitive config (see `.env.example`).
- Review third-party dependencies for security risks.

---

## Issue & Feature Request Templates

- Use the provided markdown templates for bug reports and feature requests (see `.github/ISSUE_TEMPLATE/`).
- Include steps to reproduce, expected/actual behavior, and relevant logs for bugs.
- For features, describe the use case, requirements, and acceptance criteria.

---

## Automation & CI/CD

- Use the Makefile for common automation tasks (lint, test, format, etc.).
- Integrate with CI/CD to run tests and checks on all pull requests.
- Add pre-commit hooks for formatting and linting if possible.

---

---

## Best Practices
- Keep functions small and focused; prefer composition over inheritance
- Use pathlib for file paths
- Use environment variables for secrets/config (see `.env.example`)
- Always update requirements.txt if new dependencies are added
- Add comments for non-obvious logic
- Prefer explicit over implicit (see Zen of Python)
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
	5. Save output to Summary/
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

## LLM/AI Integration (Planned)
- If integrating LLMs, use modular design and keep API keys/secrets out of source code
- Place LLM-related scripts in a dedicated folder (e.g., `LLMTools/`)
- Document all prompts and expected outputs

---

## Attribution & License
- All contributions must comply with the CC BY-NC 4.0 license
- Attribute original authors in significant new files or modules

---

## Example Copilot Prompts
- "Generate a new champion JSON for 'Arbiter' using the template."
- "Add a pytest to validate all champion JSONs in the Champions folder."
- "Create a script to batch-generate summaries for all champions."
- "Refactor championAnalysis.py to use pathlib and add type hints."

---

## Contact
For questions, open an issue or contact the repository owner.



