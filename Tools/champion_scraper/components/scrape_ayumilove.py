import json
import os

def load_template(template_path=None):
    # Load the canonical champion template from file
    if template_path is None:
        # Default path relative to this script
        template_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../input/Templates/Champion_Dictionary_Template.json'))
    with open(template_path, 'r', encoding='utf-8') as f:
        return json.load(f)
import requests
from bs4 import BeautifulSoup
import sys
import re

# Optional OCR imports - will use if available
try:
    from PIL import Image
    import pytesseract
    from io import BytesIO
    OCR_AVAILABLE = True
    # Configure tesseract path for Windows if not in PATH
    import platform
    if platform.system() == 'Windows':
        # Try common installation paths
        possible_paths = [
            r'C:\Program Files\Tesseract-OCR\tesseract.exe',
            r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe',
        ]
        tesseract_found = False
        for path in possible_paths:
            if os.path.exists(path):
                pytesseract.pytesseract.tesseract_cmd = path
                tesseract_found = True
                print(f"[OCR] Configured Tesseract at: {path}")
                break
        if not tesseract_found:
            print("[OCR][WARNING] Tesseract not found in common paths. Trying system PATH...")
except ImportError as e:
    OCR_AVAILABLE = False
    print(f"[INFO] OCR libraries not available: {e}")
    print("[INFO] Install 'pillow' and 'pytesseract' for image-based stat extraction.")


def fetch_champion_page(url):
    resp = requests.get(url)
    resp.raise_for_status()
    return resp.text


def extract_base_info(soup):
    # Find the <p> block with base info (under Overview)
    info = {"name": "", "faction": "", "rarity": "", "role": "", "affinity": ""}
    for p in soup.find_all('p'):
        txt = p.get_text(" ", strip=True)
        if "NAME:" in txt and "FACTION:" in txt:
            # Use regex for more reliable extraction instead of fragile next_sibling parsing
            # This handles variations in HTML structure better
            
            # Extract NAME (first capture group after "NAME:")
            name_match = re.search(r'NAME:\s*([A-Za-z\s\'-]+?)(?:\s+FACTION:|$)', txt, re.IGNORECASE)
            if name_match:
                info["name"] = name_match.group(1).strip()
            
            # Extract FACTION (capture until next label or end)
            faction_match = re.search(r'FACTION:\s*([A-Za-z\s]+?)(?:\s+RARITY:|$)', txt, re.IGNORECASE)
            if faction_match:
                info["faction"] = faction_match.group(1).strip()
            
            # Extract RARITY (capture until next label or end)
            rarity_match = re.search(r'RARITY:\s*([A-Za-z]+?)(?:\s+ROLE:|$)', txt, re.IGNORECASE)
            if rarity_match:
                info["rarity"] = rarity_match.group(1).strip()
            
            # Extract ROLE (capture until next label or end)
            role_match = re.search(r'ROLE:\s*([A-Za-z]+?)(?:\s+AFFINITY:|$)', txt, re.IGNORECASE)
            if role_match:
                info["role"] = role_match.group(1).strip()
            
            # Extract AFFINITY (capture until end or next section)
            affinity_match = re.search(r'AFFINITY:\s*([A-Za-z]+?)(?:\s|$)', txt, re.IGNORECASE)
            if affinity_match:
                info["affinity"] = affinity_match.group(1).strip()
            
            # Log extracted values for debugging
            print(f"[Ayumilove][INFO] Extracted info: Name={info.get('name')}, Faction={info.get('faction')}, "
                  f"Rarity={info.get('rarity')}, Role={info.get('role')}, Affinity={info.get('affinity')}")
            break
    
    if not info.get("faction") or not info.get("affinity"):
        print("[Ayumilove][WARNING] Failed to extract faction/affinity - verify with Owned_champion_list.md")
    
    return info

