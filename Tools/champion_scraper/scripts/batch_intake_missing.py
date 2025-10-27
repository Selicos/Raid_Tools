"""
Batch process all owned champions missing from Champion_stats.md.

Reads missing_champions.txt and processes each champion through the scraper.
"""

from pathlib import Path
import subprocess
import sys

def main():
    repo_root = Path(__file__).parent.parent.parent.parent
    missing_file = Path(__file__).parent / 'missing_champions.txt'
    scraper_script = repo_root / 'Tools/champion_scraper/champion_scraper.py'
    
    if not missing_file.exists():
        print(f"[ERROR] Missing champions file not found: {missing_file}")
        return
    
    with open(missing_file, 'r', encoding='utf-8') as f:
        champions = [line.strip() for line in f if line.strip()]
    
    print(f"[BATCH] Processing {len(champions)} missing champions...")
    print()
    
    # Get rarity for each champion from Owned_champion_list.md
    owned_file = repo_root / 'input/Owned_champion_list.md'
    rarities = {}
    with open(owned_file, 'r', encoding='utf-8') as f:
        for line in f:
            if line.strip().startswith('|') and '|---' not in line and '| Name |' not in line:
                parts = [p.strip() for p in line.split('|') if p.strip()]
                if len(parts) >= 3:
                    name, owned, rarity = parts[0], parts[1], parts[2]
                    rarities[name] = rarity
    
    failed = []
    for i, champ in enumerate(champions, 1):
        rarity = rarities.get(champ, 'Legendary')  # Default to Legendary if not found
        
        print(f"\n{'='*80}")
        print(f"[BATCH] ({i}/{len(champions)}) Processing: {champ} ({rarity})")
        print(f"{'='*80}\n")
        
        try:
            # Run champion_scraper.py for this champion
            cmd = [
                sys.executable,
                str(scraper_script),
                champ,  # Positional argument, not --champion
                '--rarity', rarity
            ]
            
            result = subprocess.run(cmd, check=False, capture_output=False, text=True)
            
            if result.returncode != 0:
                print(f"[WARNING] Scraper returned non-zero exit code for {champ}")
                failed.append(champ)
        
        except Exception as e:
            print(f"[ERROR] Failed to process {champ}: {e}")
            failed.append(champ)
    
    print(f"\n{'='*80}")
    print(f"[BATCH] COMPLETE - Processed {len(champions)} champions")
    if failed:
        print(f"[BATCH] {len(failed)} FAILED:")
        for champ in failed:
            print(f"  - {champ}")
    else:
        print(f"[BATCH] All champions processed successfully!")
    print(f"{'='*80}\n")


if __name__ == '__main__':
    main()
