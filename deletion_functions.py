# Code for handling the deletion of functions and parsing of path links. 
import os
import sys
import obtain_functions as ob
import helper_functions as hf
from validation_functions import RECOGNIZED_SS_EXTENSIONS
from helper_functions import STATES, FOLDERS

FILE_PATH = os.path.realpath(__file__)

def delete_from_cwd(cwd=None, delete_from_subdirs=False):
    cwd = hf.cwd_none_check(cwd)
    hf.path_validation(cwd)
    to_delete = ob.get_save_states(cwd=cwd, scan_subdirs=delete_from_subdirs)

    for save_state in to_delete:
        save_state_path = os.path.join(cwd, save_state)
        os.remove(save_state_path)

def delete_from_text_file():
    if not os.path.exists(STATES):
        print("Creating a text file to hold save states...")
        with open(STATES, "r") as state_file:
            print(f"{STATES} has been created")
            return 
    else:
        with open(STATES, "r") as states:
            save_states = states.readlines()
            for save_state in save_states:
                hf.path_validation(save_state)
                os.remove(save_state)

def delete_from_folders(delete_from_subdirs=False):
    if not os.path.exists(FOLDERS):
        print("Creating a text file to hold save states...")
        with open(FOLDERS, "r") as state_file:
            print(f"{FOLDERS} has been created")
            return 

    else:
        with open(FOLDERS, "r") as directories:
            folders = directories.readlines()
            for folder in folders:
                delete_from_cwd(cwd=folder, delete_from_subdirs=delete_from_subdirs)
