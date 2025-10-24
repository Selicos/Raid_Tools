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
    # For now, just return the skills text as a single block; real parsing can split into skill dicts later
    info = {"image_url": image_url}
    skills = [{"name": "SKILLS", "desc": skills_text}] if skills_text else []
    return {'info': info, 'stats': stats, 'skills': skills}

if __name__ == "__main__":
    main()
