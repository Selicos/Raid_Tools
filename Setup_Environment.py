# setup_environment.py
import subprocess
import sys
import shutil
import os

required_packages = ["pyperclip", "pytest"]
optional_tools = {"VS Code CLI": "code"}

def create_and_activate_venv(venv_dir=".venv"):
    if not os.path.isdir(venv_dir):
        print(f"🔧 Creating virtual environment in {venv_dir} ...")
        subprocess.check_call([sys.executable, "-m", "venv", venv_dir])
    else:
        print(f"✅ Virtual environment already exists in {venv_dir}")

    # Determine the python executable in the venv
    if os.name == "nt":
        python_exe = os.path.join(venv_dir, "Scripts", "python.exe")
    else:
        python_exe = os.path.join(venv_dir, "bin", "python")
    return python_exe

def check_and_install_packages(python_exe, packages):
    for pkg in packages:
        try:
            subprocess.check_call([python_exe, "-c", f"import {pkg}"])
        except subprocess.CalledProcessError:
            print(f"📦 Installing {pkg} ...")
            subprocess.check_call([python_exe, "-m", "pip", "install", pkg])

def check_optional_tools(tools):
    for name, cmd in tools.items():
        if not shutil.which(cmd):
            print(f"⚠️ {name} not found. You may need to add it to your PATH.")

def install_requirements_file(python_exe, requirements_path="requirements.txt"):
    if os.path.isfile(requirements_path):
        print(f"📦 Installing packages from {requirements_path} ...")
        subprocess.check_call([python_exe, "-m", "pip", "install", "-r", requirements_path])
    else:
        print(f"⚠️  {requirements_path} not found. Skipping requirements file installation.")

def run_setup():
    print("🔧 Running environment setup...")

    venv_dir = ".venv"
    python_exe = create_and_activate_venv(venv_dir)

    print(f"🔎 Using Python interpreter: {python_exe}")

    # Install from requirements.txt if present
    install_requirements_file(python_exe)

    # Ensure required packages are present (fallback)
    check_and_install_packages(python_exe, required_packages)
    check_optional_tools(optional_tools)

    print("\n✅ Environment ready.")
    print(f"➡️  To activate your virtual environment, run:")
    if os.name == "nt":
        print(f"   .\\{venv_dir}\\Scripts\\Activate")
    else:
        print(f"   source {venv_dir}/bin/activate")
    print("➡️  To run tools and tests, use:")
    print(f"   python -m pytest")
    print(f"   python ChampionAnalysisTool/championAnalysis.py")
    print(f"   python Summarize\\ Champion\\ Results/jsonToMdPerChamp.py")
    print(f"   python Champion Review and Comparison/Tools/champIntake.py")

if __name__ == "__main__":
    run_setup()
