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
            if key in data_section and data_section[key] not in [None, ""]:
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
    # Patch: Map scraped_data['info'] fields to top-level template fields
    info = scraped_data.get('info', {})
    for key in ['name', 'faction', 'rarity', 'role', 'affinity']:
        if key in info and info[key]:
            template[key] = info[key]
    # Patch: Map scraped_data['skills'] to forms[0]['skills'] if present
    if 'skills' in scraped_data and scraped_data['skills']:
        if 'forms' in template and isinstance(template['forms'], list) and len(template['forms']) > 0:
            # Transform scraped skills to match template structure
            template_skill = template['forms'][0]['skills'][0]
            transformed_skills = []
            for skill in scraped_data['skills']:
                # Create a copy of the template skill
                import copy
                new_skill = copy.deepcopy(template_skill)
                # Map scraped fields to template fields
                new_skill['name'] = skill.get('name', '')
                new_skill['type'] = skill.get('type', '')
                new_skill['description'] = skill.get('desc', '')  # Map 'desc' to 'description'
                # Keep template defaults for fields we don't scrape yet
                # effects, cooldown_booked, mechanics_tags, book_value, notes remain as template defaults
                transformed_skills.append(new_skill)
            template['forms'][0]['skills'] = transformed_skills
    # Patch: Map scraped_data['aura'] to forms[0]['aura'] if present
    if 'aura' in scraped_data and scraped_data['aura']:
        if 'forms' in template and isinstance(template['forms'], list) and len(template['forms']) > 0:
            template['forms'][0]['aura'] = scraped_data['aura']
    # Patch: Map scraped_data['stats'] to forms[0]['base_stats'] if present
    if 'stats' in scraped_data and scraped_data['stats']:
        if 'forms' in template and isinstance(template['forms'], list) and len(template['forms']) > 0:
            print(f"[DEBUG] Mapping stats to template: {scraped_data['stats']}")
            # Map stat names to template field names (should already be mapped in champion_scraper.py)
            # These keys should match the valid_stats in champion_scraper.py
            stat_mapping = {
                'HP': 'HP',
                'ATK': 'ATK',
                'DEF': 'DEF',
                'SPD': 'SPD',
                'C.RATE': 'C.RATE',
                'C.DMG': 'C.DMG',
                'RES': 'RES',
                'ACC': 'ACC'
            }
            for scraped_name, template_name in stat_mapping.items():
                if scraped_name in scraped_data['stats']:
                    value = scraped_data['stats'][scraped_name]
                    print(f"[DEBUG] Mapping {scraped_name} ({value}) -> {template_name}")
                    # Convert to int if possible
                    try:
                        template['forms'][0]['base_stats'][template_name] = int(value)
                    except (ValueError, TypeError):
                        template['forms'][0]['base_stats'][template_name] = value
                else:
                    print(f"[DEBUG] Stat {scraped_name} not found in scraped data")
    champion_json = fill_template_with_data(template, scraped_data)
    champion_json["draft"] = True

    # Add validation metadata if available
    validation_info = scraped_data.get('validation', {})
    print(f"[DEBUG] Validation info in scraped_data: {validation_info}")
    if validation_info:
        champion_json['validation_metadata'] = {
            'stat_confidence': validation_info.get('confidence', 0),
            'stat_differences': validation_info.get('differences', []),
            'data_sources': validation_info.get('sources', ''),
            'ocr_notes': 'Stats compared between RaidWiki and Ayumilove OCR' if 'validated' in validation_info.get('sources', '') else 'OCR only - consider manual verification'
        }
        print(f"[DEBUG] Added validation_metadata to champion JSON")

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(champion_json, f, indent=2, ensure_ascii=False)

    print(f"Champion JSON for {champion_name} written to {output_path}")
