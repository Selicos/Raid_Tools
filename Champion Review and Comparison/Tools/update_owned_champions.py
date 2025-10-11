import os
import json
import sys
from datetime import datetime, timedelta

# Paths
champion_dir = r"Champion Review and Comparison\Champions"
owned_list_path = os.path.join(champion_dir, "Owned Champions", "Owned_Champion_list.md")

# Load owned champions and last update dates
def load_owned_champions():
    owned = {}
    if not os.path.exists(owned_list_path):
        return owned
    with open(owned_list_path, "r", encoding="utf-8") as f:
        for line in f:
            if "|" in line:
                parts = line.strip().split("|")
                name = parts[0].replace("-", "").strip()
                date_str = parts[1].replace("Last Updated:", "").strip()
                try:
                    owned[name] = datetime.strptime(date_str, "%Y-%m-%d")
                except ValueError:
                    owned[name] = None
    return owned

# Save updated owned list
def save_owned_champions(owned):
    with open(owned_list_path, "w", encoding="utf-8") as f:
        f.write("# Owned Champions\n\n")
        for name, date in owned.items():
            date_str = date.strftime("%Y-%m-%d") if date else "Unknown"
            f.write(f"- {name} | Last Updated: {date_str}\n")

# Load champion log
def load_champion_log(name):
    path = os.path.join(champion_dir, f"{name}.json")
    if not os.path.exists(path):
        return None, path
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f), path

# Generate new overview block (placeholder logic)
def generate_overview(champion_data):
    return {
        "role": "Updated Role",
        "archetype": "Updated Archetype",
        "best_mastery": {
            "pve_pvp": "Helmsmasher",
            "clan_boss": "Warmaster"
        },
        "booking_roi": "High",
        "gear_sets": {
            "pvp_offense": ["Savage", "Cruel"],
            "clan_boss": ["Reflex", "Relentless"],
            "dungeons": ["Perception", "Speed"]
        },
        "focus_stats": {
            "arena_dungeons": ["ATK%", "Crit Rate", "Speed"],
            "clan_boss": ["Accuracy", "HP%", "Speed"]
        },
        "accuracy_resistance": {
            "hard_10_dungeons": "Accuracy ~250–300",
            "hydra": "Accuracy ~350+",
            "iron_twins": "Accuracy ~400+"
        },
        "best_dungeon_use": "Dragon HARD 10"
    }

# Update champion log
def update_champion_log(name, owned):
    data, path = load_champion_log(name)
    if not data:
        print(f"❌ Champion log not found: {name}")
        return False

    data["overview"] = generate_overview(data)

    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

    owned[name] = datetime.today()
    print(f"✅ Updated: {name}")
    return True

# Main logic
def run_updates():
    owned = load_owned_champions()
    specified = sys.argv[1:]  # Optional list of champions to force update

    for name in owned:
        last_update = owned[name]
        needs_update = (
            name in specified or
            not last_update or
            (datetime.today() - last_update).days > 30
        )
        if needs_update:
            update_champion_log(name, owned)

    save_owned_champions(owned)

if __name__ == "__main__":
    run_updates()
