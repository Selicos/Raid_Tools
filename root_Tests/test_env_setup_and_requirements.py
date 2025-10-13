import os
import subprocess
import sys
import importlib
# pytest is required for this test file. If not installed, attempt to install it.
try:
    import pytest
except ImportError:
    import subprocess
    import sys
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pytest"])
    import pytest

REQUIRED_PACKAGES = [
    "colorama",
    "pyperclip",
    "pytest",
    "black",
    "iniconfig",
    "packaging",
    "pluggy",
    "pygments",
]


# All paths are now relative to the Raid_Tools root
PROJECT_COMPONENTS = [
    ("ChampionIntake/Champions", True),
    ("ChampionIntake/Prompt", True),
    ("ChampionIntake/Tests", True),
    ("ChampionIntake/templates/logTemplate.json", False),
    ("ChampionIntake/README.md", False),
    ("Tools/cleanup_duplicate_champions.py", False),
    ("Tools/validate_json.py", False),
    ("Tools/Setup_Environment.py", False),
    ("ChampionIntake/modules/Champion_Review_Module_0.md", False),
    ("ChampionIntake/modules/merge_modules.py", False),
    ("ChampionSummary/generateChampionSummaries.py", False),
    ("ChampionAnalysisTool/championAnalysis.py", False),
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
        assert os.path.isdir(abs_path), f"Missing required directory: {abs_path}"
    else:
        assert os.path.exists(abs_path), f"Missing required file: {abs_path}"


def test_virtualenv_active():
    # Check if running inside a virtual environment
    assert hasattr(sys, "real_prefix") or (
        hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix
    ), "Not running inside a virtual environment. Activate .venv before running tests."


def test_python_version():
    assert sys.version_info >= (
        3,
        9,
    ), f"Python 3.9+ required, found {sys.version_info.major}.{sys.version_info.minor}"


def test_venv_exists():
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    venv_path = os.path.join(project_root, ".venv")
    assert os.path.isdir(venv_path), f".venv directory not found at {venv_path}"


def test_requirements_txt_matches_installed():
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    req_path = os.path.join(project_root, "requirements.txt")
    if not os.path.exists(req_path):
        pytest.skip("requirements.txt not found")
    # Try utf-8, then fallback to utf-8-sig, then utf-16
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
    # Map known package names to their import names
    name_map = {
        "Pygments": "pygments",
        # Add more mappings here if needed
    }
    for req in req_lines:
        import_name = name_map.get(req, req)
        try:
            importlib.import_module(import_name)
        except ImportError:
            pytest.fail(
                f"requirements.txt package not installed or import name mismatch: {req} (tried import '{import_name}')"
            )

    # 2. Test pip version is up-to-date (warn if not, but do not fail)
    def test_pip_version():
        import pkg_resources
        pip_version = pkg_resources.get_distribution("pip").version
        major, minor, *_ = map(int, pip_version.split(".")[:2])
        # Warn if pip is older than 23.0 (arbitrary, but recent)
        if major < 23:
            print(f"Warning: pip version is {pip_version}. Consider upgrading to pip>=23.0 for best compatibility.")

    # 4. Test VS Code config files are valid JSON
    import json
    import glob

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

    # 5. Test Makefile targets 'setup' and 'test' run without error
    import shlex

    def test_makefile_targets():
        project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
        makefile_path = os.path.join(project_root, "Makefile")
        if not os.path.exists(makefile_path):
            pytest.skip("Makefile not found")
        for target in ["setup", "test"]:
            try:
                result = subprocess.run(["make", target], cwd=project_root, capture_output=True, text=True, timeout=120)
            except Exception as e:
                pytest.fail(f"Error running 'make {target}': {e}")
            if result.returncode != 0:
                pytest.fail(f"'make {target}' failed with exit code {result.returncode}. Output:\n{result.stdout}\n{result.stderr}")

    # 6. Test .env file exists and required keys are present (if .env.example exists)
    def test_env_file_keys():
        project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
        env_example = os.path.join(project_root, ".env.example")
        env_file = os.path.join(project_root, ".env")
        if not os.path.exists(env_example):
            pytest.skip(".env.example not found; skipping .env key check.")
        if not os.path.exists(env_file):
            pytest.skip(".env not found; skipping .env key check.")
        def parse_env(path):
            keys = set()
            with open(path, "r", encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if line and not line.startswith("#") and "=" in line:
                        keys.add(line.split("=", 1)[0].strip())
            return keys
        example_keys = parse_env(env_example)
        env_keys = parse_env(env_file)
        missing = example_keys - env_keys
        if missing:
            pytest.fail(f".env is missing required keys: {', '.join(sorted(missing))}")

    # 8. Test requirements.txt matches installed packages exactly (no drift)
    def test_requirements_txt_exact_match():
        project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
        req_path = os.path.join(project_root, "requirements.txt")
        if not os.path.exists(req_path):
            pytest.skip("requirements.txt not found")
        # Get installed packages
        import pkg_resources
        installed = {pkg.key for pkg in pkg_resources.working_set}
        # Parse requirements.txt
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
            pytest.fail("requirements.txt could not be decoded with utf-8, utf-8-sig, or utf-16.")
        req_set = set(req_lines)
        missing = req_set - installed
        extra = installed - req_set
        if missing:
            pytest.fail(f"requirements.txt lists packages not installed: {', '.join(sorted(missing))}")
        # Optionally, warn if there are extra installed packages not in requirements.txt
        if extra:
            print(f"Warning: Extra packages installed not listed in requirements.txt: {', '.join(sorted(extra))}")
