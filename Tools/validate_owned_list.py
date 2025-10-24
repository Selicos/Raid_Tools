"""
Validation Script for Owned Champion List
------------------------------------------
Validates the format, consistency, and integrity of input/Owned_champion_list.md

Checks:
1. Format consistency: Name | Rarity | Affinity | Faction | Last Updated
2. Alphabetical ordering
3. Duplicate detection
4. Valid rarity values (Common, Uncommon, Rare, Epic, Legendary, Mythic)
5. Valid affinity values (Magic, Force, Spirit, Void)
6. Date format validation (YYYY-MM-DD)

Usage:
    python Tools/validate_owned_list.py
    python Tools/validate_owned_list.py --fix-order  # Auto-fix alphabetical order
"""

import re
import sys
from datetime import datetime
from pathlib import Path
from typing import List, Tuple, Dict

# Valid values
VALID_RARITIES = ['Common', 'Uncommon', 'Rare', 'Epic', 'Legendary', 'Mythic']
VALID_AFFINITIES = ['Magic', 'Force', 'Spirit', 'Void']


# Updated ChampionEntry for markdown table rows
class ChampionEntry:
    def __init__(self, columns: list, line_number: int):
        self.line_number = line_number
        self.name = columns[0].strip() if len(columns) > 0 else None
        self.rarity = columns[1].strip() if len(columns) > 1 else None
        self.affinity = columns[2].strip() if len(columns) > 2 else None
        self.faction = columns[3].strip() if len(columns) > 3 else None
        self.last_updated = columns[4].strip() if len(columns) > 4 else None
        self.is_valid = False
        self.errors = []
        self.parse()

    def parse(self):
        # Validate required fields
        if not self.name:
            self.errors.append(f"Line {self.line_number}: Missing champion name")
        if not self.rarity:
            self.errors.append(f"Line {self.line_number}: Missing rarity field")
        if not self.affinity:
            self.errors.append(f"Line {self.line_number}: Missing affinity field")
        if not self.faction:
            self.errors.append(f"Line {self.line_number}: Missing faction field")
        if not self.last_updated:
            self.errors.append(f"Line {self.line_number}: Missing 'Last Updated' field")

        # Validate rarity
        if self.rarity and self.rarity not in VALID_RARITIES:
            self.errors.append(f"Line {self.line_number}: Invalid rarity '{self.rarity}' (must be one of {VALID_RARITIES})")
        # Validate affinity
        if self.affinity and self.affinity not in VALID_AFFINITIES:
            self.errors.append(f"Line {self.line_number}: Invalid affinity '{self.affinity}' (must be one of {VALID_AFFINITIES})")
        # Validate date
        if self.last_updated:
            try:
                datetime.strptime(self.last_updated, '%Y-%m-%d')
            except ValueError:
                self.errors.append(f"Line {self.line_number}: Invalid date format '{self.last_updated}' (expected YYYY-MM-DD)")

        self.is_valid = len(self.errors) == 0

    def __str__(self):
        return f"| {self.name} | {self.rarity} | {self.affinity} | {self.faction} | {self.last_updated} |"


