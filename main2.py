import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")



    client = genai.Client(api_key=api_key)


    # check if  a command line argument for the prompt exists

    if len(sys.argv) >= 2:
        user_prompt = sys.argv[1]

        response = client.models.generate_content(
        model='gemini-2.0-flash-001',
        contents=[user_prompt])

        print(response.text) # take the first argument in the prompt

        if len(sys.argv) >= 3 and sys.argv[2] == "--verbose":
            print(response.text)
            print(f"User prompt: {sys.argv[1]}")
            print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
            print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
        
        else:
            print(response.text)
    else:
        # provide a default prompt
        print("Error: No prompt provided. Please provide a prompt as a command-line argument.")
        sys.exit(1)

if __name__ == "__main__":
    main()