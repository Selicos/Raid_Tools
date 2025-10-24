import json
import sys
import argparse
import os

try:
    import jsonschema
    JSONSCHEMA_AVAILABLE = True
except Exception:
    JSONSCHEMA_AVAILABLE = False

def validate_json_file(file_path, schema=None, strict=False):
    """Validate a JSON file and provide detailed error information."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        print(f"✓ JSON is valid!")
        # If schema/strict requested, run jsonschema validation
        if strict or schema is not None:
            if not JSONSCHEMA_AVAILABLE:
                print("! jsonschema package not available — skipping schema validation")
            else:
                try:
                    if schema is None:
                        jsonschema.validate(instance=data, schema=schema)
                    else:
                        jsonschema.validate(instance=data, schema=schema)
                except jsonschema.ValidationError as ve:
                    print(f"✗ Schema validation error: {ve.message}")
                    try:
                        # Attempt to show the path to the offending element
                        path = list(ve.absolute_path) if hasattr(ve, 'absolute_path') else list(ve.path)
                        if path:
                            pointer = '/' + '/'.join(str(p) for p in path)
                        else:
                            pointer = '/'
                        print(f"  JSON path: {pointer}")
                        # Try to locate the offending key in source text
                        try:
                            with open(file_path, 'r', encoding='utf-8') as f:
                                text = f.read()
                            # Look for the last path element as a JSON key occurrence
                            last_key = str(path[-1]) if path else None
                            if last_key is not None:
                                import re

                                # build a regex that matches the key and the value start
                                key_regex = re.compile(r'"' + re.escape(last_key) + r'"\s*:\s*', re.MULTILINE)
                                m = None
                                # search from the start; prefer later occurrences if path has indices
                                for match in key_regex.finditer(text):
                                    m = match
                                if m:
                                    start = m.start()
                                    # compute line and column
                                    line = text.count('\n', 0, start) + 1
                                    col = start - text.rfind('\n', 0, start)
                                    print(f"  Location: line {line}, column {col}")
                                    # show a small snippet
                                    lines = text.splitlines()
                                    snippet_start = max(0, line - 3)
                                    snippet_end = min(len(lines), line + 2)
                                    for i in range(snippet_start, snippet_end):
                                        ln = i + 1
                                        prefix = '>' if ln == line else ' '
                                        print(f"{prefix} {ln:4d}: {lines[i]}")
                                    # point to column (best-effort)
                                    pointer_line = ' ' * (col + 6) + '^'
                                    print(pointer_line)
                                else:
                                    print('  (Could not locate the key text in file; showing nearby JSON dump)')
                                    # dump the offending instance if available
                                    try:
                                        inst = ve.instance
                                        print(json.dumps(inst, indent=2))
                                    except Exception:
                                        pass
                        except Exception as e:
                            print(f"  (Could not read source file to locate error: {e})")
                    except Exception:
                        pass
                    return False
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

def validate_all_champion_jsons(directory, schema=None, strict=False):
    """Validate all champion JSON files in the given directory."""
    json_files = [f for f in os.listdir(directory) if f.endswith('.json') and not f.endswith('.old.json')]

    print(f"Validating {len(json_files)} champion JSON files in {directory}...")
    valid_count = 0

    for json_file in json_files:
        file_path = os.path.join(directory, json_file)
        print(f"\n--- Validating {json_file} ---")
        if validate_json_file(file_path, schema=schema, strict=strict):
            valid_count += 1

    print(f"\n=== Summary ===")
    print(f"Valid files: {valid_count}/{len(json_files)}")
    return valid_count == len(json_files)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Validate champion JSON files.")
    parser.add_argument('file', nargs='?', help='Path to a champion JSON file to validate')
    parser.add_argument('--all', action='store_true', help='Validate all files in input/Champion_Dictionary (default for --all)')
    parser.add_argument('--all-output', action='store_true', help='Validate all files in output/Champions (legacy behavior)')
    parser.add_argument('--dir', help='Validate all JSON files in the given directory')
    parser.add_argument('--schema', action='store_true', help='Enable JSON Schema validation using the template')
    parser.add_argument('--strict', action='store_true', help='Alias for --schema')

    args = parser.parse_args()

    # Load schema if requested and available
    schema = None
    if (args.schema or args.strict):
        schema_path = os.path.join(os.path.dirname(__file__), '..', 'input', 'Templates', 'Champion_Dictionary_Schema.json')
        try:
            with open(schema_path, 'r', encoding='utf-8') as sf:
                schema = json.load(sf)
        except Exception as e:
            print(f"! Could not load schema from {schema_path}: {e}")
            schema = None

    exit_code = 0

    # Determine mode
    if args.all_output:
        target_dir = os.path.join(os.path.dirname(__file__), '..', 'output', 'Champions')
        ok = validate_all_champion_jsons(target_dir, schema=schema, strict=args.strict)
        exit_code = 0 if ok else 1
    elif args.all or (not args.file and not args.dir and not args.all_output):
        # default --all behavior: validate input/Champion_Dictionary
        target_dir = os.path.join(os.path.dirname(__file__), '..', 'input', 'Champion_Dictionary')
        if os.path.isdir(target_dir):
            ok = validate_all_champion_jsons(target_dir, schema=schema, strict=args.strict)
            exit_code = 0 if ok else 1
        else:
            print(f"! Directory not found: {target_dir}")
            exit_code = 1
    elif args.dir:
        target_dir = args.dir
        if os.path.isdir(target_dir):
            ok = validate_all_champion_jsons(target_dir, schema=schema, strict=args.strict)
            exit_code = 0 if ok else 1
        else:
            print(f"! Directory not found: {target_dir}")
            exit_code = 1
    elif args.file:
        ok = validate_json_file(args.file, schema=schema, strict=args.strict)
        exit_code = 0 if ok else 1
    else:
        # Interactive prompt
        file_path = input("Enter path to champion JSON file to validate: ").strip()
        if file_path:
            ok = validate_json_file(file_path, schema=schema, strict=args.strict)
            exit_code = 0 if ok else 1
        else:
            print("No file path provided. Exiting.")
            exit_code = 1

    sys.exit(exit_code)