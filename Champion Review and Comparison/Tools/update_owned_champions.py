import os
import sys
import importlib.util

# Path to Champ_Intake.py in the parent directory
champ_intake_path = os.path.join(os.path.dirname(__file__), "..", "Champ_Intake.py")
champ_intake_path = os.path.abspath(champ_intake_path)

# Load Champ_Intake.py as a module
spec = importlib.util.spec_from_file_location("Champ_Intake", champ_intake_path)
champ_intake = importlib.util.module_from_spec(spec)
spec.loader.exec_module(champ_intake)

print("📋 Using owned champion list for prompt generation...\n")
champ_intake.run_smart_batch_from_owned_list(fast_mode=True)
