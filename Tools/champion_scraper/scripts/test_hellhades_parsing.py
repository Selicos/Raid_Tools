"""
Test script to analyze HellHades HTML files and extract champion data.
Uses local HTML files from input/Stat_Test/ to determine best parsing approach.
"""

import re
import json
from pathlib import Path
from bs4 import BeautifulSoup

def extract_from_meta_tags(soup):
    """Extract champion info from meta tags in HTML head"""
    info = {}
    
    # Meta description often has: "Champion Name is a Rarity Affinity Role champion in the Faction faction"
    meta_desc = soup.find('meta', {'name': 'description'})
    if meta_desc and meta_desc.get('content'):
        desc = meta_desc['content']
        print(f"[META] Description: {desc}")
        
        # Pattern: "Name is a Rarity Affinity Role champion in the Faction faction"
        pattern = r'(.+?)\s+is\s+an?\s+(\w+)\s+(\w+)\s+(\w+)\s+champion\s+in\s+the\s+(.+?)\s+faction'
        match = re.search(pattern, desc, re.IGNORECASE)
        if match:
            info['name'] = match.group(1).strip()
            info['rarity'] = match.group(2).strip()
            info['affinity'] = match.group(3).strip()
            info['role'] = match.group(4).strip()
            info['faction'] = match.group(5).strip()
            print(f"[META] Extracted: {info}")
    
    # OG image often points to splash artwork
    og_image = soup.find('meta', {'property': 'og:image'})
    if og_image and og_image.get('content'):
        info['splash_image'] = og_image['content']
        print(f"[META] Splash image: {info['splash_image']}")
    
    return info

def find_splash_image(soup, champion_name):
    """Find the champion splash artwork image with stats"""
    images = []
    
    # Look for class="raid_champion_splash"
    splash_imgs = soup.find_all('img', class_='raid_champion_splash')
    for img in splash_imgs:
        src = img.get('data-orig-src') or img.get('src')
        if src:
            images.append(('splash_class', src))
            print(f"[IMAGE] Found via class raid_champion_splash: {src}")
    
    # Look for images with champion name in URL
    all_imgs = soup.find_all('img')
    for img in all_imgs:
        src = img.get('data-orig-src') or img.get('src')
        if src and champion_name.lower().replace(' ', '-') in src.lower():
            images.append(('name_match', src))
            print(f"[IMAGE] Found via name match: {src}")
    
    return images

def extract_javascript_data(html_content):
    """Extract champion data embedded in JavaScript"""
    # Look for JSON data in script tags
    script_pattern = r'<script[^>]*>(.*?)</script>'
    scripts = re.findall(script_pattern, html_content, re.DOTALL | re.IGNORECASE)
    
    print(f"\n[JS] Found {len(scripts)} script blocks")
    
    # Look for common data patterns
    for i, script in enumerate(scripts):
        # Look for champion data assignments
        if 'raid' in script.lower() or 'champion' in script.lower() or 'skill' in script.lower():
            print(f"\n[JS] Script block {i+1} (contains raid/champion/skill keywords):")
            print(f"    Length: {len(script)} chars")
            
            # Try to find JSON structures
            json_pattern = r'\{[^{}]*(?:\{[^{}]*\}[^{}]*)*\}'
            json_matches = re.findall(json_pattern, script[:2000])  # First 2000 chars
            if json_matches:
                print(f"    Found {len(json_matches)} potential JSON objects")
                for j, match in enumerate(json_matches[:3]):  # Show first 3
                    print(f"    JSON {j+1} preview: {match[:200]}...")

def extract_from_html_containers(soup):
    """Extract data from specific HTML containers"""
    data = {}
    
    # Look for raid-aura-container
    aura = soup.find('div', {'id': 'raid-aura', 'class': 'raid-aura-container'})
    if aura:
        print(f"[CONTAINER] Found raid-aura container")
        data['aura'] = 'Found (needs JS parsing)'
    
    # Look for raid-skills-container
    skills = soup.find('div', {'id': 'raid-skills', 'class': 'raid-skills-container'})
    if skills:
        print(f"[CONTAINER] Found raid-skills container")
        print(f"[CONTAINER] Content: {skills.get_text()[:200] if skills.get_text() else 'EMPTY - JS loaded'}")
        data['skills'] = 'Found (needs JS parsing)'
    
    # Look for raid-ratings
    ratings = soup.find('div', {'id': 'overall-rating', 'class': 'raid-ratings-overall'})
    if ratings:
        print(f"[CONTAINER] Found overall-rating container")
        data['ratings'] = 'Found (needs JS parsing)'
    
    return data

