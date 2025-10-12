import os
import re

REPO_ROOT = os.path.dirname(os.path.abspath(__file__))

def find_py_files(root):
    for dirpath, _, filenames in os.walk(root):
        for fname in filenames:
            if fname.endswith('.py'):
                yield os.path.join(dirpath, fname)

def extract_paths_from_line(line):
    string_matches = re.findall(r"[rR]?['\"]([a-zA-Z]:[\\/][^'\"]+|\.{0,2}[\\/][^'\"]+|[\\/]+)[\"']", line)
    paths = []
    for match in string_matches:
        # Ignore if the match is only slashes/backslashes or escape characters (any length)
        if all(c in "\\/ntbrfa" for c in match.strip()):
            continue
        if (("\\" in match or "/" in match)
            and len(match.strip()) > 1
            and not match.strip().startswith("*")
            and not match.strip().isidentifier()):
            paths.append(match)
    return paths

def check_paths():
    missing = []
    for pyfile in find_py_files(REPO_ROOT):
        with open(pyfile, encoding='utf-8') as f:
            for lineno, line in enumerate(f, 1):
                for path in extract_paths_from_line(line):
                    # Normalize and check if path exists (relative to repo root)
                    abs_path = os.path.normpath(os.path.join(REPO_ROOT, path))
                    if not os.path.exists(abs_path):
                        missing.append((pyfile, lineno, path))
    return missing

def test_all_paths_exist():
    missing = check_paths()
    assert not missing, (
        "Missing or invalid paths found:\n" +
        "\n".join(f"{pyfile}:{lineno} -> {path}" for pyfile, lineno, path in missing)
    )

if __name__ == "__main__":
    missing = check_paths()
    if missing:
        print("Missing or invalid paths found:")
        for pyfile, lineno, path in missing:
            print(f"{pyfile}:{lineno} -> {path}")
        exit(1)
    else:
        print("All referenced paths in .py files exist and are valid.")