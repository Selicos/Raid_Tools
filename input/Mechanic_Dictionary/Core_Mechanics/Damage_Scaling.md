### Mechanic information for how Defense scales against Attack damage, with diminishing returns.

## Basic equations

# Damage Reduction or D from Defense:

$$
\text{DR} = \frac{\text{DEF}}{600 + \text{DEF}}
$$

# Weak hit damage reduction:

$$
\text{WEAK\_DMG} = 0.7 \times \text{Initial_DAMAGE} 
$$

- 35% chance of a weak hit against enemies with a stronger Affinity
- Weak hits cannot crit


## Markdown tables

# Damage Reduction 
| Defense (DEF) | Damage Reduction (%) |
|---------------|----------------------|
| 0             | 0.00%                |
| 200           | 25.00%               |
| 400           | 40.00%               |
| 600           | 50.00%               |
| 800           | 57.14%               |
| 1000          | 62.50%               |
| 1200          | 66.67%               |
| 1400          | 70.00%               |
| 1600          | 72.73%               |
| 1800          | 75.00%               |
| 2000          | 76.92%               |
| 2200          | 78.57%               |
| 2400          | 80.00%               |
| 2600          | 81.25%               |
| 2800          | 82.35%               |
| 3000          | 83.33%               |
| 3200          | 84.21%               |
| 3400          | 85.00%               |
| 3600          | 85.71%               |
| 3800          | 86.36%               |
| 4000          | 86.96%               |
| 4200          | 87.50%               |
| 4400          | 87.96%               |
| 4600          | 88.46%               |
| 4800          | 88.89%               |
| 5000          | 89.29%               |
| 5200          | 89.66%               |
| 5400          | 90.00%               |
| 5600          | 90.32%               |
| 5800          | 90.59%               |
| 6000          | 90.91%               |


