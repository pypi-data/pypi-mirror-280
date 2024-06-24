import os

from osbot_utils.utils.Env import get_env

from osbot_utils.utils.Files import folder_name, parent_folder, current_folder


def env__home():                           # todo: this should be refatored to be env__home__is__root
    return get_env('HOME', '')

def env__pwd():
    return get_env('PWD', '')

def env__old_pwd():
    return get_env('OLDPWD', '')

def env__remove__old_pwd(value):
    return value.replace(env__old_pwd(), '')

def convert_paths_into_folder_dict(data_set):
    def insert_into_dict(d, parts):
        if len(parts) == 1:
            if "files" not in d:
                d["files"] = {}
            d["files"][parts[0]] = None  # Or some default value
        else:
            head, *tail = parts
            if head not in d:
                d[head] = {}
            insert_into_dict(d[head], tail)

    folder_dict = {}

    for item in data_set:
        parts = item.split('/')
        insert_into_dict(folder_dict, parts)

    return folder_dict


def path_combine_safe(base_path, file_location, raise_exception=False):                                  # handle possible directory transversal attacks
    full_path            = os.path.join(base_path, file_location)                                       # Combine and normalize paths
    normalised_base_path = os.path.normpath(base_path)
    normalised_full_path = os.path.normpath(full_path)

    if os.path.commonpath([normalised_base_path, normalised_full_path]) == normalised_base_path:        # Check for directory traversal
        return normalised_full_path
    if raise_exception:
        raise ValueError("Invalid file location: directory traversal attempt detected.")
    return None

def parent_folder_name(target):
    return folder_name(parent_folder(target))