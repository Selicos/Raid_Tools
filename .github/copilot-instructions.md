## 16. Troubleshooting & Maintenance

### Common Issues & Solutions

**Copilot not following instructions:**
- Ensure instructions are specific and actionable, not vague or ambiguous.
- Check for conflicting or duplicated guidance between base and project files.
- If instructions are too long, prioritize the most important at the top and remove unnecessary duplication.

**Copilot ignoring project-specific file:**
- Confirm the file is in the `.github` folder and named with `_copilot-instructions.md` or `-instructions.md`.
- Validate markdown syntax (no broken links, proper formatting).

**Instructions too long or verbose:**
- Remove duplicated content from base instructions; reference instead.
- Summarize examples and link to full examples elsewhere if needed.
- Focus on "what" and "why"; let Copilot determine "how" unless implementation is critical.

### Maintenance Best Practices
- Review and update project instructions regularly as requirements change.
- Use the changelog to document all major edits and updates.
- Validate Table of Contents links and section anchors after major changes.
- Test Copilot behavior after significant instruction updates and refine as needed.

---
# RAID Shadow Legends Project Instructions (DRAFT v0.7)

> This file is a DRAFT for the unified project instructions, workflows, and templates for champion, boss, mechanic, and team dictionary/guide generation. All edits and section reviews will be staged here before final consolidation and ToC/anchor update.

## Table of Contents (DRAFT)

