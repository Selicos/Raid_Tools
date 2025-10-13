
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
    md = f"# Champion: {champ_name}\n\n"
    md += f"**Role:** {champ.get('overview', {}).get('role', 'N/A')}\n\n"
    md += f"**Archetype:** {champ.get('overview', {}).get('archetype', 'N/A')}\n\n"
    md += f"**Best Mastery (Clan Boss):** {champ.get('overview', {}).get('best_mastery', {}).get('clan_boss', 'N/A')}\n\n"
    md += f"**Booking ROI:** {champ.get('overview', {}).get('booking_roi', 'N/A')}\n\n"
    md += f"**Best Dungeon Use:** {champ.get('overview', {}).get('best_dungeon_use', 'N/A')}\n\n"
    md += f"**Synergy (Relentless Viability):** {champ.get('synergy', {}).get('relentless_viability', 'N/A')}\n\n"
    md += f"**Investment Notes:** {champ.get('investment', {}).get('notes', 'N/A')}\n\n"
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
