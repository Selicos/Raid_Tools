
"""
Champion Summary Markdown Generator

This script generates human-readable summary markdown files for each champion, consolidating key information from champion JSON files and including skill order and expected damage results from the cooldown analysis tool.

Script Flow:
1. Load champion JSON files from the Champions directory
2. Parse skills and stats
3. Run cooldown analysis (if available)
4. Generate markdown summary
5. Save output to Summary/
"""

import json
import os
from typing import Optional, Dict, Any, List

champions_dir: str = os.path.join(
    os.path.dirname(__file__),
    "..",
    "ChampionIntake",
    "Champions",
)
summary_dir: str = os.path.join(os.path.dirname(__file__), "Summary")
cooldown_analysis_dir: str = os.path.join(
    champions_dir, "..", "ChampionAnalysisTool", "cooldown_analysis"
)
os.makedirs(summary_dir, exist_ok=True)

def get_cooldown_analysis(champion_name: str) -> Optional[str]:
    """
    Retrieve the cooldown analysis summary for a champion, if available.

    Args:
        champion_name (str): Name of the champion.

    Returns:
        Optional[str]: Cooldown analysis summary text, or None if not found.
    """
    md_path = os.path.join(cooldown_analysis_dir, f"{champion_name}.md")
    if not os.path.exists(md_path):
        return None
    try:
        with open(md_path, encoding="utf-8") as f:
            lines = f.readlines()
    except Exception as e:
        print(f"[Warning] Could not read cooldown analysis for {champion_name}: {e}")
        return None
    summary: List[str] = []
    for line in lines:
        if line.startswith("## "):
            break
        summary.append(line)
    return "".join(summary).strip() if summary else None

def write_champion_summary_md(champ: Dict[str, Any], champ_name: str) -> None:
    """
    Write the summary markdown for a champion.

    Args:
        champ (Dict[str, Any]): Champion data dictionary.
        champ_name (str): Champion name.
    """
    overview = champ.get('overview', {})
    synergy = champ.get('synergy', {})
    investment = champ.get('investment', {})
    skills = champ.get('skills', {})
    team_inputs = champ.get('team_inputs', {})
    md = f"# {champ_name} — Champion Summary\n\n"
    md += f"## Executive Summary\n"
    md += f"- **Role:** {overview.get('role', 'N/A')}\n"
    md += f"- **Archetype:** {overview.get('archetype', 'N/A')}\n"
    md += f"- **Best Content:** {overview.get('best_dungeon_use', 'N/A')}\n"
    md += f"- **Booking ROI:** {overview.get('booking_roi', 'N/A')}\n"
    md += f"- **Investment Notes:** {investment.get('notes', 'N/A')}\n"
    md += f"- **Synergy/Relentless Viability:** {synergy.get('relentless_viability', 'N/A')}\n\n"

    md += f"## Recommended Gear & Stats\n"
    md += f"- **Primary Stat:** {overview.get('primary_damage_stat', 'N/A')}\n"
    md += f"- **Focus Stats (Arena/Dungeons):** {', '.join(overview.get('focus_stats', {}).get('arena_dungeons', []))}\n"
    md += f"- **Focus Stats (Clan Boss):** {', '.join(overview.get('focus_stats', {}).get('clan_boss', []))}\n"
    md += f"- **Gear Sets (PvP Offense):** {', '.join(overview.get('gear_sets', {}).get('pvp_offense', []))}\n"
    md += f"- **Gear Sets (PvP Defense):** {', '.join(overview.get('gear_sets', {}).get('pvp_defense', []))}\n"
    md += f"- **Gear Sets (Clan Boss):** {', '.join(overview.get('gear_sets', {}).get('clan_boss', []))}\n"
    md += f"- **Gear Sets (Dungeons):** {', '.join(overview.get('gear_sets', {}).get('dungeons', []))}\n"
    md += f"- **Gear Sets (Hydra):** {', '.join(overview.get('gear_sets', {}).get('hydra', []))}\n"
    md += f"- **Gear Sets (Iron Twins):** {', '.join(overview.get('gear_sets', {}).get('iron_twins', []))}\n"
    md += f"- **Gear Sets (Solo Farming):** {', '.join(overview.get('gear_sets', {}).get('solo_farming', []))}\n"
    md += f"- **Gear Tradeoffs:**\n"
    for gt in overview.get('gear_tradeoffs', []):
        md += f"    - {gt.get('set', '')}: Pros: {gt.get('pros', '')}; Cons: {gt.get('cons', '')}\n"
    md += f"\n"

    md += f"## Skill & Attack Order\n"
    skill_order = team_inputs.get('skill_priority', [])
    # Map skill names to A3/A2/A1
    skill_name_to_slot = {}
    for slot in ['a1', 'a2', 'a3']:
        sk = skills.get(slot, {})
        if sk and sk.get('name'):
            skill_name_to_slot[sk['name']] = slot.upper()
    # Show the 16-turn sequence if available
    turn_sequence = skills.get('rotation', {}).get('turn_sequence', [])
    if turn_sequence:
        md += f"- **16-Turn Attack Order (Skill Names):** {' -> '.join(turn_sequence)}\n"
        attack_order_16 = []
        for name in turn_sequence:
            slot = skill_name_to_slot.get(name)
            if slot:
                attack_order_16.append(slot)
            else:
                attack_order_16.append(name)
        md += f"- **16-Turn Attack Order (A3/A2/A1):** {' -> '.join(attack_order_16)}\n"
    if skill_order:
        md += f"- **Ideal Skill Order:** {' -> '.join(skill_order)}\n"
        # Build recommended attack order string
        attack_order = []
        for name in skill_order:
            slot = skill_name_to_slot.get(name)
            if slot:
                attack_order.append(slot)
            else:
                attack_order.append(name)
        md += f"- **Recommended Attack Order:** {' -> '.join(attack_order)}\n"
    else:
        md += f"- **Ideal Skill Order:** N/A\n"
        md += f"- **Recommended Attack Order:** N/A\n"
    md += f"- **First Turn Skill:** {team_inputs.get('first_turn_skill', 'N/A')}\n"
    md += f"- **Disabled Skills:** {', '.join(team_inputs.get('disabled_skills', [])) or 'None'}\n"
    md += f"\n"
    md += f"### Skill Details\n"
    for k in ['a1', 'a2', 'a3']:
        sk = skills.get(k, {})
        if sk:
            md += f"- **{sk.get('name', k.upper())}**: {sk.get('notes', '')} (Type: {sk.get('type', 'N/A')}, Cooldown: {sk.get('cooldown', 'N/A')}, Multiplier: {sk.get('multiplier', 'N/A')})\n"
    if skills.get('passive', {}).get('exists'):
        md += f"- **Passive:** {skills.get('passive', {}).get('impact', '')}\n"
    md += f"\n"
    md += f"## Mastery & Booking\n"
    md += f"- **Best Mastery (PvE/PvP):** {overview.get('best_mastery', {}).get('pve_pvp', 'N/A')}\n"
    md += f"- **Best Mastery (Clan Boss):** {overview.get('best_mastery', {}).get('clan_boss', 'N/A')}\n"
    md += f"- **Booking Impact:** {skills.get('booking', {}).get('impact', 'N/A')} — {skills.get('booking', {}).get('notes', '')}\n"
    md += f"\n"
    cooldown_summary = get_cooldown_analysis(champ_name)
    out_path = os.path.join(summary_dir, f"{champ_name}.md")
    try:
        with open(out_path, "w", encoding="utf-8") as out_f:
            out_f.write(md)
            if cooldown_summary:
                out_f.write("\n---\n")
                out_f.write("## Cooldown Analysis Summary\n")
                out_f.write(cooldown_summary)
        print(f"Wrote summary for {champ_name} to {out_path}")
    except Exception as e:
        print(f"[Error] Could not write summary for {champ_name}: {e}")

