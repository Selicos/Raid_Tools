# Copilot & AI Agent Instructions (Variant 2)

> This file is the codebase-specific guide for all AI coding agents. Universal rules: `.github/ai-assistant-instructions.md`.

## Project Focus & Data Flow
- **Owned champion list** (`input/Owned_Champions/Owned_champion_list.md`) is the canonical source for all outputs.
- **Boss context:** Default to Hard mode for all bosses; design for future expansion.
- **Champion data:** Validate all skills/mechanics with at least two online sources (Ayumilove, Hellhades, Wiki). Document validation.
- **Output:** Generate modular, actionable markdown and JSON for each boss, using only owned champions.

## Key Workflows
- **Setup:** `python Tools/Setup_Environment.py` or `make setup`
- **Champion list update:** Edit `input/Owned_Champions/Owned_champion_list.md`
- **Team generation:** For each boss, generate teams/guides using only owned champions, referencing validated data.
- **Validation:** Use `Tools/validate_json.py` for JSON validation.

## Conventions
- **Champion JSONs:** Only allowed top-level keys (`champion`, `rarity`, `owned`, `modules`).
- **No file/folder deletion** by AI agents.
- **Prompt/JSON overwrite:** Never overwrite a completed prompt in `output/completed_prompts/`.
- **No legacy paths:** Use only current folder/script names.
- **Testing:** All new features require pytest tests in `Tests/` or `root_Tests/`.

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
