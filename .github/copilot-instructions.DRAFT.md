# RAID Shadow Legends Project Instructions (DRAFT v0.7)

> This file is a DRAFT for the unified project instructions, workflows, and templates for champion, boss, mechanic, and team dictionary/guide generation. All edits and section reviews will be staged here before final consolidation and ToC/anchor update.


## Table of Contents (DRAFT)

1. [Project Purpose & Scope](#project-purpose--scope)
2. [User Content Priorities & Focus](#user-content-priorities--focus)
3. [Authoritative Data Sources](#authoritative-data-sources)
4. [Champion Dictionary Entry Workflow](#champion-dictionary-entry-workflow)
5. [Boss Guide Entry Workflow](#boss-guide-entry-workflow)


## 1. Project Purpose & Scope
- Build evaluation and optimization for actual user champion setups

7. **Continuous Improvement:** Update all instructions, workflows, and templates as new content, mechanics, or user needs arise. Consolidate duplicate sections and keep the knowledge base current.

- Mechanic entries: JSON or Markdown (as needed)
- Team recommendations: Markdown/JSON (linked to boss and champion entries)
- All new or updated templates should be referenced in the instructions and included in the repo for future automation and consistency.

- All entries must be validated from at least two authoritative sources (Ayumilove, HellHades, RaidHQ, in-game)
---

## 2. User Content Priorities & Focus

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

## 2. Authoritative Data Sources

### Validation Rules
- All champion, boss, mechanic, and team data must be validated from at least two authoritative sources before entry creation or update. 
- Stats may be pulled from screenshots of the champions base stats. If unsure, confirm in chat.
### Primary Sources
- **RaidHQ**: Official boss mechanics, trial requirements, stat thresholds. (https://raid-hq.com/)
- **Ayumilove**: Champion guides, skill descriptions, gear/mastery recommendations. (https://ayumilove.net/raid-shadow-legends-guide/)
- **HellHades**: Team compositions, speed tuning, tier lists, champion ratings. (https://hellhades.com/)
- **In-Game Testing**: User-provided simulation results, screenshots, and direct observation.

### Source Documentation
- Always cite sources in each entry and in commit messages.
- Mark uncertainties or conflicts in a dedicated "Citations & Conflicts" section.


### Purpose
Establish a validated, canonical process for creating, updating, and maintaining champion dictionary entries in the RAID Shadow Legends knowledge base. This ensures all champion data is accurate, cross-referenced, and indexable for downstream guide and team generation.

### Canonical Template
- All champion entries must use the canonical template in `input/Champion_Dictionary_Prompt_template.md`.
- Template fields include: Name, Rarity, Affinity, Faction, Role(s), Mechanics Tags, Skills (with cooldowns, effects, multipliers), Booking Priority, Gear/Mastery Recommendations, and Validation Sources.
- Mechanics tags must be selected from the canonical list in the template; propose additions only after review.

### Entry Creation Workflow
1. **Data Gathering**
	- Collect champion data from authoritative sources: Ayumilove, HellHades, RaidHQ, and in-game.
	- Cross-validate all skill descriptions, cooldowns, multipliers, and unique mechanics.
	- Document all sources in the entry.
2. **Template Population**
	- Populate all required fields in the template.
	- Use mechanics tags to enable search and team-building automation.
	- Specify gear/mastery recommendations for each major content type (Clan Boss, Dungeons, Arena, etc.).
3. **Validation**
	- Cross-check all data with at least two sources.
	- Note any conflicts or uncertainties in the entry.
	- Mark data confidence level (High/Medium/Low) if sources disagree.
4. **Entry Review & Approval**
	- Present new or updated entry for review (in chat or PR).
	- After approval, add to the champion dictionary (JSON or Markdown as required).
	- Update index and search tools if new mechanics tags or roles are added.

### Update & Maintenance Workflow
- When a champion is buffed, nerfed, or reworked, repeat the data gathering and validation steps.
- Mark outdated entries for review and update as soon as possible.
- Use versioning for major changes (e.g., `ChampionName_v2.md`).
- Document all changes in the entry changelog or commit message.

### Validation & Documentation Standards
- All entries must cite sources for skills, mechanics, and recommendations.
- If a skill or mechanic is ambiguous, note the uncertainty and preferred interpretation.
- Use in-game testing for final validation when possible.

### Automation & Indexing
- Entries must be structured for automated parsing (JSON or Markdown with clear field delimiters).
- Mechanics tags and roles must be consistent for search and team-building scripts.
- Update the champion index after each addition or major update.

---

## 4. Boss Guide Entry Workflow

### Purpose
Define a validated, modular process for creating, updating, and maintaining boss guide entries for RAID Shadow Legends. Ensure all guides are actionable, cross-referenced, and optimized for owned champion rosters and current meta.

### Canonical Template
- All boss guides must use the canonical template in `input/Boss_Guide_Template.md`.
- Template sections include: Table of Contents, Boss Mechanics & Stat Requirements, Trial/Mechanic Mapping, Quick Reference Tables, Detailed Team Recommendations, Best Champions & Team Participation, Champion Comparisons, Ideal Champions to Pull, General Notes, Actionable Advice, Validation & Simulation Notes.
- All sections and anchors must match the template; update ToC and anchors as needed.

### Guide Creation Workflow
1. **Research & Data Gathering**
	- Review authoritative boss guides (RaidHQ, Ayumilove, HellHades, in-game).
	- Document all boss forms/phases, turn order, affinities, unique mechanics, and trial/stat requirements.
	- Cross-validate and cite sources in the guide.
2. **Trial/Mechanic Mapping**
	- Map all boss trials/mechanics to the owned champion list (see Section 3 for champion entry standards).
	- Build per-trial and combo tables, noting affinity safety/risk and special notes for each champion.
3. **Team Building & Simulation**
	- Build and simulate 5–8 unique teams using only owned champions, maximizing trial/mechanic completion, damage, and hybrid approaches.
	- For each team, specify all required details: roles, alternates, speed tuning, gear, masteries, manual/auto, strengths, weaknesses, simulated results, affinity safety/risk, actionable advice.
	- Run at least 3 simulations per team and document results in the guide.
4. **Guide Structure & Output**
	- Use a modular, anchor-linked Table of Contents.
	- Add quick reference tables for best teams by difficulty/trial/damage tier.
	- Populate all required sections per the canonical template.
5. **Update & Validation**
	- After any roster change, re-run all mapping, team building, and simulation steps.
	- Regenerate all tables and recommendations as needed.
	- Document all validation and simulation steps for transparency.
	- Never overwrite the original file directly; always preserve previous versions and stage changes for review.

### Update & Maintenance Workflow
- When a boss is reworked or new mechanics are added, repeat the research and validation steps.
- Mark outdated guides for review and update as soon as possible.
- Use versioning for major changes (e.g., `BossName_v2.md`).
- Document all changes in the guide changelog or commit message.

### Validation & Documentation Standards
- All guides must cite sources for mechanics, stat requirements, and team recommendations.
- If a mechanic or stat is ambiguous, note the uncertainty and preferred interpretation.
- Use in-game testing for final validation when possible.

### Automation & Indexing
- Guides must be structured for automated parsing (Markdown with clear section anchors and tables).
- Mapping tables and team sections must be consistent for search and team-building scripts.
- Update the boss guide index after each addition or major update.

### Simulation and speed tune testing
- Identify meta speed tunes for teams and run simulations on likely outcomes for battles.
- For Clan Boss, prefer high damage and auto friendly teams. Speed tune may be critical
- For other bosses, prefer reliable completion teams.
- Cheese teams should be included.

---

## 5. Mechanic Entry Workflow

### Purpose
Define a standardized process for documenting, updating, and maintaining mechanic entries (buffs, debuffs, passives, unique effects) in the RAID Shadow Legends knowledge base. Ensure all mechanics are indexable, cross-referenced, and usable for automation and team-building.

### Canonical Template
- All mechanic entries must use a canonical template (JSON or Markdown) specifying: Name, Type (buff, debuff, passive, unique), Description, Affected Skills/Champions, Interactions, Counters, and Validation Sources.
- Mechanics tags must be consistent with those used in champion and boss entries.
- Propose new mechanics or tags only after review and consensus.

### Entry Creation Workflow
1. **Data Gathering**
	- Collect mechanic data from authoritative sources: Ayumilove, HellHades, RaidHQ, and in-game.
	- Cross-validate all descriptions, interactions, and counters.
	- Document all sources in the entry.
2. **Template Population**
	- Populate all required fields in the template.
	- Link to all affected champions, bosses, and teams.
	- Specify known counters and unique interactions.
3. **Validation**
	- Cross-check all data with at least two sources.
	- Note any conflicts or uncertainties in the entry.
	- Mark data confidence level (High/Medium/Low) if sources disagree.
4. **Entry Review & Approval**
	- Present new or updated entry for review (in chat or PR).
	- After approval, add to the mechanic dictionary (JSON or Markdown as required).
	- Update index and search tools if new mechanics or tags are added.

### Update & Maintenance Workflow
- When a mechanic is reworked or new interactions are discovered, repeat the data gathering and validation steps.
- Mark outdated entries for review and update as soon as possible.
- Use versioning for major changes (e.g., `MechanicName_v2.md`).
- Document all changes in the entry changelog or commit message.

### Validation & Documentation Standards
- All entries must cite sources for descriptions, interactions, and counters.
- If a mechanic is ambiguous, note the uncertainty and preferred interpretation.
- Use in-game testing for final validation when possible.

### Automation & Indexing
- Entries must be structured for automated parsing (JSON or Markdown with clear field delimiters).
- Mechanics tags must be consistent for search and team-building scripts.
- Update the mechanic index after each addition or major update.

### Core summary of info to index
- Boss mechanics
- Game mechanic index/dictionary
- interaction guidelines
- Passive mechanics
- Meta interactions and setups
- Hp Burn and Poison and other damage based on Boss or Max HP mechanics 
- 'Cheese' teams and mechanics ex unkillable, revive on death, block damage, poison explosion, etc

---

## 6. Team Creation & Analysis Workflow

### Purpose
Define a systematic, validated process for building, simulating, and analyzing teams for all RAID content (bosses, dungeons, Faction Wars, Arena, etc.), using only owned champions and validated mechanics. Ensure all teams are actionable, optimized, and documented for both manual and auto play.

### Canonical Template
- All team entries must use a standard template specifying: Team Name, Content Type, Difficulty, Team Composition (champions/roles), Alternates, Speed Tuning, Gear/Masteries, Manual/Auto, Strengths, Weaknesses, Simulated Results, Affinity Safety/Risk, Actionable Advice, and Validation Sources.
- Use quick reference tables for best teams by damage, trial completion, or clear speed.
- Link to all relevant champion, boss, and mechanic entries.

### Team Creation Workflow
1. **Team Archetype Selection**
	- Identify required mechanics/trials for the target content (see boss/mechanic entries).
	- Select team archetypes (HP Burn, Poison, Unkillable, Control, etc.) based on owned champions and content requirements.
2. **Team Building**
	- Build 5–8 unique teams using only owned champions, maximizing trial/mechanic completion, damage, and hybrid approaches.
	- For each team, specify all required details: core roles, alternates, speed tuning, gear, masteries, manual/auto, strengths, weaknesses, simulated results, affinity safety/risk, actionable advice.
	- Ensure all teams are unique (no champion appears in multiple teams unless explicitly allowed for cheese/duplicate strategies).
3. **Simulation & Validation**
	- Run at least 3 test runs per team (manual and/or auto as appropriate).
	- Document clear times, damage scores, trial completion, and success rates.
	- Note affinity safety/risk and any observed issues (weak hits, debuff failures, etc.).
	- Use in-game testing, calculators, or community tools for validation.
4. **Documentation & Output**
	- Populate all required fields in the team template.
	- Add quick reference tables and detailed team sections to the relevant boss/guide entry.
	- Link to all referenced champion and mechanic entries.

### Update & Maintenance Workflow
- When new champions are acquired or mechanics change, re-run team building and simulation steps.
- Mark outdated teams for review and update as soon as possible.
- Use versioning for major changes (e.g., `TeamName_v2.md`).
- Document all changes in the team changelog or commit message.

### Validation & Documentation Standards
- All teams must cite sources for strategy, speed tuning, and validation results.
- If a team fails a trial or mechanic, document the failure and suggest upgrades or alternates.
- Use in-game testing for final validation when possible.

### Automation & Indexing
- Teams must be structured for automated parsing (Markdown or JSON with clear field delimiters).
- Team tables and sections must be consistent for search and team-building scripts.
- Update the team index after each addition or major update.

---

## 7. Build Evaluation & Optimization

### Purpose
Provide a structured workflow for evaluating, optimizing, and documenting actual user champion builds for all RAID content. Ensure feedback is actionable, content-specific, and supports continuous improvement of the owned roster.

### Canonical Template
- All build evaluations must use a standard template specifying: Champion Name, Content Type, Current Build (gear sets, stats, masteries, skill books), Recommended Build (gear sets, stats, masteries, skill books), Gaps/Issues, Upgrade Priorities, and Validation Sources.
- Include a comparison table of current vs. recommended stats and gear.
- Link to relevant champion, team, and boss entries.

### Build Evaluation Workflow
1. **Input Collection**
	- Gather current build details: level, ascension, skill books, gear sets, stats (HP, ATK, DEF, SPD, Crit Rate, Crit Damage, ACC, RES), and masteries.
	- Specify primary content use (Clan Boss, Dungeon, Arena, etc.).
2. **Comparison & Analysis**
	- Compare current build to recommended build for the target content.
	- Identify gaps in stats, gear, masteries, or skill books.
	- Note if the build is optimal, suboptimal, or misaligned for the intended use.
3. **Upgrade & Optimization Advice**
	- Prioritize upgrades (e.g., "Increase ACC to 250+ for Clan Boss UNM").
	- Suggest gear swaps, mastery changes, or skill book investments as needed.
	- Recommend respec if champion is built for the wrong content.
4. **Documentation & Output**
	- Populate all required fields in the build evaluation template.
	- Add actionable notes and upgrade path to the relevant champion/team entry.
	- Link to referenced guides and validation sources.

### Update & Maintenance Workflow
- When a champion is rebuilt, rebooked, or re-geared, repeat the evaluation and optimization steps.
- Mark outdated evaluations for review and update as soon as possible.
- Use versioning for major changes (e.g., `ChampionName_Build_v2.md`).
- Document all changes in the evaluation changelog or commit message.

### Validation & Documentation Standards
- All evaluations must cite sources for recommended builds and stat targets.
- If a recommended build is ambiguous, note the uncertainty and preferred interpretation.
- Use in-game testing for final validation when possible.

### Automation & Indexing
- Evaluations must be structured for automated parsing (Markdown or JSON with clear field delimiters).
- Build tables and sections must be consistent for search and optimization scripts.
- Update the build index after each addition or major update.

---

## 8. Guide Update & Versioning Policy

### Purpose
Establish clear policies and workflows for updating, versioning, and maintaining all knowledge base entries (champion, boss, mechanic, team, build) to ensure accuracy, traceability, and reproducibility.

### Update Workflow
1. **Trigger for Update**
	- New champion acquired, champion/boss/mechanic reworked, or new content/mechanics released.
	- User requests update or identifies outdated information.
2. **Staging & Drafting**
	- Create a DRAFT version of the entry (e.g., `GuideName_DRAFT.md`).
	- Make all edits and additions in the DRAFT file, preserving the original FINAL version.
    - Stage detailed prompt files in input to describe listed workflows in more detail, including template info.
3. **Validation & Review**
	- Run validation scripts and cross-check with authoritative sources.
	- Present DRAFT for user or peer review.
	- Iterate as needed until approved.
4. **Promotion to FINAL**
	- After approval, archive the old FINAL version (e.g., `GuideName_OLD_YYYY-MM-DD.md`).
	- Rename DRAFT to FINAL (e.g., `GuideName_FINAL.md`).
	- Move archived files to an `Archive/` folder if desired.
5. **Documentation & Commit**
	- Document all changes in the changelog or commit message, including validation steps and sources.
	- Use detailed commit messages for traceability.

### Versioning Policy
- Never overwrite FINAL files directly; always use DRAFT-to-FINAL workflow.
- Use date-stamped or versioned filenames for major changes (e.g., `_v2.md`, `_2025-10-21.md`).
- Archive old versions for rollback and comparison.
- Update indexes and references after each major update.

### Validation & Documentation Standards
- All updates must be validated with at least two authoritative sources.
- Document all validation steps, sources, and simulation results in the entry or commit message.
- Note any uncertainties, conflicts, or assumptions in a dedicated section.

### Automation & Indexing
- Updates must be structured for automated detection and indexing (e.g., by filename pattern or metadata tag).
- Update all relevant indexes and cross-references after each update.

---

## 9. Validation & Documentation Standards

### Purpose
Define rigorous standards for validating, documenting, and cross-referencing all knowledge base entries (champion, boss, mechanic, team, build) to ensure accuracy, transparency, and reproducibility.

### Validation Standards
- All entries must be validated with at least two authoritative sources (Ayumilove, HellHades, RaidHQ, in-game testing).
- In-game testing and user-provided screenshots take highest priority for stat and mechanic validation.
- If sources conflict, note the discrepancy and prefer community consensus (RaidHQ + Ayumilove/HellHades).
- Mark data confidence level (High/Medium/Low) if sources disagree or data is ambiguous.

### Documentation Standards
- Cite all sources in each entry and in commit messages.
- Document all validation steps, simulation results, and assumptions in a dedicated section of each entry.
- Note any uncertainties, conflicts, or alternate interpretations.
- Use clear, modular sectioning and field delimiters for automated parsing.

### Simulation & Testing
- For teams and builds, run at least 3 test runs (manual and/or auto as appropriate) and document results.
- Note clear times, damage scores, trial completion, success rates, and affinity safety/risk.
- Use calculators or community tools for additional validation as needed.

### Cross-Referencing & Indexing
- Link all entries to relevant champions, bosses, mechanics, and teams.
- Update indexes and cross-references after each major addition or update.
- Use consistent tags and field names for search and automation.

---

## 10. Templates & Examples

### Purpose
Provide canonical templates and example entries for all knowledge base types (champion, boss, mechanic, team, build) to ensure consistency, automation, and ease of use.

### Template Documentation
- For each entry type, document or specify the canonical template (JSON or Markdown) in the instructions.
- If a template does not exist, create and add it to the project (see below for reference formats).
- All new or updated templates should be referenced in the instructions and included in the repo for future automation and consistency.

### Champion Dictionary Template (JSON)
See `input/Champion_Dictionary_Template.json` for the canonical champion dictionary entry template. This file provides the required structure and field documentation for all champion entries. Do not specify the JSON syntax in multiple places—always reference this template for champion dictionary entry format.

### Boss Guide Template (Markdown) 
See `input/Boss_Guide_Template.md` for the full canonical template. Include anchors. Key sections:
- Table of Contents (anchor-linked)
- Boss Mechanics & Stat Requirements
- Trial/Mechanic Mapping
- Quick Reference Tables
- Detailed Team Recommendations
- Best Champions & Team Participation
- Champion Comparisons
- Ideal Champions to Pull
- General Notes
- Actionable Advice
- Validation & Simulation Notes

### Mechanic Entry Template (JSON/Markdown) DRAFT
```json
{
	"name": "Mechanic Name",
	"type": "buff/debuff/passive/unique",
	"description": "Mechanic effect description.",
	"affected": ["Champion A", "Champion B", ...],
	"interactions": ["Countered by X", "Synergizes with Y"],
	"validation_sources": ["Ayumilove", "HellHades"],
	"notes": "Any special notes or conflicts."
}
```

### Team Entry Template (Markdown/JSON) DRAFT
```markdown
| Team Name | Content | Difficulty | Champions | Alternates | Speed Tune | Gear | Masteries | Manual/Auto | Strengths | Weaknesses | Sim Results | Affinity Safety/Risk | Actionable Advice | Validation Sources |
|-----------|---------|------------|-----------|------------|------------|------|-----------|-------------|-----------|------------|-------------|----------------------|-------------------|-------------------|
| Example   | Clan Boss | UNM | [A, B, C, D, E] | [F, G] | 191/171/171/171/171 | Speed, Lifesteal | Warmaster | Auto | High damage | Needs books | 70M avg | Safe (all neutral) | Use A2 on turn 1 | Ayumilove, HH |
```

### Build Evaluation Template (Markdown/JSON) DRAFT
```markdown
| Champion | Content | Current Build | Recommended Build | Gaps/Issues | Upgrade Priorities | Validation Sources |
|----------|---------|---------------|-------------------|-------------|--------------------|-------------------|
| Example  | Clan Boss | Speed+Lifesteal, 210 SPD, 220 ACC | Speed+Lifesteal, 220 SPD, 250 ACC | ACC low | 1. ACC 2. SPD | Ayumilove, HH |
```

---

## 11. Review Questions & Feedback

### Purpose
Provide a structured set of review questions and feedback prompts to ensure all workflows, templates, and outputs meet project standards and user needs. Use these questions for self-review, peer review, and user validation after each major update or new entry.

### General Review Questions
- Are all required sections present and in the correct order?
- Are all templates referenced from a single canonical file (no duplication)?
- Are all entries validated with at least two authoritative sources?
- Are mechanics, tags, and roles consistent and indexable?
- Are all outputs modular, human-readable, and automation-friendly?
- Are versioning and update policies followed for all changes?
- Are all validation steps, sources, and simulation results documented?
- Are uncertainties, conflicts, or assumptions clearly noted?

### Champion Entry Review Questions
- Are all mechanics for this champion listed and tagged under the main entry?
- Are meta ratings present and up to date?
- Are all forms/alternate kits included (for mythics)?
- Are gear/mastery/blessing recommendations current?
- Is the mechanics tagging list complete and indexable?
- Is the entry standardized and chat-readable?
- Are update & review notes present?

### Boss Guide Review Questions
- Are all boss mechanics, forms, and stat requirements fully documented?
- Are trial/mechanic mapping tables complete and accurate?
- Are all teams unique, actionable, and validated with simulations?
- Are affinity safety/risk notes explicit and multi-line?
- Are quick reference tables and detailed team sections present?
- Are ideal champions to pull and upgrade paths documented?
- Are validation & simulation notes complete?

### Mechanic Entry Review Questions
- Is the mechanic description clear and validated?
- Are all affected champions, bosses, and teams linked?
- Are interactions, counters, and unique effects documented?
- Is the entry indexable and automation-ready?

### Team & Build Review Questions
- Are all team/build fields populated and validated?
- Are simulation results, strengths, and weaknesses documented?
- Are actionable advice and upgrade priorities included?
- Are all cross-references and links up to date?

### Workflow & Instruction Feedback
- Is the workflow clear, logical, and easy to follow?
- Are all dependencies and update triggers documented?
- Are there any redundant or conflicting instructions?
- What improvements or clarifications are needed?

---
