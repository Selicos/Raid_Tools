# Copilot & AI Agent Instructions (Variant 1 - Expanded)

> Authoritative guide for AI coding agents. For universal rules, see `.github/ai-assistant-instructions.md`.

## Project Focus & Data Flow
- **Main workflow:** Use `input/Owned_Champions/Owned_champion_list.md` to generate boss-specific, actionable markdown and JSON outputs for Raid Shadow Legends.
- **Boss context:** Default to Hard mode for all bosses; design for easy expansion.
- **Champion data:** Always validate skills/mechanics with at least two online sources (Ayumilove, Hellhades, Wiki). Document validation in prompts, commits, or logs.
- **Output:** Modular, human-readable markdown and JSON for each boss, using only owned champions.

## Essential Workflows
- **Setup:** `python Tools/Setup_Environment.py` or `make setup` (creates `.venv`, installs requirements, sets up VS Code config)
- **Champion list update:** Edit `input/Owned_Champions/Owned_champion_list.md` to reflect current roster.
- **Team generation:** For each boss, generate teams/guides using only owned champions, referencing validated data.
- **Markdown/JSON output:** All team guides and summaries must be modular, actionable, and human-readable. Use clear headers, tables, and role separation. Save outputs in the appropriate `Notes/` or `output/` subfolder.
- **Validation:** Cross-check all champion and boss data with at least two sources. Use `Tools/validate_json.py` for JSON validation if applicable.

## Conventions & Methodology
- **Champion JSONs:** Use only allowed top-level keys (`champion`, `rarity`, `owned`, `modules`). All modules (e.g., `synergy`, `gear`, `summary`) are nested under `modules`.
- **No file/folder deletion** by AI agents—never run or suggest destructive operations.
- **Prompt/JSON overwrite policy:** Never overwrite a completed prompt in `output/completed_prompts/`. Prompts in `input/Prompt/` are always overwritten unless a completed prompt exists.
- **Validation:** All champion data must be cross-checked with at least two sources (Ayumilove, Hellhades, Wiki). Document validation in prompts or commits.
- **No legacy paths:** Always use the latest folder/script names (e.g., `ChampionIntake/`, not `Champion Review and Comparison/`).
- **Testing:** All new features require pytest tests in `Tests/` or `root_Tests/`.
- **Formatting:** Use Black and flake8 for all Python code. All markdown files should use consistent header levels and section numbering.
- **Error Handling:** Use Python exceptions with clear, actionable messages. Prefer line-by-line edits for clarity and easier review.
- **Documentation:** Update README and internal docs to reflect current workflow and file structure. Use clear, concise language without emojis.
- **Automation:** Use Makefile and VS Code tasks for all core operations. Keep these in sync with scripts.
- **Cross-Platform:** All scripts must work on Windows, macOS, and Linux. Use `.venv` for isolation.
- **Dependencies:** Only add to `requirements.txt` if used in codebase. Remove unused packages after refactor.

## AI Assistant Behavior
- **Persistence:** Continue working on multi-step tasks for up to 4 cycles without asking for confirmation.
- **Proactivity:** Suggest better solutions, tools, or implementations when applicable.
- **Completeness:** Ensure full task completion before moving to next items.
- **Context Awareness:** Leverage conversation history and project context for informed decisions.
- **Tool Usage:** Prefer built-in tools over manual commands when available.
- **Code Generation:** Always include type hints and docstrings for new functions. Use pathlib for file operations. Implement proper error handling with try/except blocks. Update requirements.txt when adding new dependencies.

## Example: Boss Team Markdown Output
```markdown
# Hard Spider Teams (Owned Champions Only)
1. Teams by Estimated Clear Speed & Consistency
2. Key Boss Mechanics & Stat Requirements
3. High-Damage Nuker Teams
...etc.
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
