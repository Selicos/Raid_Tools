"""
import_owned_champions.py

Bulk update the Owned_Champion_list.md file with new champions, supporting both direct input and file import.
- Direct input: Enter champion name (with spaces) and rarity (number or string).
- File input: Use --input <file> (CSV/Markdown/JSON supported).
- Maintains last updated date and avoids duplicates.
- Optionally triggers champion intake for new entries.
"""
import argparse
import csv
import json
import os
import re
from datetime import datetime
from pathlib import Path

OWNED_LIST_MD = Path("input/Owned_Champions/Owned_Champion_list.md")
RARITY_MAP = {"5": "Legendary", "4": "Epic", "3": "Rare", "2": "Uncommon", "1": "Common"}


def parse_args():
    parser = argparse.ArgumentParser(description="Bulk update owned champion list.")
    parser.add_argument('--input', type=str, help='Input file (CSV, JSON, or Markdown table)')
    parser.add_argument('--trigger-intake', action='store_true', help='Trigger champion intake for new entries')
    parser.add_argument('--from-owned-list', action='store_true', help='Process all champions in the owned list and trigger intake for each')
    return parser.parse_args()


def read_owned_list():
    if not OWNED_LIST_MD.exists():
        return {}
    owned = {}
    pat = re.compile(r"^- ([^|]+)\s*\|\s*Rarity: ([^|]+)\| Last Updated: (\d{4}-\d{2}-\d{2})")
    with open(OWNED_LIST_MD, encoding='utf-8') as f:
        for line in f:
            m = pat.match(line.strip())
            if m:
                name, rarity, date = m.groups()
                owned[name.strip()] = {'rarity': rarity.strip(), 'date': date.strip()}
            else:
                # Try to match lines without rarity
                m2 = re.match(r"^- ([^|]+)\| Last Updated: (\d{4}-\d{2}-\d{2})", line.strip())
                if m2:
                    name, date = m2.groups()
                    owned[name.strip()] = {'rarity': '', 'date': date.strip()}
    return owned


def write_owned_list(owned):
    lines = ["# Owned Champions\n"]
    for name, info in sorted(owned.items()):
        rarity = f" | Rarity: {info['rarity']}" if info['rarity'] else ''
        lines.append(f"- {name}{rarity}")
    with open(OWNED_LIST_MD, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines) + '\n')


def parse_input_file(path):
    ext = Path(path).suffix.lower()
    champions = []
    if ext == '.csv':
        with open(path, encoding='utf-8') as f:
            reader = csv.reader(f)
            for row in reader:
                if not row or row[0].startswith('#') or 'champion' in row[0].lower():
                    continue
                # Defensive: skip rows with too many columns or empty name
                if len(row) < 1 or not row[0].strip():
                    print(f"[WARN] Skipping malformed row: {row}")
                    continue
                name = row[0].strip()
                rarity = str(row[1]).strip() if len(row) > 1 else ''
                # Defensive: skip if rarity looks like a name or is missing
                if '|' in name or name.lower().startswith('rarity:'):
                    print(f"[WARN] Skipping malformed name: {name}")
                    continue
                champions.append((name, rarity))
    elif ext == '.json':
        with open(path, encoding='utf-8') as f:
            data = json.load(f)
            for entry in data:
                name = entry.get('champion', '').strip()
                rarity = str(entry.get('rarity', '')).strip()
                if name:
                    champions.append((name, rarity))
    elif ext in {'.md', '.markdown'}:
        with open(path, encoding='utf-8') as f:
            for line in f:
                # Accept lines like: - Name | Rarity: Epic | Last Updated: ...
                m = re.match(r"^-\s*([^|]+)\|\s*Rarity:\s*([^|]+)", line.strip())
                if m:
                    name, rarity = m.groups()
                    champions.append((name.strip(), rarity.strip()))
                    continue
                # Accept table lines: | Name | Rarity |
                m2 = re.match(r"[\|-]?\s*([A-Za-z0-9 .'-]+)\s*\|\s*([A-Za-z]+)", line)
                if m2:
                    name, rarity = m2.groups()
                    champions.append((name.strip(), rarity.strip()))
                    continue
                # Warn on malformed lines
                if line.strip() and not line.strip().startswith('#'):
                    print(f"[WARN] Skipping malformed markdown line: {line.strip()}")
    else:
        raise ValueError(f"Unsupported file type: {ext}")
    return champions