1. [Project Purpose & Scope](#1-project-purpose--scope)
2. [Continuous Improvement Policy](#2-continuous-improvement-policy)
3. [User Content Priorities & Focus](#3-user-content-priorities--focus)
4. [Authoritative Data Sources](#4-authoritative-data-sources)
5. [Champion Dictionary Entry Workflow](#5-champion-dictionary-entry-workflow)
6. [Boss Guide Entry Workflow](#6-boss-guide-entry-workflow)
7. [Mechanic Entry Workflow](#7-mechanic-entry-workflow)
8. [Team Creation & Analysis Workflow](#8-team-creation--analysis-workflow)
9. [Build Evaluation & Optimization](#9-build-evaluation--optimization)
10. [Guide Update & Versioning Policy](#10-guide-update--versioning-policy)
11. [Validation & Documentation Standards](#11-validation--documentation-standards)
12. [Templates & Examples](#12-templates--examples)
13. [Review Questions & Feedback](#13-review-questions--feedback)
14. [Change Log & Version History](#14-change-log--version-history)


## 1. Project Purpose & Scope
- The goal of this project is to create a comprehensive, automation-ready dictionary of RAID Shadow Legends content, focused on the user's actual owned champions, teams, and mechanics.
- The project supports:
	- Creating JSON dictionary entries for every owned champion, using the canonical process in `Champion_Dictionary_Prompt_template.md`.
	- Creating similar entries for all bosses (with Hard difficulty focus if available), documenting mechanics, stat requirements, and all relevant trials.
	- Adding/updating mechanic entries (buffs, debuffs, passives, unique effects) as needed for indexing and team-building.
	- Enabling automated team creation, mechanic mapping, and testing using champion and mechanic entries.
	- Building teams for each boss and mechanic, including meta, cheese, and hybrid teams, with analysis of damage, gearing, speed tunes, alternates, and ideal pulls (unowned champions).
	- Advising on best team archetypes for each boss/dungeon (e.g., HP Burn, Poison, raw damage, buff spread).
	- Inputting and evaluating actual champion builds/setups for effectiveness in their best use case, recommending upgrades, speed tunes, and new team compositions based on current builds and meta.
	- Generating actionable boss guides and team notes using current builds, with recommendations for improvement.
	- Focusing on maximizing damage (Clan Boss), reliability/clear speed (dungeons/bosses), and Faction Wars progression.
	- Recommending new speed tunes and strategies as the meta evolves, and supporting continuous learning as new content and mechanics are released.

---

## 2. Continuous Improvement Policy

**Continuous Improvement Policy**

Continuous improvement is an active, ongoing process during all project work. The goal is to rapidly identify, test, and implement better ways of working—improving accuracy, automation, and user value as the project evolves. This section defines how to practice continuous improvement in real time:

- **Iterative Workflow Refinement:**
	- Treat every workflow (champion intake, boss guide, team building, etc.) as a living process. After each use, review what worked, what was slow, and what caused errors or confusion.
	- Propose and test small changes immediately—update templates, checklists, or scripts as soon as a better approach is found.

- **Rapid Feedback Loops:**
	- After each major entry, guide, or team is created, review the process and output with the user or team. Capture feedback on clarity, speed, and accuracy.
	- Use feedback to adjust instructions, templates, or validation steps before the next cycle.

- **Learning from Errors:**
	- When mistakes, omissions, or inefficiencies are found (e.g., missed mechanics, validation errors, unclear instructions), document the issue and update the relevant workflow or template immediately.
	- Add troubleshooting notes or new review questions to prevent recurrence.

- **Process Adaptation:**
	- As new content, mechanics, or user needs arise, adapt workflows in real time—do not wait for a formal review cycle.
	- If a new type of entry or validation is needed, create a draft template and test it on the next relevant task.

- **Documentation of Improvements:**
	- Summarize all significant workflow or template changes in the change log (see Section 12).
	- Note the reason for each change (e.g., "Added new validation step after missed mechanic in Hydra guide").

- **Continuous Skill Development:**
	- Stay current with community best practices, new tools, and meta strategies. Integrate new knowledge into project workflows as soon as it is validated.

This approach ensures the project remains efficient, accurate, and responsive to both user needs and game evolution. Continuous improvement is not a separate phase—it is embedded in every step of project work.

---

## 3. User Content Priorities & Focus

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

## 4. Authoritative Data Sources

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


## 5. Champion Dictionary Entry Workflow
### Purpose
Establish a validated, canonical process for creating, updating, and maintaining champion dictionary entries in the RAID Shadow Legends knowledge base. This ensures all champion data is accurate, cross-referenced, and indexable for downstream guide and team generation.

### Canonical Template
- All champion entries must use the canonical template in `input/Champion_Dictionary_Prompt_template.md` (see file for full field list and mechanics tag index; if missing, mark as WIP and stage a placeholder).


### Entry Creation Workflow
Follow the unified standards in Sections 8 (Guide Update & Versioning Policy) and 9 (Validation & Documentation Standards) for all entry creation, validation, documentation, and automation requirements. The canonical process is:
1. **Data Gathering**: Collect and cross-validate champion data from authoritative sources (see Section 3). Document all sources.
2. **Template Population**: Populate all required fields in the canonical template. Use mechanics tags for automation.
3. **Validation**: Validate all data per Section 9. Note conflicts, uncertainties, and data confidence.
4. **Entry Review & Approval**: Present for review, then add to the dictionary. Update index/search tools as needed.

### Update & Maintenance Workflow
Follow the update, versioning, and documentation standards in Section 8 for all changes. Use DRAFT-to-FINAL workflow, versioning, and changelog documentation as described.

### Automation & Indexing
### Cheese/Meta Teams
Add a dedicated section or tag for cheese/meta teams in all team and boss guide entries. Check for boss, champion, or mechanic-specific cheese teams based on owned champions. Reference these in both the main team workflow and a dedicated cheese/meta section.
All entries must be structured for automated parsing and indexing as described in Sections 8 and 9. Use consistent tags and field names.

---

## 6. Boss Guide Entry Workflow

### Purpose
Define a validated, modular process for creating, updating, and maintaining boss guide entries for RAID Shadow Legends. Ensure all guides are actionable, cross-referenced, and optimized for owned champion rosters and current meta.

### Canonical Template
- All boss guides must use the canonical template in `input/Boss_Guide_Template.md` (see file for full section list; if missing, mark as WIP and stage a placeholder).


### Guide Creation Workflow
Follow the unified standards in Sections 8 (Guide Update & Versioning Policy) and 9 (Validation & Documentation Standards) for all guide creation, validation, documentation, and automation requirements. The canonical process is:
1. **Research & Data Gathering**: Review and cross-validate boss data from authoritative sources (see Section 3). Document all sources.
2. **Trial/Mechanic Mapping**: Map all boss trials/mechanics to the owned champion list. Build per-trial and combo tables, noting affinity safety/risk and special notes.
3. **Team Building & Simulation**: Build and simulate 5–8 unique teams using only owned champions, maximizing trial/mechanic completion, damage, and hybrid approaches. For each team, specify all required details and run at least 3 simulations per team (see Section 9 for simulation standards).
4. **Guide Structure & Output**: Use the canonical template and modular ToC. Populate all required sections. Add quick reference tables as needed.
5. **Update & Validation**: After any roster change, re-run all mapping, team building, and simulation steps. Regenerate all tables and recommendations as needed. Use DRAFT-to-FINAL workflow and document all validation steps.

### Update & Maintenance Workflow
Follow the update, versioning, and documentation standards in Section 8 for all changes. Use DRAFT-to-FINAL workflow, versioning, and changelog documentation as described.

### Automation & Indexing
All guides must be structured for automated parsing and indexing as described in Sections 8 and 9. Use consistent tags, anchors, and field names.

---

## 7. Mechanic Entry Workflow

### Purpose
Define a standardized process for documenting, updating, and maintaining mechanic entries (buffs, debuffs, passives, unique effects) in the RAID Shadow Legends knowledge base. Ensure all mechanics are indexable, cross-referenced, and usable for automation and team-building.

### Canonical Template
- All mechanic entries must use the mechanics tag index and field documentation in `input/Champion_Dictionary_Prompt_template.md` (see file for mechanics list and tag details; if missing, mark as WIP and stage a placeholder). If a standalone mechanic template is needed, create and reference it here.


### Entry Creation Workflow
Follow the unified standards in Sections 8 (Guide Update & Versioning Policy) and 9 (Validation & Documentation Standards) for all entry creation, validation, documentation, and automation requirements. The canonical process is:
1. **Data Gathering**: Collect and cross-validate mechanic data from authoritative sources (see Section 3). Document all sources.
2. **Template Population**: Populate all required fields in the canonical template. Link to all affected champions, bosses, and teams. Specify known counters and unique interactions.
3. **Validation**: Validate all data per Section 9. Note conflicts, uncertainties, and data confidence.
4. **Entry Review & Approval**: Present for review, then add to the mechanic dictionary. Update index/search tools as needed.

### Update & Maintenance Workflow
Follow the update, versioning, and documentation standards in Section 8 for all changes. Use DRAFT-to-FINAL workflow, versioning, and changelog documentation as described.

### Automation & Indexing
All entries must be structured for automated parsing and indexing as described in Sections 8 and 9. Use consistent tags and field names.

### Core summary of info to index
- Boss mechanics
- Game mechanic index/dictionary
- interaction guidelines
- Passive mechanics
- Meta interactions and setups
- Hp Burn and Poison and other damage based on Boss or Max HP mechanics 
- 'Cheese' teams and mechanics ex unkillable, revive on death, block damage, poison explosion, etc

---

## 8. Team Creation & Analysis Workflow

### Purpose
Define a systematic, validated process for building, simulating, and analyzing teams for all RAID content (bosses, dungeons, Faction Wars, Arena, etc.), using only owned champions and validated mechanics. Ensure all teams are actionable, optimized, and documented for both manual and auto play.

### Canonical Template
- All team entries must use the standard template in Section 12 (see file for example; if a dedicated team prompt file exists, reference it here; if missing, mark as WIP and stage a placeholder).


### Team Creation Workflow
Follow the unified standards in Sections 8 (Guide Update & Versioning Policy) and 9 (Validation & Documentation Standards) for all team creation, validation, documentation, and automation requirements. The canonical process is:
1. **Team Archetype Selection**: Identify required mechanics/trials for the target content (see boss/mechanic entries). Select team archetypes based on owned champions and content requirements.
2. **Team Building**: Build 5–8 unique teams using only owned champions, maximizing trial/mechanic completion, damage, and hybrid approaches. For each team, specify all required details per the canonical template. Ensure all teams are unique unless cheese/duplicate strategies are explicitly allowed.
3. **Simulation & Validation**: Run at least 3 test runs per team (manual and/or auto as appropriate). If results are highly variable (RNG, new bosses, cheese teams), run up to 5. Rerun simulations if speed tunes or team comps change. Document results per Section 9.
4. **Documentation & Output**: Populate all required fields in the team template. Add quick reference tables and detailed team sections to the relevant boss/guide entry. Link to all referenced champion and mechanic entries.

### Update & Maintenance Workflow
Follow the update, versioning, and documentation standards in Section 8 for all changes. Use DRAFT-to-FINAL workflow, versioning, and changelog documentation as described.

### Automation & Indexing
All teams must be structured for automated parsing and indexing as described in Sections 8 and 9. Use consistent tags and field names.

---

## 9. Build Evaluation & Optimization

### Purpose
Provide a structured workflow for evaluating, optimizing, and documenting actual user champion builds for all RAID content. Ensure feedback is actionable, content-specific, and supports continuous improvement of the owned roster.

### Canonical Template
- All build evaluations must use a standard template specifying: Champion Name, Content Type, Current Build (gear sets, stats, masteries, skill books), Recommended Build (gear sets, stats, masteries, skill books), Gaps/Issues, Upgrade Priorities, and Validation Sources.
- Include a comparison table of current vs. recommended stats and gear.
- Link to relevant champion, team, and boss entries.


### Build Evaluation Workflow
Follow the unified standards in Sections 8 (Guide Update & Versioning Policy) and 9 (Validation & Documentation Standards) for all build evaluation, validation, documentation, and automation requirements. The canonical process is:
1. **Input Collection**: Gather current build details and specify primary content use.
2. **Comparison & Analysis**: Compare current build to recommended build for the target content. Identify gaps and note if the build is optimal, suboptimal, or misaligned.
3. **Upgrade & Optimization Advice**: Prioritize upgrades and suggest changes as needed. Recommend respec if appropriate.
4. **Documentation & Output**: Populate all required fields in the build evaluation template. Add actionable notes and upgrade path to the relevant champion/team entry. Link to referenced guides and validation sources.

### Update & Maintenance Workflow
Follow the update, versioning, and documentation standards in Section 8 for all changes. Use DRAFT-to-FINAL workflow, versioning, and changelog documentation as described.

### Automation & Indexing
All evaluations must be structured for automated parsing and indexing as described in Sections 8 and 9. Use consistent tags and field names.

---

## 10. Guide Update & Versioning Policy

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
- Rely on git for version history and rollback; an Archive/ folder is not required but may be used optionally.
**Review Frequency:** Continuous improvement should be reviewed every hour when working on the project. Create tasks for improvements as they arise. Formal review cycles (monthly/quarterly) are not required unless desired.
- Update indexes and references after each major update.

### Validation & Documentation Standards
- All updates must be validated with at least two authoritative sources.
- Document all validation steps, sources, and simulation results in the entry or commit message.
- Note any uncertainties, conflicts, or assumptions in a dedicated section.

### Automation & Indexing
- Updates must be structured for automated detection and indexing (e.g., by filename pattern or metadata tag).
- Update all relevant indexes and cross-references after each update.

---

## 11. Validation & Documentation Standards

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

## 12. Templates & Examples

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

## 13. Review Questions & Feedback

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


## 15. Housekeeping, Shift-Left, and Proactive Maintenance

### Purpose
Establish best practices for keeping the project clean, up-to-date, and continuously improving, with a focus on early error detection, automation, and reducing technical debt.

### Housekeeping Guidelines
- Regularly archive or remove obsolete files, prompts, and templates (rely on git for version history).
- Keep the workspace organized: maintain clear folder structures, consistent naming, and up-to-date indexes.
- Remove or refactor deprecated scripts, workflows, or mechanics as soon as they are replaced.
- Document all major changes in the changelog and commit messages.
- Review and update the Table of Contents and section anchors after major edits.

### Shift-Left Principles
- Validate data, templates, and automation outputs as early as possible in the workflow.
- Run validation, simulation, and linting scripts before merging or promoting any FINAL file.
- Encourage early peer review and feedback on new workflows, templates, and automation scripts.
- Integrate new validation or automation tools as soon as they are available.

### Proactive Maintenance
- Schedule regular (hourly when working) reviews of instructions, templates, and automation scripts for improvement opportunities.
- Create and track housekeeping or improvement tasks as soon as issues are identified.
- Update validation, simulation, and automation standards as the meta or project needs evolve.
- Ensure all new content, mechanics, or workflows are indexed and cross-referenced immediately.

### Automation & Continuous Improvement
- Use automation for repetitive housekeeping tasks (e.g., index updates, validation runs, changelog generation).
- Document and share new automation scripts or tools with the team.
- Encourage a culture of continuous improvement and early error detection (shift-left mindset).

---

### Purpose
Maintain a clear, chronological record of all major changes, updates, and version history for the project instructions, templates, and workflows. This ensures transparency, traceability, and supports collaborative development.

### Change Log Format
- Date (YYYY-MM-DD)
- Author
- Description of change (what was added, removed, or updated)
- Affected sections/files

### Example Change Log
| Date       | Author           | Description                                      | Sections/Files                |
|------------|------------------|--------------------------------------------------|-------------------------------|
| 2025-10-21 | GitHub Copilot   | Initial draft complete through Section 12         | All sections                  |
| 2025-10-21 | Selicos          | Updated champion template to JSON, unified refs   | Champion_Dictionary_Template  |
| 2025-10-21 | GitHub Copilot   | Added Embrys mythic JSON intake example           | Embrys_the_Anomaly.json       |

### Versioning Policy
- Increment version number or add date-stamped entry for each major update.
- Archive previous versions as needed for rollback and comparison.
- Summarize key changes at the top of the file for quick reference.

---

