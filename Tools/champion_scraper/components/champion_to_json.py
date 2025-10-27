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
def generate_champion_json(champion_name, scraped_data, template_path, output_path, update_table=False):
    """
    Generate a champion JSON file using the canonical template, filling in available scraped data.
    Missing fields are left blank ("", 0, [], or {} as appropriate).
    Always sets 'draft': true unless overridden.
    
    Args:
        champion_name (str): Champion name
        scraped_data (dict): Scraped data from sources
        template_path (str): Path to template JSON
        output_path (str): Path for output JSON
        update_table (bool): If True, add/update champion in Champion_stats.md after JSON generation
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
            print(f"[DEBUG] Stats keys: {list(scraped_data['stats'].keys())}")
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
                    # Convert to int if possible (handle decimal format from Fandom)
                    try:
                        # Special handling for C.RATE and C.DMG - convert decimal to int if needed
                        if scraped_name in ['C.RATE', 'C.DMG']:
                            num_val = float(value)
                            # If decimal (0.15), convert to percentage (15)
                            if num_val < 1:
                                num_val = int(num_val * 100)
                            else:
                                num_val = int(num_val)
                            template['forms'][0]['base_stats'][template_name] = num_val
                        else:
                            template['forms'][0]['base_stats'][template_name] = int(value)
                    except (ValueError, TypeError):
                        template['forms'][0]['base_stats'][template_name] = value
                else:
                    print(f"[DEBUG] Stat {scraped_name} not found in scraped data")
    champion_json = fill_template_with_data(template, scraped_data)
    
    # Handle draft status
    if 'draft' in scraped_data:
        champion_json["draft"] = scraped_data['draft']  # Use scraped value (e.g., "scrape failed")
    else:
        champion_json["draft"] = True  # Default to true

    # Add validation metadata if available
    validation_info = scraped_data.get('validation', {})
    print(f"[DEBUG] Validation info in scraped_data: {validation_info}")
    if validation_info:
        champion_json['validation_metadata'] = {
            'stat_confidence': validation_info.get('stat_confidence', 0),
            'data_sources': validation_info.get('data_sources', ''),
            'source_priority': validation_info.get('source_priority', {}),
            'ocr_notes': ', '.join(validation_info.get('validation_notes', []))
        }
        print(f"[DEBUG] Added validation_metadata to champion JSON")

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(champion_json, f, indent=2, ensure_ascii=False)

    print(f"Champion JSON for {champion_name} written to {output_path}")
    
    # Auto-update Champion_stats.md if requested
    if update_table:
        try:
            update_champion_in_table(champion_name, champion_json)
        except Exception as e:
            print(f"[WARNING] Failed to update Champion_stats.md: {e}")
            print(f"[WARNING] Champion JSON saved successfully, but table not updated")


def update_champion_in_table(champion_name, champion_json):
    """
    Add or update champion entry in Champion_stats.md table.
    Handles: add new row if missing, update existing row if present, re-alphabetize.
    
    Uses retry logic for file write conflicts during batch processing.
    """
    from pathlib import Path
    import time
    
    table_path = Path('c:/GIT/Raid_Tools/input/Champion_Dictionary/Champion_stats.md')
    
    if not table_path.exists():
        print(f"[TABLE ERROR] Champion_stats.md not found at {table_path}")
        return
    
    # Retry logic for file conflicts (up to 3 attempts with exponential backoff)
    max_retries = 3
    for attempt in range(max_retries):
        try:
            # Load existing table
            with open(table_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Parse existing champions
            existing_champions = parse_existing_table(content)
            
            # Extract champion data from JSON
            champion_row = extract_champion_row_from_json(champion_json)
            
            # Add or update
            existing_champions[champion_name] = champion_row
            
            # Re-alphabetize
            sorted_champions = dict(sorted(existing_champions.items()))
            
            # Write back to file
            write_updated_table(table_path, sorted_champions, content)
            
            print(f"[TABLE] ✓ Updated Champion_stats.md with {champion_name}")
            return  # Success - exit function
            
        except PermissionError as e:
            if attempt < max_retries - 1:
                wait_time = 2 ** attempt  # Exponential backoff: 1s, 2s, 4s
                print(f"[TABLE] File locked, retrying in {wait_time}s... (attempt {attempt + 1}/{max_retries})")
                time.sleep(wait_time)
            else:
                raise  # Re-raise after final attempt
        except Exception as e:
            print(f"[TABLE ERROR] Failed to update table: {e}")
            raise


def parse_existing_table(content):
    """Parse Champion_stats.md and return dict of existing champions"""
    champions = {}
    lines = content.split('\n')
    in_table = False
    
    for line in lines:
        if '| Name' in line and '| Faction' in line:
            in_table = True
            continue
        if in_table and '---' in line:
            continue
        if in_table and line.strip().startswith('|'):
            cells = [cell.strip() for cell in line.split('|')]
            cells = [c for c in cells if c]
            if len(cells) >= 2:
                name = cells[0].strip()
                if name and name != '-' and len(name) >= 2:
                    champions[name] = cells  # Store full row
    
    return champions


def extract_champion_row_from_json(champion_json):
    """Extract champion data from JSON and format as table row cells"""
    # Get base stats from first form
    base_stats = {}
    if 'forms' in champion_json and len(champion_json['forms']) > 0:
        base_stats = champion_json['forms'][0].get('base_stats', {})
    
    # Convert C.RATE/C.DMG to decimal format for table (15 → 0.15)
    crate = base_stats.get('C.RATE', '')
    cdmg = base_stats.get('C.DMG', '')
    
    if crate and crate != '':
        try:
            crate_num = float(crate)
            crate = f"{crate_num / 100:.2f}" if crate_num >= 1 else str(crate)
        except:
            pass
    
    if cdmg and cdmg != '':
        try:
            cdmg_num = float(cdmg)
            cdmg = f"{cdmg_num / 100:.2f}" if cdmg_num >= 1 else str(cdmg)
        except:
            pass
    
    # Build row cells (match Champion_stats.md column order)
    row = [
        champion_json.get('name', ''),
        champion_json.get('faction', ''),
        champion_json.get('rarity', ''),
        champion_json.get('role', ''),
        champion_json.get('affinity', ''),
        str(base_stats.get('HP', '')),
        str(base_stats.get('ATK', '')),
        str(base_stats.get('DEF', '')),
        str(base_stats.get('SPD', '')),
        str(crate) if crate else '',
        str(cdmg) if cdmg else '',
        str(base_stats.get('RES', '')),
        str(base_stats.get('ACC', '')),
        '\\-',  # Aura (not in JSON yet)
        '\\-',  # Aura magnitude
        '\\-',  # Aura location
        '\\-'   # Aura for
    ]
    
    return row


def write_updated_table(table_path, sorted_champions, original_content):
    """Write updated champion table back to Champion_stats.md"""
    # Preserve header/notes from original content
    lines = original_content.split('\n')
    header_lines = []
    
    for idx, line in enumerate(lines):
        if '| Name' in line and '| Faction' in line:
            break
        header_lines.append(line)
    
    # Build new table
    new_lines = header_lines
    new_lines.append('')
    new_lines.append('| Name | Faction | Rarity | Role | Affinity | HP | ATK | DEF | SPD | C. Rate | C. DMG | RES | ACC | Aura | Aura magnitude | Aura location | Aura for |')
    new_lines.append('| ---- | ------- | ------ | ---- | -------- | -- | --- | --- | --- | ------- | ------ | --- | --- | ---- | -------------- | ------------- | -------- |')
    
    for name, cells in sorted_champions.items():
        row = '| ' + ' | '.join(cells) + ' |'
        new_lines.append(row)
    
    # Write to file
    with open(table_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(new_lines))

