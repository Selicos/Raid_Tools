import requests
from bs4 import BeautifulSoup
import sys
import re


def fetch_champion_page(url):
    resp = requests.get(url)
    resp.raise_for_status()
    return resp.text


def extract_main_image_and_stats(soup):
    # Try to find the main image (look for champion name in src or alt)
    img_tag = None
    for img in soup.find_all('img'):
        alt = img.get('alt', '').lower()
        src = img.get('src', '').lower()
        if 'coldheart' in alt or 'coldheart' in src:
            img_tag = img
            break
    image_url = img_tag['src'] if img_tag else None
    if not image_url:
        print("[DEBUG] No main image found.")

    # Try to find the stats table or block
    stats = {}
    # Look for a table with HP, ATK, DEF, etc.
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
        import re
        for stat in ["HP", "ATK", "DEF", "SPD", "C. RATE", "C. DMG", "RESIST", "ACC"]:
            m = re.search(rf'{stat}[:\s]+([\d,]+)', text)
            if m:
                stats[stat] = m.group(1).replace(',', '')
        if not stats:
            print("[DEBUG] No stats found in table or text.")
    return image_url, stats


def extract_skills_section(soup):
    # Find the SKILLS section header (case-insensitive)
    skills_header = None
    for tag in soup.find_all(['h2', 'h3']):
        if 'skills' in tag.get_text(strip=True).lower():
            skills_header = tag
            break
    if not skills_header:
        print("[DEBUG] No SKILLS section header found.")
        return None
    # Collect all text until the next major section (e.g., BUILD GUIDE)
    skills_text = []
    for sib in skills_header.next_siblings:
        if hasattr(sib, 'get_text') and sib.name in ['h2', 'h3']:
            # Stop at next major section
            if 'build guide' in sib.get_text(strip=True).lower():
                break
        if hasattr(sib, 'get_text'):
            txt = sib.get_text(strip=True)
            if txt:
                skills_text.append(txt)
        elif isinstance(sib, str):
            txt = sib.strip()
            if txt:
                skills_text.append(txt)
    if not skills_text:
        print("[DEBUG] No skills text found after SKILLS header.")
    return '\n'.join(skills_text).strip()


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
    skills = extract_skills_section(soup)

    print("Main Image URL:", image_url)
    print("Base Stats:", stats)
    print("\nSKILLS Section:\n", skills)

def scrape_ayumilove_champion(champ_name):
    norm_name = normalize_champion_name(champ_name)
    url = f"https://ayumilove.net/raid-shadow-legends-{norm_name}-skill-mastery-equip-guide/"
    print(f"[Ayumilove] Fetching: {url}")
    try:
        html = fetch_champion_page(url)
    except Exception as e:
        print(f"[Ayumilove][ERROR] Failed to fetch {champ_name}: {e}")
        return None
    soup = BeautifulSoup(html, 'lxml')
    image_url, stats = extract_main_image_and_stats(soup)
    skills_text = extract_skills_section(soup)
    info = {"image_url": image_url}
    skills = []
    if skills_text:
        # Split skills by lines starting with skill names (strong formatting or uppercase)
        skill_blocks = re.split(r'(?:^|\n)([A-Z][A-Za-z0-9 \-\(\)]+:)', skills_text)
        # If split fails, fallback to paragraphs
        if len(skill_blocks) < 3:
            skill_blocks = re.split(r'\n{2,}', skills_text)
        # Parse each skill block
        for block in skill_blocks:
            block = block.strip()
            if not block or len(block) < 10:
                continue
            # Extract skill name
            name_match = re.match(r'^([A-Z][A-Za-z0-9 \-\(\)]+):', block)
            name = name_match.group(1) if name_match else "Unknown Skill"
            # Extract type
            type_match = re.search(r'(A1|A2|A3|Passive|Aura)', block, re.IGNORECASE)
            skill_type = type_match.group(1) if type_match else ""
            # Extract description
            desc = block
            # Effects extraction (simple heuristics)
            effects = []
            # Damage
            if re.search(r'attack|damage', block, re.IGNORECASE):
                effects.append({
                    "type": "damage",
                    "stat": "ATK",
                    "value": 0.0,
                    "per_hit": "multi" in block or "times" in block,
                    "target": "aoe_enemies" if "all enemies" in block else "single_enemy",
                    "duration": 0,
                    "notes": "Auto-extracted: may need manual review."
                })
            # Debuff
            debuff_match = re.findall(r'\[(.*?)\]', block)
            for debuff in debuff_match:
                effects.append({
                    "type": "debuff",
                    "stat": "NA",
                    "value": 0.0,
                    "per_hit": False,
                    "target": "aoe_enemies" if "all enemies" in block else "single_enemy",
                    "duration": 2 if "2 turns" in block else 1,
                    "notes": f"Debuff: {debuff}"
                })
            # Turn Meter
            if "Turn Meter" in block:
                tm_val = 25 if "25%" in block else 50 if "50%" in block else 0
                effects.append({
                    "type": "turn_meter_fill" if "fill" in block else "turn_meter_steal" if "decrease" in block else "turn_meter",
                    "stat": "Turn Meter",
                    "value": tm_val,
                    "per_hit": False,
                    "target": "aoe_enemies" if "all enemies" in block else "single_enemy",
                    "duration": 0,
                    "notes": "Auto-extracted Turn Meter effect."
                })
            # Revive
            if "revive" in block:
                effects.append({
                    "type": "revive",
                    "stat": "NA",
                    "value": 0.0,
                    "per_hit": False,
                    "target": "single_ally" if "one ally" in block else "aoe_allies" if "all allies" in block else "self",
                    "duration": 0,
                    "notes": "Auto-extracted revive effect."
                })
            # Buff
            buff_match = re.findall(r'\[(.*?)\]', block)
            for buff in buff_match:
                if "Increase" in buff or "Block" in buff or "Shield" in buff:
                    effects.append({
                        "type": "buff",
                        "stat": "NA",
                        "value": 0.0,
                        "per_hit": False,
                        "target": "aoe_allies" if "all allies" in block else "single_ally",
                        "duration": 2 if "2 turns" in block else 1,
                        "notes": f"Buff: {buff}"
                    })
            # Passive/Conditional
            if "Passive" in block or "if" in block:
                effects.append({
                    "type": "other",
                    "stat": "NA",
                    "value": 0.0,
                    "per_hit": False,
                    "target": "self",
                    "duration": 0,
                    "notes": "Passive or conditional effect."
                })
            # Aura
            if "Aura" in block:
                effects.append({
                    "type": "buff",
                    "stat": "NA",
                    "value": 0.0,
                    "per_hit": False,
                    "target": "aoe_allies",
                    "duration": 0,
                    "notes": "Aura effect."
                })
            skills.append({
                "name": name,
                "type": skill_type,
                "description": desc,
                "effects": effects,
                "cooldown_booked": None,
                "mechanics_tags": [],
                "book_value": "",
                "notes": "Auto-extracted; manual review recommended for edge cases."
            })
    return {'info': info, 'stats': stats, 'skills': skills}

if __name__ == "__main__":
    main()
