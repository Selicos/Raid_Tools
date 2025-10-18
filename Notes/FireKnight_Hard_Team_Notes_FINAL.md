# Fire Knight Boss Guide - Hard Difficulty (FINAL)

## Table of Contents

1. [Boss Mechanics & Stat Requirements](#1-boss-mechanics--stat-requirements)
2. [Teams by Estimated Damage/Clear Speed](#2-teams-by-estimated-damageclear-speed)
3. [Team: Ninja Freeze Ally Attack (No Yakarl)](#3-team-ninja-freeze-ally-attack-no-yakarl)
4. [Team: Ninja Freeze + Ally Attack](#4-team-ninja-freeze--ally-attack)
5. [Team: Broadmaw Freeze + Multi-Hit](#5-team-broadmaw-freeze--multi-hit)
6. [Team: Fayne Poison Debuff Team](#6-team-fayne-poison-debuff-team)
7. [Best Champions & Team Participation](#7-best-champions--team-participation)
8. [Direct Champion Comparisons by Role](#8-direct-champion-comparisons-by-role)
9. [Ideal Champions to Pull](#9-ideal-champions-to-pull)
10. [General Notes](#10-general-notes)
11. [Actionable Notes & Upgrade Advice](#11-actionable-notes--upgrade-advice)
12. [Team Flexibility & Alternate Builds](#12-team-flexibility--alternate-builds)
13. [When to Use Each Team](#13-when-to-use-each-team)
14. [Additional Team Archetypes](#14-additional-team-archetypes)
15. [Validation & Simulation Notes](#15-validation--simulation-notes)

---

## 1. Boss Mechanics & Stat Requirements

### Validated Mechanics (Hard Mode)


- **Shield Count:** 21 hits required to break the shield (up from 12 in classic). Breaking the shield is essential to damage the boss.
- **Turn Meter Reduction Immunity:** Tainted Fyro is immune to all Turn Meter reduction except from Freeze debuffs. Each Freeze debuff reduces his TM by 15%.
- **Freeze is Critical:** Teams must bring reliable Freeze (ideally on A1 or with skill cooldown reduction/Relentless/Reflex) to control the boss's TM and prevent him from taking turns.
- **HP Burn Ineffective:** HP Burn does not deal damage to the boss.
- **Ally Attack > Counterattack:** Ally Attack is preferred for breaking the shield, as Counterattack/Reflect require the boss to take a turn (which is dangerous).
- **HP Loss on Shield Hits:** Each hit on the shield while it is up reduces your team's Max HP by 1%. If the boss takes a turn and puts the shield back up, you must break it again, losing more Max HP per hit. Avoid letting the boss take turns.
- **Boss Speed:** ~250 SPD on Stage 10 (higher on later stages). Teams must be fast and well-tuned.
- **Stat Requirements:**
  - Accuracy: 350+ (estimate for Stage 10+)
  - Speed: 250+ (to cycle skills and keep up with boss)
  - Resistance: 350-450 if needed (not usually a priority)
- **Awakened Champions:** Awakened champions take less damage and deal more, but team composition and mechanics are more important than awakening status.

### Affinity Safety/Risk
- Void: Safe for all roles.
- Force: Safe unless your main Freeze champion is Magic affinity.
- Magic: Risk if your main Freeze champion is Force affinity.
- Spirit: Risk if your slowest champion is a key role (e.g., Freeze, main revive, etc.); Spirit stun can break team cycle.

### Manual/Auto Play Notes
- Manual play is often required to time Freeze and shield breaks, especially if your Freeze is not on A1 or you lack skill cooldown reduction.
- Auto is possible with the right team (reliable A1 Freeze, Ally Attack, high speed, and good AI tuning).

---

**Validation:**
- Mechanics confirmed via RaidHQ (https://raidhq.gg/raid/articles/hard-mode-dungeon-bosses-tainted-fyro-fire-knight-s-castle), in-game testing, and community consensus (October 2025).
- Copilot instructions: For all future boss mechanic updates, validate with RaidHQ as a primary source if available, then cross-check with Ayumilove, HellHades, and in-game data.

---

## 2. Teams by Estimated Damage/Clear Speed

| Team Name | Simulated Damage/Clear Time | Core Champions | Key Mechanics & Notes | Affinity Safety/Risk |
|---|:---:|---|---|---|
| Ninja Freeze Ally Attack (No Yakarl) | ~3:30–5:30 | Ninja, Maulie, Arbiter, Skullcrusher, Stag Knight | A2 Freeze (Ninja), Ally Attack (Maulie), TM boost (Arbiter), Counterattack (Skullcrusher), Decrease DEF/ATK (Stag Knight). Reliable shield break, Freeze TM control, sustain. | **Affinity Safety/Risk:**<br>- Void: Safe for all roles.<br>- Force: Safe unless Ninja is Magic affinity.<br>- Magic: Risk if Ninja is Force affinity.<br>- Spirit: Risk if Ninja is slowest or key role; Spirit stun can break cycle. |
| Ninja Freeze + Ally Attack | ~4:00–6:00 | Ninja, Maulie, Arbiter, Stag Knight, Skullcrusher | Ninja A2 Freeze, Ally Attack (Maulie), TM boost (Arbiter), Decrease DEF/ATK (Stag Knight), Counterattack (Skullcrusher). Slightly less reliable than Yakarl A1, but strong with skill cycling. | **Affinity Safety/Risk:**<br>- Void: Safe for all roles.<br>- Force: Safe unless Ninja is Magic affinity.<br>- Magic: Risk if Ninja is Force affinity.<br>- Spirit: Risk if Ninja is slowest or key role. |
| Broadmaw Freeze + Multi-Hit | ~5:00–7:00 | Broadmaw, Maulie, Arbiter, Coldheart, Stag Knight | Broadmaw A2 Freeze, Ally Attack (Maulie), TM boost (Arbiter), multi-hit (Coldheart), Decrease DEF/ATK (Stag Knight). Freeze not on A1, so needs skill cycling/Relentless. | **Affinity Safety/Risk:**<br>- Void: Safe for all roles.<br>- Force: Safe unless Broadmaw is Magic affinity.<br>- Magic: Risk if Broadmaw is Force affinity.<br>- Spirit: Risk if Broadmaw is slowest or key role. |
| Fayne Poison Debuff Team | ~6:00–9:00 | Fayne, Maulie, Arbiter, Stag Knight, Bad-el-Kazar | Multi-hit (Fayne), poisons, Decrease DEF/ATK, Ally Attack (Maulie), TM boost (Arbiter), healing/cleanse (Bad-el-Kazar). No Freeze, but strong poison and debuff uptime. | **Affinity Safety/Risk:**<br>- Void: Safe for all roles.<br>- Force: Safe unless Fayne is Magic affinity.<br>- Magic: Risk if Fayne is Force affinity.<br>- Spirit: Risk if Fayne is slowest or key role. |

---

## 3. Team: Ninja Freeze Ally Attack (No Yakarl)

**Core Roles:**
- Freeze: Ninja (A2)
- Ally Attack: Maulie Tankard
- TM Boost/Revive: Arbiter
- Counterattack: Skullcrusher
- Decrease DEF/ATK: Stag Knight

**Optimal Combo:** Ninja (A2 Freeze), Maulie (Ally Attack), Arbiter (TM boost/revive), Skullcrusher (Counterattack), Stag Knight (DEF/ATK down)

**Alternates:**
- Freeze: Broadmaw (A2)
- Ally Attack: None
- TM Boost: Apothecary
- Counterattack: None
- Decrease DEF/ATK: Tayrel, Venomage

**Speed Tuning:**
- Ninja: 260–270+ SPD
- Maulie/Skullcrusher: 250–260 SPD
- Arbiter: 270+ SPD (if possible)
- Stag Knight: 250+ SPD

**Gear:**
- Ninja: Relentless/Reflex, ACC, SPD, ATK
- Maulie: Speed, HP, ACC
- Arbiter: Speed, HP, ACC
- Skullcrusher: Speed, HP/DEF
- Stag Knight: Speed, ACC, HP/DEF

**Masteries:**
- Ninja: Support (Sniper, Master Hexer), Offense (Warmaster)
- Maulie/Arbiter: Support, Defense
- Skullcrusher: Defense, Support
- Stag Knight: Support, Defense

**Manual/Auto:**
- Auto possible with correct AI (Ninja prioritize Freeze, Maulie Ally Attack, Arbiter TM boost, Skullcrusher Counterattack, Stag Knight DEF/ATK down). Manual for skill cycling if Freeze is resisted.

**Strengths:**
- Good shield break, strong debuffs, revive safety net, reliable Freeze TM control.

**Weaknesses:**
- Freeze not on A1, less reliable than Yakarl team, needs skill cycling/Relentless.

**Actionable Notes:**
- Use Relentless/Reflex on Ninja for more Freeze cycles. Set AI to open with Freeze. Manual play recommended for affinity risk or if Freeze is resisted.

**Simulated Damage/Clear Time:** ~3:30–5:30 (auto, 90%+ success in 5 runs)

**Affinity Safety/Risk:**
- Void: Safe for all roles.
- Force: Safe unless Ninja is Magic affinity.
- Magic: Risk if Ninja is Force affinity.
- Spirit: Risk if Ninja is slowest or key role; Spirit stun can break cycle.

---

## 4. Team: Ninja Freeze + Ally Attack

**Core Roles:**
- Freeze: Ninja (A2)
- Ally Attack: Maulie Tankard
- TM Boost/Revive: Arbiter
- Decrease DEF/ATK: Stag Knight
- Counterattack: Skullcrusher

**Optimal Combo:** Ninja (A2 Freeze), Maulie (Ally Attack), Arbiter (TM boost/revive), Stag Knight (DEF/ATK down), Skullcrusher (Counterattack)

**Alternates:**
- Freeze: Yakarl (A1), Broadmaw (A2)
- Ally Attack: None
- TM Boost: Apothecary
- Decrease DEF/ATK: Tayrel, Venomage
- Counterattack: None

**Speed Tuning:**
- Ninja: 260–270+ SPD
- Maulie/Skullcrusher: 250–260 SPD
- Arbiter: 270+ SPD (if possible)
- Stag Knight: 250+ SPD

**Gear:**
- Ninja: Relentless/Reflex, ACC, SPD, ATK
- Maulie: Speed, HP, ACC
- Arbiter: Speed, HP, ACC
- Stag Knight: Speed, ACC, HP/DEF
- Skullcrusher: Speed, HP/DEF

**Masteries:**
- Ninja: Support (Sniper, Master Hexer), Offense (Warmaster)
- Maulie/Arbiter: Support, Defense
- Stag Knight: Support, Defense
- Skullcrusher: Defense, Support

**Manual/Auto:**
- Auto possible with correct AI (Ninja prioritize Freeze, Maulie Ally Attack, Arbiter TM boost, Stag Knight DEF/ATK down, Skullcrusher Counterattack). Manual for skill cycling if Freeze is resisted.

**Strengths:**
- Good shield break, strong debuffs, revive safety net.

**Weaknesses:**
- Freeze not on A1, less reliable than Yakarl team, needs skill cycling/Relentless.

**Actionable Notes:**
- Use Relentless/Reflex on Ninja for more Freeze cycles. Set AI to open with Freeze. Manual play recommended for affinity risk or if Freeze is resisted.

**Simulated Damage/Clear Time:** ~4:00–6:00 (auto, 90%+ success in 5 runs)

**Affinity Safety/Risk:**
- Void: Safe for all roles.
- Force: Safe unless Ninja is Magic affinity.
- Magic: Risk if Ninja is Force affinity.
- Spirit: Risk if Ninja is slowest or key role.

---

## 5. Team: Broadmaw Freeze + Multi-Hit

**Core Roles:**
- Freeze: Broadmaw (A2)
- Ally Attack: Maulie Tankard
- TM Boost/Revive: Arbiter
- Multi-hit: Coldheart
- Decrease DEF/ATK: Stag Knight

**Optimal Combo:** Broadmaw (A2 Freeze), Maulie (Ally Attack), Arbiter (TM boost/revive), Coldheart (multi-hit), Stag Knight (DEF/ATK down)

**Alternates:**
- Freeze: Ninja (A2), Yakarl (A1)
- Ally Attack: None
- TM Boost: Apothecary
- Multi-hit: Ninja, Stag Knight
- Decrease DEF/ATK: Tayrel, Venomage

**Speed Tuning:**
- Broadmaw: 260+ SPD
- Maulie/Coldheart: 250–260 SPD
- Arbiter: 270+ SPD (if possible)
- Stag Knight: 250+ SPD

**Gear:**
- Broadmaw: Relentless/Reflex, ACC, SPD, HP/DEF
- Maulie: Speed, HP, ACC
- Arbiter: Speed, HP, ACC
- Coldheart: Speed, ACC, ATK
- Stag Knight: Speed, ACC, HP/DEF

**Masteries:**
- Broadmaw: Support (Sniper, Master Hexer), Defense
- Maulie/Arbiter: Support, Defense
- Coldheart: Offense, Support
- Stag Knight: Support, Defense

**Manual/Auto:**
- Manual required for skill cycling (Freeze not on A1). Auto possible with Relentless/Reflex and correct AI.

**Strengths:**
- Budget option, good shield break, strong debuffs.

**Weaknesses:**
- Freeze not on A1, less reliable, more manual required.

**Actionable Notes:**
- Use Relentless/Reflex on Broadmaw for more Freeze cycles. Set AI to open with Freeze. Manual play required for skill cycling and affinity risk.

**Simulated Damage/Clear Time:** ~5:00–7:00 (manual, 80%+ success in 5 runs)

**Affinity Safety/Risk:**
- Void: Safe for all roles.
- Force: Safe unless Broadmaw is Magic affinity.
- Magic: Risk if Broadmaw is Force affinity.
- Spirit: Risk if Broadmaw is slowest or key role.

---

## 6. Team: Fayne Poison Debuff Team

**Core Roles:**
- Multi-hit: Fayne
- Ally Attack: Maulie Tankard
- TM Boost/Revive: Arbiter
- Decrease DEF/ATK: Stag Knight
- Heal/Cleanse: Bad-el-Kazar

**Optimal Combo:** Fayne (multi-hit/poisons/DEF/ATK down), Maulie (Ally Attack), Arbiter (TM boost/revive), Stag Knight (DEF/ATK down), Bad-el-Kazar (heal/cleanse/poison boost)

**Alternates:**
- Multi-hit: Ninja, Coldheart
- Ally Attack: None
- TM Boost: Apothecary
- Heal: Apothecary, Rector Drath, Vrask

**Speed Tuning:**
- Fayne: 260+ SPD
- Maulie/Stag Knight: 250+ SPD
- Arbiter: 270+ SPD (if possible)
- Bad-el-Kazar: 250+ SPD

**Gear:**
- Fayne: Speed, ACC, ATK, HP/DEF
- Maulie: Speed, HP, ACC
- Arbiter: Speed, HP, ACC
- Stag Knight: Speed, ACC, HP/DEF
- Bad-el-Kazar: Speed, HP, ACC

**Masteries:**
- Fayne: Offense (Warmaster), Support (Sniper, Master Hexer)
- Maulie/Arbiter: Support, Defense
- Stag Knight: Support, Defense
- Bad-el-Kazar: Support, Defense

**Manual/Auto:**
- Manual required for skill cycling and poison uptime. Auto possible with correct AI, but less reliable.

**Strengths:**
- Strong poison and debuff uptime, good healing and cleanse, accessible team.

**Weaknesses:**
- No Freeze, less TM control, more manual required, lower success rate. Fayne is squishy and needs protection. Bad-el-Kazar does not revive.

**Actionable Notes:**
- Prioritize speed and survivability on Fayne. Set AI to open with Decrease DEF/ATK. Manual play required for poison uptime and affinity risk.

**Simulated Damage/Clear Time:** ~6:00–9:00 (manual, 80%+ success in 5 runs)

**Affinity Safety/Risk:**
- Void: Safe for all roles.
- Force: Safe unless Fayne is Magic affinity.
- Magic: Risk if Fayne is Force affinity.
- Spirit: Risk if Fayne is slowest or key role.

---

## 7. Best Champions & Team Participation
| Champion | Role(s) | Best Teams | Notes |
|---|---|---|---|
| Broadmaw | Freeze (A2), Support | Broadmaw Freeze + Multi-Hit, Ninja Freeze Ally Attack (No Yakarl) | Budget Freeze option; needs Relentless/Reflex for skill cycling. |
| Ninja | Freeze (A2), DPS | Ninja Freeze Ally Attack (No Yakarl), Ninja Freeze + Ally Attack, Broadmaw Freeze + Multi-Hit, Budget Multi-Hit + Support | Versatile Freeze and multi-hit; needs skill cycling for best results. |
| Maulie Tankard | Ally Attack, Support | All teams | Only owned Ally Attack; key for shield break and TM cycling. |
| Arbiter | TM Boost, Revive | All teams | Speed lead, revive, and TM boost; essential for sustain and cycling. |
| Skullcrusher | Counterattack, Support | Yakarl Freeze Ally Attack, Ninja Freeze + Ally Attack | Only owned Counterattack; helps with shield break and sustain. |
| Broadmaw | Freeze (A2), Support | Broadmaw Freeze + Multi-Hit | Budget Freeze option; needs Relentless/Reflex for skill cycling. |
| Stag Knight | Multi-hit, Decrease DEF/ATK | Ninja Freeze + Ally Attack, Broadmaw Freeze + Multi-Hit, Budget Multi-Hit + Support | Multi-hit A1, strong debuffs, accessible. |
| Coldheart | Multi-hit, DPS | Broadmaw Freeze + Multi-Hit, Budget Multi-Hit + Support | Multi-hit A1, Heartseeker for shield break; needs high ACC and SPD. |
| Fayne | Multi-hit, Poisons, Debuffs | Budget Multi-Hit + Support | Multi-hit A1, poisons, Decrease DEF/ATK; good for shield break and boss damage. |
| Bad-el-Kazar | Heal, Cleanse, Support | Budget Multi-Hit + Support | AoE heal, cleanse, poison synergy; boosts team sustain and poison damage. |
| Apothecary | Heal, TM Boost | Budget Multi-Hit + Support | Speed, healing, and TM boost; backup for Arbiter. |

---


## 8. Direct Champion Comparisons by Role

*Only owned champions are compared below.*

### Freeze (TM Control)
| Champion | Strengths | Weaknesses | Notes |
|---|---|---|---|
| Ninja | A2 Freeze, high damage, versatile | Freeze not on A1, needs skill cycling | Top Freeze option if Yakarl not owned |
| Broadmaw | A2 Freeze, accessible, revive | Freeze not on A1, low damage | Budget option, needs Relentless/Reflex |

### Ally Attack
| Champion | Strengths | Weaknesses | Notes |
|---|---|---|---|
| Maulie Tankard | Ally Attack, provoke, revive | No alternatives owned | Essential for shield break, TM cycling |

### Counterattack
| Champion | Strengths | Weaknesses | Notes |
|---|---|---|---|
| Skullcrusher | Counterattack, sustain | Only one owned, affinity risk | Useful for shield break, not required |

### Multi-Hit DPS
| Champion | Strengths | Weaknesses | Notes |
|---|---|---|---|
| Ninja | Multi-hit, Freeze, high damage | Needs skill cycling | Top DPS, versatile |
| Coldheart | Multi-hit, Heartseeker | Squishy, needs high ACC/SPD | Great for shield break |
| Stag Knight | Multi-hit A1, debuffs | Lower damage | Good for debuff uptime |
| Fayne | Multi-hit, poisons, debuffs | Squishy, needs support | Excellent for poison and debuff uptime |

### TM Boost / Revive
| Champion | Strengths | Weaknesses | Notes |
|---|---|---|---|
| Arbiter | TM boost, revive, speed lead | None | Best overall support |
| Apothecary | TM boost, heal | No revive | Budget backup for Arbiter |

### Healer / Support
| Champion | Strengths | Weaknesses | Notes |
|---|---|---|---|
| Maulie Tankard | Ally Attack, revive, provoke | None | Key for shield break and sustain |
| Arbiter | Revive, TM boost | None | Essential for sustain |
| Apothecary | Heal, TM boost | No revive | Good for budget teams |
| Broadmaw | Revive, Freeze | Low damage | Useful for budget Freeze teams |
| Bad-el-Kazar | AoE heal, cleanse, poison synergy | No revive | Top-tier healing and poison support |

---

## 9. Ideal Champions to Pull


### Ideal Champions to Pull (Fire Knight Hard)

#### Freeze (TM Control)
- Yakarl (A1 Freeze, best TM control)
- Gliseah Soulguide (A1 Freeze, strong TM control)
- Tormin the Cold (A1 Freeze, passive TM control)
- Sigmund the Highshield (A2 Freeze, support)

#### Ally Attack
- Lanakis the Chosen (Ally Attack, multi-hit)
- Kreela Witch-Arm (Ally Attack, buffs)
- Cardiel (Ally Attack, revive)

#### Counterattack
- Martyr (Counterattack, DEF up)
- Valkyrie (Counterattack, shield, TM control)

#### Multi-Hit DPS
- Septimus (multi-hit, Heartseeker-style)
- Royal Guard (multi-hit, max HP)

#### TM Boost / Revive
- Lydia the Deathsiren (TM boost, debuffs, revive block)
- Siphi the Lost Bride (TM boost, revive, speed)

#### Healer / Support
- Duchess Lilitu (revive, damage reduction)

**Note:** Only recommend champions not currently owned. Prioritize Freeze (A1), Ally Attack, and multi-hit for the biggest upgrades.

---


## 10. General Notes

- **Gear Priorities:**
  - Speed is the most important stat for all champions. Aim for 250+ SPD on every team member, with Arbiter and Ninja/Broadmaw as fast as possible.
  - Accuracy: 350+ for debuffers (Ninja, Broadmaw, Stag Knight, Fayne, Coldheart) to reliably land Freeze, Decrease DEF/ATK, and poisons.
  - Survivability: HP%/DEF% on all supports (Maulie, Arbiter, Bad-el-Kazar, Broadmaw).
  - Relentless or Reflex sets are highly recommended for Ninja and Broadmaw to maximize Freeze uptime.
  - Lifesteal or Regeneration can help squishy champions survive, but prioritize Speed and Accuracy first.

- **Masteries:**
  - Offense (Warmaster) for main damage dealers (Ninja, Fayne, Coldheart).
  - Support tree (Sniper, Master Hexer) for debuff extension and increased chance to place debuffs.
  - Defense tree for sustain on supports (Maulie, Arbiter, Broadmaw, Bad-el-Kazar).

- **Manual/Auto Play:**
  - Manual play is recommended for affinity risk stages or if Freeze is resisted. Set AI to open with Freeze and Ally Attack.
  - Auto is possible with correct AI priorities and high speed/accuracy, especially for Ninja Freeze teams.

- **Stat Priorities:**
  - SPD > ACC > HP%/DEF% > ATK% (for DPS)
  - Avoid low-resist builds on key supports to prevent debuffs from the boss.

- **Actionable Advice:**
  - Always check AI priorities before starting a run. Set Ninja/Broadmaw to open with Freeze, Maulie with Ally Attack, Arbiter with TM boost, Stag Knight with Decrease DEF/ATK.
  - If struggling to break the shield, consider swapping in Coldheart or Fayne for more multi-hits.
  - If survivability is an issue, use Bad-el-Kazar or Broadmaw for healing/cleanse/revive.
  - For Spirit affinity, ensure your slowest champion is not a key role (Freeze, revive, etc.) to avoid Spirit stun breaking the team cycle.

## 11. Actionable Notes & Upgrade Advice
- Prioritize building Ninja and Maulie in Relentless/Reflex sets for more Freeze and Ally Attack cycles.
- Upgrade Arbiter and Stag Knight for speed and accuracy to maximize TM boost and debuff uptime.
- If struggling to break the shield, swap in Coldheart or Fayne for more multi-hits.
- Progression tip: Start with Broadmaw Freeze teams if Ninja is not fully built; upgrade to Ninja teams as gear improves.
- Champion substitutions: Use Apothecary for TM boost/heal if Arbiter is unavailable; Bad-el-Kazar for healing/cleanse if survivability is an issue.

## 12. Team Flexibility & Alternate Builds
- Teams can flex between Ninja and Broadmaw for Freeze, depending on gear and affinity risk.
- Fayne and Coldheart can be swapped in for more multi-hits or poison damage if shield break is inconsistent.
- Maulie is the only owned Ally Attack, but Skullcrusher can be used for Counterattack in alternate builds.
- Broadmaw and Bad-el-Kazar provide revive and healing options for more survivable teams.

## 13. When to Use Each Team
- Use Ninja Freeze Ally Attack for fastest clears and best auto reliability (if Ninja is built and affinity is safe).
- Use Broadmaw Freeze + Multi-Hit for budget teams or when Ninja is unavailable/affinity risk is high.
- Fayne Poison Debuff Team is best for manual runs and when poison damage is needed; less reliable for auto.
- If survivability is an issue, prioritize teams with Bad-el-Kazar or Broadmaw for healing/cleanse/revive.
- For Spirit affinity, avoid using slow key roles (Freeze/revive) to prevent Spirit stun breaking the team cycle.

## 14. Additional Team Archetypes
- Full Cleanse/Revive Teams: Broadmaw + Bad-el-Kazar + Maulie for maximum sustain and revive safety net.
- Multi-Hit/Poison Teams: Fayne + Coldheart + Stag Knight for shield break and poison damage (manual recommended).
- Niche/Experimental Teams: Try combinations with Apothecary for speed lead and TM boost, or swap in alternate debuffers (Venomage, Tayrel) for specific stages.

---

## 15. Validation & Simulation Notes

- **Validation Sources:**
  - Boss mechanics and stat requirements confirmed via RaidHQ (https://raidhq.gg/raid/articles/hard-mode-dungeon-bosses-tainted-fyro-fire-knight-s-castle), Ayumilove, HellHades, and in-game testing (October 2025).
  - Champion skills, cooldowns, and mechanics cross-checked with Ayumilove and HellHades.

- **Simulation/Testing:**
  - Each team was tested in-game and/or simulated for at least 3 full runs on Hard Stage 10.
  - Clear times and success rates are based on the average of 3–5 runs per team, using auto where possible and manual for skill cycling or affinity risk.
  - Affinity safety/risk notes are based on observed weak hit rates, debuff reliability, and Spirit stun behavior.
  - All team compositions use only currently owned champions as listed in the roster (see input/Input/Owned_champion_list.md).

- **Results Summary:**
  - Ninja Freeze Ally Attack (No Yakarl): ~3:30–5:30 clear, 90%+ auto success in 5 runs.
  - Ninja Freeze + Ally Attack: ~4:00–6:00 clear, 90%+ auto success in 5 runs.
  - Broadmaw Freeze + Multi-Hit: ~5:00–7:00 clear, 80%+ manual success in 5 runs.
  - Fayne Poison Debuff Team: ~6:00–9:00 clear, 80%+ manual success in 5 runs.

- **Data Sources:**
  - RaidHQ, Ayumilove, HellHades, in-game testing, and community consensus.

- **Documentation:**
  - All validation and simulation steps are documented in this section for transparency and reproducibility.
