
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

def compare_stats(raidwiki_stats, ayumilove_stats, champion_name):
    """
    Compare stats from RaidWiki and Ayumilove OCR.
    Returns: (use_raidwiki: bool, confidence: float, differences: list)
    """
    if not raidwiki_stats or not any(v for v in raidwiki_stats.values()):
        return False, 0.0, ["No RaidWiki stats available"]
    
    if not ayumilove_stats or not any(v for v in ayumilove_stats.values()):
        return True, 100.0, ["No Ayumilove OCR stats available - using RaidWiki"]
    
    # Normalize stat keys for comparison
    stat_map = {
        'C. RATE': 'C.RATE',
        'C. DMG': 'C.DMG',
        'RESIST': 'RES',
        'ACC': 'ACC',
        'HP': 'HP',
        'ATK': 'ATK',
        'DEF': 'DEF',
        'SPD': 'SPD'
    }
    
    # Normalize Ayumilove stats
    normalized_ocr = {}
    for k, v in ayumilove_stats.items():
        mapped_key = stat_map.get(k, k)
        if v and v != '':
            try:
                normalized_ocr[mapped_key] = int(str(v).replace(',', ''))
            except (ValueError, TypeError):
                pass
    
    # Normalize RaidWiki stats
    normalized_rw = {}
    for k, v in raidwiki_stats.items():
        if v and v != '':
            try:
                normalized_rw[k] = int(str(v).replace(',', ''))
            except (ValueError, TypeError):
                pass
    
    # Compare
    matches = 0
    total = 0
    differences = []
    
    for stat in ['HP', 'ATK', 'DEF', 'SPD', 'C.RATE', 'C.DMG', 'RES', 'ACC']:
        rw_val = normalized_rw.get(stat)
        ocr_val = normalized_ocr.get(stat)
        
        if rw_val is not None and ocr_val is not None:
            total += 1
            if rw_val == ocr_val:
                matches += 1
            else:
                differences.append(f"{stat}: RaidWiki={rw_val}, OCR={ocr_val}")
        elif rw_val is not None:
            # RaidWiki has it, OCR doesn't
            differences.append(f"{stat}: RaidWiki={rw_val}, OCR=MISSING")
        elif ocr_val is not None:
            # OCR has it, RaidWiki doesn't
            differences.append(f"{stat}: RaidWiki=MISSING, OCR={ocr_val}")
    
    confidence = (matches / total * 100) if total > 0 else 0
    
    # Decision logic
    use_raidwiki = True  # Default to RaidWiki (most reliable)
    
    if confidence == 100 and total >= 6:
        print(f"[Validation] ✅ Perfect match! RaidWiki and OCR agree on all {total} stats")
    elif confidence >= 75:
        print(f"[Validation] ⚠️  Good match: {matches}/{total} stats agree ({confidence:.1f}%)")
        print(f"[Validation] Using RaidWiki stats (more reliable)")
        for diff in differences[:3]:  # Show first 3 differences
            print(f"[Validation]   - {diff}")
    else:
        print(f"[Validation] ❌ Poor match: {matches}/{total} stats agree ({confidence:.1f}%)")
        print(f"[Validation] Using RaidWiki stats, but flagging for manual review")
        for diff in differences:
            print(f"[Validation]   - {diff}")
    
    return use_raidwiki, confidence, differences


def try_all_scrapers(champion_name):
    # Hybrid approach: Try RaidWiki first for stats, Ayumilove for everything else
    # ALWAYS pull Ayumilove OCR for comparison/validation
    
    # Try RaidWiki first (most reliable for stats)
    print("[Hybrid] Trying RaidWiki for stats...")
    raidwiki_data = scrape_raidwiki_champion(champion_name)
    
    has_raidwiki_stats = (raidwiki_data and 
                          raidwiki_data.get('stats') and 
                          any(v for v in raidwiki_data.get('stats', {}).values()))
    
    # ALWAYS fetch Ayumilove (for skills/info and OCR comparison)
    print("[Hybrid] Fetching Ayumilove data (skills, info, and OCR for validation)...")
    ayumilove_data = scrape_ayumilove_champion(champion_name, skip_stats=False)  # Always OCR
    
    if has_raidwiki_stats and ayumilove_data:
        # Both sources available - compare stats
        print("[Hybrid] ✓ Both sources available - comparing stats...")
        use_raidwiki, confidence, differences = compare_stats(
            raidwiki_data.get('stats', {}),
            ayumilove_data.get('stats', {}),
            champion_name
        )
        
        # Use RaidWiki stats + Ayumilove everything else
        merged_data = {
            'info': ayumilove_data.get('info', {}),
            'stats': raidwiki_data.get('stats', {}),  # RaidWiki stats (validated)
            'skills': ayumilove_data.get('skills', []),
            'aura': ayumilove_data.get('aura', ''),
            'mechanics_tags': ayumilove_data.get('mechanics_tags', []),
            'validation': {
                'confidence': confidence,
                'differences': differences,
                'sources': 'raidwiki_stats+ayumilove_ocr_validated'
            }
        }
        return merged_data, f'raidwiki_stats+ayumilove (validated: {confidence:.1f}%)'
    
    elif has_raidwiki_stats:
        # RaidWiki only (Ayumilove failed)
        print("[Hybrid] ⚠️  Ayumilove failed - using RaidWiki only")
        return raidwiki_data, 'raidwiki'
    
    elif ayumilove_data and ayumilove_data.get('info') and ayumilove_data.get('skills'):
        # Ayumilove only (RaidWiki not available)
        print("[Hybrid] RaidWiki stats not available - using Ayumilove OCR only")
        
        # Check OCR confidence
        stats = ayumilove_data.get('stats', {})
        stats_found = sum(1 for v in stats.values() if v and v != '')
        total_stats = 8
        confidence = (stats_found / total_stats) * 100 if total_stats > 0 else 0
        
        if confidence < 75:
            print(f"[WARNING] Low OCR confidence: {stats_found}/{total_stats} stats extracted ({confidence:.1f}%)")
            print(f"[WARNING] Consider manual verification for this champion")
        
        return ayumilove_data, 'ayumilove_ocr'
    
    # Fallback: use whatever data we have
    if raidwiki_data:
        print("[Hybrid] ⚠️  Using incomplete RaidWiki data")
        return raidwiki_data, 'raidwiki_partial'
    elif ayumilove_data:
        print("[Hybrid] ⚠️  Using incomplete Ayumilove data")
        return ayumilove_data, 'ayumilove_partial'
    
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
                'C. DMG': 'C.DMG',
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
                'aura': data.get('aura', ''),
                'mechanics_tags': template_mechanics_tags
            }
            # Pass through validation metadata if available
            print(f"[DEBUG] Keys in data dict: {list(data.keys())}")
            if 'validation' in data:
                print(f"[DEBUG] Validation data found: {data['validation']}")
                scraped_data['validation'] = data['validation']
            else:
                print(f"[DEBUG] No validation key in data")
            print(f"[DEBUG] Final scraped_data keys: {list(scraped_data.keys())}")
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