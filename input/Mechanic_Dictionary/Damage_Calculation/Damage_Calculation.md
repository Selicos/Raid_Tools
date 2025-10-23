### Mechanic information for for generic damage calculations.

#### 1\. **Standard Damage (ATK/DEF/HP-based)**

*   **Formula**:
    

Damage=Stat⋅Skill Multiplier⋅Crit Multiplier⋅Mastery Bonus⋅Buffs⋅Defense Mitigation\\text{Damage} = \\text{Stat} \\cdot \\text{Skill Multiplier} \\cdot \\text{Crit Multiplier} \\cdot \\text{Mastery Bonus} \\cdot \\text{Buffs} \\cdot \\text{Defense Mitigation}

*   **Stat**: ATK, DEF, or HP depending on the champion’s skill.
    
*   **Crit Multiplier**: 1+Crit Damage1 + \\text{Crit Damage}, only applies on crits.
    
*   **Defense Mitigation**: DEF600+DEF\\frac{\\text{DEF}}{600 + \\text{DEF}}
    

#### 2\. **Enemy Max HP Damage**

*   **Formula**:
    

Damage=Enemy Max HP⋅Skill Multiplier\\text{Damage} = \\text{Enemy Max HP} \\cdot \\text{Skill Multiplier}

*   Capped in most PvE content (e.g., 10% of boss HP).
    
*   Champions like Coldheart and Husk use this mechanic.
    

#### 3\. **HP Burn**

*   Deals **3% of target’s MAX HP per tick**.
    
*   Ignores defense, crit, and buffs.
    
*   Stacks across multiple enemies in AoE scenarios.
    

#### 4\. **Poison**

*   Deals **5% of target’s MAX HP per tick**.
    
*   Reduced to **2.5%** against bosses.
    
*   Ignores defense and crit.
    

#### 5\. **Bombs**

*   **Fixed damage** based on the bomb’s multiplier and the attacker’s ATK.
    
*   Ignores defense and crit.
    
*   Delayed detonation after 2 turns unless triggered early.
    

#### 6\. **Reflect Damage**

*   Returns a percentage of incoming damage to the attacker.
    
*   Based on the damage received, not the attacker’s stats.
    

#### 7\. **Warmaster/Giant Slayer Masteries**

*   **Warmaster**: 60% chance to deal bonus damage based on enemy MAX HP (up to 10%).
    
*   **Giant Slayer**: Chance to deal bonus damage based on number of hits and skill type.