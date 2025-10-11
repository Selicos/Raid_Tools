# Ensure environment is ready
import importlib.util
import runpy
import os

setup_path = os.path.join(os.path.dirname(__file__), "setup_environment.py")
if importlib.util.find_spec("pyperclip") is None or not os.path.exists(setup_path):
    print("⚠️ Missing setup script or pyperclip. Please check your environment.")
else:
    runpy.run_path(setup_path)

import json
import pyperclip
import subprocess
import shutil
from datetime import datetime, timedelta

# Paths
champion_dir = r"Champion Review and Comparison"
champion_json_dir = os.path.join(champion_dir, "Champions")
owned_list_path = os.path.join(champion_json_dir, "Owned Champions", "Owned_Champion_list.md")
prompt_dir = os.path.join(champion_dir, "prompt")

def add_to_owned_list(champion_name, update_date=True):
    today = datetime.today().strftime("%Y-%m-%d")
    os.makedirs(os.path.dirname(owned_list_path), exist_ok=True)
    if not os.path.exists(owned_list_path):
        with open(owned_list_path, "w", encoding="utf-8") as f:
            f.write("# Owned Champions\n\n")

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
    if not os.path.exists(path):
        with open(path, "w", encoding="utf-8") as f:
            f.write("{\n  \"champion\": \"" + champion_name + "\",\n  \"owned\": true\n}")
        print(f"📁 Created placeholder JSON for {champion_name}")
    else:
        print(f"📁 JSON already exists for {champion_name}")

def create_prompt_md(champion_name):
    os.makedirs(prompt_dir, exist_ok=True)
    target_filename = f"{champion_name}.md"
    target_lower = target_filename.lower()

    for fname in os.listdir(prompt_dir):
        if fname.lower() == target_lower:
            print(f"📄 Prompt already exists: {os.path.join(prompt_dir, fname)}")
            return os.path.join(prompt_dir, fname)

    path = os.path.join(prompt_dir, target_filename)
    content = f"""# Champion Log Generation Prompt

Let's run through the modules for {champion_name}, and generate a log json file for review.

Please output the full champion log in JSON format, including:
- Modules 1–13
- Overview, skills, synergy, mastery simulation, ratings, and final summary
- Format for easy copy-paste into champions/{champion_name}.json
"""
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
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

def run_champion_intake(champion_name):
    create_json_placeholder(champion_name)
    md_path = create_prompt_md(champion_name)
    if validate_json(champion_name) and validate_md(champion_name):
        copy_prompt_to_clipboard(md_path)
        open_in_editor(md_path)
        add_to_owned_list(champion_name, update_date=True)
        return True
    else:
        print(f"⚠️ Validation failed for {champion_name}. Prompt not copied or opened.")
        return False

def run_smart_batch_from_owned_list(path=owned_list_path):
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
        if run_champion_intake(champ):
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

# Entry point
if __name__ == "__main__":
    mode = input("Use smart batch mode from owned list? (y/n): ").strip().lower()
    if mode == "y":
        run_smart_batch_from_owned_list()
    else:
        name = input("Enter champion name: ").strip()
        run_champion_intake(name)
