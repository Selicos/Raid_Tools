# Boss Guide QA, Workflow & Copilot/AI Agent Standards (Canonical, 2025+)

## QA Section for [Boss Name] Notes Generation (Copilot-Standard, Modular, Validated)

**Question:** Should the guide fully document all [Boss Name] mechanics, forms, stat requirements, and trial types before mapping champions?
**Answer:** Yes. Begin with a comprehensive, validated section on boss mechanics, forms/phases, turn order, affinities, unique mechanics, and all trial types/stat thresholds. Use RaidHQ (primary), Ayumilove, HellHades, and in-game sources for cross-validation. Document all sources in the Markdown file and commit message.

**Question:** How should trials/mechanics be mapped to the owned champion list?
**Answer:** For each trial/mechanic, list all owned champions who can fulfill the requirement. Include both a per-trial table and a combo table showing which champions can fulfill multiple trials/mechanics. Note affinity safety/risk (multi-line, explicit), and special skill/turn order notes for each champion. Use only the canonical owned champion list (`Input/Owned_champion_list.md`).

**Question:** What is the preferred team-building and simulation approach?
**Answer:** Build and simulate 5–8 unique teams using only owned champions, maximizing:
- Total trial/mechanic completion (for score/rewards)
- Raw damage output (for leaderboard/rank)
- Hybrid approaches (balance of both)
For each team, provide: core roles, optimal combo, alternates, speed tuning, gear, masteries, manual/auto, strengths, weaknesses, simulated results, explicit affinity safety/risk (multi-line), and actionable trial/mechanic advice. Run at least 3 simulations per team and document results in the guide.

**Question:** How should the Table of Contents and navigation be structured?
**Answer:** Use a modular, anchor-linked Table of Contents at the top of the guide. Update section numbers and anchors to match the actual file structure. Add quick reference tables at the start of the guide for best teams by difficulty/trial/damage tier. Ensure all sections match the canonical template (`Tools/Boss_Guide_Template.md`).

**Question:** What additional reference and summary sections are required?
**Answer:**
- Best Champions & Team Participation: Table of top champions, their roles, and team participation.
- Direct Champion Comparisons by Role: Table or summary comparing only owned champions by key roles.
- Ideal Champions to Pull: List and rationale for each, with upgrade path advice.
- General Notes: Gear, masteries, stat priorities, manual/auto advice.
- Actionable Notes & Upgrade Advice: Trial/mechanic prioritization, upgrade path, common pitfalls.
- Validation & Simulation Notes: Document all validation sources, simulation steps, and results (minimum 3 runs per team).

**Question:** How should the guide be updated after a roster change?
**Answer:**
- Supply a new `Owned_champion_list.md` or add a new champion.
- Re-run the team and trial/mechanic mapping process to update all tables and recommendations.
- Regenerate the Ideal Champions to Pull and Team Upgrade Paths sections to reflect new gaps.
- Never overwrite the original file directly; always preserve previous versions and stage changes for review.

**Question:** What is the process for handling alternates, trial-specific champions, and affinity risk?
**Answer:**
- For each team, list alternates for each core role based on the owned champion list.
- Include trial/mechanic-specific alternates (champions used only for a specific trial/mechanic).
- Explicitly document affinity safety/risk for each team and alternate in all relevant sections (multi-line, per template).

**Question:** How should failures and troubleshooting be documented?
**Answer:**
- Document teams that almost work but miss a trial/mechanic or damage threshold.
- Include notes on why a team failed and what upgrades or changes would resolve the issue.
- Add troubleshooting and upgrade path advice in the actionable notes section.

**Question:** What is the preferred output format and update policy?
**Answer:**
- All outputs must be modular, human-readable Markdown, following the standard template.
- Never delete files or folders; create new versions for major changes.
- Document all validation and simulation steps in the Markdown file or commit message for transparency and reproducibility.

---

## Canonical Workflow Steps (Copilot/AI Agent)

1. **Research & Data Gathering**
   - Review authoritative [Boss Name] guides (RaidHQ, Ayumilove, HellHades, in-game).
   - Document all boss forms/phases, turn order, affinities, unique mechanics, and trial types/stat thresholds. Cross-validate and cite sources.
2. **Champion & Trial/Mechanic Mapping**
   - Cross-reference the canonical owned champion list with trial/mechanic requirements.
   - Build per-trial and combo tables, noting affinity safety/risk (multi-line, explicit) and special notes.
3. **Team Building & Simulation**
   - Build 5–8 unique teams using only owned champions, maximizing trial/mechanic completion, damage, and hybrid approaches.
   - For each team, specify all required details (roles, alternates, speed, gear, masteries, manual/auto, strengths, weaknesses, simulated results, affinity safety/risk, actionable advice).
   - Run at least 3 simulations per team and document results in the guide.
