
import sys
import os
import time
import random
from components.scrape_ayumilove import scrape_ayumilove_champion
from components.scrape_hellhades import scrape_hellhades_champion
from components.scrape_fandom import scrape_fandom_champion
from components.scrape_raidwiki import scrape_raidwiki_champion
from components.champion_to_json import generate_champion_json, diff_champion_jsons

# ============================================================================
# STAT NAME STANDARDIZATION
# ============================================================================
# Canonical format (right side) matches JSON template: C.RATE, C.DMG, RES (no spaces)
# This constant is the SINGLE SOURCE OF TRUTH for all stat name mapping across the project
STAT_NAME_MAPPING = {
    # Crit Rate - both formats supported
    'C. RATE': 'C.RATE',  # Ayumilove OCR format (with space)
    'C.RATE': 'C.RATE',   # Fandom/JSON format (no space) - CANONICAL
    # Crit Damage - both formats supported
    'C. DMG': 'C.DMG',    # Ayumilove OCR format (with space)
    'C.DMG': 'C.DMG',     # Fandom/JSON format (no space) - CANONICAL
    # Resistance - both formats supported
    'RESIST': 'RES',      # Ayumilove OCR format (long form)
    'RES': 'RES',         # Fandom/JSON format (short form) - CANONICAL
    # Standard stats (same across all sources)
    'HP': 'HP',
    'ATK': 'ATK',
    'DEF': 'DEF',
    'SPD': 'SPD',
    'ACC': 'ACC'
}

def merge_champion_data(primary: dict | None, fallback: dict | None) -> dict:
    """Merge missing fields from fallback into primary."""
    if not primary:
        return fallback
    if not fallback:
        return primary
    merged = {}
    for key in ['info', 'stats', 'skills']:
        merged[key] = primary.get(key) if primary.get(key) else fallback.get(key)
    return merged

def compare_stats(raidwiki_stats: dict, ayumilove_stats: dict, champion_name: str) -> tuple[bool, float, list]:
    """
    Compare stats from RaidWiki and Ayumilove OCR.
    Returns: (use_raidwiki: bool, confidence: float, differences: list)
    """
    if not raidwiki_stats or not any(v for v in raidwiki_stats.values()):
        return False, 0.0, ["No RaidWiki stats available"]
    
    if not ayumilove_stats or not any(v for v in ayumilove_stats.values()):
        return True, 100.0, ["No Ayumilove OCR stats available - using RaidWiki"]
    
    # Normalize Ayumilove stats using canonical STAT_NAME_MAPPING
    normalized_ocr = {}
    for k, v in ayumilove_stats.items():
        mapped_key = STAT_NAME_MAPPING.get(k, k)
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


