import json
import sys

def validate_json_file(file_path):
    """Validate a JSON file and provide detailed error information."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        print(f"✓ JSON is valid!")
        # Champion name detection (root or overview)
        champ_name = data.get('champion')
        if not champ_name:
            champ_name = data.get('name')
        if not champ_name and 'overview' in data:
            champ_name = data['overview'].get('name', 'Unknown')
        elif not champ_name:
            champ_name = 'Unknown'
        # Rarity detection (root or overview)
        rarity = data.get('rarity')
        if not rarity and 'overview' in data:
            rarity = data['overview'].get('rarity', 'Unknown')
        elif not rarity:
            rarity = 'Unknown'
        # Print as comments
        print(f"# Champion: {champ_name}")
        print(f"# Rarity: {rarity}")
        return True
    except json.JSONDecodeError as e:
        print(f"✗ JSON Error: {e}")
        print(f"Line: {e.lineno}, Column: {e.colno}")
        print(f"Error position: {e.pos}")
        return False
    except Exception as e:
        print(f"✗ Other error: {e}")
        return False

def validate_all_champion_jsons():
    """Validate all champion JSON files in the Champions directory."""
    import os
    champions_dir = os.path.join(os.path.dirname(__file__), '..', 'output', 'Champions')
    json_files = [f for f in os.listdir(champions_dir) if f.endswith('.json') and not f.endswith('.old.json')]
    
    print(f"Validating {len(json_files)} champion JSON files...")
    valid_count = 0
    
    for json_file in json_files:
        file_path = os.path.join(champions_dir, json_file)
        print(f"\n--- Validating {json_file} ---")
        if validate_json_file(file_path):
            valid_count += 1
    
    print(f"\n=== Summary ===")
    print(f"Valid files: {valid_count}/{len(json_files)}")
    return valid_count == len(json_files)

if __name__ == "__main__":
    # Usage:
    #   python validate_json.py --all                # Validate all champion JSONs
    #   python validate_json.py <file_path>          # Validate a specific JSON file
    #   python validate_json.py                      # Prompt for a file path interactively
    if len(sys.argv) > 1 and sys.argv[1] == "--all":
        validate_all_champion_jsons()
    elif len(sys.argv) > 1:
        file_path = sys.argv[1]
        validate_json_file(file_path)
    else:
        # Prompt user for file path interactively
        file_path = input("Enter path to champion JSON file to validate: ").strip()
        if file_path:
            validate_json_file(file_path)
        else:
            print("No file path provided. Exiting.")