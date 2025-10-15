"""
Test for Tools/cleanup_test_output_dirs.py: Warns (does not fail) if files would be removed by the cleanup script.
Runs the script with --test, prints the output block, and passes if nothing would be removed.
"""
import subprocess
import sys
from pathlib import Path


import warnings
import pytest

def test_warn_files_that_would_be_cleaned():
    script_path = Path(__file__).parent.parent / 'Tools' / 'cleanup_test_output_dirs.py'
    if not script_path.exists():
        pytest.skip(f"Script not found: {script_path}")
    result = subprocess.run([sys.executable, str(script_path), '--test'], capture_output=True, text=True)
    print("\n========== CLEANUP SCRIPT STDOUT ==========")
    print(result.stdout)
    print("========== END STDOUT ==========")
    # Check for result marker in output
    if '[CLEANUP_RESULT] SUCCESS' in result.stdout:
        assert True
    elif '[CLEANUP_RESULT] WARNING' in result.stdout:
        warnings.warn("Files would be removed by the cleanup script. See output above.", UserWarning)
        assert True
    else:
        # Unexpected output, show stderr if any
        print("\n========== CLEANUP SCRIPT STDERR ==========")
        print(result.stderr)
        print("========== END STDERR ==========")
        assert False, "Cleanup script did not return a recognizable result marker."
