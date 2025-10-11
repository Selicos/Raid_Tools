# setup_environment.py
import subprocess
import sys
import shutil

required_packages = ["pyperclip"]
optional_tools = {"VS Code CLI": "code"}

def check_and_install_packages(packages):
    for pkg in packages:
        try:
            __import__(pkg)
        except ImportError:
            subprocess.check_call([sys.executable, "-m", "pip", "install", pkg])

def check_optional_tools(tools):
    for name, cmd in tools.items():
        if not shutil.which(cmd):
            print(f"⚠️ {name} not found. You may need to add it to your PATH.")

def run_setup():
    print("🔧 Running environment setup...")
    check_and_install_packages(required_packages)
    check_optional_tools(optional_tools)
    print("✅ Environment ready.\n")

if __name__ == "__main__":
    run_setup()