def try_all_scrapers(champion_name: str, debug: bool = False) -> dict | None:
    """
    FOUR-SOURCE APPROACH: Champion_stats.md → Ayumilove → HellHades → RaidWiki
    
    Args:
        champion_name: Name of champion to scrape
        debug: Enable debug output
        
    Returns:
        dict: Combined champion data from all sources, or None if all sources fail
    """
    # FOUR-SOURCE APPROACH: Champion_stats.md (local reference) → Ayumilove (primary) → HellHades (secondary) → RaidWiki (tiebreaker)
    # Priority: Champion_stats.md (validated) → Ayumilove (skills) → HellHades (info) → RaidWiki (tiebreaker)
    # Decision rule: Use Champion_stats.md for stats when available, ALWAYS use Ayumilove for skills
    
    # SOURCE 1: Champion_stats.md (local reference table - instant, validated)
    print("[4-Source] Checking Champion_stats.md (local reference)...")
    fandom_data = scrape_fandom_champion(champion_name, debug=debug)
    has_fandom_stats = (fandom_data and fandom_data.get('stats') and 
                        any(v for v in fandom_data.get('stats', {}).values() if v and v != '' and v != '-' and v != '\\-'))
    has_fandom_info = (fandom_data and fandom_data.get('info'))
    
    if has_fandom_stats:
        fandom_stats = fandom_data.get('stats', {})
        stats_count = sum(1 for v in fandom_stats.values() if v and v != '' and v != '-' and v != '\\-')
        print(f"[4-Source] ✓ Champion_stats.md has {stats_count}/8 stats (validated reference)")
    elif has_fandom_info:
        print(f"[4-Source] ⚠️  Champion_stats.md has info only (no stats)")
    else:
        print(f"[4-Source] ⚠️  Champion not in Champion_stats.md")
        print(f"[4-Source] → Will add to table after scrape if --update-table flag set")
    
    # SOURCE 2: ALWAYS fetch Ayumilove (skills + info + OCR validation)
    print("[4-Source] Fetching Ayumilove data (skills, info, OCR)...")
    ayumilove_data = scrape_ayumilove_champion(champion_name, skip_stats=False)  # ALWAYS run OCR for validation
    
    # Validate Ayumilove OCR vs Fandom reference (if Fandom has stats)
    ocr_vs_fandom_confidence = 0
    ocr_vs_fandom_notes = []
    
    if has_fandom_stats and ayumilove_data and ayumilove_data.get('stats'):
        use_fandom, ocr_vs_fandom_confidence, ocr_diffs = compare_stats(
            fandom_data.get('stats', {}),
            ayumilove_data.get('stats', {}),
            champion_name
        )
        ocr_vs_fandom_notes = ocr_diffs
        
        # Decision: Use Fandom stats (validated), but flag low OCR confidence
        # NOTE: If this threshold (90%) causes issues with accurate champions, review and adjust
        if ocr_vs_fandom_confidence >= 90:
            print(f"[4-Source] ✓ High OCR validation: Fandom vs Ayumilove ({ocr_vs_fandom_confidence:.0f}%)")
        elif ocr_vs_fandom_confidence >= 75:
            print(f"[4-Source] ⚠️  Good OCR validation: Fandom vs Ayumilove ({ocr_vs_fandom_confidence:.0f}%)")
        else:
            print(f"[4-Source] ❌ Low OCR validation: Fandom vs Ayumilove ({ocr_vs_fandom_confidence:.0f}%)")
            print(f"[4-Source] → Using Fandom (validated), but flagging for manual review")
            for diff in ocr_vs_fandom_notes[:3]:
                print(f"[4-Source]   - {diff}")
    
    # SOURCE 3: Try HellHades for info validation
    print("[4-Source] Attempting HellHades for info validation...")
    hellhades_data = None
    has_hellhades_stats = False
    
    try:
        hellhades_data = scrape_hellhades_champion(champion_name, skip_stats=True)  # Skip stats, use for info only
        has_hellhades_info = (hellhades_data and hellhades_data.get('info'))
        if has_hellhades_info:
            print("[4-Source] ✓ HellHades info available")
        else:
            print("[4-Source] ⚠️  HellHades returned no data (404 or not found)")
    except Exception as e:
        print(f"[4-Source] ⚠️  HellHades failed (skipping): {str(e)[:100]}")
    
    # Decision logic: Build final data from best available sources
    if ayumilove_data and ayumilove_data.get('skills'):
        # Ayumilove succeeded (has skills - essential data)
        ocr_stats = ayumilove_data.get('stats', {})
        stats_found = sum(1 for v in ocr_stats.values() if v and v != '')
        total_stats = 8
        ocr_confidence = (stats_found / total_stats) * 100 if total_stats > 0 else 0
        
        # Determine which sources we have
        sources_available = []
        if has_fandom_stats:
            sources_available.append('fandom')
        if ocr_stats and stats_found > 0:
            sources_available.append('ayumilove_ocr')
        if hellhades_data and hellhades_data.get('info'):
            sources_available.append('hellhades')
        
        print(f"[4-Source] Sources available: {', '.join(sources_available) if sources_available else 'Ayumilove only (info)'}")
        
        # Stats priority: Fandom (validated) > Ayumilove OCR
        final_stats = fandom_data.get('stats', {}) if has_fandom_stats else ocr_stats
        stats_source = 'fandom' if has_fandom_stats else 'ayumilove_ocr'
        
        # Log missing or invalid stats for manual review
        missing_stats = []
        invalid_stats = []
        for stat_name in ['HP', 'ATK', 'DEF', 'SPD', 'C.RATE', 'C.DMG', 'RES', 'ACC']:
            value = final_stats.get(stat_name, '')
            if not value or value in ['', '-', '\\-', 0, '0']:
                missing_stats.append(stat_name)
            # Check for obviously wrong values (e.g., HP=15 when should be 15000)
            elif stat_name == 'HP' and isinstance(value, (int, str)) and str(value).replace(',', '').isdigit():
                hp_val = int(str(value).replace(',', ''))
                if hp_val < 10000:  # HP should be 10k-25k for base stats
                    invalid_stats.append(f"{stat_name}={value} (too low, expected 10k-25k)")
            elif stat_name in ['ATK', 'DEF'] and isinstance(value, (int, str)) and str(value).replace(',', '').isdigit():
                stat_val = int(str(value).replace(',', ''))
                if stat_val < 500:  # ATK/DEF should be 500+ for base stats
                    invalid_stats.append(f"{stat_name}={value} (too low, expected 500+)")
        
        if missing_stats or invalid_stats:
            print(f"[4-Source] ⚠️  Stats validation for manual review:")
            if missing_stats:
                print(f"[4-Source]   Missing: {', '.join(missing_stats)}")
            if invalid_stats:
                print(f"[4-Source]   Invalid: {', '.join(invalid_stats)}")
        
        # Info priority: Fandom > Ayumilove > HellHades
        final_info = ayumilove_data.get('info', {})
        info_source = 'ayumilove'
        
        # Fill missing info from Fandom if available
        if has_fandom_info:
            fandom_info = fandom_data.get('info', {})
            for key in ['faction', 'affinity', 'rarity', 'role']:
                if not final_info.get(key) and fandom_info.get(key):
                    final_info[key] = fandom_info[key]
                    info_source = 'fandom+ayumilove'
                    print(f"[4-Source] ✓ Using Fandom {key}: {fandom_info[key]}")
        
        # Fill remaining missing info from HellHades
        if hellhades_data and hellhades_data.get('info'):
            hh_info = hellhades_data.get('info', {})
            for key in ['faction', 'affinity', 'rarity', 'role']:
                if not final_info.get(key) and hh_info.get(key):
                    final_info[key] = hh_info[key]
                    if 'hellhades' not in info_source:
                        info_source = info_source + '+hellhades'
                    print(f"[4-Source] ✓ Using HellHades {key}: {hh_info[key]}")
        
        # Build validation metadata with source priority
        validation_notes = []
        if has_fandom_stats:
            validation_notes.append(f"Fandom: Primary stats source (validated)")
            if ocr_vs_fandom_confidence > 0:
                validation_notes.append(f"Ayumilove OCR vs Fandom: {ocr_vs_fandom_confidence:.0f}% match")
        else:
            validation_notes.append(f"Ayumilove OCR: Primary stats source ({stats_found}/{total_stats} extracted)")
        
        validation_notes.append(f"Ayumilove: Skills source (canonical)")
        
        if hellhades_data and hellhades_data.get('info'):
            validation_notes.append(f"HellHades: Info validation")
        
        # Calculate overall confidence
        overall_confidence = ocr_vs_fandom_confidence if has_fandom_stats else ocr_confidence
        
        validation_meta = {
            'stat_confidence': overall_confidence,
            'data_sources': '+'.join(sources_available),
            'source_priority': {
                'stats': stats_source,
                'skills': 'ayumilove',
                'info': info_source
            },
            'validation_notes': validation_notes
        }
        
        # Determine source label for output
        if len(sources_available) >= 3:
            source_label = f"4-source ({', '.join(sources_available)})"
        elif len(sources_available) == 2:
            source_label = f"2-source ({', '.join(sources_available)})"
        else:
            source_label = f'ayumilove_only ({stats_found}/{total_stats} stats)'
            if ocr_confidence < 75:
                print(f"[WARNING] Low OCR confidence: {stats_found}/{total_stats} stats extracted ({ocr_confidence:.1f}%)")
                print(f"[WARNING] Consider manual verification for this champion")
        
        # Build final merged data
        merged_data = {
            'info': final_info,
            'stats': final_stats,
            'skills': ayumilove_data.get('skills', []),
            'aura': ayumilove_data.get('aura', ''),
            'mechanics_tags': ayumilove_data.get('mechanics_tags', []),
            'validation': validation_meta,
            'in_fandom_table': has_fandom_stats  # Track if champion was in table
        }
        return merged_data, source_label
    
    elif hellhades_data and hellhades_data.get('info'):
        # Ayumilove failed, HellHades has at least info (rare fallback)
        print("[4-Source] ⚠️  Ayumilove failed - using HellHades only (unusual)")
        validation_meta = {
            'stat_confidence': 0,
            'data_sources': 'hellhades_only',
            'source_priority': {
                'stats': 'none',
                'skills': 'none',
                'info': 'hellhades'
            },
            'validation_notes': ['Ayumilove failed - HellHades fallback (no skills/stats)']
        }
        hellhades_data['validation'] = validation_meta
        hellhades_data['in_fandom_table'] = False
        return hellhades_data, 'hellhades_only'
    
    # All sources failed - mark as scrape failure
    print("[ERROR] All sources (Fandom + Ayumilove + HellHades) failed - no data available")
    print("[ERROR] Setting draft: 'scrape failed' in JSON")
    
    # Return minimal data structure with failure marker
    failed_data = {
        'info': {'name': champion_name},
        'stats': {},
        'skills': [],
        'validation': {
            'stat_confidence': 0,
            'data_sources': 'none',
            'source_priority': {
                'stats': 'none',
                'skills': 'none',
                'info': 'none'
            },
            'validation_notes': ['All scrape sources failed']
        },
        'draft': 'scrape failed',
        'in_fandom_table': False
    }
    return failed_data, 'scrape_failed'

