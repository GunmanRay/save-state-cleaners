import zipfile
import logging
import obtain_functions as ob
import helper_functions as hf
from pathlib import Path

logger = logging.getLogger()

FILE_PATH = Path(__file__).resolve().parent

def zip_save_states(cwd, target_directory, scan_subdirs=False):
    cwd = Path(hf.cwd_none_check(cwd))
    hf.path_validation(cwd)

    target_directory = Path(hf.cwd_none_check(target_directory))
    hf.path_validation(cwd)

    save_states = ob.get_save_states(cwd, scan_subdirs=scan_subdirs)
    zip_path = target_directory / Path("save_state_zips.zip")

    with zipfile.ZipFile(zip_path, "w") as ss_zip:
        for save_state in save_states:
            full_path = cwd / Path(save_state)
            logger.debug("Adding %s into %s...", full_path, zip_path)
            ss_zip.write(full_path)
    logger.info("%s fully written to.", zip_path)