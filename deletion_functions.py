# Code for handling the deletion of functions and parsing of path links. 
import os
import sys
from validation_functions import RECOGNIZED_SS_FILES

# Current implementation assumes valid CWD, states and game. 
def delete_states(game, states, cwd):
    game_save_states = [".".join([game, state]) for state in states]
    for save_state in game_save_states:
        to_del = os.path.join(cwd, save_state)
        if os.path.exists(to_del):
            os.remove(to_del)