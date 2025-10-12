# Embrys Skill Cycle Summary

**Skill Order (Boss, 16 turns):**
Nightmare Chains → Shadow Wave → Dark Embrace → Dark Embrace → Nightmare Chains → Shadow Wave → Dark Embrace → Dark Embrace → Nightmare Chains → Shadow Wave → Dark Embrace → Dark Embrace → Nightmare Chains → Shadow Wave → Dark Embrace → Dark Embrace

**Total Estimated Damage (Boss, 16 turns):** 426000

**Skill Order (Wave, 16 turns):**
Nightmare Chains → Shadow Wave → Dark Embrace → Dark Embrace → Nightmare Chains → Shadow Wave → Dark Embrace → Dark Embrace → Nightmare Chains → Shadow Wave → Dark Embrace → Dark Embrace → Nightmare Chains → Shadow Wave → Dark Embrace → Dark Embrace

**Total Estimated Damage (Wave, 16 turns):** 1362000

## Embrys Skill Cycle Analysis

**⚠️ Difference detected between expected and simulated cycle. Consider updating the champion JSON.**

## Scenario: Single Boss (1 enemy)
### Simulated Skill Cycle (16 turns)
```
Nightmare Chains → Shadow Wave → Dark Embrace → Dark Embrace → Nightmare Chains → Shadow Wave → Dark Embrace → Dark Embrace → Nightmare Chains → Shadow Wave → Dark Embrace → Dark Embrace → Nightmare Chains → Shadow Wave → Dark Embrace → Dark Embrace
```
### Estimated Damage Per Turn (Sample Stats, 100% Crit)
```
30000 | 28500 | 24000 | 24000 | 30000 | 28500 | 24000 | 24000 | 30000 | 28500 | 24000 | 24000 | 30000 | 28500 | 24000 | 24000
```

**Total Estimated Damage (16 turns):** 426000

### Debuff Uptime (% of turns)
- stun: 25.0%
- decrease atk: 50.0%

---
## Scenario: Wave (5 enemies)
### Simulated Skill Cycle (16 turns)
```
Nightmare Chains → Shadow Wave → Dark Embrace → Dark Embrace → Nightmare Chains → Shadow Wave → Dark Embrace → Dark Embrace → Nightmare Chains → Shadow Wave → Dark Embrace → Dark Embrace → Nightmare Chains → Shadow Wave → Dark Embrace → Dark Embrace
```
### Estimated Damage Per Turn (Sample Stats, 100% Crit)
```
150000 | 142500 | 24000 | 24000 | 150000 | 142500 | 24000 | 24000 | 150000 | 142500 | 24000 | 24000 | 150000 | 142500 | 24000 | 24000
```

**Total Estimated Damage (16 turns):** 1362000

### Debuff Uptime (% of turns)
- stun: 25.0%
- decrease atk: 50.0%

---
## Expected (JSON 'optimal_cycle')
```
Nightmare Chains → Shadow Wave → Dark Embrace → Dark Embrace → Shadow Wave → Dark Embrace → Nightmare Chains → Dark Embrace → Shadow Wave → Dark Embrace
```
