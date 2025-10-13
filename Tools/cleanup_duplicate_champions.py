"""
cleanup_duplicate_champions.py

Overview:
---------
This utility scans the Champions and prompt directories for case-insensitive duplicate files
(e.g., 'Artak.json' and 'artak.json'), reports them, and can optionally merge or remove duplicates.
For merging, the content of duplicates is appended to the first file found, and the duplicate is deleted.

Usage:
------
- Run the script directly.
- It will report duplicates and prompt you to confirm before merging.
- Merging appends duplicate content to the first file and deletes the duplicate.

Directories:
-------------
# Champions JSON: ChampionIntake\\Champions
# Prompt Markdown: ChampionIntake\\Prompt

Notes:
------
- Always review merged files for correctness.
- The script is interactive and safe by default (requires confirmation).
"""

import os
from collections import defaultdict

champion_dir = r"ChampionIntake"
champion_json_dir = os.path.join(champion_dir, "Champions")
prompt_dir = os.path.join(champion_dir, "Prompt")


def find_case_duplicates(directory, extension):
    """
    Find files in the given directory with the same name differing only by case.
    Returns a dict mapping the normalized (lowercase) filename to a list of variants.
    """
    files = [f for f in os.listdir(directory) if f.lower().endswith(extension)]
    normalized = defaultdict(list)
    for f in files:
        base = f.lower()
        normalized[base].append(f)
    return {k: v for k, v in normalized.items() if len(v) > 1}


def report_duplicates():
    """
    Scan for and print case-insensitive duplicates in the Champions and prompt directories.
    """
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
    """
    For each set of duplicates, append the content of all but the first file to the first file,
    then delete the duplicates. If dry_run is True, only print actions without making changes.
    """
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
                    # os.remove(src)  # File deletion disabled for safety
                    print(f"⚠️ File deletion disabled: {dup} would have been removed after merging into {keep}")
                    print(f"✅ Merged {dup} → {keep}")
                except Exception as e:
                    print(f"❌ Failed to merge {dup}: {e}")


if __name__ == "__main__":
    # Check that directories exist before proceeding
    if not os.path.isdir(champion_json_dir):
        print(f"❌ Champions directory not found: {champion_json_dir}")
        exit(1)
    if not os.path.isdir(prompt_dir):
        print(f"❌ Prompt directory not found: {prompt_dir}")
        exit(1)

    report_duplicates()
    confirm = input("\nProceed to merge duplicates? (y/n): ").strip().lower()
    if confirm == "y":
        print("\n⚙️ Merging JSON files...")
        merge_or_rename_duplicates(champion_json_dir, ".json", dry_run=False)
        print("\n⚙️ Merging Markdown prompt files...")
        merge_or_rename_duplicates(prompt_dir, ".md", dry_run=False)
    else:
        print("🛑 Merge skipped. Run again with 'y' to apply changes.")
