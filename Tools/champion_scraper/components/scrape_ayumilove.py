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
except ImportError:
    OCR_AVAILABLE = False
    print("[INFO] OCR libraries not available. Install 'pillow' and 'pytesseract' for image-based stat extraction.")


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
            # Iterate over the children of the <p> block
            last_label = None
            for elem in p.children:
                if hasattr(elem, 'string') and elem.string:
                    label = elem.string.strip()
                    if label.startswith("NAME:"):
                        # Get value after colon, or next sibling if empty
                        val = label.replace("NAME:", "").strip()
                        if not val:
                            next_elem = elem.next_sibling
                            if next_elem and hasattr(next_elem, 'get_text'):
                                val = next_elem.get_text(strip=True)
                        info["name"] = val
                        last_label = "name"
                    elif label.startswith("FACTION:"):
                        next_elem = elem.next_sibling
                        if next_elem and hasattr(next_elem, 'get_text'):
                            info["faction"] = next_elem.get_text(strip=True)
                        last_label = "faction"
                    elif label.startswith("RARITY:"):
                        next_elem = elem.next_sibling
                        if next_elem and hasattr(next_elem, 'get_text'):
                            info["rarity"] = next_elem.get_text(strip=True)
                        last_label = "rarity"
                    elif label.startswith("ROLE:"):
                        next_elem = elem.next_sibling
                        if next_elem and hasattr(next_elem, 'get_text'):
                            info["role"] = next_elem.get_text(strip=True)
                        last_label = "role"
                    elif label.startswith("AFFINITY:"):
                        next_elem = elem.next_sibling
                        if next_elem and hasattr(next_elem, 'get_text'):
                            info["affinity"] = next_elem.get_text(strip=True)
                        last_label = "affinity"
            break
    return info

def extract_stats_from_image(image_url):
    """
    Extract champion stats from an image using OCR.
    Returns a dict of stats (HP, ATK, DEF, etc.) or empty dict if extraction fails.
    
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
        
        # Parse stats from OCR text
        stats = {}
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
        
        if stats:
            print(f"[OCR] Extracted {len(stats)} stats from image")
        return stats
    
    except Exception as e:
        print(f"[OCR][ERROR] Failed to extract stats from image: {e}")
        return {}


def extract_main_image_and_stats(soup, champ_name):
    # Try to find the main image (look for champion name in src or alt)
    img_tag = None
    champ_name_lc = champ_name.strip().lower().replace("'", "").replace(" ", "_")
    for img in soup.find_all('img'):
        alt = img.get('alt', '').lower()
        src = img.get('src', '').lower()
        # Accept match if champion name (with/without underscores/hyphens) is in alt or src
        if champ_name_lc in alt or champ_name_lc in src or champ_name.strip().lower().replace(" ", "-") in src:
            img_tag = img
            break
    image_url = img_tag['src'] if img_tag else None
    if not image_url:
        print("[DEBUG] No main image found.")

    # Try to find the stats table or block
    stats = {}
    table = None
    for t in soup.find_all('table'):
        if any('HP' in cell.get_text() for cell in t.find_all(['td', 'th'])):
            table = t
            break
    if table:
        for row in table.find_all('tr'):
            cells = row.find_all(['td', 'th'])
            if len(cells) == 2:
                stat = cells[0].get_text(strip=True)
                value = cells[1].get_text(strip=True).replace(',', '')
                stats[stat] = value
    else:
        # Fallback: look for text blocks
        text = soup.get_text("\n")
        for stat in ["HP", "ATK", "DEF", "SPD", "C. RATE", "C. DMG", "RESIST", "ACC"]:
            m = re.search(rf'{stat}[:\s]+([\d,]+)', text)
            if m:
                stats[stat] = m.group(1).replace(',', '')
        if not stats:
            print("[DEBUG] No stats found in table or text.")
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

def scrape_ayumilove_champion(champ_name, template_path=None):
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
    image_url, stats = extract_main_image_and_stats(soup, champ_name)
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