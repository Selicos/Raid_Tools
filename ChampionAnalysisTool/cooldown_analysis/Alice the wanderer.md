# Alice the wanderer Skill Cycle Analysis

**⚠️ Difference detected between expected and simulated cycle. Consider updating the champion JSON.**

## Scenario: Single Boss (1 enemy)
### Simulated Skill Cycle (16 turns)
```
Rabbit's Rally → Soothing Step → Wanderer's Touch → Wanderer's Touch → Rabbit's Rally → Soothing Step → Wanderer's Touch → Wanderer's Touch → Rabbit's Rally → Soothing Step → Wanderer's Touch → Wanderer's Touch → Rabbit's Rally → Soothing Step → Wanderer's Touch → Wanderer's Touch
```
### Estimated Damage Per Turn (Sample Stats, 100% Crit)
```
0 | 11000 | 9000 | 9000 | 0 | 11000 | 9000 | 9000 | 0 | 11000 | 9000 | 9000 | 0 | 11000 | 9000 | 9000
```

**Total Estimated Damage (16 turns):** 116000

### Buff Uptime (% of turns)
- block debuffs: 25.0%

---
## Scenario: Wave (5 enemies)
### Simulated Skill Cycle (16 turns)
```
Rabbit's Rally → Soothing Step → Wanderer's Touch → Wanderer's Touch → Rabbit's Rally → Soothing Step → Wanderer's Touch → Wanderer's Touch → Rabbit's Rally → Soothing Step → Wanderer's Touch → Wanderer's Touch → Rabbit's Rally → Soothing Step → Wanderer's Touch → Wanderer's Touch
```
### Estimated Damage Per Turn (Sample Stats, 100% Crit)
```
0 | 55000 | 9000 | 9000 | 0 | 55000 | 9000 | 9000 | 0 | 55000 | 9000 | 9000 | 0 | 55000 | 9000 | 9000
```

**Total Estimated Damage (16 turns):** 292000

### Buff Uptime (% of turns)
- block debuffs: 25.0%

---
## Expected (JSON 'optimal_cycle')
```
Rabbit's Rally → Soothing Step → Wanderer's Touch → Wanderer's Touch → Soothing Step → Wanderer's Touch → Rabbit's Rally → Wanderer's Touch → Soothing Step → Wanderer's Touch
```