def write_champion_skills_md(
    champion_name: str, scenario_descs: Dict[str, Any], turns: int
) -> None:
    """
    Write a skill cycle summary markdown for a champion.

    Args:
        champion_name (str): Champion name.
        scenario_descs (Dict[str, Any]): Scenario descriptions and damage.
        turns (int): Number of turns simulated.
    """
    md_path = os.path.join(summary_dir, f"{champion_name}_skills.md")
    try:
        with open(md_path, "w", encoding="utf-8") as f:
            f.write(f"# {champion_name} Skill Cycle Summary\n\n")
            boss_cycle, boss_damage, *_ = scenario_descs["Single Boss (1 enemy)"]
            f.write(f"**Skill Order (Boss, {turns} turns):**\n")
            f.write("  ".join(boss_cycle) + "\n\n")
            f.write(f"**Total Estimated Damage (Boss, {turns} turns):** {sum(boss_damage)}\n\n")
            wave_cycle, wave_damage, *_ = scenario_descs["Wave (5 enemies)"]
            f.write(f"**Skill Order (Wave, {turns} turns):**\n")
            f.write("  ".join(wave_cycle) + "\n\n")
            f.write(f"**Total Estimated Damage (Wave, {turns} turns):** {sum(wave_damage)}\n\n")
    except Exception as e:
        print(f"[Error] Could not write skills summary for {champion_name}: {e}")

def main() -> None:
    """
    Main execution: process all champion JSON files and generate markdown summaries.
    """
    for filename in os.listdir(champions_dir):
        if filename.endswith(".json"):
            champion_log_path = os.path.join(champions_dir, filename)
            try:
                with open(champion_log_path, "r", encoding="utf-8") as f:
                    champ = json.load(f)
            except Exception as e:
                print(f"[Error] Could not load {filename}: {e}")
                continue
            champ_name = champ.get("champion", filename.replace(".json", ""))
            write_champion_summary_md(champ, champ_name)

if __name__ == "__main__":
    main()
