import os
from datetime import datetime

champion_dir = r"Champion Review and Comparison\Champions"
owned_list_path = os.path.join(champion_dir, "Owned Champions", "Owned_Champion_list.md")

def add_to_owned_list(champion_name):
    today = datetime.today().strftime("%Y-%m-%d")
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
    path = os.path.join(champion_dir, f"{champion_name}.json")
    if not os.path.exists(path):
        with open(path, "w", encoding="utf-8") as f:
            f.write("{\n  \"champion\": \"" + champion_name + "\",\n  \"owned\": true\n}")
        print(f"📁 Created placeholder JSON for {champion_name}")
    else:
        print(f"📁 JSON already exists for {champion_name}")

def generate_prompt(champion_name):
    prompt = f"Let's run through the modules for {champion_name}, and generate a log json file for review."
    print("\n📋 Copilot Prompt:\n" + prompt)

if __name__ == "__main__":
    name = input("Enter champion name: ").strip()
    add_to_owned_list(name)
    create_json_placeholder(name)
    generate_prompt(name)
