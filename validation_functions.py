# Validates whether save state files exist

import os 
import sys
import glob

RECOGNIZED_SS_EXTENSIONS = [".ss[0-9]", ".ds[0-9]"]
SET_SS = set(RECOGNIZED_SS_EXTENSIONS)

MGBA = f"*{RECOGNIZED_SS_EXTENSIONS[0]}"
MELONDS = DESMUME = f"*{RECOGNIZED_SS_EXTENSIONS[1]}"

def has_mgba(cwd=None):
    """Checks for the EXISTENCE of particular save states in cwd in the
    given parameter."""
    if os.path.exists(cwd):
        glob_link = os.path.join(cwd, MGBA) 

        if glob.glob(glob_link): return True
        else: return False
    else:
        raise FileNotFoundError("The Given cwd does not exist.")