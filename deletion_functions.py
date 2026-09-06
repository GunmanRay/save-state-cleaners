# Code for handling the deletion of functions and parsing of path links. 
import os
import logging
import obtain_functions as ob
import helper_functions as hf
from validation_functions import RECOGNIZED_SS_EXTENSIONS
from helper_functions import STATES, FOLDERS
from pathlib import Path 

logger = logging.getLogger()
FILE_PATH = Path(__file__).resolve().parent

def delete_from_cwd(cwd=None, delete_from_subdirs=False):
    cwd = Path(hf.cwd_none_check(cwd))
    hf.path_validation(cwd)
    to_delete = ob.get_save_states(cwd=cwd, scan_subdirs=delete_from_subdirs)

    for save_state in to_delete:
        save_state_path = cwd / Path(save_state)
        logger.info("Deleting %s", save_state_path)
        Path(save_state_path).unlink(missing_ok=True)

def delete_from_states_txt():
    if not Path.exists(STATES):
        print("Creating a text file to hold save states...")
        with open(STATES, "r") as state_file:
            print(f"{STATES} has been created")
            return 
    else:
        with open(STATES, "r") as states:
            save_states = states.read().splitlines()
            for save_state in save_states:
                hf.path_validation(save_state)
                logger.info("Deleting %s", save_state)
                Path(save_state).unlink(missing_ok=True)

def delete_from_folders_txt(delete_from_subdirs=False):
    if not Path.exists(FOLDERS):
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