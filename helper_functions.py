import os
import sys
import glob
from save_files import Emulators
from validation_functions import RECOGNIZED_SS_EXTENSIONS, MGBA, MELONDS

def path_validation(path):
    if not os.path.exists(path):
        raise FileNotFoundError(f"{path} is not recognized as a valid file.")

def input_cwd():
    cwd = input("Input the path of a folder that contains save states: ")
    return cwd

def get_save_states(cwd=None):
    """Returns a list of all the save states found in the cwd.
    This function assumes the cwd is valid."""

    while cwd is None: 
        try:
            cwd = input_cwd()
        except FileNotFoundError:
            cwd = None

    path_validation(cwd)
    os.chdir(cwd)
    extensions = []

    # O(n^2), should be faster...
    for extension in RECOGNIZED_SS_EXTENSIONS:
        matches = glob.glob(extension)
        extensions += matches

    if extensions: print(extensions)
    else: print("There are no save states in the given directory.")

def get_specific_save_states(emulator, cwd=None):
    if type(emulator) != Emulators or type(emulator) != int: 
        raise TypeError("Non-indexable type passed")

    while cwd is None: 
        try:
            cwd = input_cwd()
        except FileNotFoundError:
            cwd = None
    
        path_validation(cwd)
        os.chdir(cwd)

        state_ext = RECOGNIZED_SS_EXTENSIONS[emulator.value]
        matches = glob.glob(state_ext)
        
        if matches: print(matches)
        else: print("There are no save states in the given directory.")

        

def get_subdirectories(cwd=None):
    if cwd is None: cwd = input_cwd()

    file_list = os.listdir(cwd)
    subdirs = []
    for file in file_list:
        if os.path.isdir(file):
            subdirs.append(file)
    return file_list