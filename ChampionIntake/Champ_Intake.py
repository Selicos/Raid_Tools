def generate_and_save_champion_json_from_prompt(champion_name):

    """
    Champion Intake Workflow Instructions (Updated Oct 2025)

    1. The intake script reads the list of owned champions from input/Owned_Champions/Owned_champion_list.md.
    2. For each champion, it generates a prompt file in input/Prompt/ that walks through the canonical JSON template (ChampionIntake/templates/Prompt_Template.json) section by section.
        - Each prompt file uses canonical field names and structure, and is formatted for easy LLM or human completion.
        - The prompt file does NOT contain a completed markdown summary; it is only for data intake.
    3. After the prompt is filled out (by LLM or human), the resulting JSON is saved to output/Champions/.
    4. The summary script (not the intake script) reads the JSON and generates the completed prompt markdown file in output/completed_prompts/.

    This ensures all champion data is collected in a modular, canonical JSON format, and all human-readable summaries are generated from validated JSON only.
    """
    prompt_path = os.path.join(prompt_dir, f"{champion_name}_prompt.md")
    if not os.path.exists(prompt_path):
        print(f"❌ Prompt file not found: {prompt_path}")
        return False

    with open(prompt_path, "r", encoding="utf-8") as f:
        prompt_text = f.read()

    # Prevent overwriting existing champion JSON
    json_path = os.path.join(champion_json_dir, f"{champion_name}.json")
    if os.path.exists(json_path):
        print(f"⚠️ Champion JSON already exists for {champion_name}. Skipping overwrite.")
        return False

    # Parse the prompt file for module sections and build a nested/module-based JSON structure
    import re
    rarity = None
    # Try to extract rarity from prompt or ask for it
    rarity_match = re.search(r'"rarity"\s*:\s*"(\w+)"', prompt_text, re.IGNORECASE)
    if rarity_match:
        rarity = rarity_match.group(1).capitalize()
    if not rarity:
        rarity = input(f"Enter rarity for {champion_name} (Rare/Epic/Legendary/Mythic or 3/4/5/6): ").strip().capitalize()

    # Find all module sections in the prompt (## Module N)
    module_pattern = re.compile(r'^## Module (\d+)[^\n]*\n(.*?)(?=^## Module |\Z)', re.MULTILINE | re.DOTALL)
    modules = {str(i): {} for i in range(21)}
    for match in module_pattern.finditer(prompt_text):
        module_num = match.group(1)
        module_content = match.group(2).strip()
        # Try to extract the JSON object for this module
        json_match = re.search(r'```json\s*(\{[\s\S]*?\})\s*```', module_content)
        if json_match:
            try:
                module_json = json.loads(json_match.group(1))
                modules[module_num] = module_json
            except Exception as e:
                print(f"⚠️ Failed to parse JSON for module {module_num}: {e}")
                modules[module_num] = {"error": "Invalid JSON"}
        else:
            modules[module_num] = {"notes": module_content}

    # Build the champion JSON as a dictionary of modules
    champion_json = {
        "champion": champion_name,
        "rarity": rarity,
        "owned": True,
        "modules": modules
    }

    # Optionally, expand skill/attack order to 16 turns if possible (inside the relevant module)
    skills_mod = modules.get("1", {})  # Example: skills module is module 1
    rotation = skills_mod.get("rotation", {})
    optimal_cycle = rotation.get("optimal_cycle", [])
    if optimal_cycle and isinstance(optimal_cycle, list):
        expanded = []
        idx = 0
        while len(expanded) < 16:
            expanded.append(optimal_cycle[idx % len(optimal_cycle)])
            idx += 1
            if len(expanded) >= 2 * len(optimal_cycle):
                if expanded[-len(optimal_cycle):] == expanded[-2*len(optimal_cycle):-len(optimal_cycle)]:
                    break
        rotation["turn_sequence"] = expanded[:16]
        skills_mod["rotation"] = rotation
        modules["1"] = skills_mod

    # Save the generated JSON
    save_champion_json(champion_name, champion_json)
    add_to_owned_list(champion_name, update_date=True)
    print(f"✅ Champion JSON generated and saved for {champion_name}")
    return True
# Ensure environment is ready

