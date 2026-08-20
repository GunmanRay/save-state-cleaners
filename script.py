# Script for actually running the code

# Outline (NON-SUBDIR VERSION): 
# - Obtains the given directory path
#   - Checks if the directory path is valid
# - Scans for all the save state files
# - Puts them into a list.
# - Deletes the save state files. 

# Outline (SUBDIR VERSION):
# - Obtains the given directory path
#   - Checks if the directory path is valid
# - Creates a list of subdirectories. 
#   - For every subdirectory, repeat the subdir process.
#   - If there's no more subdirectories, do the non-sub-dir ver. 
# - Scans for all the save state files
# - Puts them into a list.
# - Deletes the save state files. 