# Artak — Champion Summary

## Executive Summary
- **Role:** HP Burner / Debuffer
- **Archetype:** AoE HP Burn / Debuff Specialist / Soloist
- **Best Content:** Spider, Hydra, Ice Golem, Dragon
- **Booking ROI:** High (A2/A3)
- **Investment Notes:** Top-tier free legendary for HP Burn, soloing, and debuffing. Books are a great investment.
- **Synergy/Relentless Viability:** High for PvE, can disrupt strict speed tunes in CB/Arena.

## Recommended Gear & Stats
- **Primary Stat:** HP
- **Focus Stats (Arena/Dungeons):** HP%, SPD, ACC, C.RATE, C.DMG
- **Focus Stats (Clan Boss):** HP%, SPD, ACC
- **Gear Sets (PvP Offense):** Protection, Stoneskin, Perception
- **Gear Sets (PvP Defense):** Stoneskin, Zeal
- **Gear Sets (Clan Boss):** Relentless, Perception
- **Gear Sets (Dungeons):** Regeneration, Immortal
- **Gear Sets (Hydra):** Relentless, Perception
- **Gear Sets (Iron Twins):** Regeneration, Immortal
- **Gear Sets (Solo Farming):** Regeneration, Immortal
- **Gear Tradeoffs:**
    - Relentless: Pros: Extra turns for more burns and debuffs; Cons: Unpredictable rotation, can desync team
    - Regeneration: Pros: Sustain for soloing and hard content; Cons: Lower damage potential

## Skill & Attack Order
- **Ideal Skill Order:** Purifyre -> Dogs Of War -> Chaosrazor
- **Recommended Attack Order:** A3 -> A2 -> A1
- **First Turn Skill:** Purifyre
- **Disabled Skills:** None

### Skill Details
- **Chaosrazor**: Attacks all enemies. 35% chance to extend [HP Burn] debuffs by 1 turn. (Type: AoE, Cooldown: None, Multiplier: 0.1x HP)
- **Dogs Of War**: Attacks all enemies. Instantly activates [HP Burn] debuffs. 75% chance to place 50% [Decrease ATK] for 2 turns. (Type: AoE, Cooldown: 3 turns (booked), Multiplier: 0.25x HP)
- **Purifyre**: Attacks all enemies 2 times. First hit: 75% chance to place [HP Burn] for 2 turns. Restores destroyed MAX HP by 10% for each [HP Burn] placed. Heals by 5% MAX HP for each [HP Burn] attempt blocked or resisted. (Type: AoE (2 hits), Cooldown: 3 turns (booked), Multiplier: 0.14x HP)
- **Passive:** Whenever a [HP Burn] is activated, destroys this champion’s MAX HP by 5% (up to 50%). Increases DMG, C.DMG, DEF by 1% and SPD, RES by 2 for each 1% destroyed MAX HP.

## Mastery & Booking
- **Best Mastery (PvE/PvP):** Warmaster
- **Best Mastery (Clan Boss):** Warmaster
- **Booking Impact:** High — A2 and A3 gain significant cooldown reduction and effect chance.



---

## Turn Cycle & Cooldown Analysis (from ChampionTurnAnalysis tool)

# Artak Skill Cycle Summary

**Skill Order (Boss, 16 turns):**
Purifyre → Dogs Of War → Chaosrazor → Purifyre → Dogs Of War → Chaosrazor → Purifyre → Dogs Of War → Chaosrazor → Purifyre → Dogs Of War → Chaosrazor → Purifyre → Dogs Of War → Chaosrazor → Purifyre

**Total Estimated Damage (Boss, 16 turns):** 171500

**Skill Order (Wave, 16 turns):**
Purifyre → Dogs Of War → Chaosrazor → Purifyre → Dogs Of War → Chaosrazor → Purifyre → Dogs Of War → Chaosrazor → Purifyre → Dogs Of War → Chaosrazor → Purifyre → Dogs Of War → Chaosrazor → Purifyre

**Total Estimated Damage (Wave, 16 turns):** 521500

## Artak Skill Cycle Analysis

**⚠️ Difference detected between expected and simulated cycle. Consider updating the champion JSON.**

## Scenario: Single Boss (1 enemy)
### Simulated Skill Cycle (16 turns)
```
Purifyre → Dogs Of War → Chaosrazor → Purifyre → Dogs Of War → Chaosrazor → Purifyre → Dogs Of War → Chaosrazor → Purifyre → Dogs Of War → Chaosrazor → Purifyre → Dogs Of War → Chaosrazor → Purifyre
```
### Estimated Damage Per Turn (Sample Stats, 100% Crit)
```
14000 | 12500 | 5000 | 14000 | 12500 | 5000 | 14000 | 12500 | 5000 | 14000 | 12500 | 5000 | 14000 | 12500 | 5000 | 14000
```

**Total Estimated Damage (16 turns):** 171500
### Estimated Healing Per Turn
```
1000 | 0 | 0 | 1000 | 0 | 0 | 1000 | 0 | 0 | 1000 | 0 | 0 | 1000 | 0 | 0 | 1000
```

**Total Estimated Healing (16 turns):** 6000

### Debuff Uptime (% of turns)
- hp burn: 100.0%
- decrease atk: 31.2%

---
## Scenario: Wave (5 enemies)
### Simulated Skill Cycle (16 turns)
```
Purifyre → Dogs Of War → Chaosrazor → Purifyre → Dogs Of War → Chaosrazor → Purifyre → Dogs Of War → Chaosrazor → Purifyre → Dogs Of War → Chaosrazor → Purifyre → Dogs Of War → Chaosrazor → Purifyre
```
### Estimated Damage Per Turn (Sample Stats, 100% Crit)
```
14000 | 62500 | 25000 | 14000 | 62500 | 25000 | 14000 | 62500 | 25000 | 14000 | 62500 | 25000 | 14000 | 62500 | 25000 | 14000
```

**Total Estimated Damage (16 turns):** 521500
### Estimated Healing Per Turn
```
1000 | 0 | 0 | 1000 | 0 | 0 | 1000 | 0 | 0 | 1000 | 0 | 0 | 1000 | 0 | 0 | 1000
```

**Total Estimated Healing (16 turns):** 6000

### Debuff Uptime (% of turns)
- hp burn: 100.0%
- decrease atk: 31.2%

