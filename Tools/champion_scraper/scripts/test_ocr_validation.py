"""
OCR Test Suite for Champion Stat Extraction

This script tests OCR extraction on multiple champion images and compares
results with known stats from RaidWiki when available.

Usage:
    python test_ocr_validation.py --champion "Champion Name"
    python test_ocr_validation.py --all  # Test all champions in test list
    python test_ocr_validation.py --validate  # Compare Ayumilove OCR vs RaidWiki
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'components'))

from scrape_ayumilove import scrape_ayumilove_champion, extract_stats_from_image
from scrape_raidwiki import scrape_raidwiki_champion
import json

# Test champions list - add more as you test
TEST_CHAMPIONS = [
    "Gretel Hagbane",  # Known working
    "Husk",  # Known partial failure
    # Add more here
]

def test_ocr_extraction(champion_name, show_ocr_debug=True):
    """
    Test OCR extraction for a single champion and show results.
    """
    print("=" * 80)
    print(f"Testing OCR for: {champion_name}")
    print("=" * 80)
    
    # Get Ayumilove data (with OCR)
    ayumilove_data = scrape_ayumilove_champion(champion_name)
    
    if not ayumilove_data:
        print(f"❌ Failed to scrape Ayumilove data for {champion_name}")
        return None
    
    ayumilove_stats = ayumilove_data.get('stats', {})
    
    print("\n📊 Ayumilove OCR Stats:")
    print("-" * 40)
    for stat, value in ayumilove_stats.items():
        status = "✅" if value and value != '' else "❌"
        print(f"{status} {stat:10} : {value}")
    
    return ayumilove_stats


def compare_with_raidwiki(champion_name):
    """
    Compare Ayumilove OCR stats with RaidWiki stats (when available).
    """
    print("=" * 80)
    print(f"Comparing Ayumilove OCR vs RaidWiki for: {champion_name}")
    print("=" * 80)
    
    # Get both sources
    ayumilove_data = scrape_ayumilove_champion(champion_name)
    raidwiki_data = scrape_raidwiki_champion(champion_name)
    
    if not ayumilove_data or not raidwiki_data:
        print(f"⚠️  Cannot compare - missing data source")
        if not ayumilove_data:
            print("   - Ayumilove: FAILED")
        if not raidwiki_data:
            print("   - RaidWiki: FAILED")
        return
    
    ayumilove_stats = ayumilove_data.get('stats', {})
    raidwiki_stats = raidwiki_data.get('stats', {})
    
    print("\n📊 Stat Comparison:")
    print("-" * 80)
    print(f"{'Stat':<10} | {'Ayumilove OCR':<15} | {'RaidWiki':<15} | {'Match':<10}")
    print("-" * 80)
    
    all_stats = ['HP', 'ATK', 'DEF', 'SPD', 'C. RATE', 'C. DMG', 'RESIST', 'ACC']
    matches = 0
    total = 0
    
    for stat in all_stats:
        ayumilove_val = ayumilove_stats.get(stat, '')
        raidwiki_val = raidwiki_stats.get(stat, '')
        
        if ayumilove_val and raidwiki_val:
            total += 1
            match = str(ayumilove_val) == str(raidwiki_val)
            if match:
                matches += 1
                status = "✅ MATCH"
            else:
                status = "❌ DIFF"
        elif ayumilove_val:
            status = "⚠️  No RaidWiki"
        elif raidwiki_val:
            status = "⚠️  OCR Failed"
        else:
            status = "❌ Both Missing"
        
        print(f"{stat:<10} | {str(ayumilove_val):<15} | {str(raidwiki_val):<15} | {status}")
    
    if total > 0:
        accuracy = (matches / total) * 100
        print("-" * 80)
        print(f"OCR Accuracy: {matches}/{total} ({accuracy:.1f}%)")
    
    # Suggest which source to use
    print("\n💡 Recommendation:")
    if matches == total and total >= 6:
        print(f"   ✅ Use Ayumilove (OCR working perfectly)")
    elif matches >= total * 0.75 and total >= 6:
        print(f"   ⚠️  Use Ayumilove with manual verification")
    else:
        print(f"   ❌ Use RaidWiki or manual entry (OCR unreliable)")
    
    return {
        'champion': champion_name,
        'ayumilove': ayumilove_stats,
        'raidwiki': raidwiki_stats,
        'matches': matches,
        'total': total,
        'accuracy': (matches / total * 100) if total > 0 else 0
    }


def test_all_champions():
    """
    Test OCR extraction for all champions in TEST_CHAMPIONS list.
    """
    results = []
    for champion_name in TEST_CHAMPIONS:
        result = compare_with_raidwiki(champion_name)
        if result:
            results.append(result)
        print("\n")
    
    # Summary
    print("=" * 80)
    print("SUMMARY")
    print("=" * 80)
    for result in results:
        accuracy = result['accuracy']
        status = "✅" if accuracy == 100 else "⚠️" if accuracy >= 75 else "❌"
        print(f"{status} {result['champion']:<30} : {result['matches']}/{result['total']} ({accuracy:.1f}%)")


def save_test_report(output_file="ocr_test_report.json"):
    """
    Generate and save a detailed test report.
    """
    results = []
    for champion_name in TEST_CHAMPIONS:
        result = compare_with_raidwiki(champion_name)
        if result:
            results.append(result)
    
    report_path = os.path.join(os.path.dirname(__file__), output_file)
    with open(report_path, 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=2)
    
    print(f"\n📝 Test report saved to: {report_path}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python test_ocr_validation.py --champion \"Champion Name\"")
        print("  python test_ocr_validation.py --all")
        print("  python test_ocr_validation.py --validate \"Champion Name\"")
        print("  python test_ocr_validation.py --report")
        sys.exit(1)
    
    if sys.argv[1] == "--champion" and len(sys.argv) >= 3:
        champion_name = sys.argv[2]
        test_ocr_extraction(champion_name)
    
    elif sys.argv[1] == "--validate" and len(sys.argv) >= 3:
        champion_name = sys.argv[2]
        compare_with_raidwiki(champion_name)
    
    elif sys.argv[1] == "--all":
        test_all_champions()
    
    elif sys.argv[1] == "--report":
        save_test_report()
    
    else:
        print("Invalid arguments. Use --help for usage.")
