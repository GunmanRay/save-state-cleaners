# Validates whether save state files exist

import os 
import sys

RECOGNIZED_SS_FILES = set([f".ss{i}" for i in range(1, 10)])

def has_save_states(cwd=None):
    """Checks for the EXISTENCE of particular save states in cwd in the
    given parameter."""
    if os.path.exists(cwd):
        file_list = os.listdir(cwd)
        for file in file_list:
            filename, file_ext = os.path.splitext(file)
            if file_ext in RECOGNIZED_SS_FILES:
                return True
        return False
    else:
        raise FileNotFoundError("The Given cwd does not exist.")