"""
Update Champion_stats.md table with all Complete/ champions and alphabetize.
Extracts data from Complete/ JSONs and merges with existing Champion_stats.md table.
"""

import json
from pathlib import Path

def load_complete_champions():
    """Load all Complete/ champion JSONs"""
    complete_dir = Path('c:/GIT/Raid_Tools/input/Champion_Dictionary/Complete')
    champions = {}
    
    for json_file in complete_dir.glob('*.json'):
        try:
            with open(json_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
                
                # Extract base stats from first form
                stats = {}
                if data.get('forms') and len(data['forms']) > 0:
                    stats = data['forms'][0].get('base_stats', {})
                
                # Extract aura info (if present)
                aura_info = data.get('aura', {})
                
                champions[data.get('name')] = {
                    'name': data.get('name'),
                    'faction': data.get('faction', ''),
                    'rarity': data.get('rarity', ''),
                    'role': data.get('role', ''),
                    'affinity': data.get('affinity', ''),
                    'hp': stats.get('HP', ''),
                    'atk': stats.get('ATK', ''),
                    'def': stats.get('DEF', ''),
                    'spd': stats.get('SPD', ''),
                    'crate': stats.get('C.RATE', ''),
                    'cdmg': stats.get('C.DMG', ''),
                    'res': stats.get('RES', ''),
                    'acc': stats.get('ACC', ''),
                    'aura_stat': aura_info.get('stat', '\\-'),
                    'aura_magnitude': aura_info.get('magnitude', '\\-'),
                    'aura_location': aura_info.get('location', '\\-'),
                    'aura_affinity': aura_info.get('affinity', '\\-'),
                }
        except Exception as e:
            print(f"[ERROR] Failed to load {json_file.name}: {e}")
    
    print(f"[LOCAL] Loaded {len(champions)} champions from Complete/")
    return champions

def load_existing_table():
    """Load existing Champion_stats.md table"""
    md_path = Path('c:/GIT/Raid_Tools/input/Champion_Dictionary/Champion_stats.md')
    champions = {}
    
    with open(md_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    lines = content.split('\n')
    
    # Find table rows (skip header and separator)
    in_table = False
    
    for idx, line in enumerate(lines):
        # Skip until we find the table header
        if '| Name' in line and '| Faction' in line:
            in_table = True
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
            
            name = cells[0].strip()
            
            # Skip empty names or invalid rows
            if not name or name == '-' or len(name) < 2:
                continue
            
            champions[name] = {
                'name': name,
                'faction': cells[1] if len(cells) > 1 else '',
                'rarity': cells[2] if len(cells) > 2 else '',
                'role': cells[3] if len(cells) > 3 else '',
                'affinity': cells[4] if len(cells) > 4 else '',
                'hp': cells[5] if len(cells) > 5 else '',
                'atk': cells[6] if len(cells) > 6 else '',
                'def': cells[7] if len(cells) > 7 else '',
                'spd': cells[8] if len(cells) > 8 else '',
                'crate': cells[9] if len(cells) > 9 else '',
                'cdmg': cells[10] if len(cells) > 10 else '',
                'res': cells[11] if len(cells) > 11 else '',
                'acc': cells[12] if len(cells) > 12 else '',
                'aura_stat': cells[13] if len(cells) > 13 else '\\-',
                'aura_magnitude': cells[14] if len(cells) > 14 else '\\-',
                'aura_location': cells[15] if len(cells) > 15 else '\\-',
                'aura_affinity': cells[16] if len(cells) > 16 else '\\-',
            }
    
    print(f"[EXISTING] Loaded {len(champions)} champions from Champion_stats.md")
    return champions

def merge_and_sort_champions(existing, complete):
    """Merge existing table with Complete/ champions, preferring Complete/ data"""
    merged = {}
    
    # Start with existing champions
    for name, data in existing.items():
        merged[name] = data
    
    # Update/add Complete/ champions (overwrites existing with Complete/ data)
    for name, data in complete.items():
        merged[name] = data
        print(f"[MERGE] Updated/added: {name}")
    
    # Sort alphabetically by name
    sorted_champions = dict(sorted(merged.items()))
    
    print(f"[MERGE] Total champions: {len(sorted_champions)}")
    return sorted_champions

def format_table_row(champ):
    """Format a champion as a markdown table row"""
    # Convert C.RATE and C.DMG to decimal format (15 -> 0.15)
    crate = champ.get('crate', '')
    cdmg = champ.get('cdmg', '')
    
    if crate and crate != '\\-':
        try:
            crate_num = float(crate)
            crate = f"{crate_num / 100:.2f}" if crate_num >= 1 else str(crate)
        except ValueError:
            pass
    
    if cdmg and cdmg != '\\-':
        try:
            cdmg_num = float(cdmg)
            cdmg = f"{cdmg_num / 100:.2f}" if cdmg_num >= 1 else str(cdmg)
        except ValueError:
            pass
    
    return (
        f"| {champ.get('name', '')} "
        f"| {champ.get('faction', '')} "
        f"| {champ.get('rarity', '')} "
        f"| {champ.get('role', '')} "
        f"| {champ.get('affinity', '')} "
        f"| {champ.get('hp', '')} "
        f"| {champ.get('atk', '')} "
        f"| {champ.get('def', '')} "
        f"| {champ.get('spd', '')} "
        f"| {crate} "
        f"| {cdmg} "
        f"| {champ.get('res', '')} "
        f"| {champ.get('acc', '')} "
        f"| {champ.get('aura_stat', '\\-')} "
        f"| {champ.get('aura_magnitude', '\\-')} "
        f"| {champ.get('aura_location', '\\-')} "
        f"| {champ.get('aura_affinity', '\\-')} |"
    )

def write_updated_table(champions):
    """Write updated table to Champion_stats.md"""
    md_path = Path('c:/GIT/Raid_Tools/input/Champion_Dictionary/Champion_stats.md')
    
    # Create header
    header = """## Champion stats and other basic information

## This is not a comprehensive table. Values on this table need to be validated using ayumilove scrape, and raidwiki if available
## From: https://raidshadowlegends.fandom.com/wiki/Champion_List
## Updated with Complete/ champion JSONs - Complete/ data takes precedence


| Name | Faction | Rarity | Role | Affinity | HP | ATK | DEF | SPD | C. Rate | C. DMG | RES | ACC | Aura | Aura magnitude | Aura location | Aura for |
| ---- | ------- | ------ | ---- | -------- | -- | --- | --- | --- | ------- | ------ | --- | --- | ---- | -------------- | ------------- | -------- |
"""
    
    # Create rows
    rows = []
    for name in sorted(champions.keys()):
        rows.append(format_table_row(champions[name]))
    
    # Write file
    content = header + '\n'.join(rows) + '\n'
    
    with open(md_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"[WRITE] Updated Champion_stats.md with {len(champions)} champions (alphabetized)")

def main():
    """Main workflow"""
    print("Updating Champion_stats.md table...\n")
    
    # Load Complete/ champions
    complete_champions = load_complete_champions()
    
    # Load existing table
    existing_champions = load_existing_table()
    
    # Merge and sort
    merged_champions = merge_and_sort_champions(existing_champions, complete_champions)
    
    # Write updated table
    write_updated_table(merged_champions)
    
    print(f"\n✓ Champion_stats.md updated successfully!")
    print(f"  - Total champions: {len(merged_champions)}")
    print(f"  - From Complete/ JSONs: {len(complete_champions)}")
    print(f"  - From existing table: {len(existing_champions)}")
    print(f"  - Table is now alphabetized by champion name")

if __name__ == '__main__':
    main()
