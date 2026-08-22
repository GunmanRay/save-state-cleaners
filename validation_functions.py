# Validates whether save state files exist

import os 
import sys
import glob
from save_files import Emulators

RECOGNIZED_SS_EXTENSIONS = [".ss[0-9]", ".ds[0-9]"]
SET_SS = set(RECOGNIZED_SS_EXTENSIONS)

def h(cwd=None):
    """Checks for the EXISTENCE of MGBA-specific save states in the given cwd."""
    if os.path.exists(cwd):
        glob_link = os.path.join(cwd, Emulators.MGBA) 

        if glob.glob(glob_link): return True
        else: return False
    else:
        raise FileNotFoundError("The Given cwd does not exist.")