import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)
model = "gemini-2.0-flash-001"


if len(sys.argv) > 1:
    user_prompt = sys.argv[1]
    isVerbose = "--verbose" in sys.argv
    messages = [
            types.Content(role="user", parts=[types.Part(text=user_prompt)])
        ]

    response = client.models.generate_content(
            model=model, 
            contents=messages
        )

    metadata = response.usage_metadata

    print(response.text)

    if (isVerbose):
        print(f"User prompt: {user_prompt}")
        print(f"Prompt tokens: {metadata.prompt_token_count}")
        print(f"Response tokens: {metadata.candidates_token_count}")

else:
    print("Error. Prompt Required")
    raise SystemExit(1)
