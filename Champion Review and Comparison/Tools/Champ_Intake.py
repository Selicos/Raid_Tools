import os
import json
import pyperclip
import subprocess
import shutil
from datetime import datetime

# Paths
champion_dir = r"Champion Review and Comparison"
champion_json_dir = os.path.join(champion_dir, "Champions")
owned_list_path = os.path.join(champion_json_dir, "Owned Champions", "Owned_Champion_list.md")
prompt_dir = os.path.join(champion_dir, "prompt")

def add_to_owned_list(champion_name):
    today = datetime.today().strftime("%Y-%m-%d")
    os.makedirs(os.path.dirname(owned_list_path), exist_ok=True)
    if not os.path.exists(owned_list_path):
        with open(owned_list_path, "w", encoding="utf-8") as f:
            f.write("# Owned Champions\n\n")
    with open(owned_list_path, "r+", encoding="utf-8") as f:
        lines = f.readlines()
        if any(champion_name in line for line in lines):
            print(f"✅ {champion_name} already in owned list.")
            return
        f.write(f"- {champion_name} | Last Updated: {today}\n")
        print(f"✅ Added {champion_name} to owned list.")

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
    path = os.path.join(prompt_dir, f"{champion_name}.md")
    if os.path.exists(path):
        print(f"📄 Prompt already exists: {path}")
        return path
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
    add_to_owned_list(champion_name)
    create_json_placeholder(champion_name)
    md_path = create_prompt_md(champion_name)
    if validate_json(champion_name) and validate_md(champion_name):
        copy_prompt_to_clipboard(md_path)
        open_in_editor(md_path)
    else:
        print(f"⚠️ Validation failed for {champion_name}. Prompt not copied or opened.")

def run_batch_from_file(file_path="champion_batch_list.txt"):
    if not os.path.exists(file_path):
        print(f"❌ Batch file not found: {file_path}")
        return
    with open(file_path, "r", encoding="utf-8") as f:
        champions = [line.strip() for line in f if line.strip()]
    print(f"📦 Running batch intake for {len(champions)} champions...\n")
    for champ in champions:
        print(f"🔄 Processing: {champ}")
        run_champion_intake(champ)
        print("-" * 40)

if __name__ == "__main__":
    mode = input("Run in batch mode from file? (y/n): ").strip().lower()
    if mode == "y":
        run_batch_from_file()
    else:
        name = input("Enter champion name: ").strip()
        run_champion_intake(name)
