"""
Sync Champion_stats.md table with data from JSON files.

Reads all champion JSON files from input/Champion_Dictionary/
and updates the Champion_stats.md table with their stats.

Usage:
    python Tools/champion_scraper/scripts/sync_table_from_json.py [--dry-run]
"""

import json
import sys
from pathlib import Path

# Add parent directories to path for imports
script_dir = Path(__file__).parent
champion_scraper_dir = script_dir.parent
components_dir = champion_scraper_dir / 'components'
sys.path.insert(0, str(components_dir))

from champion_to_json import update_champion_in_table


def sync_all_champions(json_dir: Path, dry_run: bool = False):
    """
    Read all JSON files and sync their stats to Champion_stats.md.
    
    Args:
        json_dir: Directory containing champion JSON files
        dry_run: If True, show what would be updated without making changes
    """
    json_files = list(json_dir.glob('*.json'))
    
    if not json_files:
        print(f"[SYNC] No JSON files found in {json_dir}")
        return
    
    print(f"[SYNC] Found {len(json_files)} JSON files")
    print(f"[SYNC] {'DRY RUN - ' if dry_run else ''}Syncing to Champion_stats.md...")
    print()
    
    updated = 0
    skipped = 0
    errors = 0
    
    for json_file in sorted(json_files):
        try:
            with open(json_file, 'r', encoding='utf-8') as f:
                champion_data = json.load(f)
            
            champion_name = champion_data.get('name', '')
            
            if not champion_name:
                print(f"[SYNC] ⚠️  Skipping {json_file.name}: no name in JSON")
                skipped += 1
                continue
            
            # Get base stats from first form
            base_stats = {}
            if 'forms' in champion_data and len(champion_data['forms']) > 0:
                base_stats = champion_data['forms'][0].get('base_stats', {})
            
            # Check if any stats are populated (not empty, not \-, not 0)
            has_stats = any(
                v and v not in ['', '-', '\\-', 0, '0']
                for v in base_stats.values()
            )
            
            if not has_stats:
                print(f"[SYNC] ⚠️  Skipping {champion_name}: no stats in JSON")
                skipped += 1
                continue
            
            if dry_run:
                print(f"[SYNC] Would update: {champion_name}")
                updated += 1
            else:
                # Update table
                update_champion_in_table(champion_name, champion_data)
                print(f"[SYNC] ✓ Updated: {champion_name}")
                updated += 1
                
        except Exception as e:
            print(f"[SYNC] ❌ Error processing {json_file.name}: {e}")
            errors += 1
    
    print()
    print(f"[SYNC] Summary:")
    print(f"[SYNC]   Updated: {updated}")
    print(f"[SYNC]   Skipped: {skipped}")
    print(f"[SYNC]   Errors: {errors}")
    
    if dry_run:
        print(f"[SYNC] DRY RUN complete - no changes made")
        print(f"[SYNC] Run without --dry-run to apply updates")


def main():
    """Main entry point."""
    import argparse
    
    parser = argparse.ArgumentParser(description='Sync Champion_stats.md from JSON files')
    parser.add_argument('--dry-run', action='store_true',
                        help='Show what would be updated without making changes')
    parser.add_argument('--dir', type=str, default='input/Champion_Dictionary',
                        help='Directory containing JSON files (default: input/Champion_Dictionary)')
    
    args = parser.parse_args()
    
    # Get JSON directory
    json_dir = Path(args.dir)
    if not json_dir.is_absolute():
        # Relative to repo root
        json_dir = Path(__file__).parent.parent.parent.parent / args.dir
    
    if not json_dir.exists():
        print(f"[ERROR] Directory not found: {json_dir}")
        sys.exit(1)
    
    sync_all_champions(json_dir, dry_run=args.dry_run)


if __name__ == '__main__':
    main()
