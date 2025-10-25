
import sys
import os
import time
import random
from components.scrape_raidwiki import scrape_raidwiki_champion
from components.scrape_ayumilove import scrape_ayumilove_champion
from components.champion_to_json import generate_champion_json, diff_champion_jsons

def merge_champion_data(primary, fallback):
    # Merge missing fields from fallback into primary
    if not primary:
        return fallback
    if not fallback:
        return primary
    merged = {}
    for key in ['info', 'stats', 'skills']:
        merged[key] = primary.get(key) if primary.get(key) else fallback.get(key)
    return merged

def try_all_scrapers(champion_name):
    # Try RaidWiki first
    data = scrape_raidwiki_champion(champion_name)
    if data and data.get('info') and data.get('stats') and data.get('skills'):
        return data, 'raidwiki'
    # Try Ayumilove as fallback
    fallback = scrape_ayumilove_champion(champion_name)
    merged = merge_champion_data(data, fallback)
    if merged and merged.get('info') and merged.get('stats') and merged.get('skills'):
        return merged, 'ayumilove+raidwiki'
    if fallback:
        return fallback, 'ayumilove'
    return None, None

def main():
    if len(sys.argv) < 2:
        print("Usage: python champion_scraper.py <champion name> | --list <file>")
        sys.exit(1)

    if sys.argv[1] == '--list' and len(sys.argv) >= 3:
        with open(sys.argv[2], 'r', encoding='utf-8') as f:
            champ_names = [line.strip() for line in f if line.strip() and not line.strip().startswith('#')]
    else:
        champ_names = [sys.argv[1]]

    template_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../input/Templates/Champion_Dictionary_Template.json'))
    out_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../input/Champion_Dictionary'))

    for i, champ_name in enumerate(champ_names):
        print(f"Processing: {champ_name}")
        data, source = try_all_scrapers(champ_name)
        output_path = os.path.join(out_dir, f"{champ_name.replace(' ', '_')}.json")
        if data:
            # If file exists, generate diff log
            if os.path.exists(output_path):
                with open(output_path, 'r', encoding='utf-8') as f:
                    old_json = f.read()
                try:
                    import json
                    old_json = json.loads(old_json)
                except Exception as e:
                    print(f"[ERROR] Failed to load existing JSON for diff: {e}")
                    old_json = None
            else:
                old_json = None
            # Map scraped info/stats keys to template field names
            info = data.get('info', {})
            stats = data.get('stats', {})
            skills = data.get('skills', [])
            # Key mapping for top-level fields
            info_map = {
                'Faction': 'faction',
                'Affinity': 'affinity',
                'Rarity': 'rarity',
                'Role': 'role',
                'Name': 'name'
            }
            mapped_info = {}
            for k, v in info.items():
                mapped_info[k.lower()] = v
            # Only allow valid stat keys, fill missing with blank or zero
            valid_stats = ['HP', 'ATK', 'DEF', 'SPD', 'C.RATE', 'C.DMG', 'RES', 'ACC']
            mapped_stats = {k: '' for k in valid_stats}
            stat_map = {
                'HP': 'HP',
                'ATK': 'ATK',
                'DEF': 'DEF',
                'SPD': 'SPD',
                'C. RATE': 'C.RATE',
                'C.DMG': 'C.DMG',
                'RESIST': 'RES',
                'ACC': 'ACC'
            }
            for k, v in stats.items():
                mapped_key = stat_map.get(k, None)
                if mapped_key and mapped_key in mapped_stats:
                    mapped_stats[mapped_key] = v
            # Build scraped_data for template
            # Use template mechanics_tags value
            template_mechanics_tags = ["Relevant mechanic tags"]
            scraped_data = {
                'info': {
                    'name': mapped_info.get('name', champ_name),
                    'faction': mapped_info.get('faction', ''),
                    'affinity': mapped_info.get('affinity', ''),
                    'rarity': mapped_info.get('rarity', ''),
                    'role': mapped_info.get('role', ''),
                },
                'stats': mapped_stats,
                'skills': skills,
                'mechanics_tags': template_mechanics_tags
            }
            # If Ayumilove fallback used, map extra overview fields to comments
            if source.startswith('ayumilove') and info:
                comments = []
                if 'rank' in info and info['rank']:
                    comments.append(f"Rank: {info['rank']}")
                if 'usability' in info and info['usability']:
                    comments.append(f"Usability: {info['usability']}")
                if 'tomes' in info and info['tomes']:
                    comments.append(f"Tomes: {info['tomes']}")
                if comments:
                    scraped_data['comments'] = ' '.join(comments)
            generate_champion_json(champ_name, scraped_data, template_path, output_path)
            print(f"Champion JSON for {champ_name} written to {output_path} (source: {source})")
            # Diff log
            if old_json:
                new_json = None
                try:
                    with open(output_path, 'r', encoding='utf-8') as f:
                        new_json = json.load(f)
                except Exception as e:
                    print(f"[ERROR] Failed to load new JSON for diff: {e}")
                if new_json:
                    log_path = os.path.join(out_dir, f"Champion_diff_{champ_name.replace(' ', '_')}.log")
                    diff_champion_jsons(old_json, new_json, log_path)
        else:
            print(f"[ERROR] Could not fetch data for {champ_name} from any source.")
        if len(champ_names) > 1 and i < len(champ_names) - 1:
            pause = random.randint(5, 10)
            print(f"Pausing {pause} seconds before next champion...")
            time.sleep(pause)

if __name__ == "__main__":
    main()