def main() -> None:
    """Main entry point for champion scraper CLI."""
    import argparse
    
    parser = argparse.ArgumentParser(description='Scrape champion data from multiple sources')
    parser.add_argument('champion', nargs='?', help='Champion name to scrape (or use --list)')
    parser.add_argument('--list', type=str, metavar='FILE', help='File with list of champion names (one per line)')
    parser.add_argument('--owned', type=int, default=None, metavar='N',
                        help='Owned count (0-N). Updates Owned column in Champion_stats.md. If omitted, reads from existing table.')
    parser.add_argument('--update-table', action='store_true', 
                        help='Auto-update Champion_stats.md after scraping (default: False)')
    
    args = parser.parse_args()
    
    # Determine champion list
    if args.list:
        with open(args.list, 'r', encoding='utf-8') as f:
            champ_names = [line.strip() for line in f if line.strip() and not line.strip().startswith('#')]
    elif args.champion:
        champ_names = [args.champion]
    else:
        parser.print_help()
        sys.exit(1)
    
    template_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../input/Templates/Champion_Dictionary_Template.json'))
    out_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../input/Champion_Dictionary'))

    for i, champ_name in enumerate(champ_names):
        print(f"Processing: {champ_name}")
        data, source = try_all_scrapers(champ_name, debug=False)  # Set to True for debugging
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
            
            # Use canonical STAT_NAME_MAPPING for stat normalization
            for k, v in stats.items():
                mapped_key = STAT_NAME_MAPPING.get(k, None)
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
            if 'validation' in data:
                scraped_data['validation'] = data['validation']
            
            # Pass through draft status if scrape failed
            if 'draft' in data and data['draft'] == 'scrape failed':
                scraped_data['draft'] = 'scrape failed'
                print(f"[WARNING] Scrape failed for {champ_name} - marking as draft: 'scrape failed'")
            
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
            
            # Generate JSON with optional table update
            in_fandom = data.get('in_fandom_table', False)
            # Force table update if --owned is specified, otherwise auto-update if not in Fandom table
            if args.owned is not None:
                should_update_table = True  # Always update table when --owned is specified
            else:
                should_update_table = not in_fandom if not args.update_table else (args.update_table and not in_fandom)
            
            # Add owned count to scraped_data (use --owned flag if provided, otherwise will read from table)
            if args.owned is not None:
                scraped_data['owned'] = args.owned
            
            generate_champion_json(
                champ_name, 
                scraped_data, 
                template_path, 
                output_path,
                update_table=should_update_table
            )
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