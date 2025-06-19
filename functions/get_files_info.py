import os

def get_files_info(working_directory, directory=None):
    target_path = os.path.abspath(os.path.join(working_directory, directory))

    if not target_path.startswith(os.path.abspath(working_directory)):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory.'

    if not os.path.isdir(target_path):
        return f'Error: "{directory}" is not a directory'

    else:
        directory_contents = os.listdir(target_path)
        contents_info = ""
        for item in directory_contents:
            item_path = os.path.join(target_path, item)
            contents_info += build_info_string(item, item_path)

        return contents_info[:-1]


def build_info_string(item, path):
    size = get_size(path)
    return f"- {item}: file_size={os.path.getsize(path)}, is_dir={os.path.isdir(path)}\n"

def get_size(path):
    total_size = 0
    if not os.path.isdir(path):
        total_size += os.path.getsize(path)
        return total_size
    else:
        for sub_item in os.listdir(path):
            total_size += get_size(os.path.join(path, sub_item))
            return total_size
    return total_size