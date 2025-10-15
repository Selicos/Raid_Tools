import os
import sys
from pathlib import Path

DIRS_TO_CLEAN = [
	'output/Champions/',
	'output/completed_prompts/',
	'output/Summary/',
	'output/Comparisons/',
	'output/SkillTurnAnalysis/',
	'input/Prompt/',
	'input/turn_analysis/',
]

PLACEHOLDER_NAMES = {'.placeholder'}

def is_placeholder(file_path: Path) -> bool:
	return file_path.name in PLACEHOLDER_NAMES

def would_be_removed(file_path: Path) -> bool:
	return file_path.is_file() and file_path.suffix.lower() in {'.json', '.md'} and not is_placeholder(file_path)


def find_dirs_with_files_to_remove(base: Path):
	"""Return a list of (relative_dir, has_files) for each dir in DIRS_TO_CLEAN."""
	result = []
	for rel_dir in DIRS_TO_CLEAN:
		abs_dir = base / rel_dir
		has_removable = False
		if abs_dir.exists() and abs_dir.is_dir():
			has_removable = any(
				would_be_removed(item)
				for item in abs_dir.iterdir() if item.is_file()
			)
		result.append((rel_dir.rstrip('/'), has_removable))
	return result


def clean_dir(dir_path: Path) -> bool:
	"""Remove files in dir_path, return True if any files were removed."""
	if not dir_path.exists() or not dir_path.is_dir():
		return False
	removed = False
	for item in dir_path.iterdir():
		if item.is_file() and not is_placeholder(item):
			if item.suffix.lower() in {'.json', '.md'}:
				try:
					item.unlink()
					removed = True
				except Exception as e:
					print(f"Failed to remove {item}: {e}")
		elif item.is_dir():
			# Do not recurse for top-level warning, but still clean subdirs
			clean_dir(item)
	return removed


def main():
	base = Path(__file__).parent.parent
	args = sys.argv[1:]
	test_mode = '--test' in args
	# Parse --all or --dir=... options
	clean_all = '--all' in args
	selected_dirs = set()
	for arg in args:
		if arg.startswith('--dir='):
			val = arg.split('=', 1)[1].rstrip('/')
			selected_dirs.add(val)

	dir_status = find_dirs_with_files_to_remove(base)

	if test_mode:
		print("\n========== CLEANUP TEST OUTPUT BLOCK ==========")
		any_files = False
		for rel_dir, has_files in dir_status:
			if has_files:
				print(f"[WARN] {rel_dir} contains files that would be removed.")
				any_files = True
			else:
				print(f"[OK]   {rel_dir} is clean.")
		if any_files:
			print("[CLEANUP_RESULT] WARNING")
		else:
			print("[CLEANUP_RESULT] SUCCESS")
		print("========== END CLEANUP TEST OUTPUT ==========" )
		return 0

	# Interactive/human/AI mode
	# Determine which dirs to clean
	to_clean = []
	if clean_all:
		to_clean = [rel_dir for rel_dir, has_files in dir_status if has_files]
	elif selected_dirs:
		to_clean = [rel_dir for rel_dir, has_files in dir_status if has_files and rel_dir in selected_dirs]
	else:
		# Interactive prompt for each dir
		print("[INFO] Cleanup candidate directories:")
		for idx, (rel_dir, has_files) in enumerate(dir_status, 1):
			if has_files:
				print(f"  {idx}. {rel_dir} [files present]")
			else:
				print(f"  {idx}. {rel_dir} [clean]")
		print("\nSelect directories to clean:")
		print("  [a] All dirty dirs  [n] None  [1-N] Comma-separated list (e.g. 1,3,5)")
		resp = input("Your choice: ").strip().lower()
		if resp == 'a':
			to_clean = [rel_dir for rel_dir, has_files in dir_status if has_files]
		elif resp == 'n' or not resp:
			print("Aborted by user. No files were deleted.")
			return 0
		else:
			try:
				idxs = {int(x.strip()) for x in resp.split(',') if x.strip().isdigit()}
				to_clean = [rel_dir for i, (rel_dir, has_files) in enumerate(dir_status, 1) if has_files and i in idxs]
			except Exception:
				print("Invalid input. Aborted.")
				return 1

	if not to_clean:
		print("No directories selected for cleanup. No files were deleted.")
		return 0

	cleaned_dirs = []
	for rel_dir in to_clean:
		abs_dir = base / rel_dir
		if clean_dir(abs_dir):
			cleaned_dirs.append(rel_dir)
	if cleaned_dirs:
		print("[INFO] The following directories had files removed by the cleanup task:")
		for d in cleaned_dirs:
			print(f"  - {d}")
	else:
		print("[INFO] No files were removed by the cleanup task.")
	print("Cleanup complete.")

if __name__ == "__main__":
	sys.exit(main())
