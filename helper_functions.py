import os
import sys
import glob

SS_CLEANER_PATH = os.path.dirname(os.path.abspath(__file__))
INFO_FOLDER = os.path.join(SS_CLEANER_PATH, "info_folder")
FOLDERS = os.path.join(INFO_FOLDER, "folders.txt")
STATES = os.path.join(INFO_FOLDER, "save_states.txt")

def path_validation(path):
    if not os.path.exists(path):
        raise FileNotFoundError(f"{path} is not recognized as a valid file.")

def input_cwd():
    cwd = input("Input the path of a folder that contains save states: ")
    return cwd

def cwd_none_check(cwd):
    while cwd is None: 
        try:
            cwd = input_cwd()
        except FileNotFoundError:
            cwd = None
    return cwd 

def ask_for_writing_perms(file_list, write_to_states_file):
    valid_ans = {"Y", "N"}
    print("Would you like to write these directories to a text file?")
    answer = input("Input either Y or N (CASE SENSITIVE!):")
    while answer.strip() not in valid_ans:
        print("Answer not recognized (Recognized answers are Y or N exactly)")
        answer = input("Input either Y or N (CASE SENSITIVE!):")

    if answer != "N":
        path = ""
        if write_to_states_file: path = STATES
        else: path = FOLDERS

        with open(path, "w") as record_file:
            record_file.writelines(file_list)  
