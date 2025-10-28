# python
import os
from google.genai import types
from config import MAX_CHARS

def get_file_content(working_directory, file_path):
    # Return text content of a file within the working directory, with length cap
    try:
        # Resolve absolute paths for security checks
        abs_working = os.path.abspath(working_directory)
        abs_target = os.path.abspath(os.path.join(working_directory, file_path))

        # Disallow path escapes outside the working directory
        if os.path.commonpath([abs_working, abs_target]) != abs_working:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

        # Ensure it’s a regular file
        if not os.path.isfile(abs_target):
            return f'Error: File not found or is not a regular file: "{file_path}"'

        # Read text file (UTF-8)
        with open(abs_target, "r", encoding="utf-8") as f:
            content = f.read()

        # Truncate overly long files to MAX_CHARS and annotate
        if len(content) > MAX_CHARS:
            content = content[:MAX_CHARS] + f'\n[... File "{file_path}" truncated at {MAX_CHARS} characters]'

        return content

    except Exception as e:
        # Catch-all to prevent tool from crashing the app
        return f"Error: {e}"


# Tool schema so the model knows how to call this function
schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Reads and returns text file contents, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to the file to read, relative to the working directory."
            ),
        },
        # Optional: add required=["file_path"] if you want to force the argument
    ),
)