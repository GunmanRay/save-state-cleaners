import os
import sys
import glob
import helper_functions as hf
from save_files import Emulators
# from helper_functions import input_cwd, path_validation
from validation_functions import RECOGNIZED_SS_EXTENSIONS

def get_save_states(cwd=None):
    """Returns a list of all the save states found in the cwd.
    This function assumes the cwd is valid."""

    cwd = hf.cwd_none_check(cwd)

    hf.path_validation(cwd)
    os.chdir(cwd)
    save_states = []

    # O(n^2), should be faster...
    for extension in RECOGNIZED_SS_EXTENSIONS:
        matches = glob.glob(extension)
        save_states += matches

    if save_states: print(save_states)
    else: print("There are no save states in the given directory.")
    return save_states
        

def get_save_states_recursive(cwd=None):
    cwd = hf.cwd_none_check()
    hf.path_validation(cwd)

    save_states = []

    recursive_path = os.path.join(cwd, "**")

    for extension in RECOGNIZED_SS_EXTENSIONS:
        recursive_state = os.path.join(recursive_path, extension)
        matches = glob.glob(recursive_state, recursive=True)
        save_states += matches

    if save_states: print(save_states)
    else: print("There are no save states in the given directory.")
    return save_states


    return save_states

def get_specific_save_states(emulator, cwd=None):
    """Returns a list of all the save states that are specific to the given
    emulator parameter. This function assumes the cwd is valid."""
    if not isinstance(emulator, Emulators) or type(emulator) != int:
        raise TypeError("Non-indexable parameter passed.")

    while cwd is None: 
        try:
            cwd = hf.input_cwd()
        except FileNotFoundError:
            cwd = None

    hf.path_validation(cwd)
    os.chdir(cwd)
    extension = RECOGNIZED_SS_EXTENSIONS[emulator.value]

    save_states = glob.glob(extension)

    if save_states: print(save_states)
    else: print("There are no save states in the given directory.")

    return save_states

def get_subdirectories(cwd=None):
    cwd = hf.cwd_none_check(cwd)

    file_list = os.listdir(cwd)
    subdirs = []
    for file in file_list:
        if os.path.isdir(file):
            subdirs.append(file)

    print(subdirs)
    return file_list

def get_save_states_in_subdirs(cwd=None):
    subdirs = get_subdirectories(cwd)
    if not subdirs:
        print("This file does not have any subdirectories to scan.")
        get_save_states(cwd)
    else:
        pass