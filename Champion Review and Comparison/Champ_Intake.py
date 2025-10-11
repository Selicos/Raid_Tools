# Ensure environment is ready
import importlib.util
import runpy
import os
import subprocess
import json

setup_path = os.path.join(os.path.dirname(__file__), "setup_environment.py")
if importlib.util.find_spec("pyperclip") is None or not os.path.exists(setup_path):
    print("⚠️ Missing setup script or pyperclip. Please check your environment.")
else:
    runpy.run_path(setup_path)

import pyperclip
import subprocess
import shutil
from datetime import datetime, timedelta

# Base directory for this script
BASE_DIR = os.path.dirname(__file__)
champion_json_dir = os.path.join(BASE_DIR, "Champions")
owned_list_path = os.path.join(champion_json_dir, "Owned_Champions", "Owned_Champion_list.md")
prompt_dir = os.path.join(os.path.dirname(__file__), "Prompt")
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

    for i, line in enumerate(lines):
        if line.startswith("- "):
            line_name = line[2:].split("|")[0].strip().lower()
            if line_name == champ_lower:
                if update_date:
                    lines[i] = f"- {champion_name} | Last Updated: {today}\n"
                    updated = True
                break
    else:
        lines.append(f"- {champion_name} | Last Updated: {today}\n")
        updated = True

    if updated:
        with open(owned_list_path, "w", encoding="utf-8") as f:
            f.writelines(lines)
        print(f"✅ Updated owned list for {champion_name}")
    else:
        print(f"✅ {champion_name} already up to date")

def create_json_placeholder(champion_name):
    os.makedirs(champion_json_dir, exist_ok=True)
    path = os.path.join(champion_json_dir, f"{champion_name}.json")
    # Always set owned to true by default
    with open(path, "w", encoding="utf-8") as f:
        f.write("{\n  \"champion\": \"" + champion_name + "\",\n  \"owned\": true\n}")
    print(f"📁 Placeholder JSON for {champion_name} created/updated with owned=true")

def create_prompt_md(champion_name):
    os.makedirs(prompt_dir, exist_ok=True)
    target_filename = f"{champion_name}.md"
    path = os.path.join(prompt_dir, target_filename)

    prompt = f"# Champion Log Generation Prompt for {champion_name}\n\n"
    prompt += (
        "You are to generate a complete champion log for {0} in JSON format, using the following module templates as structure and guidance. "
        "Each module (0–13) is included below. For each, fill in the relevant information for {0}. Output a single JSON object with each module as a key (e.g., \"overview\", \"skills\", \"synergy\", etc.).\n\n"
        "---\n"
        "## Example output structure:\n"
        "```json\n"
        "{{\n"
        "  \"champion\": \"{0}\",\n"
        "  \"owned\": true,\n"
        "  \"overview\": {{ ... }},\n"
        "  \"skills\": {{ ... }},\n"
        "  \"team_inputs\": {{ ... }},\n"
        "  \"mastery_simulation\": {{ ... }},\n"
        "  \"clan_boss\": {{ ... }},\n"
        "  \"synergy\": {{ ... }},\n"
        "  \"investment\": {{ ... }},\n"
        "  \"intelligence\": {{ ... }},\n"
        "  \"turn_meter\": {{ ... }},\n"
        "  \"utility_comparison\": {{ ... }},\n"
        "  \"ratings\": {{ ... }},\n"
        "  \"final_summary\": {{ ... }},\n"
        "  \"synergy_engine\": {{ ... }}\n"
        "}}\n"
        "```\n"
        "---\n"
        "Instructions:\n"
        "- Fill in each section for {0} using the module templates below.\n"
        "- Output only the final JSON object.\n\n"
    ).format(champion_name)

    modules_dir = os.path.join(os.path.dirname(__file__), "modules")
    for i in range(0, 14):
        module_file = os.path.join(modules_dir, f"Champion_Review_Module_{i}.md")
        prompt += f"---\n## Module {i}\n"
        if os.path.exists(module_file):
            with open(module_file, "r", encoding="utf-8") as f:
                prompt += f.read() + "\n\n"
        else:
            prompt += "(Missing module file)\n\n"

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
    path = os.path.join(prompt_dir, f"{champion_name}.md")
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

def copy_prompt_to_clipboard(path):
    with open(path, "r", encoding="utf-8") as f:
        pyperclip.copy(f.read())
    print("📋 Prompt copied to clipboard.")

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

def run_champion_intake(champion_name, fast_mode=False):
    create_json_placeholder(champion_name)
    md_path = create_prompt_md(champion_name)
    if validate_json(champion_name) and validate_md(champion_name):
        copy_prompt_to_clipboard(md_path)
        if not fast_mode:
            open_in_editor(md_path)
        add_to_owned_list(champion_name, update_date=True)
        return True
    else:
        print(f"⚠️ Validation failed for {champion_name}. Prompt not copied or opened.")
        return False

def run_smart_batch_from_owned_list(path=owned_list_path, fast_mode=False):
    if not os.path.exists(path):
        print(f"❌ Owned list not found: {path}")
        return

    with open(path, "r", encoding="utf-8") as f:
        lines = [line.strip() for line in f if line.strip().startswith("- ")]

    threshold = datetime.today() - timedelta(days=30)
    champions_to_update = []

    for line in lines:
        parts = line[2:].split("|")
        name = parts[0].strip()
        date_str = None

        if len(parts) > 1 and "Last Updated:" in parts[1]:
            try:
                date_str = parts[1].split("Last Updated:")[1].strip()
                last_updated = datetime.strptime(date_str, "%Y-%m-%d")
                if last_updated < threshold:
                    champions_to_update.append(name)
            except Exception as e:
                print(f"⚠️ Could not parse date for {name}: {e}")
                champions_to_update.append(name)
        else:
            champions_to_update.append(name)

    print(f"📦 Updating {len(champions_to_update)} champions...\n")
    success, failed = [], []

    for champ in champions_to_update:
        print(f"🔄 Processing: {champ}")
        if run_champion_intake(champ, fast_mode=fast_mode):
            success.append(champ)
        else:
            failed.append(champ)
        print("-" * 40)

    print("\n📊 Batch Summary")
    print(f"✅ Updated: {len(success)} champions")
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

if __name__ == "__main__":
    print("🔍 Champion Intake")
    print("Enter a champion name to process individually.")
    print("Leave blank to use the owned champion list.")

    user_input = input("Champion name: ").strip()

    if user_input == "":
        confirm = input("⚠️ No champion entered. Run owned list instead? (y/n): ").strip().lower()
        if confirm == "y":
            run_smart_batch_from_owned_list(fast_mode=False)
        else:
            print("❌ Cancelled. No champion processed.")
    else:
        run_champion_intake(user_input, fast_mode=False)
        prompt = generate_prompt_for_champion(user_input)
        prompt_path = os.path.join(prompt_dir, f"{user_input}_prompt.md")
        with open(prompt_path, "w", encoding="utf-8") as f:
            f.write(prompt)
        print(f"✅ Prompt for {user_input} written to {prompt_path}")
