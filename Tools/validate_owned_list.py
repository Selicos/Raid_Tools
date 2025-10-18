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

class ChampionEntry:
    def __init__(self, line: str, line_number: int):
        self.raw_line = line.strip()
        self.line_number = line_number
        self.name = None
        self.rarity = None
        self.affinity = None
        self.faction = None
        self.last_updated = None
        self.is_valid = False
        self.errors = []
        
        self.parse()
    
    def parse(self):
        """Parse champion entry line"""
        # Expected format: - Name | Rarity: Value | Affinity: Value | Faction: Value | Last Updated: YYYY-MM-DD
        # or legacy format: - Name | Rarity: Value | Last Updated: YYYY-MM-DD
        
        if not self.raw_line.startswith('-'):
            self.errors.append(f"Line {self.line_number}: Missing leading dash")
            return
        
        content = self.raw_line[1:].strip()
        parts = [p.strip() for p in content.split('|')]
        
        if len(parts) < 3:
            self.errors.append(f"Line {self.line_number}: Insufficient fields (need at least Name, Rarity, Last Updated)")
            return
        
        # Parse name
        self.name = parts[0].strip()
        
        # Parse remaining fields
        for part in parts[1:]:
            if ':' not in part:
                self.errors.append(f"Line {self.line_number}: Invalid field format '{part}' (expected 'Field: Value')")
                continue
            
            field, value = part.split(':', 1)
            field = field.strip()
            value = value.strip()
            
            if field == 'Rarity':
                self.rarity = value
                if value not in VALID_RARITIES:
                    self.errors.append(f"Line {self.line_number}: Invalid rarity '{value}' (must be one of {VALID_RARITIES})")
            
            elif field == 'Affinity':
                self.affinity = value
                if value not in VALID_AFFINITIES:
                    self.errors.append(f"Line {self.line_number}: Invalid affinity '{value}' (must be one of {VALID_AFFINITIES})")
            
            elif field == 'Faction':
                self.faction = value
            
            elif field == 'Last Updated':
                self.last_updated = value
                # Validate date format
                try:
                    datetime.strptime(value, '%Y-%m-%d')
                except ValueError:
                    self.errors.append(f"Line {self.line_number}: Invalid date format '{value}' (expected YYYY-MM-DD)")
        
        # Check required fields
        if not self.name:
            self.errors.append(f"Line {self.line_number}: Missing champion name")
        if not self.rarity:
            self.errors.append(f"Line {self.line_number}: Missing rarity field")
        if not self.last_updated:
            self.errors.append(f"Line {self.line_number}: Missing 'Last Updated' field")
        
        self.is_valid = len(self.errors) == 0
    
    def __str__(self):
        if self.affinity and self.faction:
            return f"- {self.name} | Rarity: {self.rarity} | Affinity: {self.affinity} | Faction: {self.faction} | Last Updated: {self.last_updated}"
        else:
            return f"- {self.name} | Rarity: {self.rarity} | Last Updated: {self.last_updated}"


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
    
    # Parse champions
    champions: List[ChampionEntry] = []
    in_list_section = False
    
    for i, line in enumerate(lines, start=1):
        line_stripped = line.strip()
        
        # Detect start of champion list
        if line_stripped.startswith('## Champion List') or line_stripped.startswith('## Owned Champions'):
            in_list_section = True
            continue
        
        # Skip empty lines and headers
        if not line_stripped or line_stripped.startswith('#'):
            continue
        
        # Parse champion entries
        if in_list_section and line_stripped.startswith('-'):
            entry = ChampionEntry(line_stripped, i)
            if not entry.is_valid:
                errors.extend(entry.errors)
            champions.append(entry)
    
    print(f"✅ Parsed {len(champions)} champion entries")
    
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
        
        if fix_order:
            print("\n🔧 Fixing alphabetical order...")
            # Re-sort champions and rewrite file
            champions_sorted = sorted(champions, key=lambda c: c.name.lower() if c.name else '')
            
            # Reconstruct file with sorted champions
            new_lines = []
            wrote_champions = False
            
            for line in lines:
                line_stripped = line.strip()
                
                # Write champions after the header
                if not wrote_champions and (line_stripped.startswith('## Champion List') or line_stripped.startswith('## Owned Champions')):
                    new_lines.append(line)
                    new_lines.append('\n')
                    for champ in champions_sorted:
                        new_lines.append(str(champ) + '\n')
                    wrote_champions = True
                
                # Skip old champion entries
                elif line_stripped.startswith('-') and ' | Rarity:' in line:
                    continue
                
                # Keep other lines (headers, notes, etc.)
                elif not wrote_champions:
                    new_lines.append(line)
            
            # Write back to file
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
    parser.add_argument('--fix-order', action='store_true', help='Auto-fix alphabetical ordering')
    parser.add_argument('--file', type=str, default='input/Owned_champion_list.md', help='Path to owned list file')
    
    args = parser.parse_args()
    
    # Resolve file path
    script_dir = Path(__file__).parent.parent
    file_path = script_dir / args.file
    
    print(f"Validating: {file_path}")
    print("="*60 + "\n")
    
    is_valid, messages = validate_owned_list(file_path, fix_order=args.fix_order)
    
    sys.exit(0 if is_valid else 1)


if __name__ == '__main__':
    main()
