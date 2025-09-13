import sys
import os
from google import genai
from google.genai import types
from dotenv import load_dotenv


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