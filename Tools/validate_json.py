import json
import sys

def validate_json_file(file_path):
    """Validate a JSON file and provide detailed error information."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        print(f"✓ JSON is valid!")
        print(f"Champion: {data.get('champion', 'Unknown')}")
        print(f"Rarity: {data.get('rarity', 'Unknown')}")
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
    champions_dir = r'c:\GIT\Raid_Tools\Champion Review and Comparison\Champions'
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
    if len(sys.argv) > 1 and sys.argv[1] == "--all":
        validate_all_champion_jsons()
    else:
        file_path = r'c:\GIT\Raid_Tools\Champion Review and Comparison\Champions\Alice the wanderer.json'
        validate_json_file(file_path)