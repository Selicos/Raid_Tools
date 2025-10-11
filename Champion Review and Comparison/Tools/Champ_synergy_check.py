import json
import os
import sys

# Directory for champion logs
champion_dir = r"Champion Review and Comparison\Champions"

# Prompt for champion name if not passed as argument
def get_champion_name():
    if len(sys.argv) > 1:
        return sys.argv[1]
    return input("Enter champion name: ").strip()

# Load existing champion log
def load_champion_log(champion_name):
    file_path = os.path.join(champion_dir, f"{champion_name}.json")
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Champion data file not found: {file_path}")
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f), file_path

# Generate new overview summary (placeholder logic — customize as needed)
def generate_overview_summary(champion_data):
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

# Append or update the overview block
def append_overview(champion_name):
    try:
        data, file_path = load_champion_log(champion_name)
        new_overview = generate_overview_summary(data)
        data["overview"] = new_overview

        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)
        print(f"✅ Overview updated in {file_path}")

    except FileNotFoundError as e:
        print(f"❌ Error: {e}")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")

# Run the script
if __name__ == "__main__":
    champ = get_champion_name()
    append_overview(champ)
