# RAID Shadow Legends Boss Guides - Copilot Instructions

> This file extends the Generic AI & Copilot Instructions with RAID Shadow Legends boss guide generation standards, champion mapping workflows, and team-building methodologies.

---

## Reference to Generic Standards

See `Generic_AI_Copilot_Instructions.md` for universal AI assistant standards including:
- AI Assistant Behavior
- Safety & File Operations Policy
- Chat Response Standards
- Task Management & Progress Tracking
- Output Formatting & Style Standards
- Change Management & File Versioning
- Code Quality Standards
- Language-Specific Standards
- Project Housekeeping & Shift-Left Workflow
- Validation & Documentation
- Data Privacy & Security

All generic standards apply to this project. The sections below provide RAID Shadow Legends boss guide-specific extensions.

---

## Table of Contents

- [Project Purpose & Scope](#project-purpose--scope)
- [Authoritative Data Sources](#authoritative-data-sources)
- [Boss Guide QA Standards](#boss-guide-qa-standards)
- [Guide Generation Workflow](#guide-generation-workflow)
- [Champion & Trial Mapping](#champion--trial-mapping)
- [Team Building & Simulation](#team-building--simulation)
- [Affinity Safety & Risk Requirements](#affinity-safety--risk-requirements)
- [Guide Structure & Required Sections](#guide-structure--required-sections)
- [Update & Staging Policy](#update--staging-policy)
- [Section-by-Section Maintenance](#section-by-section-maintenance)
- [Validation & Documentation Standards](#validation--documentation-standards)
- [Templates & Examples](#templates--examples)
- [Task Checklist](#task-checklist)

---

## Project Purpose & Scope

### Objectives

This project produces comprehensive, actionable boss/encounter guides for RAID Shadow Legends, tailored to the user's owned champion roster with validated mechanics, team compositions, and strategy recommendations.

### Primary Outputs

**Boss Guide Markdown Files**
- One file per boss (e.g., `Bommal_Boss_Guide.md`, `Hydra_Boss_Guide.md`)
- Modular, human-readable Markdown following standard template
- Includes boss mechanics, trial/mechanic mapping, team recommendations, and upgrade paths
- Optimized for Hard mode by default (expandable to other difficulties)

**Canonical References**
- `Tools/Boss_Guide_Template.md` - Standard template for all guides
- `Input/Owned_champion_list.md` - Single source of truth for champion roster
- RaidHQ, Ayumilove, HellHades - Authoritative external sources

---

## Authoritative Data Sources

### Primary Sources (Always Cross-Validate)

**RaidHQ** (Primary)
- URL: https://raid-hq.com/
- Boss mechanics, trial requirements, stat thresholds
- Priority: Highest for official boss data

**Ayumilove**
- URL: https://ayumilove.net/raid-shadow-legends-guide/
- Champion guides, skill descriptions, gear recommendations
- Priority: High for champion-specific data

**HellHades**
- URL: https://hellhades.com/
- Team compositions, speed tuning, tier lists
- Priority: High for team-building strategies

**In-Game Testing**
- User-provided simulation results
- Direct observation of mechanics
- Priority: Highest for validation

### Source Validation Rules

- Cross-check all boss and champion data with **at least two sources**
- Document conflicts and prefer community consensus (RaidHQ + Ayumilove/HellHades)
- Mark uncertainties in "Data Confidence" or "Validation & Simulation Notes" sections
- Always cite sources in Markdown file and commit messages

---

## Boss Guide QA Standards

### Question & Answer Framework

Before starting guide generation, answer these questions:

**Q: Should the guide fully document all boss mechanics, forms, stat requirements, and trial types before mapping champions?**

**A:** Yes. Begin with a comprehensive, validated section on boss mechanics, forms/phases, turn order, affinities, unique mechanics, and all trial types/stat thresholds. Use RaidHQ (primary), Ayumilove, HellHades, and in-game sources for cross-validation. Document all sources in the Markdown file and commit message.

**Q: How should trials/mechanics be mapped to the owned champion list?**

**A:** For each trial/mechanic, list all owned champions who can fulfill the requirement. Include both a per-trial table and a combo table showing which champions can fulfill multiple trials/mechanics. Note affinity safety/risk (multi-line, explicit), and special skill/turn order notes for each champion. Use only the canonical owned champion list (`Input/Owned_champion_list.md`).

**Q: What is the preferred team-building and simulation approach?**

**A:** Build and simulate 5–8 unique teams using only owned champions, maximizing:
- Total trial/mechanic completion (for score/rewards)
- Raw damage output (for leaderboard/rank)
- Hybrid approaches (balance of both)

For each team, provide: core roles, optimal combo, alternates, speed tuning, gear, masteries, manual/auto, strengths, weaknesses, simulated results, explicit affinity safety/risk (multi-line), and actionable trial/mechanic advice. Run at least 3 simulations per team and document results in the guide.

**Q: How should the Table of Contents and navigation be structured?**

**A:** Use a modular, anchor-linked Table of Contents at the top of the guide. Update section numbers and anchors to match the actual file structure. Add quick reference tables at the start of the guide for best teams by difficulty/trial/damage tier. Ensure all sections match the canonical template (`Tools/Boss_Guide_Template.md`).

**Q: What additional reference and summary sections are required?**

**A:**
- Best Champions & Team Participation: Table of top champions, their roles, and team participation
- Direct Champion Comparisons by Role: Table or summary comparing only owned champions by key roles
- Ideal Champions to Pull: List and rationale for each, with upgrade path advice (only non-owned champions)
- General Notes: Gear, masteries, stat priorities, manual/auto advice
- Actionable Notes & Upgrade Advice: Trial/mechanic prioritization, upgrade path, common pitfalls
- Validation & Simulation Notes: Document all validation sources, simulation steps, and results (minimum 3 runs per team)

**Q: How should the guide be updated after a roster change?**

**A:**
- Supply a new `Owned_champion_list.md` or add a new champion
- Re-run the team and trial/mechanic mapping process to update all tables and recommendations
- Regenerate the Ideal Champions to Pull and Team Upgrade Paths sections to reflect new gaps
- Never overwrite the original file directly; always preserve previous versions and stage changes for review

**Q: What is the process for handling alternates, trial-specific champions, and affinity risk?**

**A:**
- For each team, list alternates for each core role based on the owned champion list
- Include trial/mechanic-specific alternates (champions used only for a specific trial/mechanic)
- Explicitly document affinity safety/risk for each team and alternate in all relevant sections (multi-line, per template)

**Q: How should failures and troubleshooting be documented?**

**A:**
- Document teams that almost work but miss a trial/mechanic or damage threshold
- Include notes on why a team failed and what upgrades or changes would resolve the issue
- Add troubleshooting and upgrade path advice in the actionable notes section

**Q: What is the preferred output format and update policy?**

**A:**
- All outputs must be modular, human-readable Markdown, following the standard template
- Never delete files or folders; create new versions for major changes (e.g., `_v2.md` or date-stamped)
- Document all validation and simulation steps in the Markdown file or commit message for transparency and reproducibility

---

## Guide Generation Workflow

### Canonical Workflow Steps (Shift-Left Applied)

**Step 1: Research & Data Gathering**
- Review authoritative boss guides (RaidHQ, Ayumilove, HellHades, in-game)
- Document all boss forms/phases, turn order, affinities, unique mechanics, and trial types/stat thresholds
- Cross-validate and cite sources
- Output: Boss Mechanics section with validation notes

**Step 2: Champion & Trial/Mechanic Mapping**
- Cross-reference the canonical owned champion list with trial/mechanic requirements
- Build per-trial and combo tables, noting affinity safety/risk (multi-line, explicit) and special notes
- Output: Trial/mechanic mapping tables

**Step 3: Team Building & Simulation**
- Build 5–8 unique teams using only owned champions, maximizing trial/mechanic completion, damage, and hybrid approaches
- For each team, specify all required details (roles, alternates, speed, gear, masteries, manual/auto, strengths, weaknesses, simulated results, affinity safety/risk, actionable advice)
- Run at least 3 simulations per team and document results in the guide
- Output: Team recommendation sections with detailed specs

**Step 4: Guide Structure & Output**
- Use a modular, anchor-linked Table of Contents
- Add quick reference tables at the start of the guide
- Populate all required sections: boss mechanics, trial/mechanic mapping, team tables, detailed team sections, best champions, direct comparisons, ideal pulls, general notes, actionable advice, validation/simulation notes
- Use the canonical template (`Tools/Boss_Guide_Template.md`) for all guides
- Output: Complete draft guide

**Step 5: Update & Validation**
- After any roster change, re-run all mapping, team building, and simulation steps
- Regenerate all tables and recommendations as needed
- Document all validation and simulation steps for transparency
- Never overwrite the original file directly; always preserve previous versions and stage changes for review
- Output: Finalized guide ready for user review

---

## Champion & Trial Mapping

### Per-Trial Mapping

For each boss trial or mechanic requirement, create a table listing all owned champions who can fulfill that requirement.

**Table Format:**
| Champion | Affinity | Role/Skill | Notes |
|----------|----------|------------|-------|
| Champion A | Magic | Debuff: Decrease DEF | A3 skill, 3-turn CD, 75% chance |
| Champion B | Spirit | Debuff: Decrease DEF | A2 skill, 4-turn CD, 100% with books |

**Per-Trial Requirements:**
- List only owned champions (reference `Input/Owned_champion_list.md`)
- Note affinity for each champion
- Specify which skill/ability fulfills the requirement
- Include cooldowns, chance rates, duration
- Note gear/mastery dependencies
- Flag affinity risks (weak hits, unreliable debuffs)

### Combo Tables

Create tables showing which champions can fulfill **multiple trials/mechanics** simultaneously.

**Combo Table Format:**
| Champion | Trial 1 | Trial 2 | Trial 3 | Affinity Safety |
|----------|---------|---------|---------|-----------------|
| Champion A | ✅ Dec DEF | ✅ HP Burn | ❌ | Safe (Magic) |
| Champion B | ✅ Dec DEF | ❌ | ✅ Ally Protect | Risky (Weak to Force) |

**Combo Table Benefits:**
- Identify high-value champions (fulfill 3+ trials)
- Optimize team slots (fewer champions needed)
- Spot gaps (trials with few or no champions)
- Prioritize upgrades (high-value champions first)

### Affinity Safety Notes

For each champion in mapping tables, note:
- **Safe affinities**: Champion affinity is strong or neutral vs boss
- **Risky affinities**: Champion is weak affinity (will miss debuffs/attacks more often)
- **Critical roles**: If a champion is weak affinity but fills a critical role, note the risk and suggest backup

**Example:**
- Champion A (Spirit): **Risky** - Weak vs Magic boss, may miss Decrease DEF debuff. Consider Champion C (Force) as backup.

---

## Team Building & Simulation

### Team Specifications

For each recommended team, provide the following details:

**Core Roles:**
- Tank/Damage Dealer/Support/Debuffer/Healer
- Specify which champion fills which role

**Optimal Combo:**
- List the ideal 5-champion lineup
- Note synergies (e.g., Champion A's buff enables Champion B's nuke)

**Alternates:**
- For each core role, list 1-3 alternate champions from owned roster
- Note when alternates are trial-specific (used only for specific mechanics)

**Speed Tuning:**
- Specify turn order (e.g., Debuffer → Buffer → Nuker → Cleanser → Healer)
- Note speed requirements (e.g., Debuffer needs 220+ speed to go first)
- Flag if speed tuning is flexible or strict

**Gear:**
- List gear sets for each role (e.g., Speed + Accuracy for debuffer)
- Note stat priorities (e.g., Debuffer: 250+ ACC, 220+ SPD, 35k+ HP)

**Masteries:**
- Note key masteries (e.g., Warmaster for damage dealers, Support tree for healers)
- Flag if specific masteries are required for trial completion

**Manual/Auto:**
- Specify if team works on auto or requires manual play
- Note which skills to prioritize in manual mode

**Strengths:**
- List trials/mechanics the team excels at
- Note expected damage tier or clear time

**Weaknesses:**
- List trials/mechanics the team struggles with or cannot complete
- Note affinity risks or gear/skill dependencies

**Simulated Results:**
- Document clear times, damage scores, trial completion
- Note success rate (e.g., 8/10 runs, 2 fails due to RNG)

**Affinity Safety/Risk (Multi-Line):**
```
Affinity Safety/Risk:
- Champion A (Magic): Safe vs Spirit boss
- Champion B (Force): Risky vs Magic boss, may miss debuffs
- Champion C (Void): Safe (neutral vs all affinities)
```

**Actionable Trial/Mechanic Advice:**
- Step-by-step skill usage for trial completion
- Example: "Turn 1: Champion A applies Decrease DEF. Turn 2: Champion B applies HP Burn. Turn 3: All champions attack to complete HP Burn trial."

### Simulation Requirements

**Minimum Simulations per Team:**
- Run at least **3 test runs** per team
- Document results for each run (clear time, damage, trials completed)

**What to Document:**
- Average clear time (or fastest, if times vary significantly)
- Average damage score
- Success rate (e.g., 10/10 runs, 7/10 runs)
- Trial completion consistency (which trials were completed in all runs vs some runs)
- Affinity risk observations (e.g., weak hit rate, debuff failure rate)

**Data Sources for Validation:**
- In-game testing (highest priority)
- Community calculators (HellHades optimizer, Deadwood Jedi speed calculator)
- Team composition guides (RaidHQ, Ayumilove, HellHades)

---

## Affinity Safety & Risk Requirements

### Documentation Requirements

**Every boss/team Markdown file must include:**

1. **Boss Mechanics & Stat Requirements Section:**
   - Explicit affinity information for the boss (e.g., "Boss is Magic affinity, weak to Force champions")
   - Note any affinity-based mechanics (e.g., "Boss gains extra turn when hit by weak affinity")

2. **Team Summary Table:**
   - Add explicit, multi-line "Affinity Safety/Risk" column for each team

3. **Detailed Team Sections:**
   - For each team, include a multi-line "Affinity Safety/Risk" note
   - Specify which affinities are safe, which are risky, and why
   - Example format:
   ```markdown
   **Affinity Safety/Risk:**
   - Champion A (Magic): Safe vs Spirit boss, strong affinity
   - Champion B (Force): Risky vs Magic boss, may miss Decrease DEF debuff (60% weak hit rate observed)
   - Champion C (Void): Safe, neutral affinity
   - Overall: Low risk, only 1 champion has weak affinity and is not in critical role
   ```

### Weak Affinity Guidance

**When to Avoid Weak Affinity Champions:**
- **Critical debuffer roles**: If a champion must land a debuff to complete a trial, avoid weak affinity
- **Low success rate**: If weak affinity causes >30% failure rate, note as high risk

**When Weak Affinity May Be Acceptable:**
- **Non-critical roles**: Tank or support roles where weak hits are less impactful
- **High base accuracy**: Champion has 400+ accuracy and can partially offset weak hit penalty
- **No better alternative**: If no neutral/strong affinity champion exists for the role, use weak affinity with explicit warning

**Always Document:**
- Why a weak affinity champion is recommended (if applicable)
- What the risk is (e.g., "May fail to land Decrease DEF 30% of the time")
- What the backup plan is (e.g., "If debuff fails, restart run or use Champion D as alternate")

---

## Guide Structure & Required Sections

### Table of Contents

**Requirements:**
- Modular, anchor-linked Table of Contents at top of guide
- Section numbers and anchors must match actual file structure
- Update ToC whenever sections are added or reordered

**Standard ToC Structure:**
```markdown
## Table of Contents

1. [Boss Mechanics & Stat Requirements](#boss-mechanics--stat-requirements)
2. [Trial/Mechanic Mapping](#trialmechanic-mapping)
3. [Quick Reference: Best Teams by Difficulty/Trial/Damage Tier](#quick-reference-best-teams)
4. [Detailed Team Recommendations](#detailed-team-recommendations)
   - [Team 1: High Damage, Manual](#team-1-high-damage-manual)
   - [Team 2: Auto-Friendly, Trial Focused](#team-2-auto-friendly-trial-focused)
5. [Best Champions & Team Participation](#best-champions--team-participation)
6. [Direct Champion Comparisons by Role](#direct-champion-comparisons-by-role)
7. [Ideal Champions to Pull](#ideal-champions-to-pull)
8. [General Notes](#general-notes)
9. [Actionable Notes & Upgrade Advice](#actionable-notes--upgrade-advice)
10. [Validation & Simulation Notes](#validation--simulation-notes)
```

### Boss Mechanics Section

**Required Content:**
- Boss forms/phases (e.g., Phase 1: Shield phase, Phase 2: Damage phase)
- Turn order and boss actions per turn
- Boss affinity and affinity-based mechanics
- Unique mechanics (e.g., shields, counterattacks, stuns, debuff limits)
- Trial types and stat/ability thresholds (e.g., "Complete 10 HP Burns", "Apply Decrease DEF 15 times")
- Manual/Auto Play Notes subsection

**Validation:**
- Cross-validate with at least 2 sources (RaidHQ, Ayumilove, HellHades)
- Document sources in this section or in Validation & Simulation Notes

### Trial/Mechanic Mapping Section

**Required Content:**
- Per-trial tables (see Champion & Trial Mapping section above)
- Combo tables showing multi-trial champions
- Affinity safety notes for each champion

### Team Recommendation Sections

**Quick Reference Table:**
```markdown
| Team Name | Difficulty | Damage Tier | Trials Completed | Manual/Auto | Affinity Safety/Risk |
|-----------|------------|-------------|------------------|-------------|----------------------|
| Team 1    | Hard       | High (15M+) | 8/10             | Manual      | Low risk (1 weak)    |
| Team 2    | Hard       | Medium (10M)| 10/10            | Auto        | Safe (all neutral)   |
```

**Detailed Team Sections:**
For each team, include all specifications from "Team Building & Simulation" section above.

**Uniqueness Requirement:**
- All teams must use unique, owned champions (no champion appears in multiple teams)
- If multiple teams would use the same champion list, suggest variations based on:
  - Boss mechanics (e.g., Team A for Phase 1, Team B for Phase 2)
  - Use case (e.g., Team A for manual high damage, Team B for auto trial completion)
  - Affinity risk (e.g., Team A for safe affinity, Team B with risky affinity if needed)
  - Clear speed (e.g., Team A for fast clear, Team B for consistent clear)

### Reference Sections

**Best Champions & Team Participation:**
- Table of top champions, their roles, and which teams they appear in
- Sort by participation (champions in multiple teams) or role importance

**Direct Champion Comparisons by Role:**
- Table comparing only owned champions by key roles (e.g., all owned debuffers, all owned damage dealers)
- Include a note: "This section compares only owned champions."

**Ideal Champions to Pull:**
- List champions **not on the owned list** that would improve team performance
- Provide rationale (e.g., "Champion X would enable Trial Y completion")
- Provide upgrade path advice (e.g., "Pull Champion X first, then Champion Y")
- **Important:** Only include non-owned champions in this section

**General Notes:**
- Gear priorities (e.g., "Accuracy > Speed > HP for debuffers")
- Masteries priorities (e.g., "Warmaster for all damage dealers")
- Stat priorities by role
- Manual/auto play general advice

**Actionable Notes & Upgrade Advice:**
- Trial/mechanic prioritization (which trials to focus on first)
- Upgrade path (which champions to upgrade first, which gear to farm)
- Common pitfalls (e.g., "Don't use Spirit champions on Magic boss")

**Validation & Simulation Notes:**
- Number of simulations/test runs performed (minimum 3 per team)
- How clear times and success rates were determined (average, fastest, manual/auto)
- Affinity safety/risk notes based on observed weak hit rates and debuff reliability
- Data sources used for validation (e.g., HellHades, Ayumilove, in-game testing)

---

## Update & Staging Policy

### When Owned Champion List Changes

**Process:**
1. Supply a new `Owned_champion_list.md` or note the added/removed champion
2. Re-run the team and trial/mechanic mapping process to update all tables and recommendations
3. Regenerate the "Ideal Champions to Pull" and "Team Upgrade Paths" sections to reflect new gaps
4. **Never overwrite the original file directly**; always preserve previous versions and stage changes for review

**File Versioning:**
- Create new file with version suffix (e.g., `Bommal_Boss_Guide_v2.md`) or date stamp (e.g., `Bommal_Boss_Guide_2025-10-17.md`)
- Preserve original file for comparison
- After user review, original may be archived or replaced

**Update Scope:**
- All trial/mechanic mapping tables
- All team recommendations (may need to rebuild teams if key champions are added/removed)
- Best Champions & Team Participation table
- Direct Champion Comparisons by Role
- Ideal Champions to Pull (remove now-owned, reprioritize)
- Validation & Simulation Notes (note when file was updated and why)

---

## Section-by-Section Maintenance

### Maintenance Workflow

For each section in the Table of Contents, follow this process:

**1. Review and Update Table of Contents**
- Ensure ToC matches actual sections in the file
- Update section numbers and anchors if structure changed

**2. Boss Mechanics & Stat Requirements**
- Re-validate mechanics, stat thresholds, affinity notes
- Ensure "Manual/Auto Play Notes" subsection is present
- Cross-check with at least 2 sources (RaidHQ, Ayumilove, HellHades)

**3. Teams by Estimated Damage/Clear Speed**
- Update table with any new teams or removed teams
- Add explicit, multi-line affinity column if missing
- Verify all teams use only unique, owned champions
- If multiple teams use the same champion list, suggest variations based on boss mechanics or use case (manual vs auto, affinity risk, clear speed, etc.)

**4. Detailed Team Sections**
- Add/refresh explicit, multi-line affinity notes for each team
- Ensure all required subfields are present (roles, alternates, speed, gear, masteries, manual/auto, strengths, weaknesses, simulated results, affinity safety/risk, actionable advice)
- If two teams use the same champion list, suggest variations based on boss mechanics, affinity, or playstyle

**5. Best Champions & Team Participation**
- Update for new teams/champions
- Re-sort by participation or role importance

**6. Direct Champion Comparisons by Role**
- Update for new roster
- Only list owned champions in this section
- Include a note clarifying this (e.g., "This section compares only owned champions.")

**7. Ideal Champions to Pull**
- Remove now-owned champions
- Reprioritize based on new gaps
- Only include champions not on the owned list

**8. General Notes**
- Add or update actionable advice on gear, masteries, stat priorities, manual/auto play
- Ensure advice is current with latest champion roster

**9. Validation & Simulation Notes**
- Document all validation and simulation steps
- Include:
  - Number of test runs (minimum 3 per team recommended)
  - Clear time methodology (average, fastest, manual/auto)
  - Affinity risk observations (weak hit rates, debuff reliability)
  - Data sources (HellHades, Ayumilove, in-game testing)

---

## Validation & Documentation Standards

### Source Cross-Validation

**All champion and boss data must be cross-checked with at least two sources:**
- RaidHQ (primary for boss mechanics)
- Ayumilove (champion skills, gear recommendations)
- HellHades (team compositions, tier lists)
- In-game testing (highest priority for validation)

**Document Conflicts:**
- If sources disagree, note the conflict in "Validation & Simulation Notes"
- Prefer community consensus (RaidHQ + Ayumilove/HellHades agree)
- If no consensus, note as "Uncertain" or "Data Confidence: Medium/Low"

### Simulation Documentation

**Every boss/team Markdown file must include a "Validation & Simulation Notes" section at the end, stating:**
- **Number of simulations/test runs performed** (minimum 3 per team recommended)
- **How clear times and success rates were determined** (average, fastest, manual/auto, etc.)
- **Affinity safety/risk notes** based on observed weak hit rates and debuff reliability
- **Data sources used for validation** (e.g., HellHades, Ayumilove, in-game testing)

**Alternative:** If not using a dedicated section, include explicit documentation of simulation/validation steps for each team in the team's detailed section.

### Transparency & Reproducibility

- Document all validation and simulation steps in the Markdown file or commit message
- Enable users to reproduce results or validate recommendations
- Note assumptions (e.g., "Assumes all champions are level 60, fully ascended, with Warmaster/Helmsmasher")

---

## Templates & Examples

### Boss Guide Template

**Canonical Template:**
- `Tools/Boss_Guide_Template.md` is the standard template for all guides
- All boss guides must match template structure and required sections
- Use template as starting point for new boss guides

### Team Table Format

**Quick Reference Table:**
```markdown
| Team Name | Difficulty | Damage Tier | Trials Completed | Manual/Auto | Affinity Safety/Risk |
|-----------|------------|-------------|------------------|-------------|----------------------|
| Example   | Hard       | High (15M+) | 8/10             | Manual      | Low risk (1 weak)    |
```

### Trial Mapping Table Format

**Per-Trial Table:**
```markdown
| Champion | Affinity | Role/Skill | Notes |
|----------|----------|------------|-------|
| Example  | Magic    | Debuff     | A3 skill, 3-turn CD |
```

**Combo Table:**
```markdown
| Champion | Trial 1 | Trial 2 | Trial 3 | Affinity Safety |
|----------|---------|---------|---------|-----------------|
| Example  | ✅      | ✅      | ❌      | Safe (Magic)    |
```

### Affinity Safety/Risk Note Format

**Multi-Line Format (Preferred):**
```markdown
**Affinity Safety/Risk:**
- Champion A (Magic): Safe vs Spirit boss, strong affinity
- Champion B (Force): Risky vs Magic boss, may miss debuffs (60% weak hit rate)
- Champion C (Void): Safe, neutral affinity
- Overall: Low risk, only 1 champion has weak affinity in non-critical role
```

---

## Task Checklist

**For Each Boss Guide, Complete the Following:**

- [ ] **Gather and summarize all boss mechanics**, forms/phases, turn order, affinities, unique mechanics, trial types, and stat thresholds (validated, sources cited)
- [ ] **Map all trials/mechanics to owned champions** (per-trial and combo tables, with affinity safety/risk and special notes)
- [ ] **Draft and update a modular, anchor-linked Table of Contents** (per template)
- [ ] **Add quick reference tables** for best teams by difficulty/trial/damage tier
- [ ] **Build and simulate 5–8 unique teams** (trial-focused, damage-focused, hybrid)
- [ ] **For each team, document:** core roles, optimal combo, alternates, speed tuning, gear, masteries, manual/auto, strengths, weaknesses, simulated results, affinity safety/risk, actionable trial/mechanic advice
- [ ] **Run at least 3 simulations per team** and document results
- [ ] **Summarize best champions & team participation** (table)
- [ ] **Create direct champion comparisons by role** (owned only)
- [ ] **List ideal champions to pull** and team upgrade paths (non-owned only)
- [ ] **Add general notes**, actionable advice, and common pitfalls
- [ ] **Document all validation and simulation steps** (sources, methodology, results)
- [ ] **After any roster change**, re-run all mapping, team building, and simulation steps; update all tables and recommendations
- [ ] **Never delete files or folders**; create new versions for major changes

---

## Additional Questions for User/Reviewer

These questions were answered by the user and should guide all boss guide generation:

**1. Are there any specific team archetypes or trial/mechanic types you want prioritized in future updates?**
- **Answer:** Not any at this time. But leave this as an open option.

**2. Should the guide include more detailed turn-by-turn skill usage for each team, or is the current actionable advice sufficient?**
- **Answer:** Use more detailed skill by skill usage. Include specific skill order from each champion to accomplish trials/mechanics as required.

**3. Would you like to see more auto-friendly team options, or is manual play optimization the main focus?**
- **Answer:** Add auto friendly teams. Show the compromise in damage or trials/mechanics completed.

**4. Are there any additional quick reference tables or summary formats you would find useful?**
- **Answer:** We need to review the teams and note speed tune, if applicable.

**5. Should failures and troubleshooting notes be expanded with more detail or examples?**
- **Answer:** Yes, include enough information to identify where to restart in generating information about the boss.

**6. Is the current update and validation process clear and easy to follow for future roster changes?**
- **Answer:** It looks good for now, yes.

---

## Changelog

- **2025-10-17:** Completed all sections with full content from original RAID_copilot-instructions.md, expanding Champion & Trial Mapping, Team Building & Simulation, Affinity Safety & Risk Requirements, Guide Structure & Required Sections, Update & Staging Policy, Section-by-Section Maintenance, Validation & Documentation Standards, Templates & Examples, Task Checklist, and Additional Questions for User/Reviewer
- **2025-10-16:** Initial creation incorporating Generic AI & Copilot Instructions standards and project-specific boss guide generation workflows, QA standards, and team-building methodologies
