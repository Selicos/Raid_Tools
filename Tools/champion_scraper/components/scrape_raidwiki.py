import requests
from bs4 import BeautifulSoup
import sys
import re
import os

def extract_champion_info(soup):
    info = {'Faction': '', 'Affinity': '', 'Rarity': '', 'Role': ''}
    text = soup.get_text("\n")
    m = re.search(r'belongs to "([^"]+)" faction', text)
    if m:
        info['Faction'] = m.group(1)
    m = re.search(r'Affinity\s+([A-Za-z]+)', text)
    if m:
        info['Affinity'] = m.group(1)
    m = re.search(r'Rarity\s+([A-Za-z]+)', text)
    if m:
        info['Rarity'] = m.group(1)
    m = re.search(r'Role\s+([A-Za-z]+)', text)
    if m:
        info['Role'] = m.group(1)
    return info

def normalize_champion_name(name):
    name = name.strip().lower().replace("'", "")
    name = re.sub(r"[^a-z0-9 ]", "", name)
    name = re.sub(r"\s+", "-", name)
    return name

def fetch_champion_page(url):
    resp = requests.get(url)
    resp.raise_for_status()
    return resp.text

def extract_stats(soup):
    stats = {}
    stat_map = {
        'Health Points:': 'HP',
        'Attack:': 'ATK',
        'Defense:': 'DEF',
        'Speed:': 'SPD',
        'Critical Rate:': 'C. RATE',
        'Critical Damage:': 'C. DMG',
        'Debuff Resistance:': 'RESIST',
        'Debuff Accuracy': 'ACC',
    }
    for row in soup.find_all('tr'):
        strong = row.find('strong')
        if strong:
            label = strong.get_text(strip=True)
            if label in stat_map:
                tds = row.find_all('td')
                if len(tds) >= 2:
                    value_tag = tds[1].find('a') or tds[1]
                    value = value_tag.get_text(strip=True).replace(',', '').replace('%','')
                    stats[stat_map[label]] = value
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
    skills = []
    skills_section = None
    for h4 in soup.find_all('h4'):
        if "skills" in h4.get_text(strip=True).lower():
            skills_section = h4
            break
    if not skills_section:
        print("[DEBUG] No <h4> Skills section found.")
        return skills
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

def scrape_raidwiki_champion(champ_name):
    norm_name = normalize_champion_name(champ_name)
    url = f"https://raidwiki.com/champion/{norm_name}"
    print(f"[RaidWiki] Fetching: {url}")
    try:
        html = fetch_champion_page(url)
    except Exception as e:
        print(f"[RaidWiki][ERROR] Failed to fetch {champ_name}: {e}")
        return None
    soup = BeautifulSoup(html, 'lxml')
    info = extract_champion_info(soup)
    stats = extract_stats(soup)
    skills = extract_skills(soup)
    
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
    
    return {'info': info, 'stats': stats, 'skills': filtered_skills, 'aura': aura_desc}

def main():
    if len(sys.argv) < 2:
        print("Usage: python scrape_raidwiki.py <champion name>")
        sys.exit(1)
    champ_name = sys.argv[1]
    data = scrape_raidwiki_champion(champ_name)
    if not data:
        print("[ERROR] No data returned.")
        sys.exit(1)
    print("Champion Info:", data['info'])
    print("Base Stats:", data['stats'])
    print("Skills:", data['skills'])

if __name__ == "__main__":
    main()
