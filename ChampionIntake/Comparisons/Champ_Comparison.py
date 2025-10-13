import os
import sys
import json
from datetime import datetime

# Paths
champions_dir = os.path.join(os.path.dirname(__file__), "..", "Champions")
owned_file = os.path.join(champions_dir, "Owned_Champions", "Owned_champion_list.md")

def load_owned_list():
    if not os.path.exists(owned_file):
        print("❌ Owned_champion_list.md not found.")
        return []
    with open(owned_file, "r", encoding="utf-8") as f:
        lines = f.readlines()
        return [line.strip() for line in lines if line.strip() and not line.startswith("#") and not line.startswith("-")]

def load_champion_log(champion_name):
    path = os.path.join(champions_dir, f"{champion_name}.json")
    if not os.path.exists(path):
        print(f"❌ Champion log not found for {champion_name}")
        return None
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def compare_to_others(base_champ, other_champs):
    base_role = base_champ.get("overview", {}).get("role", "")
    base_attack = base_champ.get("overview", {}).get("attack", 0)
    print(f"Comparing {base_champ.get('champion')} (role: {base_role}, attack: {base_attack})")
    outclassed_by = []
    for champ in other_champs:
        other_role = champ.get("overview", {}).get("role", "")
        other_attack = champ.get("overview", {}).get("attack", 0)
        print(f"  vs {champ.get('champion')} (role: {other_role}, attack: {other_attack})")
        if other_role == base_role and other_attack > base_attack:
            outclassed_by.append(champ.get("champion", "Unknown"))
    return outclassed_by

def compare_all_owned():
    owned = load_owned_list()
    logs = {name: load_champion_log(name) for name in owned}
    results = []
    for name, log in logs.items():
        if not log:
            continue
        others = [logs[n] for n in owned if n != name and logs[n]]
        outclassed_by = compare_to_others(log, others)
        results.append((name, outclassed_by))
    return results

def compare_single(champion_name):
    owned = load_owned_list()
    if champion_name not in owned:
        print(f"{champion_name} is not in the owned champions list.")
        return [(champion_name, [])]
    base_log = load_champion_log(champion_name)
    if not base_log:
        return [(champion_name, [])]
    other_logs = [load_champion_log(name) for name in owned if name != champion_name]
    other_logs = [log for log in other_logs if log]
    outclassed_by = compare_to_others(base_log, other_logs)
    return [(champion_name, outclassed_by)]

def write_results_md(results):
    today = datetime.today().strftime("%Y-%m-%d")
    out_path = os.path.join(os.path.dirname(__file__), f"Comparison_Results_{today}.md")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(f"# Champion Comparison Results ({today})\n\n")
        for name, outclassed_by in results:
            if outclassed_by:
                f.write(f"## {name}\nOutclassed by: {', '.join(outclassed_by)}\n\n")
            else:
                f.write(f"## {name}\nNo owned champion outclasses this champion in their role.\n\n")
    print(f"✅ Results written to {out_path}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        results = compare_single(sys.argv[1])
    else:
        results = compare_all_owned()
    write_results_md(results)
