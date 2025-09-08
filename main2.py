import sys
import os
from google import genai
from google.genai import types
from dotenv import load_dotenv


def main():
    load_dotenv()

    # Determine if --verbose flag is present anywhere in the command line arguments
    verbose = "--verbose" in sys.argv

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

    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    # Join the remaining arguments to form the full user prompt
    user_prompt = " ".join(args)

    # If verbose mode is enabled, print the user prompt.
    if verbose:
        print(f"User prompt: {user_prompt}\n")

    # Construct the message payload for the API call.
    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]

    # Call the helper function to generate and print content, passing the verbose flag.
    generate_content(client, messages, verbose)


def generate_content(client, messages, verbose):
    # Generate the content from the model. This happens only once.
    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=messages,
    )

    # If verbose mode is enabled, print the token counts.
    if verbose:
        print("Prompt tokens:", response.usage_metadata.prompt_token_count)
        print("Response tokens:", response.usage_metadata.candidates_token_count)

    # Always print the main response text.
    print("Response:")
    print(response.text)


if __name__ == "__main__":
    main()