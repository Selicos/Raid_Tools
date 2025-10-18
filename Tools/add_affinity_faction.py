"""
Add Affinity and Faction fields to owned champion list.

This script reads the owned champion list and adds Affinity and Faction
fields for all champions by looking up data from Ayumilove.

Usage:
    python Tools/add_affinity_faction.py
"""

import re
from pathlib import Path

# Champion data - manually curated from authoritative sources
# Format: "Champion Name": ("Affinity", "Faction")
CHAMPION_DATA = {
    "Abbess": ("Force", "Sacred Order"),
    "Adelyn": ("Spirit", "High Elves"),
    "Akoth the Seared": ("Force", "Demonspawn"),
    "Alice the Wanderer": ("Magic", "Shadowkin"),
    "Alure": ("Spirit", "Demonspawn"),
    "Aox the Rememberer": ("Void", "Lizardmen"),
    "Apothecary": ("Magic", "High Elves"),
    "Arbiter": ("Void", "High Elves"),
    "Archmage Hellmut": ("Force", "Banner Lords"),
    "Artak": ("Force", "Barbarians"),
    "Astralon": ("Magic", "Dark Elves"),
    "Bad-el-Kazar": ("Spirit", "Undead Hordes"),
    "Black Knight": ("Void", "Banner Lords"),
    "Brakus the Shifter": ("Magic", "Ogryn Tribes"),
    "Broadmaw": ("Spirit", "Lizardmen"),
    "Burangiri": ("Force", "Shadowkin"),
    "Caoilte the Asharrow": ("Magic", "Sylvan Watchers"),
    "Cleopterix": ("Void", "Demonspawn"),
    "Coldheart": ("Spirit", "Dark Elves"),
    "Criodan the Blue": ("Force", "Sylvan Watchers"),
    "Crohnam": ("Force", "Barbarians"),
    "Dark Athel": ("Magic", "Undead Hordes"),
    "Dark Kael": ("Force", "Undead Hordes"),
    "Deacon Armstrong": ("Force", "Knights Revenant"),
    "Deudan the Runic": ("Magic", "Barbarians"),
    "Dhukk the Pierced": ("Magic", "Skinwalkers"),
    "Djamarsa": ("Spirit", "Demonspawn"),
    "Drexthar Bloodtwin": ("Force", "Demonspawn"),
    "Elenaril": ("Magic", "High Elves"),
    "Embrys the Anomaly": ("Void", "Sylvan Watchers"),
    "Eolfrig": ("Spirit", "Barbarians"),
    "Fayne": ("Magic", "Dark Elves"),
    "Fenshi": ("Spirit", "Shadowkin"),
    "Frozen Banshee": ("Spirit", "Undead Hordes"),
    "Fyt-gun Isable": ("Force", "Ogryn Tribes"),
    "Geomancer": ("Magic", "Barbarians"),
    "Ghostborn": ("Magic", "Knights Revenant"),
    "Godseeker Aniri": ("Void", "Barbarians"),
    "Gretel Hagbane": ("Spirit", "Sylvan Watchers"),
    "Guurda Bogbrew": ("Force", "Ogryn Tribes"),
    "He-Man": ("Void", "Eternals"),
    "High Khatun": ("Spirit", "Barbarians"),
    "Hotatsu": ("Magic", "Shadowkin"),
    "Husk": ("Force", "Skinwalkers"),
    "Ithos": ("Void", "Sacred Order"),
    "Iudex Artor": ("Magic", "Knights Revenant"),
    "Juliana": ("Magic", "Knights Revenant"),
    "Kalvalax": ("Magic", "Demonspawn"),
    "Kantra the Cyclone": ("Force", "Barbarians"),
    "Kinagashi": ("Spirit", "Shadowkin"),
    "Lady Annabelle": ("Magic", "Knights Revenant"),
    "Leminisi the Gold-Wing": ("Force", "Sylvan Watchers"),
    "Loki the Deceiver": ("Void", "Asgardians"),
    "Lord Champfort": ("Magic", "Banner Lords"),
    "Lord Shazar": ("Force", "Demonspawn"),
    "Lua": ("Spirit", "Shadowkin"),
    "Maulie Tankard": ("Magic", "Dwarves"),
    "Mausoleum Mage": ("Void", "Undead Hordes"),
    "Michelangelo": ("Void", "Eternals"),
    "Mistrider Daithi": ("Force", "Sylvan Watchers"),
    "Mithrala Lifebane": ("Spirit", "Undead Hordes"),
    "Narma the Returned": ("Void", "Undead Hordes"),
    "Ninja": ("Spirit", "Shadowkin"),
    "Nogdar the Headhunter": ("Force", "Ogryn Tribes"),
    "Nogoryo": ("Magic", "Shadowkin"),
    "Norog": ("Magic", "Skinwalkers"),
    "Pain Keeper": ("Void", "Knights Revenant"),
    "Paragon": ("Void", "Undead Hordes"),
    "Quargan the Crowned": ("Magic", "Ogryn Tribes"),
    "Queen Eva": ("Void", "Banner Lords"),
    "Rathalos Blademaster": ("Force", "Lizardmen"),
    "Rector Drath": ("Spirit", "Knights Revenant"),
    "Relickeeper": ("Magic", "Sacred Order"),
    "Rhazin Scarhide": ("Magic", "Lizardmen"),
    "Rian the Conjurer": ("Force", "High Elves"),
    "Robar": ("Magic", "Banner Lords"),
    "Runekeeper Dazdurk": ("Magic", "Dwarves"),
    "Sanguinia": ("Spirit", "Demonspawn"),
    "Scyl of the Drakes": ("Spirit", "Barbarians"),
    "Seeker": ("Force", "High Elves"),
    "Skeletor": ("Void", "Eternals"),
    "Skullcrown": ("Force", "Undead Hordes"),
    "Skullcrusher": ("Void", "Ogryn Tribes"),
    "Stag Knight": ("Spirit", "Sacred Order"),
    "Sun Wukong": ("Magic", "Asgardians"),
    "Tagoar": ("Force", "Ogryn Tribes"),
    "Taurus": ("Force", "Demonspawn"),
    "Taya": ("Force", "High Elves"),
    "Tayrel": ("Spirit", "High Elves"),
    "Ugir the Wyrm Eater": ("Spirit", "Skinwalkers"),
    "Ultimate Galek": ("Force", "Orcs"),
    "Uugo": ("Void", "Skinwalkers"),
    "Venomage": ("Spirit", "Lizardmen"),
    "Vergis": ("Spirit", "Banner Lords"),
    "Vergumkaar": ("Magic", "Demonspawn"),
    "Visix the Unbowed": ("Void", "Dark Elves"),
    "Vogoth": ("Force", "Demonspawn"),
    "Vrask": ("Spirit", "Skinwalkers"),
    "Warchief": ("Force", "Ogryn Tribes"),
    "White Dryad Nia": ("Magic", "Sylvan Watchers"),
}