def analyze_html_file(file_path):
    """Analyze a HellHades HTML file and extract all possible data"""
    print(f"\n{'='*80}")
    print(f"ANALYZING: {file_path.name}")
    print(f"{'='*80}\n")
    
    # Read HTML
    with open(file_path, 'r', encoding='utf-8') as f:
        html_content = f.read()
    
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Extract URL from comment
    url_comment = re.search(r'<!--\s*view-source:(https?://[^\s]+)\s*-->', html_content)
    if url_comment:
        url = url_comment.group(1)
        champion_name = url.split('/')[-2].replace('-', ' ').title()
        print(f"[URL] {url}")
        print(f"[CHAMPION] Inferred name: {champion_name}\n")
    else:
        champion_name = "Unknown"
    
    # 1. Extract from meta tags
    print("\n--- META TAG EXTRACTION ---")
    meta_info = extract_from_meta_tags(soup)
    
    # 2. Find splash images
    print("\n--- SPLASH IMAGE SEARCH ---")
    images = find_splash_image(soup, champion_name)
    
    # 3. Extract JavaScript data
    print("\n--- JAVASCRIPT DATA EXTRACTION ---")
    extract_javascript_data(html_content)
    
    # 4. Extract from HTML containers
    print("\n--- HTML CONTAINER EXTRACTION ---")
    container_data = extract_from_html_containers(soup)
    
    # Summary
    print(f"\n{'='*80}")
    print(f"SUMMARY for {champion_name}")
    print(f"{'='*80}")
    print(f"Meta info extracted: {len(meta_info)} fields")
    print(f"Images found: {len(images)}")
    print(f"Containers found: {len(container_data)}")
    print(f"\nRecommended approach:")
    print(f"  1. Use meta description for faction/affinity/rarity/role")
    print(f"  2. Use splash image for OCR stat extraction (like Ayumilove)")
    print(f"  3. Skills require JavaScript parsing or API endpoint")
    print(f"{'='*80}\n")

def main():
    """Test with all available HTML files"""
    test_dir = Path('c:/GIT/Raid_Tools/input/Stat_Test')
    html_files = list(test_dir.glob('*.html'))
    
    if not html_files:
        print(f"No HTML files found in {test_dir}")
        return
    
    print(f"Found {len(html_files)} HTML files to analyze\n")
    
    for html_file in sorted(html_files):
        analyze_html_file(html_file)
        print("\n" * 2)
    
    # Generate recommendations
    print(f"\n{'='*80}")
    print("RECOMMENDATIONS FOR HELLHADES SCRAPER")
    print(f"{'='*80}\n")
    print("Based on analysis, the HellHades scraper should:")
    print()
    print("1. Extract champion info from meta description tag")
    print("   - Faction, Affinity, Rarity, Role")
    print("   - Pattern: 'Name is a Rarity Affinity Role champion in the Faction faction'")
    print()
    print("2. Find splash artwork image (class='raid_champion_splash')")
    print("   - Use data-orig-src attribute")
    print("   - Download and OCR for base stats (like Ayumilove)")
    print()
    print("3. Skills extraction: TWO OPTIONS")
    print("   Option A: Parse embedded JavaScript data")
    print("   Option B: Make API call to HellHades API (if exists)")
    print("   Option C: Skip skills, use Ayumilove as primary for skills")
    print()
    print("4. Validation use case:")
    print("   - Use HellHades for faction/affinity/rarity validation")
    print("   - Use splash image OCR as secondary stat source")
    print("   - Rely on Ayumilove for skills (primary source)")
    print(f"\n{'='*80}\n")

if __name__ == '__main__':
    main()
