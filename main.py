import sys
import os
from google import genai
from google.genai import types
from dotenv import load_dotenv
from functions.get_files_info import schema_get_files_info

def main():
    #this reads .env in the current working directory
    load_dotenv()

    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    # Filter out any arguments that start with '--' (like --verbose)
    # to only keep the actual prompt parts.
    args = []
    for arg in sys.argv[1:]:
        if not arg.startswith("--"):
            args.append(arg)

    # If no prompt arguments remain after filtering, display usage and exit.
    if not args:
        print("AI Code Assistant")
        print('\nUsage: python main.py "your prompt here" [--verbose]')
        print('Example: python main.py "How do I build a calculator app?"')
        sys.exit(1)

    # Join the remaining arguments to form the full user prompt
    user_prompt = " ".join(args)

    # Determine if --verbose flag is present anywhere in the command line arguments
    verbose = "--verbose" in sys.argv

    # If verbose mode is enabled, print the user prompt.
    if verbose:
        print(f"User prompt: {user_prompt}\n")

    # Construct the message payload for the API call.
    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]

    system_prompt = """
    You are a helpful AI coding agent.

    When a user asks a question or makes a request, make a function call plan. 
    You can perform the following operations:

    - List files and directories

    All paths you provide should be relative to the working directory. 
    You do not need to specify the working directory in your function calls as it is automatically 
    injected for security reasons.
    """

    available_functions = types.Tool(
        function_declarations=[
            schema_get_files_info
        ]
    )
    generate_config = types.GenerateContentConfig(tools=[available_functions], 
                                                  system_instruction=system_prompt)


    # Call the helper function to generate and print content, passing the verbose flag.
    generate_content(client, messages, verbose, generate_config)


def generate_content(client, messages, verbose, generate_config):
    # Generate the content from the model. This happens only once.
    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=messages,
        config=generate_config
    )

    # If verbose mode is enabled, print the token counts.
    if verbose:
        print("Prompt tokens:", response.usage_metadata.prompt_token_count)
        print("Response tokens:", response.usage_metadata.candidates_token_count)

    # Always print the main response text.
    print("Response:")
    print(response.text)
    # print("Args", sys.argv)


if __name__ == "__main__":
    main()

