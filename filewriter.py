# writes and manages files
import log
import os
import shutil

# =================================================================================
# COPY, RENAME, MOVE, OR DELETE A FILE
# =================================================================================

def copy_file(filepath, new_directory):
    new_file = new_directory + filepath.split("/")[-1]
    success = False
    i = 0
    while not success or i < 3:
        try:
            shutil.copy2(filepath, new_file)
        except:
            log.warning(f"COPY_FILE(): Attempt {i} to copy {filepath} to {new_file} failed.")
        if os.path.isfile(new_file):
            success = True
        i += 1
    if not success:
        log.error(f"COPY_FILE(): Attempts to copy {filepath} to {new_file} failed.")


def rename_file(filepath, rename):
    rename = filepath.split("/")[:-1] + rename
    success = False
    i = 0
    while not success or i < 3:
        try:
            os.rename(filepath, rename)
        except:
            log.warning(f"RENAME_FILE(): Attempt {i} to rename {filepath} to {rename} failed.")
        if os.path.isfile(rename) and not os.path.isfile(filepath):
            success = True
        i += 1
    if not success:
        log.error(f"RENAME_FILE(): Attempts to rename {filepath} to {rename} failed.")


def move_file(filepath, new_directory):
    new_file = new_directory + filepath.split("/")[-1]
    success = False
    i = 0
    while not success or i < 3:
        try:
            shutil.move(filepath, new_file)
        except:
            log.warning(f"MOVE_FILE(): Attempt {i} to move {filepath} failed.")
        success = False if (os.path.isfile(new_directory) and not os.path.isfile(filepath)) else False
        i += 1
    if not success:
        log.error(f"MOVE_FILE(): Attempts to move {filepath} failed.")


def delete_file(filepath):
    success = False
    i = 0
    while not success or i < 3:
        try:
            os.remove(filepath)
        except OSError:
            log.warning(f"DELTE_FILE(): Attempt {i} to delete {filepath} failed.")
        success = False if os.path.isfile(filepath) else True
        i += 1
    if not success:
        log.error(f"DELETE_FILE(): Attemps to delete {filepath} failed.")



# =================================================================================
# WRITE OR APPEND TO A FILE
# =================================================================================


def write_file(filepath, message):
    try:
        file = open(filepath, "w")
        file.write(message)
    except OSError:
        log.error(f"WRITE_FILE(): Unable to access {filepath}")
    finally:
        file.close()

def append_file(filepath, message):
    try:
        file = open(filepath, "a")
        file.write(message)
    except OSError:
        log.error(f"APPEND_FILE(): Unable to access or write to {filepath}")
    finally:
        file.close()
