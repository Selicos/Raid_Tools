# Michelangelo Skill Cycle Analysis

**⚠️ Difference detected between expected and simulated cycle. Consider updating the champion JSON.**

## Scenario: Single Boss (1 enemy)
### Simulated Skill Cycle (16 turns)
```
Restoration Fresco → Masterpiece Guard → Chisel Strike → Chisel Strike → Restoration Fresco → Masterpiece Guard → Chisel Strike → Chisel Strike → Restoration Fresco → Masterpiece Guard → Chisel Strike → Chisel Strike → Restoration Fresco → Masterpiece Guard → Chisel Strike → Chisel Strike
```
### Estimated Damage Per Turn (Sample Stats, 100% Crit)
```
0 | 1100 | 900 | 900 | 0 | 1100 | 900 | 900 | 0 | 1100 | 900 | 900 | 0 | 1100 | 900 | 900
```

**Total Estimated Damage (16 turns):** 11600

### Buff Uptime (% of turns)
- increase def: 25.0%
- block debuffs: 25.0%

### Debuff Uptime (% of turns)
- decrease atk: 50.0%

---
## Scenario: Wave (5 enemies)
### Simulated Skill Cycle (16 turns)
```
Restoration Fresco → Masterpiece Guard → Chisel Strike → Chisel Strike → Restoration Fresco → Masterpiece Guard → Chisel Strike → Chisel Strike → Restoration Fresco → Masterpiece Guard → Chisel Strike → Chisel Strike → Restoration Fresco → Masterpiece Guard → Chisel Strike → Chisel Strike
```
### Estimated Damage Per Turn (Sample Stats, 100% Crit)
```
0 | 5500 | 900 | 900 | 0 | 5500 | 900 | 900 | 0 | 5500 | 900 | 900 | 0 | 5500 | 900 | 900
```

**Total Estimated Damage (16 turns):** 29200

### Buff Uptime (% of turns)
- increase def: 25.0%
- block debuffs: 25.0%

### Debuff Uptime (% of turns)
- decrease atk: 50.0%

---
## Expected (JSON 'optimal_cycle')
```
Restoration Fresco → Masterpiece Guard → Chisel Strike → Chisel Strike → Masterpiece Guard → Chisel Strike → Restoration Fresco → Chisel Strike → Masterpiece Guard → Chisel Strike
```
