"""
Debug image finding for Gretel Hagbane
"""
import requests
from bs4 import BeautifulSoup

url = "https://ayumilove.net/raid-shadow-legends-gretel-hagbane-skill-mastery-equip-guide/"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')

champ_name = "Gretel Hagbane"
champ_name_lc = champ_name.strip().lower().replace("'", "").replace(" ", "_")
champ_name_hyphen = champ_name.strip().lower().replace(" ", "-")

print(f"Looking for: {champ_name}")
print(f"  Lowercase underscore: {champ_name_lc}")
print(f"  Lowercase hyphen: {champ_name_hyphen}")
print("\n" + "=" * 80)

all_imgs = soup.find_all('img')
print(f"\nFound {len(all_imgs)} images on the page")

print("\n" + "=" * 80)
print("Images with 'gretel' in src or alt:")
print("=" * 80)

for i, img in enumerate(all_imgs):
    src = img.get('src', '')
    data_src = img.get('data-src', '')
    data_lazy_src = img.get('data-lazy-src', '')
    alt = img.get('alt', '')
    
    if 'gretel' in src.lower() or 'gretel' in alt.lower() or 'gretel' in data_src.lower() or 'gretel' in data_lazy_src.lower():
        print(f"\nImage {i+1}:")
        print(f"  src: {src[:100]}")
        print(f"  data-src: {data_src}")
        print(f"  data-lazy-src: {data_lazy_src}")
        print(f"  alt: {alt}")
        
        # Check if it matches our logic
        actual_url = data_src or data_lazy_src or src
        if champ_name_lc in alt.lower() or champ_name_lc in actual_url.lower() or champ_name_hyphen in actual_url.lower():
            print("  ✅ MATCH!")
        else:
            print("  ❌ No match")
