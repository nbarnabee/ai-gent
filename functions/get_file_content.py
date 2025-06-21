import os

MAX_CHARS = 10000

def get_file_content(working_directory, file_path):
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))

    if not abs_file_path.startswith(os.path.abspath(working_directory)):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory.'

    if not os.path.isfile(abs_file_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'

    try:
        with open(abs_file_path, "r") as f:
            content = f.read(MAX_CHARS)
            # essentially, if there's more left after we have taken the first 10k chars, we know it was truncated
            if len(f.read(1)):
                content += f'\n[..File "{abs_file_path}" truncated at {MAX_CHARS} characters]'


        return content

    except Exception as e:
        return f"Error: error reading file '{file_path}': {e}"

