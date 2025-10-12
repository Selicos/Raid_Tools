"""
Champion Skill Cycle Simulation and Analysis

This script loads champion JSON files, simulates skill usage over a turn cycle for both single-target (boss) and multi-target (wave) scenarios,
calculates damage, healing, shield generation, and buff/debuff uptime, and outputs a detailed markdown report for each champion.
It compares the simulated skill order to the expected order in the JSON and flags mismatches.

Improvements:
- Summary title at the top of markdown.
- Placeholder for advanced skill description parsing.
- Type hints, docstrings, and improved comments.
- Constants for buffs, debuffs, and turns.
- Helper function for skill selection.
- All output, cache, and documentation in the Cooldown_Analysis folder.
"""

import os
import json
import re
from typing import List, Dict, Tuple, Optional

# === Constants ===
BUFFS = ["increase atk", "increase def", "block debuffs", "shield", "crit rate", "speed"]
DEBUFFS = ["decrease atk", "decrease def", "hp burn", "poison", "stun", "freeze", "provoke"]
TURNS = 16

# Directory containing champion JSON files and output
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
CHAMPIONS_DIR = os.path.join(BASE_DIR, "Champion Review and Comparison", "Champions")
COOLDOWN_ANALYSIS_DIR = os.path.join(os.path.dirname(__file__), "cooldown_analysis")
os.makedirs(COOLDOWN_ANALYSIS_DIR, exist_ok=True)

def load_champion_json(champion_name: str) -> dict:
    """
    Load champion JSON data by name (case-insensitive, no extension).
    """
    for fname in os.listdir(CHAMPIONS_DIR):
        if fname.lower() == f"{champion_name.lower()}.json":
            with open(os.path.join(CHAMPIONS_DIR, fname), encoding="utf-8") as f:
                return json.load(f)
    raise FileNotFoundError(f"Champion JSON not found: {champion_name}")

def extract_attacks_and_cooldowns(champion_data: dict) -> List[dict]:
    """
    Extract skill data (name, cooldown, multipliers, hits, type, bonus effects, buffs, debuffs, notes) from the champion JSON.
    """
    skills = champion_data.get("skills", {})
    attacks = []
    for key in ["a1", "a2", "a3", "a4", "a5", "a6"]:
        if key in skills:
            skill = skills[key]
            # Advanced parsing placeholder
            parsed = parse_skill_description(skill.get("notes", ""))
            bonus_hits = parsed.get("bonus_hits", 0)
            extra_turn = parsed.get("extra_turn", False)
            attacks.append({
                "name": skill.get("name", key),
                "cooldown": parse_cooldown(skill.get("cooldown", "")),
                "order": key,
                "multiplier": skill.get("multiplier", ""),
                "hit_count": skill.get("hit_count", 1),
                "type": skill.get("type", "Single Target"),
                "bonus_hits": bonus_hits,
                "extra_turn": extra_turn,
                "buffs": extract_buffs(skill),
                "debuffs": extract_debuffs(skill),
                "notes": skill.get("notes", "").lower()
            })
    return attacks

def extract_buffs(skill: dict) -> List[str]:
    """
    Extract buffs from skill notes.
    """
    notes = skill.get("notes", "").lower()
    return [buff for buff in BUFFS if buff in notes]

def extract_debuffs(skill: dict) -> List[str]:
    """
    Extract debuffs from skill notes.
    """
    notes = skill.get("notes", "").lower()
    return [debuff for debuff in DEBUFFS if debuff in notes]

def parse_cooldown(cooldown_str: str) -> int:
    """
    Extract the minimum cooldown from a string like '4 turns (3 when booked)'.
    """
    numbers = [int(n) for n in re.findall(r"\d+", cooldown_str)]
    return min(numbers) if numbers else 0

def parse_multiplier(multiplier_str: str) -> Tuple[float, Optional[str]]:
    """
    Parse a multiplier string like '0.2x HP' and return (float multiplier, stat).
    Returns (0, None) if not found.
    """
    match = re.match(r"([\d.]+)x\s*(\w+)", multiplier_str)
    if match:
        return float(match.group(1)), match.group(2)
    return 0, None

