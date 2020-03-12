import os


def dir_exists(dir_path):
    return os.path.isdir(dir_path) and os.path.exists(dir_path)


def file_exists(file_path):
    return os.path.isfile(file_path) and os.path.exists(file_path)


def is_file_empty(file_path):
    if not file_exists(file_path):
        return True

    return os.path.getsize(file_path) == 0


def create_file_if_not_exists(full_file_path):
    if not file_exists(full_file_path):
        with open(full_file_path, 'w'):
            pass


def create_dir_if_not_exists(full_dir_path):
    if not dir_exists(full_dir_path):
        os.makedirs(full_dir_path)
