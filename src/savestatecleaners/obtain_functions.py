import os
import logging
from . import helper_functions as hf
from pathlib import Path 
from . save_files import Emulators
from savestatecleaners.validation_functions import RECOGNIZED_SS_EXTENSIONS

logger = logging.getLogger(__name__)

def get_save_states(cwd=None, scan_subdirs=False):
    """Returns a list of all the save states found in the cwd.
    This function assumes the cwd is valid."""

    cwd = Path(hf.cwd_none_check(cwd))
    hf.path_validation(cwd)

    os.chdir(cwd)
    save_states = []
    logger.debug("Scanning for save states...")
    # O(n^2), should be faster...
    for extension in RECOGNIZED_SS_EXTENSIONS:
        if scan_subdirs:
            extension = Path("**") / Path(extension)
        matches = Path(cwd).glob(pattern=extension, recurse_symlinks=scan_subdirs)
        logger.info("Found save states: %s", matches)
        save_states += matches

    if save_states: logger.info("Obtained files: %s", save_states)
    else: logger.info("There are no save states in the given directory.")
    return list(save_states)
        
def get_specific_save_states(emulator, cwd=None, use_recursion=False):
    """Returns a list of all the save states that are specific to the given
    emulator parameter. This function assumes the cwd is valid."""

    if not isinstance(emulator, Emulators):
        raise TypeError("Non-indexable parameter passed.")

    while cwd is None: 
        try:
            cwd = hf.input_cwd()
        except FileNotFoundError:
            cwd = None

    hf.path_validation(cwd)
    os.chdir(cwd)
    extension = Path(RECOGNIZED_SS_EXTENSIONS[emulator.value])

    if use_recursion:
        extension = Path("**") / extension
    logger.debug("Scanning for save states...")
    save_states = Path(cwd).glob(pattern=extension)

    if save_states: logger.info("Obtained files: %s", save_states)
    else: logger.info("There are no save states in the given directory.")

    return list(save_states)

def get_subdirectories(cwd=None):
    cwd = hf.cwd_none_check(cwd)

    file_list = os.listdir(cwd)
    subdirs = []
    for file in file_list:
        if os.path.isdir(file):
            subdirs.append(file)

    print(subdirs)
    return file_list

# TO BE DELETED UNDERNEATH:

def get_save_states_in_subdirs(cwd=None):
    subdirs = get_subdirectories(cwd)
    if not subdirs:
        print("This file does not have any subdirectories to scan.")
        get_save_states(cwd)
    else:
        pass

def get_save_states_recursive(cwd=None):
    cwd = Path(hf.cwd_none_check())
    hf.path_validation(cwd)

    save_states = []

    recursive_path = cwd / Path("**")

    for extension in RECOGNIZED_SS_EXTENSIONS:
        recursive_state = recursive_path / Path(extension)
        matches = Path(cwd).glob(pattern=recursive_state, recurse_symlinks=True)
        save_states += matches

    if save_states: print(save_states)
    else: print("There are no save states in the given directory.")
    return list(save_states)