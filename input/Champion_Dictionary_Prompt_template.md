
# RAID Champion Dictionary & Mechanics Index - Prompt & Template Reference
#
# Project Instructions & Champion Entry Template
#
# This file is the anchor for all champion data, mechanics, and synergy reviews. **All champion entries must use the canonical JSON template file as the single source of truth.**
#
## Champion Entry Template (Reference Only)
---
**IMPORTANT:**
- All champion entries must use the canonical template in `input/Champion_Dictionary_Template.json`.
- Do NOT copy or maintain a separate template structure here. The JSON template file is the only version to reference and use for all champion entries.
- If the template changes, update only `Champion_Dictionary_Template.json` and notify in chat.

**Output Directory:**
- All champion entries should be saved in the `Champion Dictionary` directory.

**Data Format:**
- Champion entries are stored in JSON for lookup and automation.

**Standardized Mechanics & Tagging:**
- All mechanics, buffs, debuffs, and status effects must use the standardized tags listed in the "Standardized Mechanics Tag List" section below.
- Only use tags from this list for all champion entries. If a new mechanic is needed, add it to the list first.

---


  ## Standardized Mechanics Tag List

  **Buffs:**
  - Increase ATK
  - Increase DEF
  - Increase SPD
  - Increase C.RATE
  - Increase C.DMG
  - Block Debuffs
  - Block Damage
  - Counterattack
  - Ally Protection
  - Shield
  - Strengthen
  - Reflect Damage
  - Continuous Heal
  - Unkillable
  - Revive on Death
  - Veil
  - Perfect Veil
  - Increase ACC
  - Increase RES
  - Extend Buffs
  - Extra Turn
  - Increase Ally SPD in [Area]
  - Stoneskin
  - Taunt Immunity
  - Debuff Spread
  - Debuff Extension
  - Buff Spread
  - Buff Extension
  - Debuff Transfer Immunity
  - Buff Transfer Immunity
  - Immortality
  - Life Barrier
  - Block Revive
  - Block Skill Reduction
  - Block Skill Increase
  - Block Turn Meter Reduction
  - Block Turn Meter Increase
  - Block Healing
  - Block Damage Reflection
  - Block Passive Activation
  - Block Passive Suppression
  - Block Skill Suppression
  - Block Skill Activation
  - Block Skill Steal
  - Block Skill Copy
  - Block Skill Reset
  - Block Skill Cooldown Increase
  - Block Skill Cooldown Reduction
  - Block Skill Transfer
  - Block Skill Reflection
  - Block Skill Immunity
  - Block Skill Absorption
  - Block Skill Conversion
  - Block Skill Inversion
  - Block Skill Amplification
  - Block Skill Diminish
  - Block Skill Nullify
  - Block Skill Delay
  - Block Skill Acceleration
  - Block Skill Deceleration
  - Block Skill Overload
  - Block Skill Underload
  - Block Skill Chain
  - Block Skill Break
  - Block Skill Link
  - Block Skill Unlink
  - Block Skill Merge
  - Block Skill Split
  - Block Skill Summon
  - Block Skill Desummon
  - Block Skill Morph
  - Block Skill Demorph
  - Block Skill Evolve
  - Block Skill Devolve
  - Block Skill Upgrade
  - Block Skill Downgrade
  - Block Skill Empower
  - Block Skill Disempower
  - Block Skill Enhance
  - Block Skill Weaken
  - Block Skill Strengthen
  - Block Skill Fortify
  - Block Skill Shatter
  - Block Skill Repair
  - Block Skill Corrupt
  - Block Skill Purify
  - Block Skill Bless
  - Block Skill Curse
  - Block Skill Mark
  - Block Skill Unmark
  - Block Skill Tag
  - Block Skill Untag
  - Block Skill Flag
  - Block Skill Unflag
  - Block Skill Signal

  **Debuffs:**
  - Decrease ATK
  - Decrease DEF
  - Decrease SPD
  - Decrease C.RATE
  - Decrease ACC
  - Weaken
  - Poison
  - Poison Sensitivity
  - HP Burn
  - Freeze
  - Stun
  - Sleep
  - Provoke
  - Fear
  - True Fear
  - Block Buffs
  - Block Active Skills
  - Block Passive Skills
  - Heal Reduction
  - Bomb
  - Decrease MAX HP
  - Leech
  - Hex
  - Decrease RES
  - Decrease C.DMG
  - Taunt
  - Debuff Spread
  - Debuff Extension
  - Debuff Transfer
  - Debuff Steal
  - Debuff Removal
  - Unhealable
  - Marked
  - Cursed
  - Corrupted
  - Shattered
  - Fortified
  - Diminished
  - Nullified
  - Suppressed
  - Silenced
  - Sealed
  - Immobilized
  - Disarmed
  - Disrupted
  - Delayed
  - Slowed
  - Weakened
  - Broken
  - Linked
  - Unlinked
  - Merged
  - Split
  - Summoned
  - Desummoned
  - Morphed
  - Demorphed
  - Evolved
  - Devolved
  - Upgraded
  - Downgraded
  - Empowered
  - Disempowered
  - Enhanced
  - Purified
  - Repaired

  **Status/Other:**
  - Turn Meter Boost
  - Turn Meter Reduction
  - Revive
  - Heal
  - Remove Debuffs
  - Remove Buffs
  - Steal Buffs
  - Transfer Debuffs
  - Place Debuffs
  - Place Buffs
  - Reset Cooldowns
  - Increase Cooldowns
  - Decrease Cooldowns
  - Ignore DEF
  - Ignore Unkillable
  - Ignore Block Damage
  - Extra Hit
  - Multi-hit
  - AoE Attack
  - Single Target Attack
  - Ally Join Attack
  - Ally Attack
  - Passive Damage
  - Passive Heal
  - Damage Mitigation
  - Damage Reflection
  - Stat Swap
  - Stat Steal
  - Stat Copy
  - Skill Suppression
  - Skill Activation
  - Skill Disable
  - Skill Copy
  - Skill Steal
  - Skill Extension
  - Skill Reduction
  - Skill Reset
  - Skill Cooldown Increase
  - Skill Cooldown Reduction
  - Skill Block
  - Skill Unblock
  - Skill Transfer
  - Skill Reflection
  - Skill Immunity
  - Skill Absorption
  - Skill Conversion
  - Skill Inversion
  - Skill Amplification
  - Skill Diminish
  - Skill Nullify
  - Skill Delay
  - Skill Acceleration
  - Skill Deceleration
  - Skill Overload
  - Skill Underload
  - Skill Chain
  - Skill Break
  - Skill Link
  - Skill Unlink
  - Skill Merge
  - Skill Split
  - Skill Summon
  - Skill Desummon
  - Skill Morph
  - Skill Demorph
  - Skill Evolve
  - Skill Devolve
  - Skill Upgrade
  - Skill Downgrade
  - Skill Empower
  - Skill Disempower
  - Skill Enhance
  - Skill Weaken
  - Skill Strengthen
  - Skill Fortify
  - Skill Shatter
  - Skill Repair
  - Skill Corrupt
  - Skill Purify
  - Skill Bless
  - Skill Curse
  - Skill Mark
  - Skill Unmark
  - Skill Tag
  - Skill Untag
  - Skill Flag
  - Skill Unflag
  - Skill Signal
  - Skill Uns
  - Aura
  - Unique Passive
  - Conditional Effect
  - Random Effect
  - Chance-Based Effect
  - Guaranteed Effect
  - Scaling Effect
  - Stat-Based Effect
  - Turn-Based Effect
  - Cooldown-Based Effect
  - Area-Based Effect
  - Target-Based Effect
  - Self-Target
  - Ally-Target
  - Enemy-Target
  - All-Enemy-Target
  - All-Ally-Target
  - Wave-Based Effect
  - Boss-Specific Effect
  - PVE-Only Effect
  - PVP-Only Effect

  ---

  All entries must be:
  - Standardized, chat-readable, and easily searchable
  - All forms/alternate kits for mythics must be included in one entry
  - Every skill must be tagged with specific mechanics (see reference list below)
  - Team table/automation is deferred until all champion data is complete

  **Update Workflow:**
  - Always update this template before adding new champion entries
  - Use meta ratings as the starting point for all new entries
  - Add new mechanics to the tagging list as needed (every buff, debuff, status, etc. must be indexible)
  - For quick updates, edit this template directly and notify in chat
  - When creating json entries:
    1. Intake a champion name and a screenshot of their base stats
    2. Identify and pull in their skills and other character info needed to complete the template.
    3. Generate the json file with validated info. 
    4. Confirm, then prep to loop back to 1.
    - this should be a one chat/prompt cycle. Provide champion name and states, create json and confirm, repeat.

  ---


  ## Champion Entry Template


  ### [Champion Name] (Plarium champion_id, Rarity, Affinity, Faction)

  #### Meta Ratings
  - Clan Boss: X/10
  - Dungeons: X/10
  - Doom Tower: X/10
  - Arena: X/10
  - Faction Wars: X/10

  #### Forms/Alternate Kits
  - [List all forms, e.g., Base, Empowered, Alternate Skillset]



