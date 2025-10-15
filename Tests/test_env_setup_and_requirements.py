import os
import sys
import subprocess
import importlib
import json
import glob
import shlex
import pytest

try:
    from importlib import metadata as importlib_metadata  # Python 3.8+
except ImportError:
    import importlib_metadata  # type: ignore


# Only required packages for this repo
REQUIRED_PACKAGES = [
    "pytest",
    "black",
    "iniconfig",
    "packaging",
    "pluggy",
    "pygments",
    "colorama",
]

# All required folders/files for the current workflow
PROJECT_COMPONENTS = [
    ("input/Prompt", True),
    ("output/Champions", True),
    ("output/completed_prompts", True),
    ("ChampionIntake/templates/Prompt_Template.md", False),
    (".github/copilot-instructions.md", False),
    ("ChampionIntake/Champ_Intake.py", False),
    ("ChampionSummary/generateChampionSummaries.py", False),
    ("Tools/validate_json.py", False),
    ("Tools/Setup_Environment.py", False),
    (".vscode/settings.json", False),
    (".vscode/tasks.json", False),
    (".vscode/extensions.json", False),
    ("Makefile", False),
    ("README.md", False),
]


@pytest.mark.parametrize("package", REQUIRED_PACKAGES)
def test_required_python_packages_installed(package):
    try:
        importlib.import_module(package)
    except ImportError:
        pytest.fail(f"Required package not installed: {package}")


@pytest.mark.parametrize("path,is_dir", PROJECT_COMPONENTS)
def test_project_component_exists(path, is_dir):
    # Always resolve from the project root (Raid_Tools)
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    abs_path = os.path.join(project_root, path)
    if is_dir:
        if not os.path.isdir(abs_path):
            # Create the directory if missing (setup requirement)
            os.makedirs(abs_path, exist_ok=True)
        assert os.path.isdir(
            abs_path
        ), f"Missing required directory: {abs_path} (created if missing)"
    else:
        assert os.path.exists(abs_path), f"Missing required file: {abs_path}"


def test_virtualenv_active():
    # Check if running inside a virtual environment
    assert hasattr(sys, "real_prefix") or (
        hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix
    ), (
        "Not running inside a virtual environment.\n"
        "To activate, run:\n"
        "  .\\.venv\\Scripts\\activate   # Windows\n"
        "  source .venv/bin/activate        # macOS/Linux\n"
    )


def test_python_version():
    assert sys.version_info >= (
        3,
        9,
    ), f"Python 3.9+ required, found {sys.version_info.major}.{sys.version_info.minor}"


def test_venv_exists():
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    venv_path = os.path.join(project_root, ".venv")
    assert os.path.isdir(venv_path), (
        f".venv directory not found at {venv_path}\n"
        "To create it, run: python Tools/Setup_Environment.py or make setup"
    )


def test_requirements_txt_matches_installed():
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    req_path = os.path.join(project_root, "requirements.txt")
    if not os.path.exists(req_path):
        pytest.skip("requirements.txt not found")
    encodings = ["utf-8", "utf-8-sig", "utf-16"]
    for encoding in encodings:
        try:
            with open(req_path, "r", encoding=encoding) as f:
                req_lines = [
                    line.strip().split("==")[0]
                    for line in f
                    if line.strip() and not line.startswith("#")
                ]
            break
        except UnicodeDecodeError:
            continue
    else:
        pytest.fail(
            "requirements.txt could not be decoded with utf-8, utf-8-sig, or utf-16."
        )
    # Map requirements.txt names to import names if needed
    import_name_map = {"Pygments": "pygments"}
    for req in req_lines:
        import_name = import_name_map.get(req, req)
        try:
            importlib.import_module(import_name)
        except ImportError:
            pytest.fail(
                f"requirements.txt package not installed or import name mismatch: {req}"
            )


def test_pip_version():
    pip_version = importlib_metadata.version("pip")
    major, minor, *_ = map(int, pip_version.split(".")[:2])
    if major < 23:
        print(
            f"Warning: pip version is {pip_version}. Consider upgrading to pip>=23.0 for best compatibility."
        )


def test_vscode_config_files_are_valid_json():
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    vscode_dir = os.path.join(project_root, ".vscode")
    config_files = ["settings.json", "tasks.json", "extensions.json"]
    for fname in config_files:
        fpath = os.path.join(vscode_dir, fname)
        if os.path.exists(fpath):
            with open(fpath, "r", encoding="utf-8") as f:
                try:
                    json.load(f)
                except json.JSONDecodeError as e:
                    pytest.fail(f"VS Code config file {fname} is not valid JSON: {e}")


def test_makefile_targets():
    import platform

    if platform.system() == "Windows":
        pytest.skip(
            "Makefile targets are skipped on Windows (GNU Make not required). Use VS Code tasks or run scripts directly."
        )
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    makefile_path = os.path.join(project_root, "Makefile")
    if not os.path.exists(makefile_path):
        pytest.skip("Makefile not found")
    for target in ["setup", "test"]:
        try:
            result = subprocess.run(
                ["make", target],
                cwd=project_root,
                capture_output=True,
                text=True,
                timeout=120,
            )
        except Exception as e:
            pytest.fail(f"Error running 'make {target}': {e}")
        if result.returncode != 0:
            pytest.fail(
                f"'make {target}' failed with exit code {result.returncode}. Output:\n{result.stdout}\n{result.stderr}"
            )


def test_requirements_txt_exact_match():
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    req_path = os.path.join(project_root, "requirements.txt")
    if not os.path.exists(req_path):
        pytest.skip("requirements.txt not found")
    installed = {
        dist.metadata["Name"].lower() for dist in importlib_metadata.distributions()
    }
    encodings = ["utf-8", "utf-8-sig", "utf-16"]
    for encoding in encodings:
        try:
            with open(req_path, "r", encoding=encoding) as f:
                req_lines = [
                    line.strip().split("==")[0].lower()
                    for line in f
                    if line.strip() and not line.startswith("#")
                ]
            break
        except UnicodeDecodeError:
            continue
    else:
        pytest.fail(
            "requirements.txt could not be decoded with utf-8, utf-8-sig, or utf-16."
        )
    req_set = set(req_lines)
    missing = req_set - installed
    extra = installed - req_set
    if missing:
        pytest.fail(
            f"requirements.txt lists packages not installed: {', '.join(sorted(missing))}"
        )
    if extra:
        print(
            f"Warning: Extra packages installed not listed in requirements.txt: {', '.join(sorted(extra))}"
        )


# User-specific settings for VS Code
def get_user_settings():
    return {
        "python.defaultInterpreterPath": "C:\\GIT\\Raid_Tools\\.venv\\Scripts\\python.exe",
    }
