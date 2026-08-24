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

def delete_from_states_txt():
    if not os.path.exists(STATES):
        print("Creating a text file to hold save states...")
        with open(STATES, "r") as state_file:
            print(f"{STATES} has been created")
            return 
    else:
        with open(STATES, "r") as states:
            save_states = states.read().splitlines()
            for save_state in save_states:
                hf.path_validation(save_state)
                os.remove(save_state)

def delete_from_folders_txt(delete_from_subdirs=False):
    if not os.path.exists(FOLDERS):
        print("Creating a text file to hold save states...")
        with open(FOLDERS, "r") as state_file:
            print(f"{FOLDERS} has been created")
            return 

    else:
        with open(FOLDERS, "r") as directories:
            folders = directories.read().splitlines()
            for folder in folders:
                delete_from_cwd(cwd=folder, delete_from_subdirs=delete_from_subdirs)

def delete_from_text_file_of_dirs(text_file, delete_from_subdirs=False):
    hf.path_validation(text_file)
    with open(text_file, "r") as folder_file:
        directories = folder_file.read().splitlines()

    # Make sure every line here is a valid directory
    for directory in directories:
        if not os.path.isdir(directory): 
            raise FileNotFoundError(f"{directory} is not recognized as a folder")

    for directory in directories:
        delete_from_cwd(cwd=directory, delete_from_subdirs=delete_from_subdirs)