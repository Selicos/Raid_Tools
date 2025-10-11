import os
from collections import defaultdict

# Paths
champion_dir = r"Champion Review and Comparison"
champion_json_dir = os.path.join(champion_dir, "Champions")
prompt_dir = os.path.join(champion_dir, "prompt")

def find_case_duplicates(directory, extension):
    files = [f for f in os.listdir(directory) if f.lower().endswith(extension)]
    normalized = defaultdict(list)
    for f in files:
        base = f.lower()
        normalized[base].append(f)
    return {k: v for k, v in normalized.items() if len(v) > 1}

def report_duplicates():
    print("🔍 Scanning for case-insensitive duplicates...\n")

    json_dupes = find_case_duplicates(champion_json_dir, ".json")
    md_dupes = find_case_duplicates(prompt_dir, ".md")

    if not json_dupes and not md_dupes:
        print("✅ No duplicates found.")
        return

    if json_dupes:
        print("📁 JSON duplicates:")
        for base, variants in json_dupes.items():
            print(f" - {base}: {variants}")

    if md_dupes:
        print("\n📄 Markdown prompt duplicates:")
        for base, variants in md_dupes.items():
            print(f" - {base}: {variants}")

def merge_or_rename_duplicates(directory, extension, dry_run=True):
    duplicates = find_case_duplicates(directory, extension)
    for base, variants in duplicates.items():
        keep = variants[0]
        for dup in variants[1:]:
            src = os.path.join(directory, dup)
            dst = os.path.join(directory, keep)
            if dry_run:
                print(f"🧪 Would merge {dup} → {keep}")
            else:
                try:
                    with open(src, "r", encoding="utf-8") as f:
                        content = f.read()
                    with open(dst, "a", encoding="utf-8") as f:
                        f.write("\n\n# Merged from " + dup + "\n" + content)
                    os.remove(src)
                    print(f"✅ Merged {dup} → {keep}")
                except Exception as e:
                    print(f"❌ Failed to merge {dup}: {e}")

if __name__ == "__main__":
    report_duplicates()
    confirm = input("\nProceed to merge duplicates? (y/n): ").strip().lower()
    if confirm == "y":
        print("\n⚙️ Merging JSON files...")
        merge_or_rename_duplicates(champion_json_dir, ".json", dry_run=False)
        print("\n⚙️ Merging Markdown prompt files...")
        merge_or_rename_duplicates(prompt_dir, ".md", dry_run=False)
    else:
        print("🛑 Merge skipped. Run again with 'y' to apply changes.")
