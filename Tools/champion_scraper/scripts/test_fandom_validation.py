"""
Test script to validate Fandom wiki data against existing champion entries.
Fetches data from https://raidshadowlegends.fandom.com/wiki/Champion_List
and compares against our Complete/ champion JSONs.
"""

import requests
from bs4 import BeautifulSoup
import json
from pathlib import Path
import re

def load_fandom_from_local_markdown():
    """Load Fandom champion data from local Champion_stats.md file"""
    md_path = Path('c:/GIT/Raid_Tools/input/Champion_Dictionary/Champion_stats.md')
    
    print(f"[FANDOM] Loading from local file: {md_path}")
    
    if not md_path.exists():
        raise FileNotFoundError(f"Champion_stats.md not found at {md_path}")
    
    with open(md_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    return content

def parse_champion_markdown_table(content):
    """Parse the champion table from Champion_stats.md markdown file"""
    champions = []
    
    print(f"[FANDOM] Parsing markdown table...")
    
    # Split into lines
    lines = content.split('\n')
    
    # Find table rows (skip header and separator)
    in_table = False
    header_idx = None
    
    for idx, line in enumerate(lines):
        # Skip until we find the table header
        if '| Name' in line and '| Faction' in line:
            header_idx = idx
            in_table = True
            print(f"[FANDOM] Found table header at line {idx}")
            continue
        
        # Skip separator row
        if in_table and '---' in line:
            continue
        
        # Parse data rows
        if in_table and line.strip().startswith('|'):
            # Split by pipe and clean
            cells = [cell.strip() for cell in line.split('|')]
            # Remove empty first/last elements from split
            cells = [c for c in cells if c]
            
            # Need at least name + faction to be valid
            if len(cells) < 2:
                continue
            
            # Extract champion data (based on column order in Champion_stats.md)
            # Columns: Name, Faction, Rarity, Role, Affinity, HP, ATK, DEF, SPD, C.Rate, C.DMG, RES, ACC
            name = cells[0].strip()
            
            # Skip empty names or invalid rows
            if not name or name == '-' or len(name) < 2:
                continue
            
            champ = {
                'name': name,
                'faction': cells[1] if len(cells) > 1 else '',
                'rarity': cells[2] if len(cells) > 2 else '',
                'role': cells[3] if len(cells) > 3 else '',
                'affinity': cells[4] if len(cells) > 4 else '',
                'hp': cells[5].replace(',', '') if len(cells) > 5 else '',
                'atk': cells[6].replace(',', '') if len(cells) > 6 else '',
                'def': cells[7].replace(',', '') if len(cells) > 7 else '',
                'spd': cells[8].replace(',', '') if len(cells) > 8 else '',
                'crate': cells[9].replace('%', '').replace(',', '') if len(cells) > 9 else '',
                'cdmg': cells[10].replace('%', '').replace(',', '') if len(cells) > 10 else '',
                'resist': cells[11].replace(',', '') if len(cells) > 11 else '',
                'accuracy': cells[12].replace(',', '') if len(cells) > 12 else '',
            }
            
            champions.append(champ)
    
    print(f"[FANDOM] ✓ Parsed {len(champions)} champions from markdown table")
    return champions

def load_complete_champions():
    """Load all Complete/ champion JSONs"""
    complete_dir = Path('c:/GIT/Raid_Tools/input/Champion_Dictionary/Complete')
    champions = {}
    
    if not complete_dir.exists():
        print(f"[WARNING] Complete directory not found: {complete_dir}")
        return champions
    
    for json_file in complete_dir.glob('*.json'):
        try:
            with open(json_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
                name = data.get('name')
                if name:
                    champions[name] = {
                        'file': json_file.name,
                        'faction': data.get('faction'),
                        'affinity': data.get('affinity'),
                        'rarity': data.get('rarity'),
                        'role': data.get('role'),
                        'stats': data.get('forms', [{}])[0].get('base_stats', {}) if data.get('forms') else {}
                    }
        except Exception as e:
            print(f"[ERROR] Failed to load {json_file.name}: {e}")
    
    print(f"[LOCAL] Loaded {len(champions)} champions from Complete/")
    return champions

def compare_champions(fandom_data, local_data):
    """Compare Fandom data against local champion entries"""
    print(f"\n{'='*80}")
    print("VALIDATION REPORT: Fandom vs Local Champions")
    print(f"{'='*80}\n")
    
    matches = []
    mismatches = []
    
    for fandom_champ in fandom_data:
        name = fandom_champ.get('name')
        if not name:
            continue
        
        # Try exact match
        local_champ = local_data.get(name)
        
        # Try case-insensitive match
        if not local_champ:
            for local_name, local_info in local_data.items():
                if local_name.lower() == name.lower():
                    local_champ = local_info
                    break
        
        if not local_champ:
            continue
        
        # Compare info
        info_match = True
        stat_match = True
        differences = []
        
        # Check faction
        if fandom_champ.get('faction') and local_champ.get('faction'):
            if fandom_champ['faction'].lower() != local_champ['faction'].lower():
                differences.append(f"Faction: Fandom={fandom_champ['faction']} vs Local={local_champ['faction']}")
                info_match = False
        
        # Check affinity
        if fandom_champ.get('affinity') and local_champ.get('affinity'):
            if fandom_champ['affinity'].lower() != local_champ['affinity'].lower():
                differences.append(f"Affinity: Fandom={fandom_champ['affinity']} vs Local={local_champ['affinity']}")
                info_match = False
        
        # Check rarity
        if fandom_champ.get('rarity') and local_champ.get('rarity'):
            if fandom_champ['rarity'].lower() != local_champ['rarity'].lower():
                differences.append(f"Rarity: Fandom={fandom_champ['rarity']} vs Local={local_champ['rarity']}")
                info_match = False
        
        # Check stats
        local_stats = local_champ.get('stats', {})
        stat_diffs = []
        
        for stat_key in ['hp', 'atk', 'def', 'spd', 'crate', 'cdmg', 'resist', 'accuracy']:
            fandom_val = fandom_champ.get(stat_key, '').replace(',', '').strip()
            
            # Map stat keys
            local_key_map = {
                'hp': 'HP',
                'atk': 'ATK',
                'def': 'DEF',
                'spd': 'SPD',
                'crate': 'C.RATE',
                'cdmg': 'C.DMG',
                'resist': 'RES',
                'accuracy': 'ACC'
            }
            local_key = local_key_map.get(stat_key)
            local_val = str(local_stats.get(local_key, '')).replace(',', '').strip()
            
            if fandom_val and local_val and fandom_val != local_val:
                try:
                    fandom_num = float(fandom_val)
                    local_num = float(local_val)
                    
                    # Special handling for C.RATE and C.DMG (Fandom uses decimals, we use integers)
                    if stat_key in ['crate', 'cdmg']:
                        # Convert Fandom decimal to percentage (0.15 -> 15)
                        fandom_num = fandom_num * 100 if fandom_num < 1 else fandom_num
                    
                    # Allow small floating point differences
                    if abs(fandom_num - local_num) > 0.1:
                        stat_diffs.append(f"{stat_key.upper()}: Fandom={fandom_val} vs Local={local_val}")
                        stat_match = False
                except ValueError:
                    # Non-numeric comparison
                    if fandom_val != local_val:
                        stat_diffs.append(f"{stat_key.upper()}: Fandom={fandom_val} vs Local={local_val}")
                        stat_match = False
        
        if stat_diffs:
            differences.extend(stat_diffs)
        
        # Record result
        result = {
            'name': name,
            'info_match': info_match,
            'stat_match': stat_match,
            'differences': differences
        }
        
        if info_match and stat_match:
            matches.append(result)
        else:
            mismatches.append(result)
    
    # Print results
    print(f"✓ MATCHES: {len(matches)} champions")
    print(f"✗ MISMATCHES: {len(mismatches)} champions")
    print(f"{'='*80}\n")
    
    if mismatches:
        print("MISMATCHES DETAILS:\n")
        for mismatch in mismatches[:10]:  # Show first 10
            print(f"Champion: {mismatch['name']}")
            print(f"  Info Match: {'✓' if mismatch['info_match'] else '✗'}")
            print(f"  Stat Match: {'✓' if mismatch['stat_match'] else '✗'}")
            if mismatch['differences']:
                print("  Differences:")
                for diff in mismatch['differences']:
                    print(f"    - {diff}")
            print()
    
    if matches:
        print(f"\nSAMPLE MATCHES (first 5):")
        for match in matches[:5]:
            print(f"  ✓ {match['name']}")
    
    print(f"\n{'='*80}")
    print(f"SUMMARY: {len(matches)}/{len(matches) + len(mismatches)} champions validated")
    print(f"{'='*80}\n")

def main():
    """Main validation workflow"""
    print("Fandom Wiki Champion Validation Test\n")
    
    # Load Fandom data from local markdown file
    try:
        content = load_fandom_from_local_markdown()
        fandom_champions = parse_champion_markdown_table(content)
    except Exception as e:
        print(f"[ERROR] Failed to load Fandom data: {e}")
        return
    
    if not fandom_champions:
        print("[ERROR] No champions parsed from Fandom markdown")
        return
    
    print(f"\n[FANDOM] Successfully parsed {len(fandom_champions)} champions")
    
    # Show sample Fandom data
    print(f"\nSAMPLE FANDOM DATA (first 3):")
    for champ in fandom_champions[:3]:
        print(f"  {champ.get('name')}: {champ}")
    
    # Load local champions
    local_champions = load_complete_champions()
    
    # Compare
    if local_champions:
        compare_champions(fandom_champions, local_champions)
    else:
        print("[WARNING] No local champions to compare")

if __name__ == '__main__':
    main()
