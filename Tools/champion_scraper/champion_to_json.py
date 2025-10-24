import json
import os

def champion_to_json(info, stats, skills, out_dir, champion_name):
    # Map to canonical template structure
    entry = {
        "name": champion_name,
        "rarity": info.get("Rarity", ""),
        "affinity": info.get("Affinity", ""),
        "faction": info.get("Faction", ""),
        "role": info.get("Role", ""),
        "draft": True,
        "forms": [
            {
                "form_name": "Base",
                "base_stats": {
                    "HP": int(stats.get("HP", 0)),
                    "ATK": int(stats.get("ATK", 0)),
                    "DEF": int(stats.get("DEF", 0)),
                    "SPD": int(stats.get("SPD", 0)),
                    "C.RATE": int(stats.get("C. RATE", 0)),
                    "C.DMG": int(stats.get("C. DMG", 0)),
                    "RES": int(stats.get("RESIST", 0)),
                    "ACC": int(stats.get("ACC", 0)),
                },
                "skills": [
                    {
                        "name": s["name"],
                        "description": s["desc"],
                        "type": s["type"] if "type" in s else ("Aura" if "aura" in s["name"].lower() or "aura" in s["desc"].lower() else "Active"),
                        "effects": None if ("aura" in s["name"].lower() or "aura" in s["desc"].lower()) else [],
                        "cooldown_booked": None,
                        # Add more fields as needed
                    } for s in skills
                ],
                "aura": None,
                "comments": "Imported from RaidWiki."
            }
        ],
        # Add more top-level fields as needed
    }
    # Output file path
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, f"{champion_name.replace(' ', '_')}.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(entry, f, indent=2, ensure_ascii=False)
    print(f"Champion JSON saved to {out_path}")

# Example usage (to be called from main scraper):
# champion_to_json(info, stats, skills, "../../input/Champion_Dictionary", "Coldheart")
