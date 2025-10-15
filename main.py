# python
import sys
import os
from google import genai
from google.genai import types
from dotenv import load_dotenv
from functions.get_files_info import schema_get_files_info

def main():
    # Load env vars (expects GEMINI_API_KEY in .env or environment)
    load_dotenv()

    # Create Gemini client
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    # Capture user prompt from CLI args (ignore flags like --verbose)
    args = [arg for arg in sys.argv[1:] if not arg.startswith("--")]

    # Require a prompt
    if not args:
        print("AI Code Assistant")
        print('\nUsage: python main.py "your prompt here" [--verbose]')
        print('Example: python main.py "How do I build a calculator app?"')
        sys.exit(1)

    user_prompt = " ".join(args)
    verbose = "--verbose" in sys.argv

    if verbose:
        print(f"User prompt: {user_prompt}\n")

    # User message for the model
    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]

    # System instruction: how to use tools and path constraints
    system_prompt = """
    You are a helpful AI coding agent.

    When a user asks a question or makes a request, make a function call plan. 
    You can perform the following operations:

    - List files and directories

    All paths you provide should be relative to the working directory. 
    You do not need to specify the working directory in your function calls as it is automatically 
    injected for security reasons.
    """

    # Advertise available tool(s) (function schemas) to the model
    available_functions = types.Tool(
        function_declarations=[schema_get_files_info]
    )

    # Generation config: include tools and system prompt
    generate_config = types.GenerateContentConfig(
        tools=[available_functions],
        system_instruction=system_prompt
    )

    # Send request and handle response
    generate_content(client, messages, verbose, generate_config)


def generate_content(client, messages, verbose, generate_config):
    # Single model call with our config and messages
    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=messages,
        config=generate_config
    )

    # Optional usage diagnostics
    if verbose:
        print("Prompt tokens:", response.usage_metadata.prompt_token_count)
        print("Response tokens:", response.usage_metadata.candidates_token_count)

    # If the model planned a tool call, print it; otherwise print plain text
    if response.function_calls:
        for function_call_part in response.function_calls:
            print(f"Calling function: {function_call_part.name}({function_call_part.args})")
    else:
        print("Response:")
        print(response.text)


if __name__ == "__main__":
    main()