4. **Guide Structure & Output**
   - Use a modular, anchor-linked Table of Contents.
   - Add quick reference tables at the start of the guide.
   - Populate all required sections: boss mechanics, trial/mechanic mapping, team tables, detailed team sections, best champions, direct comparisons, ideal pulls, general notes, actionable advice, validation/simulation notes.
   - Use the canonical template (`Tools/Boss_Guide_Template.md`) for all guides.
5. **Update & Validation**
   - After any roster change, re-run all mapping, team building, and simulation steps.
   - Regenerate all tables and recommendations as needed.
   - Document all validation and simulation steps for transparency.
   - Never overwrite the original file directly; always preserve previous versions and stage changes for review.

---

## Required Information & Prompts for Guide Generation

- Full list of owned champions (`Input/Owned_champion_list.md`)
- Authoritative boss mechanics and trial/mechanic requirements (RaidHQ, Ayumilove, HellHades, in-game)
- Simulation results for each team (minimum 3 runs per team)
- Gear, masteries, and stat priorities for each role
- Affinity safety/risk notes for all teams and alternates (multi-line, explicit)
- Upgrade path and ideal pulls based on current gaps
- Validation and simulation documentation (sources, methodology, results)

---

## Task Checklist for [Boss Name] Guide Generation (Copilot/AI Agent)

- [ ] Gather and summarize all [Boss Name] mechanics, forms/phases, turn order, affinities, unique mechanics, trial types, and stat/stat thresholds (validated, sources cited)
- [ ] Map all trials/mechanics to owned champions (per-trial and combo tables, with affinity safety/risk and special notes)
- [ ] Draft and update a modular, anchor-linked Table of Contents (per template)
- [ ] Add quick reference tables for best teams by difficulty/trial/damage tier
- [ ] Build and simulate 5–8 unique teams (trial, damage, hybrid)
- [ ] For each team: document core roles, optimal combo, alternates, speed tuning, gear, masteries, manual/auto, strengths, weaknesses, simulated results, affinity safety/risk, actionable trial/mechanic advice
- [ ] Run at least 3 simulations per team and document results
- [ ] Summarize best champions & team participation (table)
- [ ] Create direct champion comparisons by role (owned only)
- [ ] List ideal champions to pull and team upgrade paths
- [ ] Add general notes, actionable advice, and common pitfalls
- [ ] Document all validation and simulation steps (sources, methodology, results)
- [ ] After any roster change, re-run all mapping, team building, and simulation steps; update all tables and recommendations
- [ ] Never delete files or folders; create new versions for major changes

---

## Additional Questions for User/Reviewer (Copilot/AI Agent)

1. Are there any specific team archetypes or trial/mechanic types you want prioritized in future updates?
A: Not any at this time. But leave this as an open option.
2. Should the guide include more detailed turn-by-turn skill usage for each team, or is the current actionable advice sufficient?
A: Use more detailed skill by skill usage. Include specific skill order from each champion to accomplish trials/mechanics as required.
3. Would you like to see more auto-friendly team options, or is manual play optimization the main focus?
A: Add auto friendly teams. Show the compromise in damage or trials/mechanics completed.
4. Are there any additional quick reference tables or summary formats you would find useful?
A: We need to review the teams and note speed tune, if applicable.
5. Should failures and troubleshooting notes be expanded with more detail or examples?
A: Yes, include enough information to identify where to restart in generating information about the boss.
6. Is the current update and validation process clear and easy to follow for future roster changes?
A: It looks good for now, yes

---

# Project-Wide Copilot & AI Agent Standards

- In all chat responses, process and include a "Why/what/outcome:" statement to identify the context, reasoning, and intended result of the response. 
- Use this logic for replies, but do not include this statement in the final output unless specifically requested.
- Replies should still be concise and informative, unless asked to be verbose.

## Markdown-First, Modular Workflow
- All boss/team guides must be written in Markdown, using the standard template (`Tools/Boss_Guide_Template.md`).
- JSON is for internal data only; Markdown is the canonical output for all guides.

## Affinity Safety/Risk Requirements
- Every boss/team Markdown file must:
  - Include explicit affinity information in the "Boss Mechanics & Stat Requirements" section.
  - For each team in the summary table and detailed section, add a clear "Affinity Safety/Risk" note (multi-line, per template).
  - Affinity notes must specify which affinities are safe, which are risky, and why (e.g., Spirit stun, weak affinity for key roles).
  - Avoid recommending weak affinity champions for key roles unless justified and explained.

