import json
import os

champions_dir = os.path.join(
    os.path.dirname(__file__),
    "..",
    "Champion Review and Comparison",
    "Champions"
)
summary_dir = os.path.join(os.path.dirname(__file__), "Summary")
cooldown_analysis_dir = os.path.join(
    champions_dir, "..", "ChampionAnalysisTool", "cooldown_analysis"
)
os.makedirs(summary_dir, exist_ok=True)

def get_cooldown_analysis(champion_name):
    md_path = os.path.join(cooldown_analysis_dir, f"{champion_name}.md")
    if not os.path.exists(md_path):
        return None
    with open(md_path, encoding="utf-8") as f:
        lines = f.readlines()
    # Extract everything from the top until the first '##' header (not including it)
    summary = []
    for line in lines:
        if line.startswith("## "):
            break
        summary.append(line)
    return "".join(summary).strip() if summary else None

def create_json_placeholder(champion_name):
    os.makedirs(champion_json_dir, exist_ok=True)
    path = os.path.join(champion_json_dir, f"{champion_name}.json")
    # Set a default rarity, e.g., "Unknown"
    rarity = "Unknown"
    with open(path, "w", encoding="utf-8") as f:
        f.write("{\n"
                f'  "champion": "{champion_name}",\n'
                f'  "rarity": "{rarity}",\n'
                '  "owned": true\n'
                "}")
    print(f"📁 Placeholder JSON for {champion_name} created/updated with owned=true and rarity={rarity}")

for filename in os.listdir(champions_dir):
    if filename.endswith(".json"):
        champion_log_path = os.path.join(champions_dir, filename)
        with open(champion_log_path, "r", encoding="utf-8") as f:
            champ = json.load(f)
        champ_name = champ.get('champion', filename.replace('.json', ''))
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
        with open(out_path, "w", encoding="utf-8") as out_f:
            out_f.write(md)
            if cooldown_summary:
                out_f.write("\n---\n")
                out_f.write("## Cooldown Analysis Summary\n")
                out_f.write(cooldown_summary)
        print(f"✅ Wrote summary for {champ_name} to {out_path}")

def write_champion_skills_md(champion_name, scenario_descs, TURNS):
    md_path = os.path.join(summary_dir, f"{champion_name}_skills.md")
    with open(md_path, "w", encoding="utf-8") as f:
        # --- Add summary block ---
        f.write(f"# {champion_name} Skill Cycle Summary\n\n")
        # Boss scenario
        boss_cycle, boss_damage, *_ = scenario_descs["Single Boss (1 enemy)"]
        f.write(f"**Skill Order (Boss, {TURNS} turns):**\n")
        f.write(" → ".join(boss_cycle) + "\n\n")
        f.write(f"**Total Estimated Damage (Boss, {TURNS} turns):** {sum(boss_damage)}\n\n")
        # Wave scenario
        wave_cycle, wave_damage, *_ = scenario_descs["Wave (5 enemies)"]
        f.write(f"**Skill Order (Wave, {TURNS} turns):**\n")
        f.write(" → ".join(wave_cycle) + "\n\n")
        f.write(f"**Total Estimated Damage (Wave, {TURNS} turns):** {sum(wave_damage)}\n\n")
        # --- Existing detailed output follows ---