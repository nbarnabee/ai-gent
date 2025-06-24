import os
import sys
import pprint
from call_function import call_function
from dotenv import load_dotenv
from google import genai
from google.genai import types
from schemas import available_functions

load_dotenv()

api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)
model = "gemini-2.0-flash-001"
system_prompt = """
You are a helpful AI coding agent.

When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

- List files and directories
- Read file contents
- Execute Python files with optional arguments
- Write or overwrite files

All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
"""

if len(sys.argv) > 1:
    user_prompt = sys.argv[1]
    verbose = "--verbose" in sys.argv
    messages = [
            types.Content(role="user", parts=[types.Part(text=user_prompt)])
        ]
    try:
        response = client.models.generate_content(
                model=model,
                contents=messages,
                config=types.GenerateContentConfig(
                    system_instruction=system_prompt,
                    tools=[available_functions]
                ),
            )

        metadata = response.usage_metadata
        function_calls_list = response.function_calls

        if function_calls_list and len(function_calls_list):
            for function_call in function_calls_list:
                result = call_function(function_call, verbose)

                if result.parts[0].function_response.response:
                    if verbose:
                        print(f"-> {result.parts[0].function_response.response}")

                else:
                    raise Exception("something went wrong")


        else:
            print(response.text)

        if verbose:
            print(f"User prompt: {user_prompt}")
            print(f"Prompt tokens: {metadata.prompt_token_count}")
            print(f"Response tokens: {metadata.candidates_token_count}")

    except Exception as e:
        print(f"Error: your request encountered an issue: {e}")

else:
    print("Error. Prompt Required")
    raise SystemExit(1)
