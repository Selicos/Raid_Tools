import os
import sys
import importlib.util

champion_dir = os.path.join("Champion Review and Comparison")
champ_intake_path = os.path.join(champion_dir, "champ_intake.py")

# Load champ_intake.py as a module
spec = importlib.util.spec_from_file_location("champ_intake", champ_intake_path)
champ_intake = importlib.util.module_from_spec(spec)
spec.loader.exec_module(champ_intake)

print("📋 Using owned champion list for prompt generation...\n")
champ_intake.run_smart_batch_from_owned_list(fast_mode=True)
