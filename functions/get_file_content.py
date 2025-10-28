# python
import os
from google.genai import types
from config import MAX_CHARS

def get_file_content(working_directory, file_path):
    try:
        abs_working = os.path.abspath(working_directory)
        abs_target = os.path.abspath(os.path.join(working_directory, file_path))

        # Ensure target stays within working dir
        if os.path.commonpath([abs_working, abs_target]) != abs_working:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

        # Ensure it’s a regular file
        if not os.path.isfile(abs_target):
            return f'Error: File not found or is not a regular file: "{file_path}"'

        # Read text file (utf-8 by default)
        with open(abs_target, "r", encoding="utf-8") as f:
            content = f.read()

        # Truncate if too long
        if len(content) > MAX_CHARS:
            content = content[:MAX_CHARS] + f'\n[... File "{file_path}" truncated at {MAX_CHARS} characters]'

        return content

    except Exception as e:
        return f"Error: {e}"


schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Lists contents of a file, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The filepath to get file content from, relative to the working directory."
            ),
        },
    ),
)