def get_aoe_factor(skill: dict, enemy_count: int) -> int:
    """
    Return the number of targets hit by the skill.
    """
    if skill.get("type", "").lower() == "aoe":
        return enemy_count
    return 1

def get_total_multiplier(skill: dict, enemy_count: int) -> float:
    """
    Calculate the total multiplier for a skill, including hits, bonus hits, and AOE factor.
    """
    multiplier, _ = parse_multiplier(skill.get("multiplier", ""))
    hit_count = skill.get("hit_count", 1) + skill.get("bonus_hits", 0)
    aoe_factor = get_aoe_factor(skill, enemy_count)
    return multiplier * hit_count * aoe_factor

def parse_heal_or_shield(notes: str, stat_value: dict) -> Tuple[float, float]:
    """
    Parse healing and shield values from skill notes.
    Looks for patterns like "heals by 20% HP" or "shield equal to 30% HP".
    """
    heal = 0
    shield = 0
    heal_match = re.search(r'heals? by (\d+)% ?(hp|atk|def)?', notes)
    shield_match = re.search(r'shield (?:equal to|by)? (\d+)% ?(hp|atk|def)?', notes)
    if heal_match:
        pct = int(heal_match.group(1))
        stat = heal_match.group(2) or "hp"
        heal = pct / 100 * stat_value.get(stat.upper(), 0)
    if shield_match:
        pct = int(shield_match.group(1))
        stat = shield_match.group(2) or "hp"
        shield = pct / 100 * stat_value.get(stat.upper(), 0)
    return heal, shield

def select_skill(
    available: List[dict],
    enemy_count: int,
    skill_priority: Optional[List[str]] = None
) -> Optional[dict]:
    """
    Select the best skill to use from available skills.
    - If skill_priority is provided, use it.
    - Otherwise, prefer non-A1 skills with highest total multiplier.
    - If only A1 is available, use it.
    """
    if skill_priority:
        for prio in skill_priority:
            chosen = next((atk for atk in available if atk["order"].lower() == prio.lower() or atk["name"].lower() == prio.lower()), None)
            if chosen:
                return chosen
    non_a1 = [atk for atk in available if atk["order"].lower() != "a1"]
    if non_a1:
        return max(non_a1, key=lambda x: get_total_multiplier(x, enemy_count))
    if available:
        return next((atk for atk in available if atk["order"].lower() == "a1"), None)
    return None

def simulate_attack_cycle(
    attacks: List[dict],
    turns: int = TURNS,
    role: str = "",
    stats: Optional[dict] = None,
    enemy_count: int = 1,
    skill_priority: Optional[List[str]] = None,
    disabled_skills: Optional[List[str]] = None
) -> Tuple[List[str], List[int], List[int], List[int], Dict[str, float], Dict[str, float]]:
    """
    Simulate skill usage, damage, healing, and shield generation over a number of turns.

    Returns:
        attack_order (list): Skill names used each turn.
        damage_per_turn (list): Damage dealt each turn.
        healing_per_turn (list): Healing done each turn.
        shield_per_turn (list): Shield generated each turn.
        buffs_uptime (dict): Buff uptime percentages.
        debuffs_uptime (dict): Debuff uptime percentages.
    """
    cooldowns = {atk["name"]: 0 for atk in attacks}
    attack_order = []
    damage_per_turn = []
    healing_per_turn = []
    shield_per_turn = []
    buffs_uptime = {}
    debuffs_uptime = {}
    turn = 0
    sample_stats = stats or {"HP": 20000, "ATK": 3000, "DEF": 2000, "CRIT DMG": 1.5}
    crit_multiplier = 1 + sample_stats.get("CRIT DMG", 0.5)
    while turn < turns:
        available = [
            atk for atk in attacks
            if cooldowns[atk["name"]] == 0 and (not disabled_skills or atk["order"] not in disabled_skills)
        ]
        chosen = select_skill(available, enemy_count, skill_priority)
        if not chosen:
            a1 = next((atk for atk in attacks if atk["order"].lower() == "a1"), None)
            if a1:
                chosen = a1
            else:
                attack_order.append("No Attack")
                damage_per_turn.append(0)
                healing_per_turn.append(0)
                shield_per_turn.append(0)
                turn += 1
                continue
        attack_order.append(chosen["name"])
        cooldowns[chosen["name"]] = chosen["cooldown"]
        # Buff/debuff uptime tracking
        for buff in chosen.get("buffs", []):
            buffs_uptime[buff] = buffs_uptime.get(buff, 0) + 1
        for debuff in chosen.get("debuffs", []):
            debuffs_uptime[debuff] = debuffs_uptime.get(debuff, 0) + 1
        # Damage calculation
        multiplier, stat = parse_multiplier(chosen.get("multiplier", ""))
        hit_count = chosen.get("hit_count", 1) + chosen.get("bonus_hits", 0)
        aoe_factor = get_aoe_factor(chosen, enemy_count)
        if stat and stat in sample_stats:
            dmg = multiplier * sample_stats[stat] * hit_count * aoe_factor * crit_multiplier
            damage_per_turn.append(int(dmg))
        else:
            damage_per_turn.append(0)
        # Healing and shield calculation
        heal, shield = parse_heal_or_shield(chosen.get("notes", ""), sample_stats)
        healing_per_turn.append(int(heal))
        shield_per_turn.append(int(shield))
        # Handle extra turn
        if chosen.get("extra_turn", False):
            continue
        # Decrement cooldowns
        for atk in cooldowns:
            if cooldowns[atk] > 0:
                cooldowns[atk] -= 1
        turn += 1
    # Normalize uptime to percentage
    buffs_uptime = {k: round(v / turns * 100, 1) for k, v in buffs_uptime.items()}
    debuffs_uptime = {k: round(v / turns * 100, 1) for k, v in debuffs_uptime.items()}
    return attack_order, damage_per_turn, healing_per_turn, shield_per_turn, buffs_uptime, debuffs_uptime

