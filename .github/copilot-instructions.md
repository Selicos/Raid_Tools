# RAID Shadow Legends Boss Guides - Copilot Instructions

> This file extends the Generic AI & Copilot Instructions with RAID Shadow Legends boss guide generation standards, champion mapping workflows, and team-building methodologies.

---

## Table of Contents

- [Project Purpose & Scope](#project-purpose--scope)
- [User Content Priorities & Focus](#user-content-priorities--focus)
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
- [Champion Review Workflow](#champion-review-workflow)
  - [Champion Review Template Standards](#champion-review-template-standards)
  - [Rating System (X/10 Contextualized)](#rating-system-x10-contextualized)
  - [Gear Recommendations (Option C)](#gear-recommendations-option-c)
  - [Faction Wars Advice](#faction-wars-advice)
  - [Current Build Input Section](#current-build-input-section)
  - [Cheese Strategy Integration](#cheese-strategy-integration)
  - [Single-Champion Addition Workflow](#single-champion-addition-workflow)
- [Arena Guide Standards](#arena-guide-standards)
  - [Tier-Specific Recommendations](#tier-specific-recommendations)
  - [Defensive Team Variations](#defensive-team-variations)
  - [Live Arena Coverage](#live-arena-coverage)
  - [Tag Team Standards](#tag-team-standards)
- [DRAFT-to-FINAL Workflow](#draft-to-final-workflow)
- [Roster Update Workflow & Automation](#roster-update-workflow--automation)
  - [Directory Structure Standards](#directory-structure-standards)
  - [Owned Champion List Standards](#owned-champion-list-standards)
  - ["Cheese" Mechanics & Duplicate Champions](#cheese-mechanics--duplicate-champions)
  - [Guide Update Workflow (Roster Changes)](#guide-update-workflow-roster-changes)
  - [Validation Scripts & Tools](#validation-scripts--tools)
  - [Community & Multi-User Support](#community--multi-user-support)

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

## User Content Priorities & Focus

### Content Priority Order (Always Follow)

**Priority 1: Clan Boss UNM**
- Highest priority for all champion ratings, team recommendations, and guide updates
- User has UNM-capable clan (daily rewards secured)
- Focus on damage optimization, unkillable teams, and cheese strategies

**Priority 2: Dungeons (All Stages 25)**
- Dragon, Spider, Fire Knight, Ice Golem
- User preference: HP Burn teams (well-built), Poison teams (NOT well-built)
- Spider team confirmed strong

**Priority 3: Advanced PVE Content**
- Doom Tower Hard (boss-specific strategies)
- Cursed City and other advanced PVE encounters
- Iron Twins Fortress, Chimera, Hydra

**Priority 4: Arena**
- Classic Arena (Gold 3+)
- Tag Team Arena (Bronze 3+, lower priority than Classic)
- Live Arena (basic coverage, user still developing strategy)

**Priority 5: Faction Wars**
- **Completed Normal:** Orc, Banner Lords, Barbarian, Dwarf
- **Near Completion:** Lizardmen, Knights Revenant, High Elf, Dark Elf
- Priority: Complete remaining Normal stages, then progress to Hard

### Champion Use Case Documentation

**When documenting champions, always highlight:**
- Specific boss/dungeon applications
- Unique mechanics or cheese strategies
- Wave clear capabilities (general or content-specific)
- Role in Faction Wars (for user's in-progress factions)

### User Team Composition Preferences

**Core Arena Team (Classic):**
- **Wukong** (speed lead, buff strip, nuke, sheep control)
- **Mythrala** (buffs/cleanse, hex damage)
- **Loki** (control, buff strip, suppress mythics/active skills)
- **Flex spot:** Ninja, Michelangelo, Coldheart, Godseeker Aniri, Arbiter, Rector Drath

**Team Building Preferences:**
- HP Burn teams: Well-built and preferred
- Poison teams: Not well-built (Frozen Banshee, Elenaril, Narma weak)
- Speed tuning: Often loses speed battle in higher Arena tiers
- Cheese strategies: Prioritize SAFE cheese builds for bosses and Clan Boss

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

### Large File Operations & Batching Requirements

**When to Use Batched Processing:**

Large file operations (500+ lines, multiple sections, or complex merges) **must** be batched to prevent:
- Prompt length issues (token limit exceeded)
- Runtime/memory issues
- Difficulty in reviewing changes
- Loss of context during long operations

**Batching Strategy:**

1. **Plan the Work:**
   - Break file operations into logical sections (50-200 lines per batch)
   - Create numbered batch tasks (BATCH 1, BATCH 2, etc.)
   - Summarize batch plan in markdown for user review before starting

2. **Batch Size Guidelines:**
   - **BATCH 1:** Header/Title + Enhancement History (~50-200 lines)
   - **BATCH 2:** Table of Contents (~20-50 lines)
   - **BATCH 3:** Boss Mechanics & Trial Mapping (~200-300 lines)
   - **BATCH 4:** Team Sections 1-3 (~200-300 lines)
   - **BATCH 5:** Team Sections 4-6 (~200-300 lines)
   - **BATCH 6:** Reference Sections (~100-200 lines)
   - **BATCH 7:** Validation & Final Review
   - **BATCH 8:** Cleanup & Git Commit

3. **Batch Execution:**
   - Complete one batch at a time
   - Confirm completion with ✅ status update in chat
   - Update todo list after each batch
   - Provide brief summary (lines added, current file size)
   - Ask for user confirmation before proceeding to next batch (or proceed automatically if instructed)

4. **Batch Documentation:**
   - Create todo list items for each batch
   - Mark completed batches with ✅
   - Document what was done in each batch
   - Note any issues or deviations from plan

**Example Batch Plan:**

```markdown
## Merge Strategy Summary

### Source Files Analysis:
- File A (500 lines): Complete content
- File B (200 lines): Enhancement history
- File C (150 lines): Additional metadata

### Batching Approach:

**BATCH 1: Header + Enhancement History** ✅ Starting Now
- Create new file header
- Merge enhancement overview from Files B & C
- ~100 lines

**BATCH 2: Table of Contents**
- Copy ToC from File A
- Update section numbers
- ~30 lines

**BATCH 3-5: Main Content**
- Copy sections 1-N from File A
- Split across 3 batches if needed
- ~400 lines total

**BATCH 6: Finalize**
- Validate formatting
- Cleanup old files
```

**Critical Rules:**
- Never attempt to create/edit files >400 lines in a single operation
- Always batch when merging multiple files
- Always batch when file will exceed 500 lines
- Always provide batch summary before starting work
- Always update todo list after each batch completion

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

## Champion Review Workflow

### Champion Review Template Standards

**Purpose:** Create comprehensive, actionable individual champion reviews tailored to user's owned roster and content priorities.

**Template Location:** `input/Champion_Review_Template.md`

**Review Output Location:** `Notes/Champion Reviews/[Champion_Name]_Review.md`

**Required Sections:**
1. **Champion Overview**
   - Name, Rarity, Affinity, Faction
   - Role classification (HP Burn, Decrease DEF, Support, Damage Dealer, Tank, TM Control, Revive, Cleanse)
   - Brief summary of champion's primary use cases

2. **Content-Specific Ratings (X/10 Contextualized)**
   - See Rating System section below

3. **Skills & Mechanics**
   - Detailed skill descriptions with cooldowns, multipliers, effects
   - Unique mechanics or passive abilities
   - Skill booking priority and partial investment guidance

4. **Gear Recommendations (Option C)**
   - See Gear Recommendations section below

5. **Masteries**
   - Content-specific mastery recommendations (Clan Boss, Dungeons, Arena, etc.)
   - Key masteries to prioritize (Warmaster, Giant Slayer, etc.)

6. **Faction Wars Advice**
   - See Faction Wars Advice section below

7. **Team Synergies & Pairings**
   - Best champions to pair with (from owned roster)
   - Cheese strategy potential (if applicable)
   - Similar champions with comparable utility

8. **Investment Recommendations**
   - Priority level (CRITICAL, HIGH, MEDIUM, LOW)
   - PVE disclaimer: "This champion requires booking/building for optimal performance in [content]"
   - When to stop investment (e.g., "Book A2 only", "6-star not required for Faction Wars")

9. **Current Build Input Section**
   - See Current Build Input Section below

10. **Cheese Strategy Integration**
    - See Cheese Strategy Integration section below

11. **Validation & Sources**
    - Cross-validation with RaidHQ, Ayumilove, HellHades
    - Community consensus notes
    - In-game testing results (if applicable)

---

### Rating System (X/10 Contextualized)

**Rating Scale:** X/10 for each content area, **contextualized to owned champions**

**Content Areas (Prioritized Order):**
1. **Clan Boss UNM** (Priority 1)
2. **Dungeons** (Priority 2): Dragon, Spider, Fire Knight, Ice Golem
3. **Doom Tower Hard** (Priority 3)
4. **Advanced PVE** (Priority 3): Cursed City, Iron Twins, Chimera, Hydra
5. **Arena** (Priority 4): Classic (Gold 3+), Tag Team, Live Arena
6. **Faction Wars** (Priority 5): Normal (in-progress factions priority), Hard

**Rating Context Rules:**

**10/10 Rating:**
- Champion is best-in-class for this content among **OWNED champions** (validate before rating)
- Example: "Artak: 10/10 Clan Boss - Best HP Burn champion in your roster (validated: Artak, Ninja, Geomancer, Akoth, Drexthar owned)"
- Note if champion is unsupported: "10/10 with no support champions available (rating reflects potential)"
- **MUST validate:** Fetch skills for all owned champions in same role to confirm "best-in-class" claim

**8-9/10 Rating:**
- Champion is excellent but outclassed by 1-2 **OWNED champions** (validate before rating)
- Example: "Ninja: 9/10 Clan Boss - Excellent HP Burn, slightly behind Artak (A3 vs A2 HP Burn, validated)"

**6-7/10 Rating:**
- Champion is good, usable, but multiple better **OWNED options** exist (validate before rating)
- Example: "Akoth the Seared: 7/10 Dragon - Solid HP Burn, but Artak and Ninja have better uptime (validated)"

**4-5/10 Rating:**
- Champion is mediocre or niche for this content
- Example: "Relickeeper: 5/10 Clan Boss - Low damage, better options available"

**1-3/10 Rating:**
- Champion is poor or unusable for this content
- Example: "Paragon: 2/10 Clan Boss - Single-target unkillable cheese only, not viable for damage teams"

**Rating Documentation Requirements:**
- **CRITICAL:** ALWAYS validate champion skills by fetching Ayumilove/HellHades data before making comparisons
- **CRITICAL:** ONLY compare to OWNED champions (validate against `input/Owned_champion_list.md`)
- Build role-specific lists (HP Burn, Freeze, Decrease DEF, etc.) by validating ALL owned champions with that mechanic
- Compare to top 3 owned champions in same role/content
- Always note if champion is unsupported (e.g., "10/10 Decrease DEF but no Ally Attack champions to pair")
- Note affinity risks (e.g., "9/10 Dragon but weak affinity vs Magic boss")
- Document validation sources (Ayumilove + HellHades) in review

---

### Gear Recommendations (Option C)

**Format:** General sets + detailed artifact recommendations

**General Sets (Always Include):**
- Primary sets (e.g., "Speed + Accuracy", "Lifesteal + Speed", "Relentless + Immortal")
- Alternative sets (e.g., "Toxic for extra poison damage", "Stalwart for AoE reduction")

**Detailed Artifacts (Always Include):**
- **Banner:** Accuracy, HP, DEF, or Resist
- **Chest:** HP%, DEF%, or ATK%
- **Boots:** Speed (almost always), HP%, or DEF%
- **Gloves:** Crit Rate, Crit Damage, HP%, DEF%, or ATK%
- **Weapon/Helmet/Shield:** Prioritize stats (e.g., "Speed, Accuracy, HP, DEF")

**Stat Priorities (Always Include):**
- Example: "250+ ACC, 220+ SPD, 35k+ HP, 2.5k+ DEF for Clan Boss UNM"
- Content-specific stat targets (e.g., "180 ACC for Dragon 25, 220 ACC for Doom Tower Hard")

**Conciseness for Low-Use Champions:**
- For champions with limited use cases, keep gear section short
- Example: "Low priority. If building: Speed + Accuracy, 200+ ACC, 180+ SPD for Faction Wars support."

---

### Faction Wars Advice

**Format:** Current owned champions + ideal 5-champion pull list for that faction

**Owned Champions in Faction:**
- List all owned champions in the same faction
- Note their roles (e.g., "Vogoth: Tank/Sustain", "Frozen Banshee: Poisoner")
- Recommend faction-specific team compositions

**Faction Wars Team Recommendations:**
- Suggest 1-2 teams using owned champions for Faction Wars Normal/Hard
- Note which stages are achievable with current roster
- Highlight gaps (e.g., "No revive champion, Faction Wars 21 will be difficult")

**Ideal 5-Champion Pull List (Non-Owned Only):**
- List top 5 non-owned champions for this faction
- Rationale for each (e.g., "Duchess Lilitu: Game-changing revive + sustain for Faction Wars Hard")
- Prioritize by impact (CRITICAL > HIGH > MEDIUM)

**Faction Wars Priority by User Progress:**
- **Completed Normal:** Orc, Banner Lords, Barbarian, Dwarf - Low priority, focus on Hard stages
- **Near Completion:** Lizardmen, Knights Revenant, High Elf, Dark Elf - HIGH priority, complete Normal first
- **Not Started:** Remaining factions - MEDIUM priority, defer until core content complete

---

### Current Build Input Section

**Purpose:** Allow user to input current champion build for personalized optimization advice

**Input Fields:**
1. **Current Level:** 1-60
2. **Current Ascension:** 0-6 stars
3. **Skills Booked:** None, Partial (specify which skills), Full
4. **Current Gear Sets:** (e.g., "Speed + Accuracy")
5. **Current Stats:**
   - HP: [value]
   - ATK: [value]
   - DEF: [value]
   - SPD: [value]
   - Crit Rate: [value]
   - Crit Damage: [value]
   - Accuracy: [value]
   - Resist: [value]
6. **Current Masteries:** Full, Partial (T1-T6 breakdown), None
7. **Current Primary Use:** (e.g., "Clan Boss UNM", "Dragon 25", "Arena Gold 4")

**Optimization Output:**
- Compare current build to recommended build (from Gear Recommendations section)
- Identify gaps (e.g., "Current ACC: 180, Recommended: 250+ for Clan Boss UNM")
- Prioritize upgrades (e.g., "Priority 1: Increase ACC to 250+, Priority 2: Increase SPD to 220+")
- Suggest respeccing if champion is built for wrong content (e.g., "Currently built for Arena, but highest value is Clan Boss - consider respec")
- Note if current build is optimal (e.g., "Current build is optimal for Dragon 25, no changes needed")

---

### Cheese Strategy Integration

**Purpose:** Highlight SAFE cheese builds for bosses and Clan Boss, prioritize cheese when strictly better

**When to Include Cheese Strategy:**
- Champion enables or participates in cheese strategies (e.g., Triple Coldheart, Triple Pain Keeper, Double Nogdar)
- Cheese strategy is strictly better in speed/damage/availability than conventional teams
- Cheese strategy is SAFE (consistent, reliable, not RNG-dependent)

**Cheese Strategy Documentation:**
1. **Cheese Type:** (e.g., "MAX HP Damage Cheese", "Unkillable Cheese", "Ally Attack Spam Cheese")
2. **Required Champions:** List all champions needed (note if duplicates required)
3. **Cheese Viability:** CRITICAL (best option), HIGH (strong option), MEDIUM (niche option)
4. **Safety Level:** SAFE (consistent, reliable), RISKY (RNG-dependent), UNSAFE (rarely works)
5. **Content Applications:** Which bosses/content this cheese works on (e.g., "Fire Knight, Dragon, Ice Golem")
6. **Setup Requirements:** Gear, speed tuning, skill order
7. **Expected Results:** Clear time, damage, success rate

**Prioritization Rule:**
- If cheese strategy is strictly better AND safer than conventional teams, recommend cheese as PRIMARY strategy
- Example: "Triple Coldheart + Ally Attack is STRICTLY BETTER than conventional Fire Knight teams - prioritize this cheese"
- Note in champion review AND relevant boss guide under "Additional Team Archetypes" section

**Cross-Reference to Boss Guides:**
- Always note which boss guides include this cheese strategy
- Example: "See Clan Boss UNM guide, Section 11: Triple Pain Keeper Unkillable Cheese"

---

### Single-Champion Addition Workflow

**Purpose:** Streamline process for adding individual champion reviews and updating guides

**Workflow Steps:**

**Step 1: Gather Champion Data**
- Look up champion on RaidHQ, Ayumilove, HellHades
- Document: Rarity, Affinity, Faction, Skills, Base stats
- Note boss-specific ratings (X/10 or X/5 from external sources)

**Step 2: Generate Champion Review in Chat**
- Use Champion Review Template
- Present review in CHAT for user approval
- Do NOT create file until user approves
- Iterate based on user feedback

**Step 3: Create Champion Review File (After Approval)**
- Save to `Notes/Champion Reviews/[Champion_Name]_Review.md`
- Use DRAFT file initially: `[Champion_Name]_Review_DRAFT.md`
- After validation, promote to FINAL: `[Champion_Name]_Review.md`

**Step 4: Identify Affected Boss Guides**
- Based on champion ratings and use cases, identify which boss guides need updates
- Prioritize: CRITICAL (6/5 or 10/10) > HIGH (5/5 or 8-9/10) > MEDIUM (4/5 or 6-7/10)
- Create priority queue in chat: "Champion X affects: [Boss A (CRITICAL), Boss B (HIGH), Boss C (MEDIUM)]"

**Step 5: Update Boss Guides Systematically**
- Use DRAFT workflow (see DRAFT-to-FINAL Workflow section)
- Update Section 2: Champion-to-Mechanics Mapping
- Update Section 4: Detailed Team Sections (add new team or update existing)
- Update Section 5: Best Champions & Team Participation
- Update Section 6: Direct Champion Comparisons by Role
- Update Section 7: Ideal Champions to Pull (remove if now owned)
- Update Section 9: Actionable Notes & Upgrade Advice

**Step 6: Validate and Commit**
- Run validation: `python Tools/validate_guide_structure.py Notes/[Guide_Name]_DRAFT.md`
- Present updated guide summary in chat for user approval
- After approval, promote DRAFT to FINAL
- Commit with detailed message: "Add [Champion Name] review + update [Boss] guides"

**Scalability Notes:**
- This workflow is designed for 1 champion at a time
- For multiple champions (5+), use batch workflow from Roster Update Workflow section
- Workflow is account-agnostic: Can be repeated for any owned champion list

---

## Arena Guide Standards

### Tier-Specific Recommendations

**Purpose:** Provide separate advice for each Arena tier with tier-appropriate strategies

**Arena Tiers Covered:**
- **Gold 3:** Entry tier, basic speed tuning (250-280 SPD)
- **Gold 4:** Intermediate tier, improved speed tuning (280-310 SPD)
- **Gold 5:** Advanced tier, high speed tuning (310-340 SPD)
- **Platinum:** Elite tier, maximum speed tuning (340-370+ SPD)

**Tier-Specific Content for Each Tier:**

1. **Speed Requirements:**
   - Recommended speed for each role (Speed Lead, Buffer, Nuker, Control)
   - Example: "Gold 3: Speed Lead 280+, Buffer 260+, Nuker 240+, Control 220+"

2. **Common Team Archetypes:**
   - Speed teams (go first, nuke)
   - Tanky teams (survive first turn, counter)
   - Control teams (crowd control, debuff)
   - Buff steal teams (steal buffs, nuke)

3. **Common Threats per Tier:**
   - List common defense teams at this tier
   - Example: "Gold 4: Expect Arbiter/Lyssandra speed leads, Wukong nukers, Mythrala/Kymar buff/control"

4. **Counters & Strategies:**
   - How to counter common threats
   - Example: "If slower than enemy speed lead, use Loki to suppress active skills, preventing Arbiter revive"

5. **User-Specific Notes:**
   - User often loses speed battle in higher tiers
   - Recommend tanky/buff steal/gimmick options when speed battle not winnable
   - Example: "Gold 5+: Consider tanky Vogoth + Rector Drath team with Wukong buff strip"

**Core Arena Team (User's Confirmed Setup):**
- **Wukong** (speed lead, buff strip, nuke, sheep control)
- **Mythrala** (buffs/cleanse, hex damage)
- **Loki** (control, buff strip, suppress mythics/active skills)
- **Flex:** Ninja, Michelangelo, Coldheart, Godseeker Aniri, Arbiter, Rector Drath

---

### Defensive Team Variations

**Purpose:** Provide 3 defensive team variations with success rate estimates

**Defensive Team Requirements:**
1. **Variation 1:** Speed-based defense
   - Fast Arbiter/Lyssandra lead + fast buffers/nukers
   - Success estimate: "30-40% defense wins in Gold 3, 20-30% in Gold 4+"
   - Weakness: "Loses to faster speed teams or Loki suppress"

2. **Variation 2:** Tanky/Sustain defense
   - Vogoth + Rector Drath + Wukong + Mythrala
   - Success estimate: "40-50% defense wins in Gold 3, 30-40% in Gold 4+"
   - Weakness: "Loses to buff strip + nuke teams, slow clear time allows enemy to win"

3. **Variation 3:** Control/Debuff defense
   - Loki + Wukong + Mythrala + Arbiter (bait)
   - Success estimate: "35-45% defense wins in Gold 3, 25-35% in Gold 4+"
   - Weakness: "Loses to immunity sets or high resist teams"

**Success Estimate Documentation:**
- Based on common team archetypes at each tier
- Note: "Defense wins are inherently lower than offense wins due to AI limitations"
- Provide counterstrategy notes: "If seeing low defense wins, try Variation 2 (tanky sustain)"

---

### Live Arena Coverage

**Purpose:** Provide basic Live Arena strategy with focus on user's current approach

**User's Current Live Arena Strategy:**
- **Arbiter as bait:** Force enemy to ban Arbiter, preserving Wukong speed lead
- **Core team:** Wukong (speed lead), Mythrala, Loki, flex (Ninja, Michelangelo, Coldheart, support)
- **Future plan:** Integrate Embrys (not yet built due to book cost)

**Live Arena Basics (Coverage Level):**

1. **Ban Strategy:**
   - How to identify enemy threats (check enemy champions, predict strategy)
   - When to ban enemy speed lead vs. enemy nuker vs. enemy control
   - User's strategy: Offer Arbiter as bait, preserve Wukong

2. **Draft Order:**
   - General guidance: Speed lead → Buffer → Nuker → Control → Flex
   - Counter-draft: If enemy picks speed lead, consider tanky/sustain approach

3. **Counter Picks:**
   - How to counter common Live Arena champions
   - Example: "Enemy picks Arbiter → ban or pick Loki to suppress revive"

4. **Future Integration: Embrys**
   - Note Embrys is not yet built (book cost)
   - Recommend Embrys as future upgrade for Live Arena (Mythic tier, game-changing kit)
   - Placeholder: "When Embrys is built, integrate as primary control/debuff champion"

**Coverage Scope:**
- Basic coverage only (user still developing strategy)
- Focus on user's confirmed team and approach
- Leave room for expansion as user builds Live Arena roster

---

### Tag Team Standards

**Purpose:** Provide 3 core teams + cheese variations for Tag Team Arena, no defense focus

**Tag Team Focus:** Bronze 3+, lower priority than Classic Arena

**Core Team Requirements:**
- **Safe but fast teams** prioritized
- **3 core teams** documented
- **Cheese variations** documented
- **No defense recommendations** (user does not care about Tag Team defense)

**Core Team Documentation Format:**

**Team 1: [Name]**
- **Champions:** [5 champions]
- **Speed Tuning:** [Turn order, speed requirements]
- **Strategy:** [Go first and nuke, survive and counter, etc.]
- **Strengths:** [Fast clear, high damage, etc.]
- **Weaknesses:** [Loses to X, requires Y, etc.]
- **Success Rate:** [Estimated % vs. Bronze 3 teams]

**Team 2: [Name]**
- [Same format as Team 1]

**Team 3: [Name]**
- [Same format as Team 1]

**Cheese Variations:**
- Document 1-3 cheese team variations (e.g., Triple Coldheart + Ally Attack, Unkillable cheese, etc.)
- Note when cheese is safer/faster than core teams
- Example: "Cheese Variation 1: Triple Coldheart + Nogdar + Wukong - One-shot enemy with MAX HP damage"

**Speed Tuning Guidance:**
- Provide general speed tuning guidance by role
- Example: "Tag Team Bronze 3: Speed leads 260+, Buffers 240+, Nukers 220+, supports 200+"
- Note: "Tag Team matchmaking is less predictable than Classic Arena - prioritize safety over speed"

---

## DRAFT-to-FINAL Workflow

**Purpose:** Ensure all file updates are validated and approved before promoting to FINAL

**Workflow Overview:**

**Stage 1: DRAFT Creation**
- Always create DRAFT file when updating existing guides/reviews
- File naming: `[Original_Name]_DRAFT.md`
- Example: `Dragon_Hard_Team_Notes_DRAFT.md`

**Stage 2: DRAFT Population**
- Merge all new information into DRAFT file
- Update all affected sections (Section 2, 4, 5, 6, 7, 9, etc.)
- Preserve all existing content not affected by update
- Document changes in DRAFT file header or changelog

**Stage 3: Validation**
- Run validation scripts: `python Tools/validate_guide_structure.py Notes/[Guide_Name]_DRAFT.md`
- Fix any errors or warnings
- Cross-check with owned champion list: `python Tools/validate_owned_list.py`

**Stage 4: Chat Review & Approval**
- Present DRAFT summary in chat:
  * What sections were updated
  * What new teams/champions were added
  * What changed in recommendations
  * Validation results
- Wait for user approval before promoting to FINAL

**Stage 5: Promotion to FINAL**
- After user approval:
  * Rename old FINAL file to `[Original_Name]_OLD_[Date].md` (archive)
  * Rename DRAFT file to `[Original_Name]_FINAL.md` (promote)
  * Move OLD file to `Archive/` folder (if desired)

**Stage 6: Commit & Documentation**
- Commit changes with detailed message:
  ```
  Update [Boss/Champion] guide with [Champion Name] teams
  
  - Added [Champion] to Section 2 mechanics mapping
  - Created Team X: [Team Name] with [Champion]
  - Updated champion comparisons and pull guide
  - Validated with 3 test runs: [results summary]
  
  DRAFT promoted to FINAL after user approval
  ```

**Never Overwrite FINAL Directly:**
- Always use DRAFT workflow for updates
- Preserve version history (OLD files archived)
- Enable rollback if issues discovered post-update

---

## Roster Update Workflow & Automation

### Directory Structure Standards

**`input/` Directory:**
- **Purpose:** Input data and templates for guide generation
- **Contents:**
  * `Owned_champion_list.md` - Champion roster (single source of truth)
  * `Boss_Guide_Template.md` - Template for boss guides
  * Future: `Champion_Database.json` (if created)

**`Tools/` Directory:**
- **Purpose:** Executable scripts, validation tools, and reference templates
- **Contents:**
  * Validation scripts (Python): `validate_owned_list.py`, `validate_guide_structure.py`
  * Reference templates (Markdown): `Team_Entry_Template.md`, `Champion_Comparison_Template.md`, `Section2_Mapping_Template.md`
  * Analysis scripts (Python): `ChampionTurnAnalysis.py`, etc.
  * Setup and utility tools

**`Notes/` Directory:**
- **Purpose:** Boss guides, champion comparisons, and documentation
- **Contents:**
  * Boss guides (*_FINAL.md)
  * Champion comparisons (`Notes/Champion Comparisons/`)
  * Champion reviews (`Notes/Champion Reviews/`)
  * Reports and analysis documents

### Owned Champion List Standards

**Required Format:**
```markdown
# Owned Champions

## Champion List

- [Champion Name] | Rarity: [Value] | Affinity: [Value] | Faction: [Value] | Last Updated: YYYY-MM-DD
```

**Valid Values:**
- **Rarity:** Common, Uncommon, Rare, Epic, Legendary, Mythic
- **Affinity:** Magic, Force, Spirit, Void
- **Faction:** [Any valid RAID faction name]
- **Date:** YYYY-MM-DD format

**Duplicate Champion Notation:**
Use (xN) notation for multiple copies:
```markdown
- Nogdar the Headhunter (x2) | Rarity: Legendary | Affinity: Force | Faction: Ogryn Tribes | Last Updated: 2025-10-18
- Relickeeper (x4) | Rarity: Legendary | Affinity: Magic | Faction: Sacred Order | Last Updated: 2025-10-18
- Pain Keeper (x3) | Rarity: Epic | Affinity: Void | Faction: Knight Revenant | Last Updated: 2025-10-18
- Apothecary (x5) | Rarity: Rare | Affinity: Magic | Faction: High Elves | Last Updated: 2025-10-18
```

**Alphabetical Ordering:**
- All champions must be in alphabetical order (case-insensitive)
- Use `python Tools/validate_owned_list.py --fix-order` to auto-sort

**Validation:**
```bash
# Validate format and consistency
python Tools/validate_owned_list.py

# Validate and auto-fix alphabetical order
python Tools/validate_owned_list.py --fix-order
```

---

### "Cheese" Mechanics & Duplicate Champions

**Definition:**
"Cheese" strategies abuse specific game mechanics to trivialize boss encounters or enable unconventional victories.

**Common Cheese Strategies:**

1. **Buff Extension Cheese:**
   * Multiple copies of champions with Increase DEF, Ally Protection, or Counterattack
   * Extend buffs indefinitely with champions like Warcaster, Brogni, etc.
   * Example: Double Maulie Tankard for infinite Block Debuffs

2. **Poison Explosion Cheese:**
   * Stack massive poison debuffs (10+) on boss
   * Detonate with Zavia, Elenaril, or similar
   * Deal millions of damage in single explosion
   * Example: Double Frozen Banshee + Zavia for poison spam

3. **Max HP Damage Cheese:**
   * Multiple champions with MAX HP damage (Coldheart, Royal Guard, Sethalia, etc.)
   * Bypass boss DEF and HP scaling
   * One-shot boss waves or phases
   * Example: Triple Coldheart + Ally Attack for instant wave clear

4. **Unkillable Cheese:**
   * Multiple Pain Keepers (x3+ recommended)
   * Build unkillable teams with overlapping cooldown reduction
   * Survive indefinitely, whittle down boss
   * Example: Triple Pain Keeper + Block Damage champions

5. **Passive Sustain Cheese:**
   * Multiple Lady Annabelle or similar passive damage champions
   * Passive damage + passive heals = eventual victory
   * AFK strategy for Bommal and other sustain bosses
   * Example: Lady Annabelle solo Bommal (leave overnight)

6. **Turn Meter Cheese:**
   * Multiple TM control champions (Armiger, Coldheart, etc.)
   * Prevent boss from taking turns
   * Lock boss at 0% TM indefinitely
   * Example: Triple Armiger for Fire Knight perma-lock

7. **Ally Attack Spam Cheese:**
   * Multiple Ally Attack champions (Nogdar, Longbeard, Lanakis, etc.)
   * Chain Ally Attacks for massive turn cycling
   * Overwhelm boss with action economy
   * Example: Double Nogdar for back-to-back Ally Attacks

**How to Document Cheese Strategies in Guides:**

1. **Section 4 (Detailed Team Sections):**
   * Add "Cheese Strategy" team archetype if applicable
   * Example: "Team 7: Triple Pain Keeper Unkillable Cheese"
   * Note duplicate champion requirements

2. **Section 11 (Additional Team Archetypes):**
   * Document cheese strategies that require specific duplicate champions
   * Note: "This team requires multiple copies of [Champion Name]"
   * Explain why cheese works and when it's optimal

3. **Section 7 (Ideal Champions to Pull):**
   * Note: "Pull additional copies of [Champion Name] for cheese strategy"
   * Example: "Pull 2nd Coldheart for MAX HP damage cheese in Fire Knight"

4. **Champion-to-Mechanics Mapping (Section 2):**
   * Flag champions with "(x2)", "(x3)", etc. in mapping tables
   * Note cheese potential in "Notes" column
   * Example: "Nogdar the Headhunter (x2) - Ally Attack spam cheese potential"

**Priority for Duplicate Champions:**
- Always note duplicate counts in owned champion list
- Prioritize cheese strategies for end-game bosses (Doom Tower Hard, Hydra Brutal, etc.)
- Document alternative strategies if duplicates not available

---

### Guide Update Workflow (Roster Changes)

**When Owned Champion List Changes:**

**Step 1: Update Owned Champion List**
- Add/remove champions from `input/Owned_champion_list.md`
- Use proper format (Name | Rarity | Affinity | Faction | Last Updated)
- Add duplicate notation for multiple copies (x2, x3, etc.)
- Run validation: `python Tools/validate_owned_list.py --fix-order`

**Step 2: Identify Affected Guides (Priority Queue)**
- For each new champion, check boss ratings (RaidHQ, Ayumilove, HellHades)
- Prioritize guides based on champion rating:
  * **CRITICAL (6/5 or 10/10):** Update guide immediately
  * **HIGH (5/5 or 8-9/10):** Update within 1-2 sessions
  * **MEDIUM (4/5 or 6-7/10):** Update as time allows
  * **LOW (3/5 or 4-5/10):** Defer or skip unless gap-filling role

**Step 3: Generate Guide Update Checklist (Per Guide)**
- [ ] Section 2: Add champion to mechanics mapping tables (per-trial and combo tables)
- [ ] Section 2: Update gap analysis (note if champion fills critical gap)
- [ ] Section 3: Add/update quick reference table (if new team created)
- [ ] Section 4: Create new team section OR update existing team with champion
- [ ] Section 4: Document cheese strategy if duplicate champion enables it
- [ ] Section 5: Add champion to "Best Champions & Team Participation" table
- [ ] Section 6: Add champion to "Direct Champion Comparisons by Role"
- [ ] Section 7: Remove champion from "Ideal Champions to Pull" (now owned)
- [ ] Section 9: Update "Actionable Notes & Upgrade Advice" with new upgrade path
- [ ] Section 12: Document validation/simulation for new team (minimum 3 test runs)

**Step 4: Update Guide (Systematic Process)**
- Use reference templates from `Tools/` directory:
  * `Team_Entry_Template.md` for new teams
  * `Champion_Comparison_Template.md` for champion comparisons
  * `Section2_Mapping_Template.md` for mechanics mapping
- Follow template checklist to ensure all required fields populated
- Run simulations (minimum 3 test runs per new team)
- Document affinity safety/risk (multi-line format)
- Note cheese strategy potential if applicable

**Step 5: Validate Updated Guide**
- Run guide structure validation: `python Tools/validate_guide_structure.py Notes/[Guide_Name]_FINAL.md`
- Check TOC numbering and anchor links
- Verify all required sections present
- Check affinity documentation (minimum 1 mention per team)

**Step 6: Version Control**
- Never overwrite original guide directly
- Create new version (e.g., `_v2.md` or date-stamped)
- Commit changes with detailed message:
  ```
  Update [Boss] guide with [Champion Name] teams
  
  - Added [Champion Name] to Section 2 mechanics mapping
  - Created Team X: [Team Name] with [Champion Name]
  - Updated champion comparisons and pull guide
  - Simulated 3 runs: [results summary]
  ```
- Push to feature branch or v0.X branch

**Step 7: User Review & Finalize**
- User reviews new teams and recommendations
- Make adjustments based on feedback
- Merge to main branch after approval
- Archive old version in `Archive/` folder if needed

---

### Validation Scripts & Tools

**`Tools/validate_owned_list.py`**
- Validates owned champion list format, consistency, and integrity
- Checks: Format, duplicates, alphabetical order, rarity/affinity values, date format
- Usage: `python Tools/validate_owned_list.py [--fix-order]`

**`Tools/validate_guide_structure.py`**
- Validates boss guide structure, TOC, sections, and formatting
- Checks: TOC format, required sections, numbering, anchor links, affinity documentation
- Usage: `python Tools/validate_guide_structure.py [file] [--all]`

**Reference Templates (in `Tools/`):**
- `Team_Entry_Template.md` - Standard team specification format
- `Champion_Comparison_Template.md` - Champion comparison format
- `Section2_Mapping_Template.md` - Mechanics mapping format

**Boss Guide Template (in `input/`):**
- `Boss_Guide_Template.md` - Standard template for all boss guides

---

### Community & Multi-User Support

**For Community Users:**

1. **Fork Repository:**
   - Fork Raid_Tools repository to personal GitHub account

2. **Replace Owned Champion List:**
   - Update `input/Owned_champion_list.md` with personal roster
   - Use proper format (Name | Rarity | Affinity | Faction | Last Updated)
   - Add duplicate notation (x2, x3, etc.) for multiple copies

3. **Run Validation:**
   ```bash
   python Tools/validate_owned_list.py --fix-order
   ```

4. **Trigger Guide Regeneration:**
   - Follow "Guide Update Workflow" steps above
   - Start with highest priority bosses (end-game content first)

5. **Expected Output:**
   - Updated boss guides tailored to personal roster
   - New team recommendations based on owned champions
   - Updated pull priorities based on gaps

**Multi-User Workflow:**
- Each user maintains separate owned champion list
- Fork repository for personal use
- Share updated guides via pull requests (optional)
- Merge upstream changes periodically to get new boss guides

---

## Changelog

- **2025-10-18:** Added "Roster Update Workflow & Automation" section with directory standards, owned champion list format requirements, cheese mechanics documentation, duplicate champion tracking, guide update workflow for roster changes, validation scripts usage, and community/multi-user support guidelines
- **2025-10-17:** Added Large File Operations & Batching Requirements to Update & Staging Policy section. All file operations >500 lines or complex merges must use batched processing to prevent prompt length, runtime, and memory issues.
- **2025-10-17:** Completed all sections with full content from original RAID_copilot-instructions.md, expanding Champion & Trial Mapping, Team Building & Simulation, Affinity Safety & Risk Requirements, Guide Structure & Required Sections, Update & Staging Policy, Section-by-Section Maintenance, Validation & Documentation Standards, Templates & Examples, Task Checklist, and Additional Questions for User/Reviewer
- **2025-10-16:** Initial creation incorporating Generic AI & Copilot Instructions standards and project-specific boss guide generation workflows, QA standards, and team-building methodologies
