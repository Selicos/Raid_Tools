import os

# -----------------------------------------------------------------------------
# Champion Review Module Merger
#
# This script merges all individual Champion Review module markdown files
# (Champion_Review_Module_0.md through Champion_Review_Module_13.md)
# into a single ALL_MODULES.md file for reference or prompt generation.
#
# Usage:
#   python merge_modules.py
#
# Output:
#   - Overwrites Champion Review and Comparison\modules\other_versions\ALL_MODULES.md
#   - Lists missing modules in the terminal output
# -----------------------------------------------------------------------------

# Configuration: directories and filenames
module_dir = os.path.join("Champion Review and Comparison", "modules")
module_prefix = "Champion_Review_Module_"
module_suffix = ".md"
module_range = range(0, 14)  # Modules 0–13

# Output path: modules\other_versions\ALL_MODULES.md
output_dir = os.path.join(module_dir, "other_versions")
os.makedirs(output_dir, exist_ok=True)
output_file = os.path.join(output_dir, "ALL_MODULES.md")

def merge_modules():
    """
    Merge all module markdown files into ALL_MODULES.md in other_versions.
    Each module is separated by a header and divider.
    Missing modules are reported in the terminal.
    """
    merged_content = []
    skipped = []

    print(f"🔍 Scanning: {module_dir}\n")

    for i in module_range:
        filename = f"{module_prefix}{i}{module_suffix}"
        filepath = os.path.join(module_dir, filename)
        if os.path.isfile(filepath):
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read().strip()
                merged_content.append(f"\n\n---\n\n## Module {i}\n\n{content}")
        else:
            skipped.append(filename)

    # Write merged content to the output file (overwrite mode)
    with open(output_file, "w", encoding="utf-8") as f:
        f.write("# Champion Review — All Modules\n")
        f.write("\n".join(merged_content))
        f.write("\n")

    print(f"✅ Merged {len(merged_content)} modules into {output_file}")
    if skipped:
        print("⚠️ Skipped missing files:")
        for s in skipped:
            print(f" - {s}")

if __name__ == "__main__":
    merge_modules()