def write_champion_skills_md(
    champion_name: str,
    expected_names: List[str],
    simulated_results: List[Tuple],
    role: str,
    scenario_descs: Dict[str, Tuple],
    turn_order_match: bool
) -> None:
    """
    Write the skill comparison, damage, healing, shield, and uptime to a markdown file in Cooldown_Analysis subfolder.
    Now includes a clear summary block at the top for skill order and total damage.
    """
    md_path = os.path.join(COOLDOWN_ANALYSIS_DIR, f"{champion_name}.md")
    with open(md_path, "w", encoding="utf-8") as f:
        # --- Summary block at the top ---
        f.write(f"# {champion_name} Skill Cycle Summary\n\n")

        # Boss scenario summary
        boss_cycle, boss_damage, *_ = scenario_descs["Single Boss (1 enemy)"]
        f.write(f"**Skill Order (Boss, {TURNS} turns):**\n")
        f.write(" → ".join(boss_cycle) + "\n\n")
        f.write(f"**Total Estimated Damage (Boss, {TURNS} turns):** {sum(boss_damage)}\n\n")

        # Wave scenario summary
        wave_cycle, wave_damage, *_ = scenario_descs["Wave (5 enemies)"]
        f.write(f"**Skill Order (Wave, {TURNS} turns):**\n")
        f.write(" → ".join(wave_cycle) + "\n\n")
        f.write(f"**Total Estimated Damage (Wave, {TURNS} turns):** {sum(wave_damage)}\n\n")

        # --- Existing detailed output follows ---
        f.write(f"## {champion_name} Skill Cycle Analysis\n\n")
        if turn_order_match:
            f.write("**✅ Simulated turn order matches champion.json optimal_cycle.**\n\n")
        else:
            f.write("**⚠️ Difference detected between expected and simulated cycle. Consider updating the champion JSON.**\n\n")
        for desc, (simulated_cycle, damage_per_turn, healing_per_turn, shield_per_turn, buffs_uptime, debuffs_uptime) in scenario_descs.items():
            f.write(f"## Scenario: {desc}\n")
            f.write(f"### Simulated Skill Cycle ({TURNS} turns)\n")
            f.write("```\n" + " → ".join(simulated_cycle) + "\n```\n")
            f.write("### Estimated Damage Per Turn (Sample Stats, 100% Crit)\n")
            f.write("```\n" + " | ".join(str(dmg) for dmg in damage_per_turn) + "\n```\n")
            f.write(f"\n**Total Estimated Damage ({TURNS} turns):** {sum(damage_per_turn)}\n")
            if any(healing_per_turn):
                f.write("### Estimated Healing Per Turn\n")
                f.write("```\n" + " | ".join(str(h) for h in healing_per_turn) + "\n```\n")
                f.write(f"\n**Total Estimated Healing ({TURNS} turns):** {sum(healing_per_turn)}\n")
            if any(shield_per_turn):
                f.write("### Estimated Shield Per Turn\n")
                f.write("```\n" + " | ".join(str(s) for s in shield_per_turn) + "\n```\n")
                f.write(f"\n**Total Estimated Shield ({TURNS} turns):** {sum(shield_per_turn)}\n")
            if buffs_uptime:
                f.write("\n### Buff Uptime (% of turns)\n")
                for buff, pct in buffs_uptime.items():
                    f.write(f"- {buff}: {pct}%\n")
            if debuffs_uptime:
                f.write("\n### Debuff Uptime (% of turns)\n")
                for debuff, pct in debuffs_uptime.items():
                    f.write(f"- {debuff}: {pct}%\n")
            f.write("\n---\n")
        # Output expected cycle for reference
        f.write("## Expected (JSON 'optimal_cycle')\n")
        f.write("```\n" + " → ".join(expected_names) + "\n```\n")