def prompt_for_champions():
    champions = []
    print("Enter champion names and rarity (number or string). Leave name blank to finish.")
    while True:
        name = input("Champion name: ").strip()
        if not name:
            break
        rarity = input("Rarity (number or string): ").strip()
        champions.append((name, rarity))
    return champions


def normalize_rarity(rarity):
    if not rarity:
        return ''
    rarity = str(rarity).strip().capitalize()
    if rarity in RARITY_MAP.values():
        return rarity
    if rarity in RARITY_MAP:
        return RARITY_MAP[rarity]
    return rarity


def main():
    args = parse_args()
    owned = read_owned_list()
    if args.from_owned_list:
        # Process all champions in the owned list and trigger intake for each
        repo_root = Path(__file__).parent.parent.resolve()
        prompt_dir = repo_root / "input" / "Prompt"
        completed_dir = repo_root / "output" / "completed_prompts"
        prompt_dir.mkdir(parents=True, exist_ok=True)
        completed_dir.mkdir(parents=True, exist_ok=True)
        for champ, info in owned.items():
            completed_prompt = completed_dir / f"{champ}_prompt.completed.md"
            if completed_prompt.exists():
                print(f"[SKIP] Completed prompt exists for {champ}, skipping intake.")
                continue
            prompt_file = prompt_dir / f"{champ}_prompt.md"
            if not prompt_file.exists():
                rarity_val = info.get('rarity', '')
                rarity_num = [k for k, v in RARITY_MAP.items() if v == rarity_val]
                rarity_arg = rarity_num[0] if rarity_num else rarity_val
                print(f"Triggering intake for {champ} (rarity: {rarity_arg}) - prompt file not found.")
                os.system(f"python ChampionIntake/Champ_Intake.py '{champ}' {rarity_arg}")
        print("Completed intake for all champions in the owned list.")
        return

    # Interactive prompt for input method if not specified by argument
    input_file = args.input
    if not input_file:
        print("How would you like to add champions?")
        print("1. Import from a file (CSV, JSON, Markdown)")
        print("2. Enter champions manually")
        choice = input("Enter 1 or 2: ").strip()
        if choice == "1":
            input_file = input("Enter the path to the import file: ").strip()
            if not input_file:
                print("No file provided. Exiting.")
                return

    if input_file:
        champions = parse_input_file(input_file)
        new_entries = []
        for name, rarity in champions:
            rarity_norm = normalize_rarity(rarity)
            if name in owned:
                owned[name]['rarity'] = rarity_norm or owned[name]['rarity']
            else:
                owned[name] = {'rarity': rarity_norm}
                new_entries.append(name)
        write_owned_list(owned)
        print(f"Updated {len(champions)} champions. New: {', '.join(new_entries) if new_entries else 'None'}.")
    else:
        print("Enter champion names and rarity (number or string). Leave name blank to finish.")
        while True:
            name = input("Champion name: ").strip()
            if not name:
                break
            rarity = input("Rarity (number or string): ").strip()
            rarity_norm = normalize_rarity(rarity)
            if name in owned:
                owned[name]['rarity'] = rarity_norm or owned[name]['rarity']
            else:
                owned[name] = {'rarity': rarity_norm}
            write_owned_list(owned)
            print(f"Added/updated: {name}")

    # After updating, trigger intake for all champions in the owned list that do not have a completed prompt
    if args.trigger_intake:
        repo_root = Path(__file__).parent.parent.resolve()
        prompt_dir = repo_root / "input" / "Prompt"
        completed_dir = repo_root / "output" / "completed_prompts"
        prompt_dir.mkdir(parents=True, exist_ok=True)
        completed_dir.mkdir(parents=True, exist_ok=True)
        for champ in owned:
            completed_prompt = completed_dir / f"{champ}_prompt.completed.md"
            if completed_prompt.exists():
                print(f"[SKIP] Completed prompt exists for {champ}, skipping intake.")
                continue
            prompt_file = prompt_dir / f"{champ}_prompt.md"
            if not prompt_file.exists():
                rarity_val = owned[champ]['rarity']
                rarity_num = [k for k, v in RARITY_MAP.items() if v == rarity_val]
                rarity_arg = rarity_num[0] if rarity_num else rarity_val
                print(f"Triggering intake for {champ} (rarity: {rarity_arg}) - prompt file not found.")
                os.system(f"python ChampionIntake/Champ_Intake.py '{champ}' {rarity_arg}")

if __name__ == "__main__":
    main()
