# Chimera Boss Guide: QA Process, Workflow, and Prompt Requirements (2025)

## QA Section for Chimera Boss Notes Generation (Updated)

**Question:** Should the guide fully document all Chimera boss mechanics, forms, stat requirements, and trial types before mapping champions?
**Answer:** Yes. Begin with a comprehensive section on boss mechanics, forms, turn order, affinities, unique mechanics, and all trial types/stat thresholds. Use RaidHQ, Ayumilove, HellHades, and in-game sources for validation.

**Question:** How should trials be mapped to the owned champion list?
**Answer:** For each trial, list all owned champions who can fulfill the requirement. Include both a per-trial table and a combo table showing which champions can fulfill multiple trials. Note affinity safety/risk and special skill/turn order notes for each champion.

**Question:** What is the preferred team-building and simulation approach?
**Answer:** Build and simulate 5–8 unique teams using only owned champions, maximizing:
- Total trial completion (for score/rewards)
- Raw damage output (for leaderboard/rank)
- Hybrid approaches (balance of both)
For each team, provide: core roles, optimal combo, alternates, speed tuning, gear, masteries, manual/auto, strengths, weaknesses, simulated results, explicit affinity safety/risk, and actionable trial advice. Run at least 3 simulations per team and document results.

**Question:** How should the Table of Contents and navigation be structured?
**Answer:** Use a modular, anchor-linked Table of Contents at the top of the guide. Update section numbers and anchors to match the actual file structure. Add quick reference tables at the start of the guide for best teams by difficulty/trial/damage tier.

**Question:** What additional reference and summary sections are required?
**Answer:**
- Best Champions & Team Participation: Table of top champions, their roles, and team participation.
- Direct Champion Comparisons by Role: Table or summary comparing only owned champions by key roles.
- Ideal Champions to Pull: List and rationale for each, with upgrade path advice.
- General Notes: Gear, masteries, stat priorities, manual/auto advice.
- Actionable Notes & Upgrade Advice: Trial prioritization, upgrade path, common pitfalls.
- Validation & Simulation Notes: Document all validation sources, simulation steps, and results.

**Question:** How should the guide be updated after a roster change?
**Answer:**
- Supply a new `Owned_champion_list.md` or add a new champion.
- Re-run the team and trial mapping process to update all tables and recommendations.
- Regenerate the Ideal Champions to Pull and Team Upgrade Paths sections to reflect new gaps.

**Question:** What is the process for handling alternates, trial-specific champions, and affinity risk?
**Answer:**
- For each team, list alternates for each core role based on the owned champion list.
- Include trial-specific alternates (champions used only for a specific trial).
- Explicitly document affinity safety/risk for each team and alternate in all relevant sections.

**Question:** How should failures and troubleshooting be documented?
**Answer:**
- Document teams that almost work but miss a trial or damage threshold.
- Include notes on why a team failed and what upgrades or changes would resolve the issue.

**Question:** What is the preferred output format and update policy?
**Answer:**
- All outputs must be modular, human-readable Markdown, following the standard template.
- Never delete files; create new versions for major changes.
- Document all validation and simulation steps in the Markdown file or commit message.

---

## Workflow Steps (Canonical)

1. **Research & Data Gathering**
   - Review authoritative Chimera boss guides (RaidHQ, Ayumilove, HellHades, in-game).
   - Document all boss forms, turn order, affinities, unique mechanics, and trial types/stat thresholds.
2. **Champion & Trial Mapping**
   - Cross-reference the owned champion list with trial requirements.
   - Build per-trial and combo tables, noting affinity safety/risk and special notes.
3. **Team Building & Simulation**
   - Build 5–8 unique teams using only owned champions, maximizing trial completion, damage, and hybrid approaches.
   - For each team, specify all required details (roles, alternates, speed, gear, masteries, manual/auto, strengths, weaknesses, simulated results, affinity safety/risk, actionable advice).
   - Run at least 3 simulations per team and document results.
4. **Guide Structure & Output**
   - Use a modular, anchor-linked Table of Contents.
   - Add quick reference tables at the start of the guide.
   - Populate all required sections: boss mechanics, trial mapping, team tables, detailed team sections, best champions, direct comparisons, ideal pulls, general notes, actionable advice, validation/simulation notes.
5. **Update & Validation**
   - After any roster change, re-run all mapping, team building, and simulation steps.
   - Regenerate all tables and recommendations as needed.
   - Document all validation and simulation steps for transparency.

---

## Required Information & Prompts for Guide Generation

- Full list of owned champions (`Owned_champion_list.md`)
- Authoritative boss mechanics and trial requirements (RaidHQ, Ayumilove, HellHades, in-game)
- Simulation results for each team (at least 3 runs per team)
- Gear, masteries, and stat priorities for each role
- Affinity safety/risk notes for all teams and alternates
- Upgrade path and ideal pulls based on current gaps
- Validation and simulation documentation

---

## Task Checklist for Chimera Boss Guide Generation

- [ ] Gather and summarize all Chimera boss mechanics, forms, turn order, affinities, unique mechanics, trial types, and stat/stat thresholds
- [ ] Map all trials to owned champions (per-trial and combo tables, with affinity safety/risk and special notes)
- [ ] Draft and update a modular, anchor-linked Table of Contents
- [ ] Add quick reference tables for best teams by difficulty/trial/damage tier
- [ ] Build and simulate 5–8 unique teams (trial, damage, hybrid)
- [ ] For each team: document core roles, optimal combo, alternates, speed tuning, gear, masteries, manual/auto, strengths, weaknesses, simulated results, affinity safety/risk, actionable trial advice
- [ ] Run at least 3 simulations per team and document results
- [ ] Summarize best champions & team participation (table)
- [ ] Create direct champion comparisons by role (owned only)
- [ ] List ideal champions to pull and team upgrade paths
- [ ] Add general notes, actionable advice, and common pitfalls
- [ ] Document all validation and simulation steps
- [ ] After any roster change, re-run all mapping, team building, and simulation steps; update all tables and recommendations
- [ ] Never delete files; create new versions for major changes

---

## Additional Questions for User/Reviewer

1. Are there any specific team archetypes or trial types you want prioritized in future updates?
A: not any at this time. but leave this as an open option. 
2. Should the guide include more detailed turn-by-turn skill usage for each team, or is the current actionable advice sufficient?
A: use more detailed skill by skill usage. Include specific skill order from each champion to accomplish trials as required.
3. Would you like to see more auto-friendly team options, or is manual play optimization the main focus?
A. Add auto friendly teams. Show the compromise in damage or trials completed.
4. Are there any additional quick reference tables or summary formats you would find useful?
A: We need to review the teams and note speed tune, if applicable.
5. Should failures and troubleshooting notes be expanded with more detail or examples?
A: yes, include enough information to identify where to restart in generating information about the boss.
6. Is the current update and validation process clear and easy to follow for future roster changes?
A: it looks good for now, yes

---