import json
import os

champions_dir = os.path.join(os.path.dirname(__file__), "..")
summary_dir = os.path.join(os.path.dirname(__file__), "Summary")
os.makedirs(summary_dir, exist_ok=True)

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
        out_path = os.path.join(summary_dir, f"{champ_name}.md")
        with open(out_path, "w", encoding="utf-8") as out_f:
            out_f.write(md)
        print(f"✅ Wrote summary for {champ_name} to {out_path}")