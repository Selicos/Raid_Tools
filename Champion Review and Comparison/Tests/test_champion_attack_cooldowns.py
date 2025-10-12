import os
import json
import pytest

# Directory containing champion JSON files
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
CHAMPIONS_DIR = os.path.join(BASE_DIR, "Champions")
COOLDOWN_ANALYSIS_DIR = os.path.join(CHAMPIONS_DIR, "Cooldown_Analysis")
os.makedirs(COOLDOWN_ANALYSIS_DIR, exist_ok=True)

def load_champion_json(champion_name):
    """Load champion JSON data by name (case-insensitive, no extension)."""
    for fname in os.listdir(CHAMPIONS_DIR):
        if fname.lower() == f"{champion_name.lower()}.json":
            with open(os.path.join(CHAMPIONS_DIR, fname), encoding="utf-8") as f:
                return json.load(f)
    raise FileNotFoundError(f"Champion JSON not found: {champion_name}")

def extract_attacks_and_cooldowns(champion_data):
    """
    Extract attack names, cooldowns, multipliers, hit counts, and type (AOE/single) from the champion JSON.
    Also checks for bonus hits and special effects (future expansion).
    """
    skills = champion_data.get("skills", {})
    attacks = []
    for key in ["a1", "a2", "a3", "a4", "a5", "a6"]:
        if key in skills:
            skill = skills[key]
            attacks.append({
                "name": skill.get("name", key),
                "cooldown": parse_cooldown(skill.get("cooldown", "")),
                "order": key,
                "multiplier": skill.get("multiplier", ""),
                "hit_count": skill.get("hit_count", 1),
                "type": skill.get("type", "Single Target")
                # TODO: Add fields for bonus hits, conditional effects, etc.
            })
    return attacks

def parse_cooldown(cooldown_str):
    """Extract the minimum cooldown from a string like '4 turns (3 when booked)'."""
    import re
    numbers = [int(n) for n in re.findall(r"\d+", cooldown_str)]
    return min(numbers) if numbers else 0

def parse_multiplier(multiplier_str):
    """
    Parse a multiplier string like '0.2x HP' and return (float multiplier, stat).
    Returns (0, None) if not found.
    """
    import re
    match = re.match(r"([\d.]+)x\s*(\w+)", multiplier_str)
    if match:
        return float(match.group(1)), match.group(2)
    return 0, None

def get_aoe_factor(skill):
    # Assume 4 enemies for AOE, 1 for single target; adjust as needed for your context
    if skill.get("type", "").lower() == "aoe":
        return 4
    return 1

def get_total_multiplier(skill):
    multiplier, stat = parse_multiplier(skill.get("multiplier", ""))
    hit_count = skill.get("hit_count", 1)
    aoe_factor = get_aoe_factor(skill)
    return multiplier * hit_count * aoe_factor

def simulate_attack_cycle(attacks, turns=10, role=""):
    """
    Simulate attack order for a given number of turns based on cooldowns.
    For damage dealers, also estimate damage per turn.
    Returns the sequence of attack names used and (if not support) the estimated damage per turn.
    """
    cooldowns = {atk["name"]: 0 for atk in attacks}
    attack_order = []
    damage_per_turn = []
    # Example stats for simulation (can be adjusted or read from champion JSON)
    sample_stats = {"HP": 20000, "ATK": 3000, "DEF": 2000}
    for turn in range(turns):
        available = [atk for atk in attacks if cooldowns[atk["name"]] == 0]
        # Prefer non-A1 skills with highest total multiplier if available
        non_a1 = [atk for atk in available if atk["order"].lower() != "a1"]
        chosen = None
        if non_a1:
            # Prefer skill with highest total multiplier (damage potential)
            chosen = max(non_a1, key=lambda x: get_total_multiplier(x))
        elif available:
            # Only A1 is available
            a1 = next((atk for atk in available if atk["order"].lower() == "a1"), None)
            if a1:
                chosen = a1
        else:
            # All skills on cooldown, fallback to A1 if possible
            a1 = next((atk for atk in attacks if atk["order"].lower() == "a1"), None)
            if a1:
                chosen = a1
        if chosen:
            attack_order.append(chosen["name"])
            cooldowns[chosen["name"]] = chosen["cooldown"]
            # Estimate damage if not support
            if role.lower() != "support":
                multiplier, stat = parse_multiplier(chosen.get("multiplier", ""))
                hit_count = chosen.get("hit_count", 1)
                aoe_factor = get_aoe_factor(chosen)
                if stat and stat in sample_stats:
                    dmg = multiplier * sample_stats[stat] * hit_count * aoe_factor
                    damage_per_turn.append(int(dmg))
                else:
                    damage_per_turn.append(0)
            else:
                damage_per_turn.append(0)
        else:
            attack_order.append("No Attack")
            damage_per_turn.append(0)
        # Decrement cooldowns
        for atk in cooldowns:
            if cooldowns[atk] > 0:
                cooldowns[atk] -= 1
    return attack_order, damage_per_turn

def write_champion_skills_md(champion_name, expected_names, simulated_cycle, damage_per_turn, role):
    """Write the skill comparison and damage simulation to a markdown file in Cooldown_Analysis subfolder."""
    md_path = os.path.join(COOLDOWN_ANALYSIS_DIR, f"{champion_name}.md")
    with open(md_path, "w", encoding="utf-8") as f:
        f.write(f"# {champion_name} Skill Cycle Comparison\n\n")
        f.write("## Expected (JSON 'optimal_cycle')\n")
        f.write("```\n" + " → ".join(expected_names) + "\n```\n\n")
        f.write("## Simulated (Based on Cooldowns)\n")
        f.write("```\n" + " → ".join(simulated_cycle[:len(expected_names)]) + "\n```\n")
        f.write("\n## Full Simulated Cycle (10 turns)\n")
        f.write("```\n" + " → ".join(simulated_cycle) + "\n```\n")
        if role.lower() != "support":
            f.write("\n## Estimated Damage Per Turn (Sample Stats)\n")
            f.write("```\n" + " | ".join(str(dmg) for dmg in damage_per_turn) + "\n```\n")
            f.write(f"\nTotal Estimated Damage (10 turns): {sum(damage_per_turn)}\n")
        else:
            f.write("\n(Support champion: damage simulation skipped)\n")

# TODO: For full accuracy, consider bonus hits, conditional extra attacks, and effects like "hits again if X".
# This requires parsing skill descriptions or adding explicit fields to the JSON.

@pytest.mark.parametrize("champion_name", [
    os.path.splitext(f)[0] for f in os.listdir(CHAMPIONS_DIR) if f.endswith(".json")
])
def test_champion_attack_cycle(champion_name):
    champion_data = load_champion_json(champion_name)
    role = champion_data.get("overview", {}).get("role", "")
    attacks = extract_attacks_and_cooldowns(champion_data)
    simulated_cycle, damage_per_turn = simulate_attack_cycle(attacks, turns=10, role=role)
    expected_order = champion_data.get("skills", {}).get("rotation", {}).get("optimal_cycle", [])
    expected_names = []
    for atk in expected_order:
        for a in attacks:
            if a["order"].lower() == atk.lower() or a["name"].lower() == atk.lower():
                expected_names.append(a["name"])
                break
    # Always output the markdown file for every champion
    write_champion_skills_md(champion_name, expected_names, simulated_cycle, damage_per_turn, role)
    if expected_names and simulated_cycle[:len(expected_names)] != expected_names:
        pytest.fail(f"Attack cycle mismatch for {champion_name}. See Cooldown_Analysis/{champion_name}.md for details.")