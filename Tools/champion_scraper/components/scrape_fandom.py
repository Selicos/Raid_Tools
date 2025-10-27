"""
Scrape champion data from local Champion_stats.md reference table.

This module provides fast, validated champion stats from the local Champion_stats.md
file which serves as the primary reference for base stats. The table is cached in
memory for efficient batch processing.

Priority: Champion_stats.md → Ayumilove → HellHades → RaidWiki
"""

from pathlib import Path
import re

# Module-level cache for Champion_stats.md table
_fandom_table_cache = None

def load_fandom_table(force_reload=False, debug=False):
    """
    Load Champion_stats.md into memory cache.
    
    Args:
        force_reload (bool): Force reload from file even if cached
        debug (bool): Print debug status messages
    
    Returns:
        dict: {champion_name: {'info': {...}, 'stats': {...}}}
    
    Cache persists across multiple scrape_fandom_champion() calls for batch efficiency.
    """
    global _fandom_table_cache
    
    if _fandom_table_cache is not None and not force_reload:
        return _fandom_table_cache
    
    table_path = Path('c:/GIT/Raid_Tools/input/Champion_Dictionary/Champion_stats.md')
    
    if not table_path.exists():
        raise FileNotFoundError(f"Champion_stats.md not found at {table_path}")
    
    if debug:
        print(f"[FANDOM] Loading from: {table_path}")
    
    with open(table_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    champions = parse_champion_markdown_table(content)
    
    # Build lookup dict: key = champion name (exact match)
    _fandom_table_cache = {}
    for champ in champions:
        name = champ.get('name')
        if name:
            _fandom_table_cache[name] = {
                'info': {
                    'name': champ.get('name', ''),
                    'faction': champ.get('faction', ''),
                    'rarity': champ.get('rarity', ''),
                    'role': champ.get('role', ''),
                    'affinity': champ.get('affinity', ''),
                },
                'stats': {
                    'HP': champ.get('hp', ''),
                    'ATK': champ.get('atk', ''),
                    'DEF': champ.get('def', ''),
                    'SPD': champ.get('spd', ''),
                    'C.RATE': champ.get('crate', ''),
                    'C.DMG': champ.get('cdmg', ''),
                    'RES': champ.get('resist', ''),
                    'ACC': champ.get('accuracy', ''),
                },
                'aura': {
                    'stat': champ.get('aura', ''),
                    'magnitude': champ.get('aura_magnitude', ''),
                    'location': champ.get('aura_location', ''),
                    'affinity': champ.get('aura_for', ''),
                }
            }
    
    if debug:
        print(f"[FANDOM] Loaded {len(_fandom_table_cache)} champions from Champion_stats.md")
    
    return _fandom_table_cache


def parse_champion_markdown_table(content):
    """
    Parse the champion table from Champion_stats.md markdown file.
    
    Args:
        content (str): Full markdown file content
    
    Returns:
        list: List of champion dicts with stats and info
    """
    champions = []
    lines = content.split('\n')
    in_table = False
    
    for idx, line in enumerate(lines):
        # Find table header
        if '| Name' in line and '| Faction' in line:
            in_table = True
            continue
        
        # Skip separator row
        if in_table and '---' in line:
            continue
        
        # Parse data rows
        if in_table and line.strip().startswith('|'):
            cells = [cell.strip() for cell in line.split('|')]
            cells = [c for c in cells if c]  # Remove empty elements
            
            if len(cells) < 2:
                continue
            
            name = cells[0].strip()
            
            # Skip empty names or invalid rows
            if not name or name == '-' or len(name) < 2:
                continue
            
            # Extract champion data (column order from Champion_stats.md)
            # Columns: Name, Faction, Rarity, Role, Affinity, HP, ATK, DEF, SPD, C.Rate, C.DMG, RES, ACC, Aura, Aura magnitude, Aura location, Aura for
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
                'aura': cells[13] if len(cells) > 13 else '',
                'aura_magnitude': cells[14] if len(cells) > 14 else '',
                'aura_location': cells[15] if len(cells) > 15 else '',
                'aura_for': cells[16] if len(cells) > 16 else '',
            }
            
            champions.append(champ)
    
    return champions


def scrape_fandom_champion(champion_name, debug=False):
    """
    Lookup specific champion from cached Champion_stats.md table.
    
    Args:
        champion_name (str): Champion name (exact match required)
        debug (bool): Print debug messages
    
    Returns:
        dict: {'info': {...}, 'stats': {...}, 'aura': {...}} or None if not found
    """
    table = load_fandom_table(debug=debug)
    
    # Exact match (case-sensitive)
    champion_data = table.get(champion_name)
    
    if not champion_data:
        print(f"[FANDOM] ⚠️  Champion '{champion_name}' not found in Champion_stats.md")
        print(f"[FANDOM] → Using full champion name. Will add to table after scrape if --update-table flag set.")
        return None
    
    # Validate that stats are present and not empty
    stats = champion_data.get('stats', {})
    stats_present = sum(1 for v in stats.values() if v and v != '' and v != '-' and v != '\\-')
    
    if stats_present == 0:
        if debug:
            print(f"[FANDOM] ⚠️  Champion '{champion_name}' in table but has no stats")
        return None
    
    return champion_data


def get_fandom_champions_list():
    """
    Return list of all champion names in Champion_stats.md table.
    
    Returns:
        list: Alphabetized list of champion names
    """
    table = load_fandom_table()
    return sorted(table.keys())


def clear_cache():
    """Clear the cached Champion_stats.md table (for testing/debugging)."""
    global _fandom_table_cache
    _fandom_table_cache = None
