import os
import json
import subprocess

# Paths
champion_dir = r"C:\GIT\RAID_TOOLS\champions"
owned_file = r"C:\GIT\RAID_TOOLS\owned_champions.json"
comparison_script = r"C:\GIT\RAID_TOOLS\Comparisons\Champ_comparison.py"

# Load owned champion list
def load_owned_list():
    if not os.path.exists(owned_file):
        print("❌ owned_champions.json not found.")
        return []
    with open(owned_file, "r", encoding="utf-8") as f:
        data = json.load(f)
        return data.get("owned_champions", [])

# Run comparison script for each champion
def run_comparison(champion_name):
    try:
        subprocess.run(
            ["python", comparison_script, champion_name],
            check=True
        )
        print(f"✅ Comparison updated for: {champion_name}")
    except subprocess.CalledProcessError:
        print(f"❌ Failed to run comparison for: {champion_name}")

# Main loop
def rebuild_all_comparisons():
    owned_list = load_owned_list()
    if not owned_list:
        return

    for filename in os.listdir(champion_dir):
        if filename.endswith(".json"):
            champ_name = filename.replace(".json", "")
            run_comparison(champ_name)

if __name__ == "__main__":
    rebuild_all_comparisons()
