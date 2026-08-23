# Code for handling the deletion of functions and parsing of path links. 
import os
import sys
import obtain_functions as ob
import helper_functions as hf
from validation_functions import RECOGNIZED_SS_EXTENSIONS


FILE_PATH = os.path.realpath(__file__)

def delete_from_cwd(cwd=None, delete_from_subdirs=False):
    cwd = hf.cwd_none_check(cwd)
    hf.path_validation(cwd)
    to_delete = ob.get_save_states(cwd=cwd, use_recursion=delete_from_subdirs)

    for save_state in to_delete:
        save_state_path = os.path.join(cwd, save_state)
        os.remove(save_state_path)