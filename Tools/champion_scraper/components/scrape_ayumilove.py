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
    
    # Separate aura from skills
    aura_desc = ""
    filtered_skills = []
    for skill in skills:
        if skill["name"].strip().lower() == "aura":
            aura_desc = skill["desc"]
        else:
            filtered_skills.append(skill)
    
    # Load template and use its default values for missing fields
    template = load_template(template_path)
    mechanics_tags = template.get("mechanics_tags", ["Relevant mechanic tags"])
    
    # Return raw data with aura separated
    return {
        'info': info, 
        'stats': stats, 
        'skills': filtered_skills, 
        'aura': aura_desc,
        'mechanics_tags': mechanics_tags
    }

if __name__ == "__main__":
    main()