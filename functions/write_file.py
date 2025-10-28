# python
import os
from google.genai import types


def write_file(working_directory, file_path, content):
    try:
        abs_working = os.path.abspath(working_directory)
        abs_target = os.path.abspath(os.path.join(working_directory, file_path))
        dir_path = os.path.dirname(abs_target)

        # Prevent path escape
        if os.path.commonpath([abs_working, abs_target]) != abs_working:
            return f'Error: Cannot write to "{file_path}" because it is outside the working directory'

        # Disallow writing to a directory path
        if os.path.isdir(abs_target):
            return f'Error: "{file_path}" is a directory, not a file'

        # Ensure parent directories exist
        if dir_path and not os.path.exists(dir_path):
            os.makedirs(dir_path, exist_ok=True)

        # Coerce/validate content
        if not isinstance(content, str):
            return "Error: content must be a string"

        # Write file
        with open(abs_target, "w", encoding="utf-8") as f:
            f.write(content)
        return f'Success: wrote {len(content)} characters to "{file_path}"'

    except Exception as e:
        return f"Error: {e}"


schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes text content to a file path relative to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to the file to write, relative to the working directory.",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The text content to write into the file.",
            ),
        },
        required=["file_path", "content"],
    ),
)