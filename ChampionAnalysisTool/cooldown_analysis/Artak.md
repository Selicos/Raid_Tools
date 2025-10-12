# Artak Skill Cycle Analysis

**⚠️ Difference detected between expected and simulated cycle. Consider updating the champion JSON.**

## Scenario: Single Boss (1 enemy)
### Simulated Skill Cycle (16 turns)
```
Infernal Chains → Molten Rage → Pyroclastic Claw → Pyroclastic Claw → Infernal Chains → Molten Rage → Pyroclastic Claw → Pyroclastic Claw → Infernal Chains → Molten Rage → Pyroclastic Claw → Pyroclastic Claw → Infernal Chains → Molten Rage → Pyroclastic Claw → Pyroclastic Claw
```
### Estimated Damage Per Turn (Sample Stats, 100% Crit)
```
17500 | 15000 | 10000 | 10000 | 17500 | 15000 | 10000 | 10000 | 17500 | 15000 | 10000 | 10000 | 17500 | 15000 | 10000 | 10000
```

**Total Estimated Damage (16 turns):** 210000

### Debuff Uptime (% of turns)
- decrease def: 25.0%
- hp burn: 100.0%

---
## Scenario: Wave (5 enemies)
### Simulated Skill Cycle (16 turns)
```
Infernal Chains → Molten Rage → Pyroclastic Claw → Pyroclastic Claw → Infernal Chains → Molten Rage → Pyroclastic Claw → Pyroclastic Claw → Infernal Chains → Molten Rage → Pyroclastic Claw → Pyroclastic Claw → Infernal Chains → Molten Rage → Pyroclastic Claw → Pyroclastic Claw
```
### Estimated Damage Per Turn (Sample Stats, 100% Crit)
```
87500 | 75000 | 10000 | 10000 | 87500 | 75000 | 10000 | 10000 | 87500 | 75000 | 10000 | 10000 | 87500 | 75000 | 10000 | 10000
```

**Total Estimated Damage (16 turns):** 730000

### Debuff Uptime (% of turns)
- decrease def: 25.0%
- hp burn: 100.0%

---
## Expected (JSON 'optimal_cycle')
```
Infernal Chains → Molten Rage → Pyroclastic Claw → Pyroclastic Claw → Molten Rage → Pyroclastic Claw → Infernal Chains → Pyroclastic Claw → Molten Rage → Pyroclastic Claw
```
