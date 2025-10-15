import os

REQUIRED_FOLDERS = [
    "input/Prompt",
    "output/Champions",
    "output/completed_prompts",
]


def test_required_folders_exist():
    repo_root = os.path.dirname(os.path.abspath(__file__))
    for rel_path in REQUIRED_FOLDERS:
        abs_path = os.path.join(repo_root, "..", "..", rel_path)
        if not os.path.isdir(abs_path):
            os.makedirs(abs_path, exist_ok=True)
        assert os.path.isdir(
            abs_path
        ), f"Required folder missing (created if missing): {abs_path}"
