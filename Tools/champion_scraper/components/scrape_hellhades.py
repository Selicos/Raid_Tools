import requests
from bs4 import BeautifulSoup
import sys
import re
import os

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
        for path in possible_paths:
            if os.path.exists(path):
                pytesseract.pytesseract.tesseract_cmd = path
                break
except ImportError:
    OCR_AVAILABLE = False
    print("[HellHades][INFO] OCR libraries not available - stat extraction disabled")


def normalize_champion_name(name):
    """
    Converts champion name to HellHades URL format (lowercase, hyphens, remove special chars).
    HellHades uses similar format to Ayumilove: lowercase with hyphens.
    """
    name = name.strip().lower().replace("'", "")
    name = re.sub(r"[^a-z0-9 ]", "", name)
    name = re.sub(r"\s+", "-", name)
    return name


def fetch_champion_page(url):
    """Fetch HellHades champion page HTML."""
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    resp = requests.get(url, headers=headers, timeout=10)
    resp.raise_for_status()
    return resp.text


def extract_champion_info_from_html(soup):
    """
    Extract champion info (faction, affinity, rarity, role) from HellHades HTML.
    Uses meta description tag which follows pattern:
    "Champion Name is a Rarity Affinity Role champion in the Faction faction"
    """
    info = {"faction": "", "affinity": "", "rarity": "", "role": ""}
    
    # PRIMARY METHOD: Extract from meta description tag (most reliable)
    # Pattern: "Name is a Rarity Affinity Role champion in the Faction faction"
    meta_desc = soup.find('meta', {'name': 'description'})
    if meta_desc and meta_desc.get('content'):
        desc = meta_desc['content']
        print(f"[HellHades][DEBUG] Meta description: {desc[:100]}...")
        
        # Match pattern with 'a' or 'an' article
        pattern = r'(.+?)\s+is\s+an?\s+(\w+)\s+(\w+)\s+(\w+)\s+champion\s+in\s+the\s+(.+?)\s+faction'
        match = re.search(pattern, desc, re.IGNORECASE)
        if match:
            info['name'] = match.group(1).strip()
            info['rarity'] = match.group(2).strip()
            info['affinity'] = match.group(3).strip()
            info['role'] = match.group(4).strip()
            info['faction'] = match.group(5).strip()
            print(f"[HellHades][INFO] Extracted from meta: Faction={info['faction']}, Affinity={info['affinity']}, Rarity={info['rarity']}, Role={info['role']}")
            return info
    
    # FALLBACK METHOD: Parse page text (less reliable)
    text = soup.get_text(" ", strip=True)
    
    # Extract Faction
    faction_match = re.search(r'Faction[:\s]+([A-Za-z\s]+?)(?:\s+Affinity|\s+Rarity|\s+Type|$)', text, re.IGNORECASE)
    if faction_match:
        info["faction"] = faction_match.group(1).strip()
    
    # Extract Affinity
    affinity_match = re.search(r'Affinity[:\s]+(Magic|Spirit|Force|Void)', text, re.IGNORECASE)
    if affinity_match:
        info["affinity"] = affinity_match.group(1).strip()
    
    # Extract Rarity
    rarity_match = re.search(r'Rarity[:\s]+(Legendary|Epic|Rare|Uncommon|Common|Mythical)', text, re.IGNORECASE)
    if rarity_match:
        info["rarity"] = rarity_match.group(1).strip()
    
    # Extract Role/Type
    role_match = re.search(r'(?:Role|Type)[:\s]+(Attack|HP|Defense|Support)', text, re.IGNORECASE)
    if role_match:
        info["role"] = role_match.group(1).strip()
    
    if info["faction"] or info["affinity"]:
        print(f"[HellHades][INFO] Extracted from page text: Faction={info['faction']}, Affinity={info['affinity']}, Rarity={info['rarity']}, Role={info['role']}")
    
    return info