def extract_stats_from_image(image_url):
    """
    Extract champion stats from an image using OCR.
    Returns a dict of stats (HP, ATK, DEF, etc.) or empty dict if extraction fails.
    
    For Ayumilove images: Stats are displayed in fixed order without labels
    (HP, ATK, DEF, SPD, C.RATE, C.DMG, RESIST, ACC)
    
    Requirements:
    - pillow: pip install pillow
    - pytesseract: pip install pytesseract
    - Tesseract binary: https://github.com/tesseract-ocr/tesseract
    """
    if not OCR_AVAILABLE:
        return {}
    
    try:
        # Download the image
        response = requests.get(image_url, timeout=10)
        response.raise_for_status()
        img = Image.open(BytesIO(response.content))
        
        # Perform OCR
        text = pytesseract.image_to_string(img)
        
        print(f"[OCR][DEBUG] Extracted text from image:")
        print(text)
        print("[OCR][DEBUG] " + "=" * 60)
        
        # Parse stats from OCR text
        stats = {}
        
        # First try to find labeled stats (for images that have labels)
        stat_patterns = {
            'HP': r'HP[:\s]+(\d[\d,]*)',
            'ATK': r'ATK[:\s]+(\d[\d,]*)',
            'DEF': r'DEF[:\s]+(\d[\d,]*)',
            'SPD': r'SPD[:\s]+(\d[\d,]*)',
            'C. RATE': r'C\.?\s*RATE[:\s]+(\d+)%?',
            'C. DMG': r'C\.?\s*DMG[:\s]+(\d+)%?',
            'RESIST': r'RESIST(?:ANCE)?[:\s]+(\d+)',
            'ACC': r'ACC(?:URACY)?[:\s]+(\d+)',
        }
        
        for stat_name, pattern in stat_patterns.items():
            match = re.search(pattern, text, re.IGNORECASE)
            if match:
                value = match.group(1).replace(',', '')
                stats[stat_name] = value
        
        # If no labeled stats found, try positional extraction (Ayumilove format)
        if not stats:
            print("[OCR][INFO] No labeled stats found, trying positional extraction...")
            # Find all numbers (with optional commas)
            # Look for the stat block after "Total Stats" or similar
            numbers = re.findall(r'\d[\d,]+', text)
            
            print(f"[OCR][DEBUG] All numbers found: {numbers}")
            
            # Clean numbers (remove commas)
            clean_numbers = [n.replace(',', '') for n in numbers]
            
            # Ayumilove stats are in order: HP (4-5 digits), ATK (3-4 digits), DEF (3-4 digits), 
            # SPD (2-3 digits), C.RATE (1-2 digits), C.DMG (2-3 digits), RESIST (1-3 digits), ACC (1-3 digits)
            # Look for a sequence that matches these patterns
            stat_candidates = []
            for i, num in enumerate(clean_numbers):
                try:
                    val = int(num)
                    # Skip level (60, typically first) but include all other numbers
                    # HP is usually 10000+, so start from first 4-5 digit number
                    if i == 0 and val <= 100:
                        # Likely level number, skip
                        continue
                    # Include all reasonable stat values (10-30000)
                    if 10 <= val <= 30000:
                        stat_candidates.append(num)
                except ValueError:
                    continue
            
            print(f"[OCR][DEBUG] Stat candidates: {stat_candidates}")
            
            # Take the first 8 candidates if we have enough
            # Ayumilove order: HP, ATK, DEF, SPD, C.RATE, C.DMG, RESIST, ACC
            if len(stat_candidates) >= 8:
                stat_names = ['HP', 'ATK', 'DEF', 'SPD', 'C. RATE', 'C. DMG', 'RESIST', 'ACC']
                for i in range(8):
                    stats[stat_names[i]] = stat_candidates[i]
                print(f"[OCR][INFO] Extracted {len(stats)} stats using positional mapping")
            elif len(stat_candidates) >= 4:
                # At minimum try to get HP, ATK, DEF, SPD
                stat_names = ['HP', 'ATK', 'DEF', 'SPD']
                for i in range(min(4, len(stat_candidates))):
                    stats[stat_names[i]] = stat_candidates[i]
                print(f"[OCR][INFO] Extracted {len(stats)} core stats using positional mapping")
        
        if stats:
            print(f"[OCR] ✓ Extracted {len(stats)} stats from image")
        else:
            print(f"[OCR][WARNING] No stats matched from OCR text")
        return stats
    
    except Exception as e:
        print(f"[OCR][ERROR] Failed to extract stats from image: {e}")
        import traceback
        traceback.print_exc()
        return {}