## Update & Staging Policy
- When the owned champion list changes, all boss/team Markdown files must be updated and staged in a new file (e.g., `_v2.md` or date-stamped).
- Never overwrite the original file directly; always preserve previous versions.
- All updates must be reviewed and compared before becoming canonical.

## Section-by-Section Update & Guide Maintenance Workflow
- For each section in the Table of Contents (see `Tools/Boss_Guide_Template.md` for canonical structure and required sections):
  1. Review and update the Table of Contents in each FINAL boss note file to match the actual sections present in the file.
  2. Boss Mechanics & Stat Requirements: Re-validate mechanics, stat thresholds, affinity notes, and include a "Manual/Auto Play Notes" subsection.
  3. Teams by Estimated Damage/Clear Speed: Update table, add explicit, multi-line affinity column. All teams must use only unique, owned champions. If multiple teams use the same champion list, suggest variations based on boss mechanics or use case (e.g., manual vs auto, affinity risk, clear speed, etc.).
  4. Detailed Team Sections: Add/refresh explicit, multi-line affinity notes for each team; ensure all required subfields are present. If two teams use the same champion list, suggest variations based on boss mechanics, affinity, or playstyle.
  5. Best Champions & Team Participation: Update for new teams/champions.
  6. Direct Champion Comparisons by Role: Update for new roster. Only list owned champions in this section and include a note clarifying this.
  7. Ideal Champions to Pull: Remove now-owned, reprioritize. Only include champions not on the owned list.
  8. General Notes: Add or update actionable advice on gear, masteries, stat priorities, and manual/auto play.
  9. Validation & Simulation Notes: Document all validation and simulation steps, including number of test runs, clear time methodology, affinity risk observations, and data sources.

## Validation & Documentation
- All champion and boss data must be cross-checked with at least two sources (Ayumilove, Hellhades, Wiki).
- Every boss/team Markdown file must include a **'Validation & Simulation Notes'** section at the end, or explicit documentation of simulation/validation steps for each team. This section should state:
  - Number of simulations or test runs performed (minimum 3 per team recommended)
  - How clear times and success rates were determined (average, fastest, manual/auto, etc.)
  - Affinity safety/risk notes are based on observed weak hit rates and debuff reliability
  - Data sources used for validation (e.g., Hellhades, Ayumilove, in-game testing)
- Document all validation and simulation steps in the Markdown file or commit message for transparency and reproducibility.

## No Deletion Policy
- Never delete files or folders as part of this workflow. For large changes, create a new file for review and comparison.

## Project Focus & Data Flow
- Use `Input/Owned_champion_list.md` as the only source for team building.
- Default to Hard mode for all bosses; design for easy expansion to other difficulties and boss types.
- Always validate skills/mechanics with at least two online sources. Document validation in Markdown or commit messages.
- All outputs must follow the standard template and include boss mechanics, simulation summaries, and an indexed list of ideal champions to pull for upgrades.
- Remove or ignore all references to deprecated scripts, folders, or paths.

## Essential Workflows & Conventions
- Environment setup, champion list update, team generation, Markdown output, validation, and large change policy as described in `.github/copilot-instructions.md`.
- All Markdown files must use consistent header levels and section numbering. Use Black and flake8 for Python code. Use line-by-line edits for clarity and easier review. Prefer creating a new file for large changes.
- All champion data must be cross-checked with at least two sources. Document validation in Markdown or commit.
- All new features require pytest tests in `Tests/` or `root_Tests/`.

## AI Assistant Behavior & Code Generation Standards
- Markdown-first, modular outputs.
- Continue working on multi-step tasks for up to 4 cycles without asking for confirmation.
- Proactively suggest better solutions, tools, or implementations when applicable.
- Ensure full task completion before moving to next items.
- Leverage conversation history and project context for informed decisions.
- Prefer built-in tools over manual commands when available.
- Always include type hints and docstrings for new functions. Use pathlib for file operations. Implement proper error handling with try/except blocks. Update requirements.txt when adding new dependencies.
- Use clear, modular, human-readable Markdown. Use consistent header levels, section numbering, and tables. Prefer line-by-line edits for small changes and new files for large changes.
- Never delete files or folders. For large changes, create a new file for review and comparison.

## Safety, Security, and Fallback
- AI assistants must never delete files or folders, even if requested by a user.
- For any ambiguous workflow, defer to `.github/ai-assistant-instructions.md`.
- All destructive actions must be confirmed and executed by a human.

---

# This file merges the canonical QA/process workflow with all project-wide Copilot/AI agent standards. Use as the single source of truth for boss guide generation, validation, and maintenance in Raid Tools.