def extract_stats_from_image(image_url, champion_name):
    """
    Extract champion stats from an image using OCR.
    Returns a dict of stats (HP, ATK, DEF, etc.) or empty dict if extraction fails.
    
    For HellHades images: Stats display format may differ from Ayumilove.
    Uses similar OCR approach but with HellHades-specific parsing.
    """
    if not OCR_AVAILABLE:
        return {}
    
    try:
        # Download the image
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        response = requests.get(image_url, headers=headers, timeout=10)
        response.raise_for_status()
        img = Image.open(BytesIO(response.content))
        
        # Perform OCR
        text = pytesseract.image_to_string(img)
        
        print(f"[HellHades][OCR][DEBUG] Extracted text from image:")
        print(text)
        print("[HellHades][OCR][DEBUG] " + "=" * 60)
        
        # Parse stats from OCR text
        stats = {}
        
        # Try labeled stat extraction first
        stat_patterns = {
            'HP': r'HP[:\s]+(\d[\d,]*)',
            'ATK': r'ATK[:\s]+(\d[\d,]*)',
            'DEF': r'DEF[:\s]+(\d[\d,]*)',
            'SPD': r'SPD[:\s]+(\d[\d,]*)',
            'C.RATE': r'C\.?\s*(?:RATE|Rate)[:\s]+(\d+)%?',
            'C.DMG': r'C\.?\s*(?:DMG|Dmg)[:\s]+(\d+)%?',
            'RES': r'RES(?:IST)?[:\s]+(\d+)',
            'ACC': r'ACC(?:URACY)?[:\s]+(\d+)',
        }
        
        for stat_name, pattern in stat_patterns.items():
            match = re.search(pattern, text, re.IGNORECASE)
            if match:
                value = match.group(1).replace(',', '')
                stats[stat_name] = value
        
        # If no labeled stats found, try positional extraction
        if not stats:
            print("[HellHades][OCR][INFO] No labeled stats found, trying positional extraction...")
            numbers = re.findall(r'\d[\d,]+', text)
            clean_numbers = [n.replace(',', '') for n in numbers]
            
            # Filter for reasonable stat values
            stat_candidates = []
            for num in clean_numbers:
                try:
                    val = int(num)
                    # Skip level (60), include stat values (10-30000)
                    if 10 <= val <= 30000:
                        stat_candidates.append(num)
                except ValueError:
                    continue
            
            # HellHades order (assumed similar to Ayumilove): HP, ATK, DEF, SPD, C.RATE, C.DMG, RES, ACC
            if len(stat_candidates) >= 8:
                stat_names = ['HP', 'ATK', 'DEF', 'SPD', 'C.RATE', 'C.DMG', 'RES', 'ACC']
                for i in range(8):
                    stats[stat_names[i]] = stat_candidates[i]
                print(f"[HellHades][OCR][INFO] Extracted {len(stats)} stats using positional mapping")
        
        if stats:
            print(f"[HellHades][OCR] ✓ Extracted {len(stats)} stats from image")
        else:
            print(f"[HellHades][OCR][WARNING] No stats matched from OCR text")
        
        return stats
    
    except Exception as e:
        print(f"[HellHades][OCR][ERROR] Failed to extract stats from image: {e}")
        return {}