def extract_main_image_and_stats(soup, champ_name, skip_stats=False):
    # Try to find the main image (look for champion name in src or alt)
    img_tag = None
    champ_name_lc = champ_name.strip().lower().replace("'", "").replace(" ", "_")
    champ_name_hyphen = champ_name.strip().lower().replace("'", "").replace(" ", "-")
    
    for img in soup.find_all('img'):
        alt = img.get('alt', '').lower()
        src = img.get('src', '').lower()
        data_src = img.get('data-src', '').lower()
        
        # Check both src and data-src for lazy-loaded images
        # Accept match if champion name (with underscores or hyphens) is in the URL
        if (champ_name_lc in src or champ_name_lc in data_src or 
            champ_name_hyphen in src or champ_name_hyphen in data_src):
            img_tag = img
            break
    
    # Extract and normalize image URL
    image_url = None
    if img_tag:
        # Prefer data-src for lazy-loaded images, fall back to src
        image_url = img_tag.get('data-src') or img_tag.get('src')
        if image_url:
            # Handle protocol-relative URLs (//example.com/path)
            if image_url.startswith('//'):
                image_url = 'https:' + image_url
            # Handle relative URLs (/path)
            elif image_url.startswith('/'):
                image_url = 'https://ayumilove.net' + image_url
            print(f"[DEBUG] Found champion image: {image_url}")
    
    if not image_url:
        print("[DEBUG] No main image found.")

    # Skip stats extraction if RaidWiki provided them
    stats = {}
    if skip_stats:
        print("[Ayumilove] Skipping stats extraction (using RaidWiki stats)")
    else:
        # For Ayumilove, stats are in the champion image (lower right corner)
        # Use OCR directly instead of trying to parse HTML tables/text
        if image_url and OCR_AVAILABLE:
            print("[DEBUG] Using OCR to extract stats from champion image...")
            stats = extract_stats_from_image(image_url)
            
            # Warn if low confidence (missing many stats)
            stats_found = sum(1 for v in stats.values() if v and v != '')
            total_stats = 8
            confidence = (stats_found / total_stats) * 100 if total_stats > 0 else 0
            
            if confidence < 75:
                print(f"[WARNING] Low OCR confidence: {stats_found}/{total_stats} stats extracted ({confidence:.1f}%)")
                print(f"[WARNING] Consider manual verification for this champion")
        elif not OCR_AVAILABLE:
            print("[WARNING] OCR not available - install pillow and pytesseract for stat extraction")
    
    print(f"[DEBUG] Final stats being returned: {stats}")
    return image_url, stats


def extract_skills_structured(soup):
    # Find the SKILLS section header (case-insensitive)
    skills_header = None
    for tag in soup.find_all(['h2', 'h3']):
        if 'skills' in tag.get_text(strip=True).lower():
            skills_header = tag
            break
    if not skills_header:
        print("[DEBUG] No SKILLS section header found.")
        return []
    # Collect all <p> tags after the header until next major section (Build Guide)
    skills = []
    skill_blocks = []
    for sib in skills_header.next_siblings:
        if hasattr(sib, 'name') and sib.name in ['h2', 'h3']:
            if 'build guide' in sib.get_text(strip=True).lower():
                break
        if hasattr(sib, 'name') and sib.name == 'p':
            txt = sib.get_text("\n", strip=True)
            skill_blocks.append(txt)
    # Each skill block is a multiline string, preserve formatting
    for block in skill_blocks:
        # First line is skill name (may include cooldown/passive)
        lines = block.split('\n')
        if lines:
            skill_name = lines[0].strip()
            desc = '\n'.join(lines[1:]).strip() if len(lines) > 1 else ''
            skills.append({"name": skill_name, "desc": desc})
    if not skills:
        print("[DEBUG] No skill <p> tags found after SKILLS header.")
    return skills


