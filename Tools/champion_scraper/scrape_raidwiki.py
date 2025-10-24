def extract_champion_info(soup):
    # Look for the section with faction, affinity, rarity, role
    info = {'Faction': '', 'Affinity': '', 'Rarity': '', 'Role': ''}
    # Try to find the text after 'belongs to' or similar
    text = soup.get_text("\n")
    import re
    # Faction
    m = re.search(r'belongs to "([^"]+)" faction', text)
    if m:
        info['Faction'] = m.group(1)
    # Affinity
    m = re.search(r'Affinity\s+([A-Za-z]+)', text)
    if m:
        info['Affinity'] = m.group(1)
    # Rarity
    m = re.search(r'Rarity\s+([A-Za-z]+)', text)
    if m:
        info['Rarity'] = m.group(1)
    # Role
    m = re.search(r'Role\s+([A-Za-z]+)', text)
    if m:
        info['Role'] = m.group(1)
    return info
import requests
from bs4 import BeautifulSoup
import sys
import re

def normalize_champion_name(name):
    # Converts champion name to RaidWiki URL format (lowercase, hyphens, remove special chars)
    name = name.strip().lower().replace("'", "")
    name = re.sub(r"[^a-z0-9 ]", "", name)
    name = re.sub(r"\s+", "-", name)
    return name

def fetch_champion_page(url):
    resp = requests.get(url)
    resp.raise_for_status()
    return resp.text

def extract_stats(soup):
    # Look for <strong> tags with stat names, then get their next siblings for values
    stats = {}
    stat_map = {
        'Health Points:': 'HP',
        'Attack:': 'ATK',
        'Defense:': 'DEF',
        'Speed:': 'SPD',
        'Critical Rate:': 'C. RATE',
        'Critical Damage:': 'C. DMG',
        'Debuff Resistance:': 'RESIST',
        'Debuff Accuracy:': 'ACC',
    }
    # Try to find stats in table rows with <strong> tags
    for row in soup.find_all('tr'):
        strong = row.find('strong')
        if strong:
            label = strong.get_text(strip=True)
            if label in stat_map:
                # The value is in the next <td>, possibly inside <a>
                tds = row.find_all('td')
                if len(tds) >= 2:
                    value_tag = tds[1].find('a') or tds[1]
                    value = value_tag.get_text(strip=True).replace(',', '').replace('%','')
                    stats[stat_map[label]] = value
    # Fallback: try previous <strong> logic if table not found
    if not stats:
        for strong in soup.find_all('strong'):
            label = strong.get_text(strip=True)
            if label in stat_map:
                value = strong.next_sibling
                while (value is not None) and (str(value).strip() == '' or str(value).strip() == ':'):
                    value = value.next_sibling
                if hasattr(value, 'get_text'):
                    value = value.get_text(strip=True)
                elif value is not None:
                    value = str(value).strip()
                else:
                    value = ''
                value = value.replace('%','')
                stats[stat_map[label]] = value
    if not stats:
        print("[DEBUG] No stats found in <strong> tags.")
    return stats

def extract_skills(soup):
    # Find the <h4> header for skills
    skills = []
    skills_section = None
    for h4 in soup.find_all('h4'):
        if "skills" in h4.get_text(strip=True).lower():
            skills_section = h4
            break
    if not skills_section:
        print("[DEBUG] No <h4> Skills section found.")
        return skills
    # Use find_next_siblings to robustly traverse the section
    # Find all <div class='nk-widget-post'> blocks in the document and extract skill info
    for post in soup.find_all('div', class_='nk-widget-post'):
        h3 = post.find('h3')
        meta = post.find('div', class_='nk-post-meta-date')
        if h3 and meta:
            name = h3.get_text(strip=True)
            desc = meta.get_text("\n", strip=True)
            skill_block = {'name': name, 'desc': desc}
            if skill_block['desc']:
                skills.append(skill_block)
    return skills

def main():
    if len(sys.argv) < 2:
        print("Usage: python scrape_raidwiki.py <champion name>")
        sys.exit(1)
    champ_name = sys.argv[1]
    norm_name = normalize_champion_name(champ_name)
    url = f"https://raidwiki.com/champion/{norm_name}"
    print(f"Fetching: {url}")
    html = fetch_champion_page(url)
    soup = BeautifulSoup(html, 'lxml')
    info = extract_champion_info(soup)
    print("Champion Info:")
    for k, v in info.items():
        print(f"{k}: {v}")
    stats = extract_stats(soup)
    print("\nBase Stats:", stats)
    skills = extract_skills(soup)
    print("\nSkills:")
    for skill in skills:
        print(f"\n{skill['name']}\n{skill['desc']}")

if __name__ == "__main__":
    main()
