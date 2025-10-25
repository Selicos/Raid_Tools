def diff_champion_jsons(old_json, new_json, log_path):
    """
    Compare two champion JSON dicts and write a line-by-line diff log with JSON paths and values.
    Output format: <JSON path>: <old value> -> <new value>
    """
    diffs = []

    def compare(a, b, path=""):
        if isinstance(a, dict) and isinstance(b, dict):
            keys = set(a.keys()) | set(b.keys())
            for key in keys:
                new_path = f"{path}.{key}" if path else key
                compare(a.get(key), b.get(key), new_path)
        elif isinstance(a, list) and isinstance(b, list):
            max_len = max(len(a), len(b))
            for i in range(max_len):
                new_path = f"{path}[{i}]"
                a_val = a[i] if i < len(a) else None
                b_val = b[i] if i < len(b) else None
                compare(a_val, b_val, new_path)
        else:
            if a != b:
                diffs.append(f"{path}: {repr(a)} -> {repr(b)}")

    compare(old_json, new_json)

    with open(log_path, 'w', encoding='utf-8') as f:
        if diffs:
            f.write("Champion JSON differences found:\n")
            for diff in diffs:
                f.write(diff + "\n")
        else:
            f.write("No differences found.\n")

    print(f"Champion diff log written to {log_path}")


import json
import os

# Utility functions
def load_template(template_path):
    """Load the canonical champion template from file."""
    with open(template_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def fill_template_with_data(template_section, data_section):
    """
    Recursively fill the template with scraped data, leaving blanks for missing fields.
    """
    if isinstance(template_section, dict):
        result = {}
        for key, value in template_section.items():
            # Special case: always use mapped skills if present
            if key == 'skills' and 'skills' in data_section and isinstance(data_section['skills'], list) and len(data_section['skills']) > 0:
                result[key] = data_section['skills']
            elif key in data_section and data_section[key] not in [None, ""]:
                # Recursively fill nested dicts/lists
                if isinstance(value, (dict, list)):
                    result[key] = fill_template_with_data(value, data_section[key])
                else:
                    result[key] = data_section[key]
            else:
                result[key] = value
        return result
    elif isinstance(template_section, list):
        # If the template is a list, fill with data if available, else keep as is
        if data_section and isinstance(data_section, list):
            return data_section
        return template_section
    else:
        return data_section if data_section not in [None, ""] else template_section

def diff_champion_jsons(old_json, new_json, log_path):
    """
    Compare two champion JSON dicts and write a line-by-line diff log with JSON paths and values.
    Output format: <JSON path>: <old value> -> <new value>
    """
    diffs = []

    def compare(a, b, path=""):
        if isinstance(a, dict) and isinstance(b, dict):
            keys = set(a.keys()) | set(b.keys())
            for key in keys:
                new_path = f"{path}.{key}" if path else key
                compare(a.get(key), b.get(key), new_path)
        elif isinstance(a, list) and isinstance(b, list):
            max_len = max(len(a), len(b))
            for i in range(max_len):
                new_path = f"{path}[{i}]"
                a_val = a[i] if i < len(a) else None
                b_val = b[i] if i < len(b) else None
                compare(a_val, b_val, new_path)
        else:
            if a != b:
                diffs.append(f"{path}: {repr(a)} -> {repr(b)}")

    compare(old_json, new_json)

    with open(log_path, 'w', encoding='utf-8') as f:
        if diffs:
            f.write("Champion JSON differences found:\n")
            for diff in diffs:
                f.write(diff + "\n")
        else:
            f.write("No differences found.\n")

    print(f"Champion diff log written to {log_path}")

# Main entry point
def generate_champion_json(champion_name, scraped_data, template_path, output_path):
    """
    Generate a champion JSON file using the canonical template, filling in available scraped data.
    Missing fields are left blank ("", 0, [], or {} as appropriate).
    Always sets 'draft': true.
    """
    template = load_template(template_path)
    output = template.copy()
    output['draft'] = True
    # Fill top-level fields with scraped overview info if present
    info = scraped_data.get('info', {})
    output['name'] = info.get('name', template.get('name', ""))
    output['rarity'] = info.get('rarity', template.get('rarity', ""))
    output['affinity'] = info.get('affinity', template.get('affinity', ""))
    output['faction'] = info.get('faction', template.get('faction', ""))
    output['role'] = info.get('role', template.get('role', ""))
    # Build forms manually to ensure mapped skills are used
    forms = []
    base_form = template['forms'][0].copy()
    # Fill base stats
    base_stats = base_form['base_stats'].copy()
    for stat in base_stats:
        base_stats[stat] = scraped_data.get('stats', {}).get(stat, "")
    base_form['base_stats'] = base_stats
    # Fill skills, mapping Ayumilove data to template structure
    template_skills = template['forms'][0].get('skills', [])
    default_skill = {
        "name": "Skill Name",
        "type": "A1/A2/A3/Passive",
        "description": "Skill effect description.",
        "effects": [
            {
                "type": "damage|shield|heal|turn_meter_fill|turn_meter_steal|revive|buff|debuff|stat_swap|stat_steal|reflect_damage|other",
                "stat": "ATK|HP|DEF|MAX HP|ENEMY_MAX_HP|Turn Meter|NA|...",
                "value": 0.0,
                "per_hit": False,
                "target": "single_enemy|random_enemy|aoe_enemies|single_ally|random_ally|aoe_allies|self",
                "duration": 2,
                "notes": "Describe scaling, conditions, or special logic."
            }
        ],
        "cooldown_booked": None,
        "mechanics_tags": ["Relevant mechanic tags"],
        "book_value": "Value to fully book ex faster cooldown, more damage or debuff chance, etc.",
        "notes": "Additional notes (conditional effects, scaling, special interactions, etc.)"
    }
    ayumi_skills = scraped_data.get('skills', [])
    mapped_skills = []
    for i, skill in enumerate(ayumi_skills):
        # Use template skill as base, fill available fields
        skill_template = (template_skills[0].copy() if template_skills else default_skill.copy())
        skill_template['name'] = skill.get('name', skill_template['name'])
        skill_template['description'] = skill.get('desc', skill_template.get('description', ''))
        # Try to infer type (A1/A2/A3/Passive/Aura) from name or order
        name_lc = skill_template['name'].lower()
        if 'passive' in name_lc:
            skill_template['type'] = 'Passive'
        elif 'aura' in name_lc:
            skill_template['type'] = 'Aura'
        else:
            skill_template['type'] = f"A{i+1}"
        mapped_skills.append(skill_template)
    base_form['skills'] = mapped_skills
    forms.append(base_form)
    output['forms'] = forms

    # Add validation metadata if available
    validation_info = scraped_data.get('validation', {})
    print(f"[DEBUG] Validation info in scraped_data: {validation_info}")
    if validation_info:
        output['validation_metadata'] = {
            'stat_confidence': validation_info.get('confidence', 0),
            'stat_differences': validation_info.get('differences', []),
            'data_sources': validation_info.get('sources', ''),
            'ocr_notes': 'Stats compared between RaidWiki and Ayumilove OCR' if 'validated' in validation_info.get('sources', '') else 'OCR only - consider manual verification'
        }
        print(f"[DEBUG] Added validation_metadata to output JSON")

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(output, f, indent=2, ensure_ascii=False)

    print(f"Champion JSON for {champion_name} written to {output_path}")