def determine_skill_type(skill_name, skill_desc, skill_index, total_skills):
    """
    Determine skill type (A1, A2, A3, Passive) based on skill name, description, and position.
    
    Logic:
    - If name or description contains "Passive", it's a Passive skill
    - Otherwise, assign based on position: 0=A1, 1=A2, 2=A3, etc.
    - Skip aura skills (handled separately)
    
    Note for future sources:
    - This logic assumes standard skill ordering (basic attack first, then abilities)
    - Adjust pattern matching if source uses different passive indicators
    - Some champions may have multiple passives or non-standard skill counts
    """
    name_lower = skill_name.lower()
    desc_lower = skill_desc.lower()
    
    # Check for passive indicators
    if "passive" in name_lower or "[passive" in desc_lower:
        return "Passive"
    
    # Assign based on position (A1, A2, A3, A4, etc.)
    # Most champions have 3-4 skills before aura/passive
    skill_types = ["A1", "A2", "A3", "A4", "A5", "A6"]
    if skill_index < len(skill_types):
        return skill_types[skill_index]
    
    # Fallback for unusual cases
    return f"A{skill_index + 1}"


def normalize_champion_name(name):
    # Converts champion name to Ayumilove URL format (lowercase, hyphens, remove special chars)
    # TODO: Validate champion name against a canonical list if available
    name = name.strip().lower().replace("'", "")
    name = re.sub(r"[^a-z0-9 ]", "", name)
    name = re.sub(r"\s+", "-", name)
    return name

def main():
    if len(sys.argv) < 2:
        print("Usage: python scrape_ayumilove.py <champion name>")
        sys.exit(1)
    champ_name = sys.argv[1]
    # NOTE: Champion name should be validated before use. If a canonical list is available, check here.
    norm_name = normalize_champion_name(champ_name)
    url = f"https://ayumilove.net/raid-shadow-legends-{norm_name}-skill-mastery-equip-guide/"
    print(f"Fetching: {url}")
    html = fetch_champion_page(url)
    soup = BeautifulSoup(html, 'lxml')
    image_url, stats = extract_main_image_and_stats(soup)
    skills = extract_skills_structured(soup)

    print("Main Image URL:", image_url)
    print("Base Stats:", stats)
    print("\nSKILLS Section:\n", skills)

def scrape_ayumilove_champion(champ_name, template_path=None, skip_stats=False):
    norm_name = normalize_champion_name(champ_name)
    url = f"https://ayumilove.net/raid-shadow-legends-{norm_name}-skill-mastery-equip-guide/"
    print(f"[Ayumilove] Fetching: {url}")
    try:
        html = fetch_champion_page(url)
    except Exception as e:
        print(f"[Ayumilove][ERROR] Failed to fetch {champ_name}: {e}")
        return None
    soup = BeautifulSoup(html, 'lxml')
    info = extract_base_info(soup)
    image_url, stats = extract_main_image_and_stats(soup, champ_name, skip_stats=skip_stats)
    skills = extract_skills_structured(soup)
    info["image_url"] = image_url
    
    # Separate aura from skills and assign skill types
    aura_desc = ""
    filtered_skills = []
    skill_index = 0
    for skill in skills:
        if skill["name"].strip().lower() == "aura":
            aura_desc = skill["desc"]
        else:
            # Determine skill type based on position and content
            skill_type = determine_skill_type(
                skill["name"], 
                skill["desc"], 
                skill_index, 
                len(skills)
            )
            skill["type"] = skill_type
            filtered_skills.append(skill)
            skill_index += 1
    
    # Load template and use its default values for missing fields
    template = load_template(template_path)
    mechanics_tags = template.get("mechanics_tags", ["Relevant mechanic tags"])
    
    # Return raw data with aura separated and skill types assigned
    return {
        'info': info, 
        'stats': stats, 
        'skills': filtered_skills, 
        'aura': aura_desc,
        'mechanics_tags': mechanics_tags
    }

if __name__ == "__main__":
    main()