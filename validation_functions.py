# Validates whether save state files exist

import os 
import sys
from helper_functions import input_cwd

RECOGNIZED_SS_FILES = set([f".ss{i}" for i in range(1, 10)])

def has_save_states(cwd=None):
    """Checks for the EXISTENCE of particular save states in cwd in the
    given parameter."""
    while cwd is None: 
        cwd = input("Input the path of a folder that contains save states.")
    if os.path.isdir(cwd):
        file_list = os.listdir(cwd)
        for file in file_list:
            filename, file_ext = os.path.splitext(file)
            if file_ext in RECOGNIZED_SS_FILES:
                return True
        return False
    elif os.path.isfile(cwd): 
        raise FileExistsError("The Given cwd is a file, not a directory.")
    else:
        raise FileNotFoundError("The Given cwd does not exist or is invalid.")

def has_sav_file(cwd=None):
    while cwd is None: 
        cwd = input("Input the path of a folder that contains save states.")
    if os.path.isdir(cwd):
        file_list = os.listdir(cwd)
        for file in file_list:
            filename, file_ext = os.path.splitext(file)
            if file_ext == "sav":
                return True
        return False
    elif os.path.isfile(cwd): 
        raise FileExistsError("The Given cwd is a file, not a directory.")
    else:
        raise FileNotFoundError("The Given cwd does not exist or is invalid.")
    
    