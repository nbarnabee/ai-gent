import os

def write_file(working_directory, file_path, content):
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))

    if not abs_file_path.startswith(os.path.abspath(working_directory)):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory.'

    try:
        with open(abs_file_path, "w") as f:
            f.write(content)
            return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'


    except Exception as e:
        return f'Error: error writing to file "{file_path}": {e}'


    return f'moving on..'