def find_champion_image(soup, champion_name):
    """
    Find the champion splash artwork image on HellHades page.
    HellHades uses class='raid_champion_splash' for the main stat image.
    Returns image URL or None if not found.
    """
    champ_name_lc = champion_name.strip().lower().replace("'", "").replace(" ", "-")
    
    # PRIMARY METHOD: Look for class='raid_champion_splash' (most reliable)
    splash_imgs = soup.find_all('img', class_='raid_champion_splash')
    for img in splash_imgs:
        # HellHades uses data-orig-src for lazy loading
        src = img.get('data-orig-src') or img.get('src')
        if src:
            # Handle protocol-relative URLs
            if src.startswith('//'):
                src = 'https:' + src
            print(f"[HellHades][DEBUG] Found splash artwork image: {src}")
            return src
    
    # FALLBACK METHOD: Look for images with champion name in URL or alt text
    for img in soup.find_all('img'):
        alt = img.get('alt', '').lower()
        src = img.get('src', '').lower()
        data_src = img.get('data-src', '').lower()
        
        # Check if champion name is in image URL or alt text
        if (champ_name_lc in src or champ_name_lc in data_src or 
            champ_name_lc in alt):
            # Prefer data-src for lazy-loaded images
            image_url = img.get('data-src') or img.get('src')
            if image_url:
                # Handle protocol-relative URLs
                if image_url.startswith('//'):
                    image_url = 'https:' + image_url
                elif image_url.startswith('/'):
                    image_url = 'https://hellhades.com' + image_url
                print(f"[HellHades][DEBUG] Found champion image: {image_url}")
                return image_url
    
    print("[HellHades][DEBUG] No champion image found")
    return None


def scrape_hellhades_champion(champion_name, skip_stats=False):
    """
    Scrape HellHades champion page for stats and info.
    
    Args:
        champion_name: Champion name (e.g., "Frozen Banshee")
        skip_stats: If True, skip OCR stat extraction (faster)
    
    Returns:
        dict: {
            'info': {'faction', 'affinity', 'rarity', 'role'},
            'stats': {'HP', 'ATK', 'DEF', 'SPD', 'C.RATE', 'C.DMG', 'RES', 'ACC'},
            'validation': {'confidence': float, 'sources': str}
        }
        Or None if scraping failed
    """
    norm_name = normalize_champion_name(champion_name)
    url = f"https://hellhades.com/champions/{norm_name}/"
    
    print(f"[HellHades] Fetching: {url}")
    
    try:
        html = fetch_champion_page(url)
    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 404:
            print(f"[HellHades] Champion not found (404): {champion_name}")
        else:
            print(f"[HellHades][ERROR] HTTP error: {e}")
        return None
    except Exception as e:
        print(f"[HellHades][ERROR] Failed to fetch {champion_name}: {e}")
        return None
    
    soup = BeautifulSoup(html, 'lxml')
    
    # Extract champion info from HTML
    info = extract_champion_info_from_html(soup)
    
    # HellHades uses splash artwork images (character art overlay) - not suitable for OCR
    # Stats are obscured by champion graphics, making reliable extraction impossible
    # Use HellHades for info validation only, rely on Ayumilove for stats
    stats = {}
    stats_confidence = 0
    
    # Skip stats extraction - HellHades splash images don't have clean stat cards
    print("[HellHades] Skipping stats extraction - splash artwork not suitable for OCR")
    print("[HellHades] Using for info validation only (faction/affinity/rarity/role)")
    
    # Build validation metadata
    # HellHades provides info validation only (no stat extraction)
    validation = {
        'confidence': 0,  # No stats extracted (splash artwork not suitable for OCR)
        'sources': 'hellhades_info_only',
        'note': 'Info validation only - splash artwork not suitable for stat OCR'
    }
    
    # Log extracted values
    if info.get('faction') or info.get('affinity'):
        print(f"[HellHades][INFO] ✓ Extracted info: Faction={info.get('faction')}, "
              f"Affinity={info.get('affinity')}, Rarity={info.get('rarity')}, Role={info.get('role')}")
    else:
        print(f"[HellHades][WARNING] No info extracted from meta tags")
    
    return {
        'info': info,
        'stats': stats,  # Empty dict - no stats from splash artwork
        'validation': validation
    }


def main():
    if len(sys.argv) < 2:
        print("Usage: python scrape_hellhades.py <champion name>")
        sys.exit(1)
    
    champ_name = sys.argv[1]
    data = scrape_hellhades_champion(champ_name)
    
    if not data:
        print("[ERROR] No data returned.")
        sys.exit(1)
    
    print("\nChampion Info:", data['info'])
    print("Base Stats:", data['stats'])
    print("Validation:", data['validation'])


if __name__ == "__main__":
    main()
