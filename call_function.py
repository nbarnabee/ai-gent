from google import genai
from google.genai import types

from functions.get_file_content import get_file_content
from functions.get_files_info import get_files_info
from functions.run_python_file import run_python_file
from functions.write_file import write_file

WORKING_DIRECTORY = "calculator"
CALLABLE_FUNCTIONS = {
    "get_file_content": get_file_content,
    "get_files_info": get_files_info,
    "run_python_file": run_python_file,
    "write_file": write_file
}

def call_function(function_call):
    try:
        if function_call.name in CALLABLE_FUNCTIONS:
            func = CALLABLE_FUNCTIONS[function_call.name]
            kwargs = {}
            for key, value in function_call.args.items():
                kwargs[key] = value

            result = func(WORKING_DIRECTORY, **kwargs)

            return types.Content(
                role="tool",
                parts=[
                    types.Part.from_function_response(
                        name=function_call.name,
                        response={"result": result},
                    )
                ],
            )


        else:
            return types.Content(
                role="tool",
                parts=[
                    types.Part.from_function_response(
                        name=function_call.name,
                        response={"error": f"Unknown function: {function_call.name}"},
                    )
                ],
            )

    except Exception as e:
        print(f"Error:  {e}")

