import os
import subprocess

def run_python_file(working_directory, file_path=None):
        abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))

        if not abs_file_path.startswith(os.path.abspath(working_directory)):
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory.'

        if not os.path.exists(abs_file_path):
            return f'Error: File "{file_path}" not found.'

        if not os.path.splitext(abs_file_path)[1] == ".py":
            return f'Error: "{file_path}" is not a Python file.'

        try:
           process = subprocess.run(['python3', abs_file_path], capture_output=True, text=True, timeout=30)


           output = [f"STDOUT: {process.stdout}", f"STDERR: {process.stderr}"]
           if not process.returncode == 0:
               output.append(f"Process exited with code {process.returncode}")
           if not len(process.stdout):
               output.append("No output produced")
           return "\n".join(output)

        except Exception as e:
            return f'Error: executing Python file "{file_path}": {e}'