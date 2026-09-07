# Code for handling the deletion of functions and parsing of path links. 
import os
import logging
from . import obtain_functions as ob
from . import helper_functions as hf
from savestatecleaners.validation_functions import RECOGNIZED_SS_EXTENSIONS
from savestatecleaners.helper_functions import STATES, FOLDERS
from pathlib import Path 

logger = logging.getLogger(__name__)
FILE_PATH = Path(__file__).resolve().parent

def delete_from_cwd(cwd=None, delete_from_subdirs=False):
    cwd = Path(hf.cwd_none_check(cwd))
    hf.path_validation(cwd)
    to_delete = ob.get_save_states(cwd=cwd, scan_subdirs=delete_from_subdirs)

    for save_state in to_delete:
        save_state_path = cwd / Path(save_state)
        logger.debug("Deleting %s...", save_state_path)
        try:
            Path(save_state_path).unlink(missing_ok=True)
            logger.info("%s deleted succesfully.", save_state_path)
        except PermissionError: 
            logger.warning("%s cannot be deleted, as it is a restriced file", save_state_path)

def delete_from_states_txt():
    if not Path.exists(STATES):
        logger.debug("Creating a text file to hold save states...")
        with open(STATES, "r") as state_file:
            logger.info("%s has been created", STATES)
            return 
    else:
        with open(STATES, "r") as states:
            logger.debug("Reading lines from %s...", STATES)
            save_states = states.read().splitlines()
            for save_state in save_states:
                hf.path_validation(save_state)
                logger.debug("Deleting %s...", save_state)
                try:
                    Path(save_state).unlink(missing_ok=True)
                    logger.info("%s deleted succesfully.", save_state)
                except PermissionError: 
                    logger.warning("%s cannot be deleted, as it is a restriced file", save_state)

def delete_from_folders_txt(delete_from_subdirs=False):
    if not Path.exists(FOLDERS):
        logger.debug("Creating a text file to hold save states...")
        with open(FOLDERS, "r") as state_file:
            logger.info("%s has been created", FOLDERS)
            return 

    else:
        with open(FOLDERS, "r") as directories:
            logger.debug("Reading lines from %s...", FOLDERS)
            folders = directories.read().splitlines()
            for folder in folders:
                logger.debug("Deleting save states in %s...", folder)
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