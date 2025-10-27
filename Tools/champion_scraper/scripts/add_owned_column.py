"""
Add 'Owned' column to Champion_stats.md table.

Reads Owned_champion_list.md and adds an 'Owned' column showing:
- Number owned (e.g., 1, 2, 3)
- Empty for champions not owned

Usage:
    python Tools/champion_scraper/scripts/add_owned_column.py
"""

import re
from pathlib import Path


def parse_owned_champions(owned_file: Path) -> dict:
    """
    Parse Owned_champion_list.md and return dict of {champion_name: count}.
    
    Handles formats like:
    - "Apothecary (x3)" -> {"Apothecary": 3}
    - "Arbiter" -> {"Arbiter": 1}
    """
    owned = {}
    
    with open(owned_file, 'r', encoding='utf-8') as f:
        for line in f:
            # Look for table rows starting with |
            if not line.strip().startswith('|') or '|---' in line or '| Name |' in line:
                continue
            
            # Parse champion name (first column)
            parts = [p.strip() for p in line.split('|') if p.strip()]
            if not parts:
                continue
            
            name_field = parts[0]
            
            # Check for quantity like "Coldheart (x3)"
            match = re.match(r'(.+?)\s*\(x(\d+)\)', name_field)
            if match:
                name = match.group(1).strip()
                count = int(match.group(2))
            else:
                name = name_field.strip()
                count = 1
            
            owned[name] = count
    
    print(f"[OWNED] Loaded {len(owned)} owned champions")
    return owned


def add_owned_column_to_table(table_file: Path, owned_dict: dict):
    """
    Add 'Owned' column to Champion_stats.md table.
    
    Inserts the column after ACC (column 12) and before Aura (column 13).
    """
    with open(table_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    updated_lines = []
    updated_count = 0
    
    for line in lines:
        # Skip non-table lines
        if not line.strip().startswith('|'):
            updated_lines.append(line)
            continue
        
        # Parse table row
        cells = [c.strip() for c in line.split('|')]
        
        # Remove leading/trailing empty cells
        if cells and cells[0] == '':
            cells = cells[1:]
        if cells and cells[-1] == '':
            cells = cells[:-1]
        
        if len(cells) < 2:
            updated_lines.append(line)
            continue
        
        # Check if this is the header row
        if cells[0] == 'Name':
            # Header already has Owned column (added manually)
            updated_lines.append(line)
            continue
        
        # Check if this is the separator row
        if '---' in cells[0]:
            # Separator already updated (added manually)
            updated_lines.append(line)
            continue
        
        # This is a data row
        champion_name = cells[0]
        
        # Get owned count
        owned_count = owned_dict.get(champion_name, 0)
        owned_value = str(owned_count) if owned_count > 0 else '\\-'
        
        # Insert 'Owned' column after ACC (index 12)
        # Column order: Name(0), Faction(1), Rarity(2), Role(3), Affinity(4), 
        #               HP(5), ATK(6), DEF(7), SPD(8), C.Rate(9), C.DMG(10), RES(11), ACC(12),
        #               [INSERT OWNED HERE], Aura(13), Aura mag(14), Aura loc(15), Aura for(16)
        
        if len(cells) >= 13:
            # Insert owned column before index 13 (Aura)
            new_cells = cells[:13] + [owned_value] + cells[13:]
        else:
            # Table has fewer columns, just append
            new_cells = cells + [owned_value]
        
        # Rebuild row
        new_line = '| ' + ' | '.join(new_cells) + ' |\n'
        updated_lines.append(new_line)
        
        if owned_count > 0:
            updated_count += 1
    
    # Write updated table
    with open(table_file, 'w', encoding='utf-8') as f:
        f.writelines(updated_lines)
    
    print(f"[OWNED] Updated {updated_count} champions with owned status")


def main():
    """Main entry point."""
    repo_root = Path(__file__).parent.parent.parent.parent
    
    owned_file = repo_root / 'input/Owned_champion_list.md'
    table_file = repo_root / 'input/Champion_Dictionary/Champion_stats.md'
    
    if not owned_file.exists():
        print(f"[ERROR] Owned champions file not found: {owned_file}")
        return
    
    if not table_file.exists():
        print(f"[ERROR] Champion stats table not found: {table_file}")
        return
    
    # Parse owned champions
    owned_dict = parse_owned_champions(owned_file)
    
    # Add owned column to table
    add_owned_column_to_table(table_file, owned_dict)
    
    print(f"[OWNED] Done! Column added to {table_file.name}")


if __name__ == '__main__':
    main()