def extract_champion_name(line: str) -> str:
    """Extract champion name from line, handling (x2), (x3), etc."""
    # Pattern: "- Champion Name (x2) | Rarity: ..."
    # or: "- Champion Name | Rarity: ..."
    match = re.match(r'^- (.+?)(?: \(x\d+\))? \| Rarity:', line)
    if match:
        return match.group(1).strip()
    return ""


def update_owned_list():
    """Update owned champion list with Affinity and Faction fields."""
    input_file = Path("input/Owned_champion_list.md")
    
    if not input_file.exists():
        print(f"Error: {input_file} not found")
        return
    
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    updated_lines = []
    updated_count = 0
    missing_count = 0
    missing_champions = []
    
    for line in lines:
        if line.strip().startswith('- ') and '| Rarity:' in line:
            champ_name = extract_champion_name(line)
            
            if champ_name in CHAMPION_DATA:
                affinity, faction = CHAMPION_DATA[champ_name]
                # Insert Affinity and Faction after Rarity
                updated_line = line.rstrip()
                if '| Affinity:' not in updated_line and '| Faction:' not in updated_line:
                    # Add fields after Rarity
                    updated_line = updated_line.replace(
                        '| Rarity:',
                        f'| Rarity:'
                    )
                    # Find Rarity value and insert after it
                    parts = updated_line.split('|')
                    new_parts = []
                    for i, part in enumerate(parts):
                        new_parts.append(part)
                        if 'Rarity:' in part:
                            # Insert Affinity and Faction after Rarity
                            new_parts.append(f' Affinity: {affinity} ')
                            new_parts.append(f' Faction: {faction} ')
                    updated_line = '|'.join(new_parts)
                    updated_lines.append(updated_line + '\n')
                    updated_count += 1
                else:
                    updated_lines.append(line)
            else:
                missing_champions.append(champ_name)
                missing_count += 1
                updated_lines.append(line)
        else:
            updated_lines.append(line)
    
    # Write updated file
    with open(input_file, 'w', encoding='utf-8') as f:
        f.writelines(updated_lines)
    
    print(f"✅ Updated {updated_count} champions with Affinity and Faction")
    if missing_count > 0:
        print(f"⚠️  {missing_count} champions missing data:")
        for champ in missing_champions:
            print(f"   - {champ}")
    
    return updated_count, missing_count


if __name__ == "__main__":
    updated, missing = update_owned_list()
    print(f"\n📊 Summary:")
    print(f"   Updated: {updated} champions")
    print(f"   Missing: {missing} champions")
    
    if missing == 0:
        print(f"\n🎉 All champions updated successfully!")
    else:
        print(f"\n⚠️  Some champions need manual lookup")
