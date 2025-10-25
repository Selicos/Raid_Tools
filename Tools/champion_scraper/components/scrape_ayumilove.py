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
    # --- Skill extraction block ---
    skills = []
    # Find the SKILLS section header for this champion
    skills_header = soup.find('h2', string=lambda t: t and t.strip().lower().startswith(f"{champ_name.lower()} skills"))
    if skills_header:
        for sib in skills_header.next_siblings:
            if getattr(sib, 'name', None) == 'h2' and 'build guide' in sib.get_text(strip=True).lower():
                break
            if getattr(sib, 'name', None) == 'p':
                strong = sib.find('strong')
                if strong:
                    skill_name = strong.get_text(strip=True)
                    cooldown = ''
                    cd_match = re.search(r'\(Cooldown: (\d+) turns\)', skill_name)
                    if cd_match:
                        cooldown = cd_match.group(1)
                        skill_name = re.sub(r'\(Cooldown: \d+ turns\)', '', skill_name).strip()
                    # Skill type: try to infer from name
                    skill_type = 'Aura' if 'aura' in skill_name.lower() else ('Passive' if 'passive' in skill_name.lower() else '')
                    skill = {
                        'type': skill_type,
                        'name': skill_name,
                        'description': '',
                        'cooldown': cooldown,
                        'book_value': '',
                        'multiplier': ''
                    }
                    # Parse rest of <p> for description, booking, multiplier
                    lines = sib.decode_contents().split('<br')
                    desc_lines = []
                    for raw in lines[1:]:
                        txt = BeautifulSoup(raw, 'html.parser').text.strip()
                        if not txt:
                            continue
                        if txt.lower().startswith('level') or 'book' in txt.lower():
                            skill['book_value'] += (txt + '\n')
                        elif 'multiplier' in txt.lower():
                            skill['multiplier'] = txt.split(':',1)[-1].strip()
                        else:
                            desc_lines.append(txt)
                    skill['description'] = '\n'.join(desc_lines).strip()
                    skill['book_value'] = skill['book_value'].strip()
                    skills.append(skill)
    # --- End skill extraction block ---

    # Extract overview info (unchanged)
    overview_info = {"name": "", "faction": "", "rarity": "", "role": "", "affinity": "", "image_url": image_url}
    overview_h4 = soup.find('h4', string=lambda t: t and 'overview' in t.lower())
    if overview_h4:
        overview_p = overview_h4.find_next('p')
        if overview_p:
            lines = overview_p.decode_contents().split('<br')
            canonical_keys = ["name", "faction", "rarity", "role", "affinity", "rank", "usability", "tomes"]
            for line in lines:
                line = BeautifulSoup(line, 'html.parser').text.strip()
                if ':' in line:
                    key, value = line.split(':', 1)
                    key = key.strip().lower()
                    key = re.sub(r'^[/\\>?\n\s]+', '', key)
                    if key not in canonical_keys:
                        continue
                    value = value.strip()
                    if not value:
                        continue
                    if '(' in value:
                        value = value.split('(')[0].strip()
                    overview_info[key] = value
    print("[DEBUG] Parsed overview_info:", overview_info)
    for field in ["name", "faction", "rarity", "role", "affinity"]:
        if not overview_info.get(field):
            print(f"[WARN] Overview field missing: {field}")
    return {'info': overview_info, 'stats': stats, 'skills': skills}

if __name__ == "__main__":
    main()