**Validation Requirement:**
- All champion data must be validated from at least 2 authoritative sources (e.g., Ayumilove, HellHades, RaidHQ, in-game) before generating the champion file.
- Each champion gets a new file generated before presenting in chat for review.

  #### Stats
  - HP: [Value]
  - ATK: [Value]
  - DEF: [Value]
  - SPD: [Value]
  - C.RATE: [Value]
  - C.DMG: [Value]
  - RES: [Value]
  - ACC: [Value]

  #### Skills
  - **A1:** [Skill Name] - [Description] (Cooldown: X turns)
    - Mechanics Tags: [List all that apply]
  - **A2:** [Skill Name] - [Description] (Cooldown: X turns)
    - Mechanics Tags: [List all that apply]
  - **A3:** [Skill Name] - [Description] (Cooldown: X turns)
    - Mechanics Tags: [List all that apply]
  - **Passive:** [Skill Name] - [Description]
    - Mechanics Tags: [List all that apply]
  - **Aura:** [Description]
    - Mechanics Tags: [List all that apply]

  #### Mechanics Tagging (Indexable)
  - [List all mechanics for this champion, one per line, using the reference list below.]

  #### Gear & Mastery Recommendations
  - [Recommended sets, stats, and masteries]


  #### AI Quirks & Auto Warnings (Standardized)
  - Bad AI: [true/false]
  - AI Issue Description: [Describe problematic skill priority, targeting, or auto-play behavior]


  #### Cheese Strategy
  - Cheese Viable: [true/false]
  - Cheese Type: [e.g., unkillable, max HP, passive sustain, etc.]
  - Cheese Mechanic Info: [If true, describe the cheese mechanic and requirements]

  #### Mechanics Advisory
  - [Notes on unique mechanics, synergy, or special use cases]


  #### Citations
  - [List all sources used, with URLs and access time/date, e.g., "Ayumilove: https://ayumilove.net/raid-shadow-legends-coldheart/ (accessed 2025-10-20)"]


  #### Update & Review Notes
  - Last Updated: [Date]
  - Last Patch: [Patch version/date and summary of change]
  - Author: [Name]
  - Summary of changes

  #### Notes & Comments
  - [Freeform notes, edge cases, user/community feedback]

  ---

  ## Mechanics Tagging Reference (Expand as Needed)

  **Buffs:**
  - Increase ATK
  - Increase DEF
  - Increase SPD
  - Increase C.RATE
  - Increase C.DMG
  - Block Debuffs
  - Block Damage
  - Counterattack
  - Ally Protection
  - Shield
  - Strengthen
  - Reflect Damage
  - Continuous Heal
  - Unkillable
  - Revive on Death
  - Veil
  - Perfect Veil
  - Increase ACC
  - Increase RES
  - Extend Buffs
  - Extra Turn
  - Increase Ally SPD in [Area]
  - Stoneskin
  - Taunt Immunity
  - Debuff Spread
  - Debuff Extension
  - Buff Spread
  - Buff Extension
  - Debuff Transfer Immunity
  - Buff Transfer Immunity

  **Debuffs:**
  - Decrease ATK
  - Decrease DEF
  - Decrease SPD
  - Decrease C.RATE
  - Decrease ACC
  - Weaken
  - Poison
  - Poison Sensitivity
  - HP Burn
  - Freeze
  - Stun
  - Sleep
  - Provoke
  - Fear
  - True Fear
  - Block Buffs
  - Block Active Skills
  - Block Passive Skills
  - Heal Reduction
  - Bomb
  - Decrease MAX HP
  - Leech
  - Hex
  - Decrease RES
  - Decrease C.DMG
  - Taunt
  - Debuff Spread
  - Debuff Extension
  - Debuff Transfer
  - Debuff Steal
  - Debuff Removal

  **Status/Other:**
  - Turn Meter Boost
  - Turn Meter Reduction
  - Revive
  - Heal
  - Remove Debuffs
  - Remove Buffs
  - Steal Buffs
  - Transfer Debuffs
  - Place Debuffs
  - Place Buffs
  - Reset Cooldowns
  - Increase Cooldowns
  - Decrease Cooldowns
  - Ignore DEF
  - Ignore Unkillable
  - Ignore Block Damage
  - Extra Hit
  - Multi-hit
  - AoE Attack
  - Single Target Attack
  - Ally Join Attack
  - Ally Attack
  - Passive Damage
  - Passive Heal
  - Damage Mitigation
  - Damage Reflection
  - Stat Swap
  - Stat Steal
  - Stat Copy
  - Skill Suppression
  - Skill Activation
  - Skill Disable
  - Skill Copy
  - Skill Steal
  - Skill Extension
  - Skill Reduction
  - Skill Reset
  - Skill Cooldown Increase
  - Skill Cooldown Reduction
  - Skill Block
  - Skill Unblock
  - Skill Transfer
  - Skill Reflection
  - Skill Immunity
  - Skill Absorption
  - Skill Conversion
  - Skill Inversion
  - Skill Amplification
  - Skill Diminish
  - Skill Nullify
  - Skill Delay
  - Skill Acceleration
  - Skill Deceleration
  - Skill Overload
  - Skill Underload
  - Skill Chain
  - Skill Break
  - Skill Link
  - Skill Unlink
  - Skill Merge
  - Skill Split
  - Skill Summon
  - Skill Desummon
  - Skill Morph
  - Skill Demorph
  - Skill Evolve
  - Skill Devolve
  - Skill Upgrade
  - Skill Downgrade
  - Skill Empower
  - Skill Disempower
  - Skill Enhance
  - Skill Weaken
  - Skill Strengthen
  - Skill Fortify
  - Skill Shatter
  - Skill Repair
  - Skill Corrupt
  - Skill Purify
  - Skill Bless
  - Skill Curse
  - Skill Mark
  - Skill Unmark
  - Skill Tag
  - Skill Untag
  - Skill Flag
  - Skill Unflag
  - Skill Signal
  - Skill Uns

  **(Add new mechanics as needed. Every buff, debuff, status, and effect must be indexible for future automation.)**

  ---

  ## User Review Questions

  1. Are all mechanics for this champion listed and tagged under the main entry?
  2. Are meta ratings present and up to date?
  3. Are all forms/alternate kits included?
  4. Are gear/mastery recommendations current?
  5. Is the mechanics tagging list complete and indexible?
  6. Is the entry standardized and chat-readable?
  7. Are update & review notes present?

  ---

  ## Quick Update Workflow

  1. Edit this template directly for any changes to structure, tagging, or instructions.
  2. Notify in chat when the template is updated.
  3. Use the latest template for all new champion entries.
  4. Add new mechanics to the tagging reference as needed (every buff, debuff, status, etc. must be indexible).
  5. Confirm with user before populating champion entries.
