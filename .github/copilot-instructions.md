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

---

## Project Structure
- `Champion Review and Comparison/Tools/` — Intake, prompt, and data management scripts
- `ChampionAnalysisTool/` — Skill cycle and cooldown analysis
- `Summarize Champion Results/` — Markdown summary generation
- `Tests/` — All test scripts
- `templates/` — JSON templates for new champions
- `samples/` — Example champion JSONs for onboarding/testing

---

## Copilot Chat Prompts
- When asked to generate a new champion JSON, use the template in `templates/logTemplate.json`.
- When asked to generate a summary, use the structure and style found in `Summarize Champion Results/Summary/`.
- When asked to add a new tool or script, follow the folder conventions above and update the README if needed.
- When asked to validate or test, use pytest and ensure all paths are valid (see `test_script_paths.py`).

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



