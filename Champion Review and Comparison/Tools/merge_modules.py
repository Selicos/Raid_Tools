import os

# Configuration
module_dir = os.path.join("Champion Review and Comparison", "modules")
module_prefix = "Champion_Review_Module_"
module_suffix = ".md"
module_range = range(0, 14)  # Modules 0–13
output_file = os.path.join(module_dir, "ALL_MODULES.md")

def merge_modules():
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
