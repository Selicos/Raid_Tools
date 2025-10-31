# Speed, Turn Meter, and Tick Mechanics in RAID Shadow Legends (Draft)

## 1. Speed Stat
- **Definition:** Determines how quickly a champion’s turn meter fills.
- **Base Speed:** Each champion has a base speed (e.g., 100), modified by gear, masteries, buffs, and auras.
- **Speed Aura:** Applies only to base speed (e.g., 30% aura on 100 base speed = 130 effective speed).
- **Buffs:** Applied last, after aura boost is added. Increased Speed buff/debuff is based on overall speed, including aura boost.
- **Equation:**
	$$
		ext{Total Speed} = \text{Base Speed} + \text{Gear} + \text{Masteries} + \text{Aura}
	$$
	$$
		ext{Effective Speed} = \text{Total Speed} \times \text{Buff \%}
	$$

## 2. Ticks
- **Definition:** The smallest unit of time in the game; every tick, all champions’ TM increases using the equation above.
- **Ticks to Turn:**
    $$
        \text{Ticks to Turn} = \frac{1000}{\text{Effective Speed}}
    $$

## 3. Turn Meter (TM)
- **Definition:** A gauge (0–100%) that fills as time passes; when it reaches 100%, the champion can take a turn.
- **TM Constant:** 1428.57
- **Main TM Equation:**
	$$
		ext{TM \% Gain per Tick} = \frac{\text{Champion Speed}}{1428.57}
	$$
- **Simple Equation for quick reference:**
	$$
		ext{TM Gain per Tick} = \text{Champion Speed} \times 0.07
	$$
- **Turn Order:**
	- The champion whose TM reaches 100% first takes a turn.
	- TM can exceed 100%; the highest TM champion goes first after the next tick, and excess TM is carried over.

## 4. Turn Meter Manipulation
- **Boosts:** Skills that instantly increase TM by a percentage (e.g., Arbiter’s TM boost).
- **Reductions:** Skills that decrease enemy TM (e.g., Coldheart’s A3).
- **Buffs/Debuffs:** Speed buffs increase effective speed; Decrease SPD debuffs lower it.
- **Order of Operations:** TM boosts/reductions are applied after each tick, not continuously. After a champion takes a turn, one tick passes and the highest TM % champion then goes next.

## 5. Speed Tuning
- **Purpose:** Aligns champion turns for optimal skill rotation (critical for Clan Boss, Arena, and Dungeons).
- **Strict Tuning:** Required for Clan Boss (see 1:1 and 2:1 guides).
- **Loose Tuning:** Used in Arena and Dungeons for maximizing win rate. Team type (slow/tanky/revival/stoneskin/cheese) affects speed tuning needs.

## 6. General Equations

- **Speed Buff:**
	$$
		ext{Speed Buff} = \text{Total Speed before buff} \times 1.30
	$$
	(30% increase for Speed Buff. Applies to total speed including Aura.)
- **Speed Aura:**
	$$
		ext{Aura Speed} = \text{Base Speed} \times (1 + \text{Aura \%})
	$$
	(Speed aura applies only to base speed.)

## 7. Key Mechanics
- **Speed Sets:** +12% speed per set equipped. Other sets (Perception, Feral, etc.) also increase speed.
- **TM Boosting/Cutting In:** TM boosting skills and speed buffs (and debuffs applied to enemies) can let slow champions 'cut in' or jump ahead of fast enemies by boosting their TM higher than the enemy champion. The boost is proportional to the champion speed.

## 8. Practical Implications
- **Arena:** First team to move usually wins; speed is king.
- **Clan Boss:** Speed tuning is critical for buff/debuff uptime. Ultranightmare (UNM) clan boss has 190 effective speed.
- **Dungeons:** Higher speed = more turns = faster clears.

---

**Sources:**
- Ayumilove: [Speed and Turn Meter Guide](https://ayumilove.net/raid-shadow-legends-speed-turn-meter-guide/)
- HellHades: [Speed Tuning Guide](https://hellhades.com/speed-tuning-guide/)
- RaidWiki: [Game Mechanics](https://raid.wiki/mechanics/)

---

**Summary:**
Speed determines how quickly a champion’s turn meter fills. Each tick, TM increases by the champion’s speed stat. TM manipulation (boosts/reductions) and speed tuning are critical for optimal team performance. The key equation is “Ticks to Turn = 1000 / Speed.” Speed buffs, auras, and sets all contribute to effective speed, impacting turn order and skill rotation.