def validate_owned_list(file_path: Path, fix_order: bool = False) -> Tuple[bool, List[str]]:
    """
    Validate owned champion list
    
    Args:
        file_path: Path to Owned_champion_list.md
        fix_order: If True, auto-fix alphabetical ordering
    
    Returns:
        Tuple of (is_valid, list of error messages)
    """
    errors = []
    warnings = []
    
    if not file_path.exists():
        return False, [f"ERROR: File not found: {file_path}"]
    
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    

    # Parse champions from markdown table
    champions: List[ChampionEntry] = []
    in_table = False
    header_found = False
    for i, line in enumerate(lines, start=1):
        line_stripped = line.strip()
        # Detect table header
        if line_stripped.startswith('| Name') and 'Last Updated' in line_stripped:
            in_table = True
            header_found = True
            continue
        if in_table:
            # Skip separator row
            if line_stripped.startswith('|---'):
                continue
            # End of table (empty line or not a table row)
            if not line_stripped or not line_stripped.startswith('|'):
                break
            # Parse table row
            columns = [col.strip() for col in line_stripped.strip('|').split('|')]
            if len(columns) < 5:
                continue  # skip malformed rows
            entry = ChampionEntry(columns, i)
            if not entry.is_valid:
                errors.extend(entry.errors)
            champions.append(entry)

    print(f"✅ Parsed {len(champions)} champion entries from table")
    

    # Check for duplicates
    seen_names = {}
    for champ in champions:
        if champ.name in seen_names:
            errors.append(f"ERROR: Duplicate champion '{champ.name}' found on lines {seen_names[champ.name]} and {champ.line_number}")
        else:
            seen_names[champ.name] = champ.line_number

    # Check alphabetical order
    champion_names = [c.name for c in champions if c.name]
    sorted_names = sorted(champion_names, key=str.lower)

    if champion_names != sorted_names:
        warnings.append(f"WARNING: Champion list is not in alphabetical order")
        # Show first few out-of-order entries
        mismatches = []
        for i, (actual, expected) in enumerate(zip(champion_names, sorted_names)):
            if actual != expected:
                mismatches.append(f"  Position {i+1}: Found '{actual}', expected '{expected}'")
                if len(mismatches) >= 5:
                    mismatches.append("  ... (more mismatches)")
                    break
        warnings.extend(mismatches)
        # Always fix order if not sorted
        print("\n🔧 Fixing alphabetical order...")
        champions_sorted = sorted(champions, key=lambda c: c.name.lower() if c.name else '')
        new_lines = []
        wrote_table = False
        in_table = False
        for line in lines:
            line_stripped = line.strip()
            # Write table header and separator
            if not wrote_table and line_stripped.startswith('| Name') and 'Last Updated' in line_stripped:
                new_lines.append(line)
                wrote_table = True
                in_table = True
                continue
            if wrote_table and line_stripped.startswith('|---'):
                new_lines.append(line)
                # Write sorted, deduplicated champion rows
                seen = set()
                for champ in champions_sorted:
                    if champ.name not in seen:
                        new_lines.append(str(champ) + '\n')
                        seen.add(champ.name)
                wrote_table = False  # Only write once
                in_table = False
                continue
            # Skip all original champion rows in the table
            if in_table and line_stripped.startswith('|') and not line_stripped.startswith('|---') and not line_stripped.startswith('| Name'):
                continue
            # Keep other lines (headers, notes, etc.)
            new_lines.append(line)
        with open(file_path, 'w', encoding='utf-8') as f:
            f.writelines(new_lines)
        print(f"✅ Fixed alphabetical order and saved to {file_path}")
        warnings = []  # Clear warnings since we fixed it
    

    # Check for missing fields (affinity, faction)
    missing_affinity = sum(1 for c in champions if not c.affinity)
    missing_faction = sum(1 for c in champions if not c.faction)
    if missing_affinity > 0:
        warnings.append(f"WARNING: {missing_affinity} champions missing Affinity field")
    if missing_faction > 0:
        warnings.append(f"WARNING: {missing_faction} champions missing Faction field")
    
    # Summary
    print("\n" + "="*60)
    print("VALIDATION SUMMARY")
    print("="*60)
    print(f"Total Champions: {len(champions)}")
    print(f"Valid Entries: {sum(1 for c in champions if c.is_valid)}")
    print(f"Errors: {len(errors)}")
    print(f"Warnings: {len(warnings)}")
    
    if errors:
        print("\n❌ ERRORS:")
        for error in errors:
            print(f"  {error}")
    
    if warnings:
        print("\n⚠️  WARNINGS:")
        for warning in warnings:
            print(f"  {warning}")
    
    if not errors and not warnings:
        print("\n✅ All validation checks passed!")
    
    is_valid = len(errors) == 0
    return is_valid, errors + warnings


def main():
    """Main entry point"""
    import argparse
    
    parser = argparse.ArgumentParser(description='Validate Owned Champion List')
    parser.add_argument('--file', type=str, default='input/Owned_champion_list.md', help='Path to owned list file')

    args = parser.parse_args()

    # Resolve file path
    script_dir = Path(__file__).parent.parent
    file_path = script_dir / args.file

    print(f"Validating: {file_path}")
    print("="*60 + "\n")

    is_valid, messages = validate_owned_list(file_path)

    sys.exit(0 if is_valid else 1)


if __name__ == '__main__':
    main()
