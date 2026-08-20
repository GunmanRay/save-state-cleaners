import os
import sys
from validation_functions import RECOGNIZED_SS_FILES

def input_cwd():
    cwd = input("Input the path of a folder that contains save states: ")
    if not os.path.isdir(cwd): raise FileNotFoundError("cwd is not a directory")
    return cwd

def get_save_states(cwd=None):
    """Returns a list of all the save states found in the cwd.
    This function assumes the cwd is valid."""

    if cwd is None: cwd = input_cwd()

    file_list = os.listdir(cwd)
    save_states = []
    for file in file_list:
        filename, file_ext = os.path.splitext(file)
        if file_ext in RECOGNIZED_SS_FILES:
            save_states.append(os.path.join(cwd, file))
    return save_states 

def get_subdirectories(cwd=None):
    if cwd is None: cwd = input_cwd()

    file_list = os.listdir(cwd)
    subdirs = []
    for file in file_list:
        if os.path.isdir(file):
            subdirs.append(file)
    return file_list