def parse_skill_description(description: str) -> dict:
    """
    Extract multipliers, hits, healing, shield, buffs, debuffs, and extra turns from a skill description.
    Placeholder for advanced parsing logic.
    """
    # TODO: Implement advanced parsing using regex or NLP as needed.
    # Example return:
    # {'bonus_hits': 0, 'extra_turn': False}
    notes = description.lower()
    bonus_hits = 0
    extra_turn = False
    bonus_match = re.search(r'(\d+) bonus hit', notes)
    if bonus_match:
        bonus_hits = int(bonus_match.group(1))
    if "extra turn" in notes or "grants an extra turn" in notes:
        extra_turn = True
    return {'bonus_hits': bonus_hits, 'extra_turn': extra_turn}

def run_champion_analysis():
    for fname in os.listdir(CHAMPIONS_DIR):
        if fname.endswith(".json"):
            champion_name = os.path.splitext(fname)[0]
            try:
                champion_data = load_champion_json(champion_name)
                role = champion_data.get("overview", {}).get("role", "")
                stats = champion_data.get("overview", {}).get("base_stats", None)
                attacks = extract_attacks_and_cooldowns(champion_data)
                expected_order = champion_data.get("skills", {}).get("rotation", {}).get("optimal_cycle", [])
                skill_priority = champion_data.get("team_inputs", {}).get("skill_priority", None)
                disabled_skills = champion_data.get("team_inputs", {}).get("disabled_skills", None)
                expected_names = []
                for atk in expected_order:
                    for a in attacks:
                        if a["order"].lower() == atk.lower() or a["name"].lower() == atk.lower():
                            expected_names.append(a["name"])
                            break
                scenario_descs = {}
                simulated_results = []
                for scenario, enemy_count in [("Single Boss (1 enemy)", 1), ("Wave (5 enemies)", 5)]:
                    sim_cycle, dmg_per_turn, healing_per_turn, shield_per_turn, buffs_uptime, debuffs_uptime = simulate_attack_cycle(
                        attacks, turns=TURNS, role=role, stats=stats, enemy_count=enemy_count,
                        skill_priority=skill_priority, disabled_skills=disabled_skills
                    )
                    scenario_descs[scenario] = (sim_cycle, dmg_per_turn, healing_per_turn, shield_per_turn, buffs_uptime, debuffs_uptime)
                    simulated_results.append((sim_cycle, dmg_per_turn, healing_per_turn, shield_per_turn, buffs_uptime, debuffs_uptime))
                turn_order_match = bool(expected_names and simulated_results and simulated_results[0][0][:len(expected_names)] == expected_names)
                write_champion_skills_md(champion_name, expected_names, simulated_results, role, scenario_descs, turn_order_match)
                print(f"✅ Analysis complete for {champion_name}")
            except Exception as e:
                print(f"❌ Error analyzing {champion_name}: {e}")

if __name__ == "__main__":
    run_champion_analysis()