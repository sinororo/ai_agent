# python
import os
import sys

from dotenv import load_dotenv
from google import genai
from google.genai import types

from functions.get_files_info import schema_get_files_info
from functions.get_file_content import schema_get_file_content
from functions.write_file import schema_write_file
from functions.run_python_file import schema_run_python_file


def generate_content(client, messages, verbose, generate_config):
    """
    Send a single request to the model and print either a planned function call
    or natural language text.
    """
    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=messages,
        config=generate_config,
    )

    if verbose and response.usage_metadata:
        print("Prompt tokens:", response.usage_metadata.prompt_token_count)
        print("Response tokens:", response.usage_metadata.candidates_token_count)

    if response.function_calls:
        for function_call_part in response.function_calls:
            print(
                f"Calling function: {function_call_part.name}({function_call_part.args})"
            )
    else:
        print(response.text)


def main():
    # 1) Env and client
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    # 2) CLI args
    args = [arg for arg in sys.argv[1:] if not arg.startswith("--")]
    verbose = "--verbose" in sys.argv

    if not args:
        print("AI Code Assistant")
        print('\nUsage: python main.py "your prompt here" [--verbose]')
        print('Example: python main.py "How do I build a calculator app?"')
        sys.exit(1)

    user_prompt = " ".join(args)
    if verbose:
        print(f"User prompt: {user_prompt}\n")

    # 3) Messages
    messages = [types.Content(role="user", parts=[types.Part(text=user_prompt)])]

    # 4) System instruction
    system_prompt = """
You are a helpful AI coding agent.

When a user asks a question or makes a request, make a function call plan.
You can perform the following operations:

- List files and directories
- Read file contents
- Execute Python files with optional arguments
- Write or overwrite files

All paths you provide should be relative to the working directory.
You do not need to specify the working directory in your function calls as it is automatically
injected for security reasons.
"""

    # 5) Tools (function declarations)
    available_functions = types.Tool(function_declarations=[schema_get_files_info,
                                                            schema_write_file,
                                                            schema_get_file_content,
                                                            schema_run_python_file])

    # 6) Generation config
    generate_config = types.GenerateContentConfig(
        tools=[available_functions],
        system_instruction=system_prompt,
    )

    # 7) Call model
    generate_content(client, messages, verbose, generate_config)


if __name__ == "__main__":
    main()