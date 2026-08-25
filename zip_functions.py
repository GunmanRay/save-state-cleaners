import os
import zipfile
import obtain_functions as ob
import helper_functions as hf

FILE_PATH = os.path.realpath(__file__)

def zip_save_states(cwd, target_directory, scan_subdirs=False):
    cwd = hf.cwd_none_check(cwd)
    hf.path_validation(cwd)

    target_directory = hf.cwd_none_check(target_directory)
    hf.path_validation(cwd)

    save_states = ob.get_save_states(cwd, scan_subdirs=scan_subdirs)
    zip_path = os.path.join(target_directory, "save_state_zips.zip")

    with zipfile.ZipFile(zip_path, "w") as ss_zip:
        for save_state in save_states:
            full_path = os.path.join(cwd, save_state)
            ss_zip.write(full_path)