import importlib.util
import runpy
import os
import subprocess
import json
import sys

setup_path = os.path.join(os.path.dirname(__file__), "setup_environment.py")
if not os.path.exists(setup_path):
    print("⚠️ Missing setup script. Please check your environment.")
else:
    runpy.run_path(setup_path)

import subprocess
import shutil
from datetime import datetime, timedelta

# Base directory for this script
BASE_DIR = os.path.dirname(__file__)
champion_json_dir = os.path.join(BASE_DIR, "..", "output", "Champions")
owned_list_path = os.path.join(BASE_DIR, "..", "input", "Owned_Champions", "Owned_champion_list.md")
prompt_dir = os.path.join(BASE_DIR, "..", "input", "Prompt")
os.makedirs(prompt_dir, exist_ok=True)

def add_to_owned_list(champion_name, update_date=True):
    today = datetime.today().strftime("%Y-%m-%d")
    os.makedirs(os.path.dirname(owned_list_path), exist_ok=True)
    if not os.path.exists(owned_list_path):
        with open(owned_list_path, "w", encoding="utf-8") as f:
            f.write("# Owned_Champions\n\n")

    with open(owned_list_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    champ_lower = champion_name.lower()
    updated = False

    # Try to get rarity from champion JSON if available
    rarity = None
    json_path = os.path.join(champion_json_dir, f"{champion_name}.json")
    if os.path.exists(json_path):
        try:
            with open(json_path, "r", encoding="utf-8") as jf:
                champ_json = json.load(jf)
                rarity = champ_json.get("rarity")
        except Exception:
            pass

    for i, line in enumerate(lines):
        if line.startswith("- "):
            line_name = line[2:].split("|")[0].strip().lower()
            if line_name == champ_lower:
                if update_date:
                    if rarity:
                        lines[i] = f"- {champion_name} | Rarity: {rarity} | Last Updated: {today}\n"
                    else:
                        lines[i] = f"- {champion_name} | Last Updated: {today}\n"
                    updated = True
                break
    else:
        if rarity:
            lines.append(f"- {champion_name} | Rarity: {rarity} | Last Updated: {today}\n")
        else:
            lines.append(f"- {champion_name} | Last Updated: {today}\n")
        updated = True

    if updated:
        with open(owned_list_path, "w", encoding="utf-8") as f:
            f.writelines(lines)
        print(f"✅ Updated owned list for {champion_name}")
    else:
        print(f"✅ {champion_name} already up to date")

def create_json_placeholder(champion_name, rarity=None):
    os.makedirs(champion_json_dir, exist_ok=True)
    path = os.path.join(champion_json_dir, f"{champion_name}.json")
    if os.path.exists(path):
        print(f"⚠️ JSON for {champion_name} already exists. Skipping placeholder creation.")
        return
    rarity_map = {
        "6": "Mythic", "mythic": "Mythic", "m": "Mythic",
        "5": "Legendary", "legendary": "Legendary", "l": "Legendary",
        "4": "Epic", "epic": "Epic", "e": "Epic",
        "3": "Rare", "rare": "Rare", "r": "Rare"
    }
    if rarity is None:
        rarity = "Unknown"
    else:
        rarity = rarity_map.get(rarity.lower(), rarity.capitalize())
    with open(path, "w", encoding="utf-8") as f:
        f.write("{\n"
                f'  "champion": "{champion_name}",\n'
                f'  "rarity": "{rarity}",\n'
                '  "owned": true\n'
                "}")
    print(f"📁 Placeholder JSON for {champion_name} created/updated with owned=true and rarity={rarity}")

def create_prompt_md(champion_name):
    os.makedirs(prompt_dir, exist_ok=True)
    target_filename = f"{champion_name}_prompt.md"
    path = os.path.join(prompt_dir, target_filename)

    json_template_path = os.path.join(os.path.dirname(__file__), "templates", "Prompt_Template.json")
    if not os.path.exists(json_template_path):
        print(f"❌ JSON template not found: {json_template_path}")
        return None
    with open(json_template_path, "r", encoding="utf-8") as f:
        json_template = json.load(f)

    prompt = f"# Champion Data Intake Prompt for {champion_name}\n\n"
    prompt += (
        f"Please provide the following information for {champion_name}.\n"
        "Fill in each section below. Use the field names and structure exactly as shown.\n"
        "Respond in JSON format, matching the template.\n\n"
    )

    def section(title, json_obj):
        import json as pyjson
        pretty = pyjson.dumps(json_obj, indent=2, ensure_ascii=False)
        return f"## {title}\n\n```json\n{pretty}\n```\n"

    for key, value in json_template.items():
        if key in ["champion", "owned"]:
            continue  # These are top-level fields, not sections
        pretty_title = key.replace("_", " ").title()
        prompt += section(pretty_title, value)

    with open(path, "w", encoding="utf-8") as f:
        f.write(prompt)
    print(f"✅ Prompt file created: {path}")
    return path

def validate_json(champion_name):
    path = os.path.join(champion_json_dir, f"{champion_name}.json")
    if not os.path.exists(path):
        print(f"❌ JSON file missing: {path}")
        return False
    try:
        with open(path, "r", encoding="utf-8") as f:
            json.load(f)
        print(f"✅ Valid JSON: {path}")
        return True
    except Exception as e:
        print(f"❌ Invalid JSON: {e}")
        return False

def validate_md(champion_name):
    path = os.path.join(prompt_dir, f"{champion_name}_prompt.md")
    if not os.path.exists(path):
        print(f"❌ Markdown file missing: {path}")
        return False
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
        if "# Champion Log Generation Prompt" in content:
            print(f"✅ Valid Markdown: {path}")
            return True
        else:
            print(f"❌ Markdown header missing")
            return False


def print_copilot_hint():
    print("💬 Copilot Chat: Paste the prompt and ask for full champion log generation.")
    print("💡 Tip: In VS Code, open Copilot Chat (Ctrl+I or click the Copilot icon).")

def open_in_editor(path):
    code_path = shutil.which("code")

    if code_path:
        try:
            subprocess.run([code_path, path], check=True)
            print(f"🚀 Opened in VS Code: {path}")
            print_copilot_hint()
            return
        except Exception as e:
            print(f"⚠️ VS Code CLI failed: {e}")

    full_vscode_path = r"C:\Users\%USERNAME%\AppData\Local\Programs\Microsoft VS Code\Code.exe"
    full_vscode_path = os.path.expandvars(full_vscode_path)

    if os.path.exists(full_vscode_path):
        try:
            subprocess.run([full_vscode_path, path], check=True)
            print(f"🚀 Opened in VS Code via full path: {path}")
            print_copilot_hint()
            return
        except Exception as e:
            print(f"⚠️ VS Code full path failed: {e}")

    print("⚠️ VS Code not available. Falling back to Notepad...")
    try:
        subprocess.run(["notepad.exe", path], check=True)
        print(f"📝 Opened in Notepad: {path}")
        print("💬 Copilot Chat: Copy the prompt from Notepad and paste it into Copilot Chat manually.")
    except Exception as e:
        print(f"❌ Could not open in Notepad: {e}")

def run_champion_intake(champion_name, rarity=None, fast_mode=False, suppress_prompt_actions=False):
    # Only create placeholder if JSON does not exist
    completed_prompt_dir = os.path.join("output", "completed_prompts")
    completed_prompt_path = os.path.join(completed_prompt_dir, f"{champion_name}_prompt.completed.md")
    if os.path.exists(completed_prompt_path):
        print(f"✅ Completed prompt already exists for {champion_name}. Skipping prompt and JSON generation.")
        return True

    # Do not create a sample/placeholder JSON here; let the Copilot workflow handle JSON creation
    json_path = os.path.join(champion_json_dir, f"{champion_name}.json")
    if os.path.exists(json_path):
        print(f"⚠️ JSON for {champion_name} already exists. Skipping placeholder creation.")
    md_path = create_prompt_md(champion_name)
    if validate_json(champion_name) and validate_md(champion_name):
        # Only open the prompt file for single champion mode (not batch)
        if not suppress_prompt_actions and not fast_mode:
            open_in_editor(md_path)
        add_to_owned_list(champion_name, update_date=True)
        return True
    else:
        print(f"⚠️ Validation failed for {champion_name}. Prompt not opened.")
        return False

def run_smart_batch_from_owned_list(path=owned_list_path, fast_mode=False):
    if not os.path.exists(path):
        print(f"❌ Owned list not found: {path}")
        return

    with open(path, "r", encoding="utf-8") as f:
        lines = [line.strip() for line in f if line.strip().startswith("- ")]

    champions_to_update = []
    for line in lines:
        parts = [p.strip() for p in line[2:].split("|")]
        name = parts[0]
        rarity = None
        for p in parts[1:]:
            if p.lower().startswith("rarity:"):
                rarity = p.split(":",1)[1].strip().capitalize()
        champions_to_update.append((name, rarity))

    print(f"📦 Generating prompt files for {len(champions_to_update)} champions from owned list...\n")
    success, failed = [], []

    for champ, rarity in champions_to_update:
        print(f"🔄 Generating prompt for: {champ} (Rarity: {rarity if rarity else 'Unknown'})")
        json_path = os.path.join(champion_json_dir, f"{champ}.json")
        if os.path.exists(json_path):
            print(f"⚠️ JSON for {champ} already exists. Skipping prompt generation.")
            continue
        try:
            create_prompt_md(champ)
            # Optionally validate JSON if generated (if you want to add this step, call validate_json here)
            add_to_owned_list(champ, update_date=True)
            success.append(champ)
        except Exception as e:
            print(f"❌ Failed to generate prompt for {champ}: {e}")
            failed.append(champ)
        print("-" * 40)

    print("\n📊 Batch Prompt Generation Summary")
    print(f"✅ Prompts generated: {len(success)} champions")
    print(f"❌ Failed: {len(failed)} champions")
    if failed:
        print("⚠️ Failed champions:")
        for f in failed:
            print(f" - {f}")

def generate_prompt_for_champion(champion_name):
    modules_dir = os.path.join(os.path.dirname(__file__), "modules")
    prompt = f"# Champion Log Generation Prompt for {champion_name}\n\n"
    for i in range(0, 14):
        module_file = os.path.join(modules_dir, f"Champion_Review_Module_{i}.md")
        if os.path.exists(module_file):
            with open(module_file, "r", encoding="utf-8") as f:
                prompt += f"---\n## Module {i}\n" + f.read() + "\n\n"
        else:
            prompt += f"---\n## Module {i}\n(Missing module file)\n\n"
    return prompt

def save_champion_json(champion_name, champion_data):
    champions_dir = os.path.join(os.path.dirname(__file__), "Champions")
    os.makedirs(champions_dir, exist_ok=True)
    json_path = os.path.join(champions_dir, f"{champion_name}.json")
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(champion_data, f, indent=2)
    print(f"Champion JSON saved to {json_path}")

# Example usage after generating champion_data:
# save_champion_json("Artak", champion_data)

if __name__ == "__main__":
    # Usage: python Champ_Intake.py [champion_name] [rarity]
    champion_name = None
    rarity = None
    if len(sys.argv) > 1:
        champion_name = sys.argv[1].strip()
    if len(sys.argv) > 2:
        rarity = sys.argv[2].strip().lower()

    # Always prompt for a new champion first if not provided
    if not champion_name:
        print("🔍 Champion Intake")
        print("Enter a champion name to process individually.")
        print("Leave blank to use the owned champion list.")
        champion_name = input("Champion name: ").strip()
        if champion_name:
            rarity = input("Rarity (Rare/Epic/Legendary/Mythic or 3/4/5/6): ").strip().lower()

    if champion_name:
        run_champion_intake(champion_name, rarity=rarity, fast_mode=False)
        prompt = generate_prompt_for_champion(champion_name)
        prompt_path = os.path.join(prompt_dir, f"{champion_name}_prompt.md")
        with open(prompt_path, "w", encoding="utf-8") as f:
            f.write(prompt)
        print(f"✅ Prompt for {champion_name} written to {prompt_path}")
        # --- Automated champion JSON generation from prompt ---
        generate_and_save_champion_json_from_prompt(champion_name)
    else:
        confirm = input("⚠️ No champion entered. Run owned list instead? (y/n): ").strip().lower()
        if confirm == "y":
            run_smart_batch_from_owned_list(fast_mode=False)
        else:
            print("❌ Cancelled. No champion processed.")
