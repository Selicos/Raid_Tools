def main():
    if len(sys.argv) < 2:
        print("Usage: python champion_intake_launcher.py <champion name> | --list <file>")
        sys.exit(1)

    if sys.argv[1] == '--list' and len(sys.argv) >= 3:
        with open(sys.argv[2], 'r', encoding='utf-8') as f:
            champ_names = [line.strip() for line in f if line.strip() and not line.strip().startswith('#')]
    else:
        champ_names = [sys.argv[1]]

    out_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../input/Champion_Dictionary'))

    for i, champ_name in enumerate(champ_names):
        print(f"Processing: {champ_name}")
        data, source = try_all_scrapers(champ_name)
        if data:
            info, stats, skills = data['info'], data['stats'], data['skills']
            champion_to_json(info, stats, skills, out_dir, champ_name)
            print(f"Champion JSON for {champ_name} written to {out_dir} (source: {source})")
        else:
            print(f"[ERROR] Could not fetch data for {champ_name} from any source.")
        if len(champ_names) > 1 and i < len(champ_names) - 1:
            pause = random.randint(5, 10)
            print(f"Pausing {pause} seconds before next champion...")
            time.sleep(pause)

if __name__ == "__main__":
    main()
import sys
import os
import time
import random
from Tools.champion_scraper.scrape_raidwiki import scrape_raidwiki_champion
from Tools.champion_scraper.scrape_ayumilove import scrape_ayumilove_champion
from Tools.champion_scraper.champion_to_json import champion_to_json

def merge_champion_data(primary, fallback):
    # Merge missing fields from fallback into primary
    if not primary:
        return fallback
    if not fallback:
        return primary
    merged = {}
    for key in ['info', 'stats', 'skills']:
        if key == 'skills':
            merged[key] = primary.get(key) if primary.get(key) else fallback.get(key)
        else:
            merged[key] = primary.get(key) if primary.get(key) else fallback.get(key)
    return merged

def try_all_scrapers(champion_name):
    # Try RaidWiki first
    data = scrape_raidwiki_champion(champion_name)
    if data and data['info'] and data['stats'] and data['skills']:
        return data, 'raidwiki'
    # Try Ayumilove as fallback
    fallback = scrape_ayumilove_champion(champion_name)
    merged
    if merged and merged['info'] and merged['stats'] and merged['skills']:
        return merged, 'ayumilove+raidwiki'
    if fallback:
        return fallback, 'ayumilove'
    return None, None

if __name__ == "__main__":
    main()
