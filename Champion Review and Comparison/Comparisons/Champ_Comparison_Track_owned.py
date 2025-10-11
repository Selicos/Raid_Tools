import os
import json
import time
import subprocess

# Paths
owned_file = r"C:\GIT\RAID_TOOLS\owned_champions.json"
comparison_script = r"C:\GIT\RAID_TOOLS\Comparisons\Champ_comparison.py"

# Track last modified time
def get_last_modified(path):
    return os.path.getmtime(path) if os.path.exists(path) else 0

# Load owned champion list
def load_owned_list():
    with open(owned_file, "r", encoding="utf-8") as f:
        data = json.load(f)
        return data.get("owned_champions", [])

# Run comparison script for each champion
def run_comparisons(champion_list):
    for champ in champion_list:
        try:
            subprocess.run(["python", comparison_script, champ], check=True)
            print(f"✅ Updated comparison for: {champ}")
        except subprocess.CalledProcessError:
            print(f"❌ Failed to update: {champ}")

# Watch loop
def watch_owned_list():
    print("👀 Watching for updates to owned_champions.json...")
    last_modified = get_last_modified(owned_file)

    while True:
        time.sleep(5)  # Check every 5 seconds
        current_modified = get_last_modified(owned_file)

        if current_modified != last_modified:
            print("🔄 Detected update to owned list. Rebuilding comparisons...")
            owned_champs = load_owned_list()
            run_comparisons(owned_champs)
            last_modified = current_modified

if __name__ == "__main__":
    watch_owned_list()
