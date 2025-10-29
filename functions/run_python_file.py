# python
import os
import sys
import subprocess
from google.genai import types

def run_python_file(working_directory, file_path, args=None):
    # Run a Python script within the working directory, with optional CLI args
    try:
        # Avoid mutable default; normalize to list
        args = args or []

        # Resolve absolute paths for security checks
        abs_working = os.path.abspath(working_directory)
        abs_target = os.path.abspath(os.path.join(working_directory, file_path))

        # Disallow path escapes outside the working directory
        if os.path.commonpath([abs_working, abs_target]) != abs_working:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

        # Ensure target exists
        if not os.path.exists(abs_target):
            return f'Error: File "{file_path}" not found.'

        # Require a .py file
        if not file_path.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file.'

        # Validate args shape
        if not isinstance(args, list) or not all(isinstance(a, str) for a in args):
            return 'Error: "args" must be a list of strings.'

        # Execute using the current Python interpreter for portability
        completed = subprocess.run(
            [sys.executable, file_path, *args],
            capture_output=True,
            text=True,
            cwd=abs_working,
            timeout=30,
        )

        # If nothing was printed to stdout or stderr
        if not completed.stdout and not completed.stderr:
            return "No output produced."

        # Collate outputs and return code info
        output = ""
        if completed.stdout:
            output += f"STDOUT: {completed.stdout}"
        if completed.stderr:
            output += f"STDERR: {completed.stderr}"
        if completed.returncode != 0:
            output += f"Process exited with code {completed.returncode}"

        return output

    except Exception as e:
        # Catch-all to avoid crashing the tool
        return f"Error: executing Python file: {e}"


# Tool schema declaration so the model knows how to call this function
schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Runs a Python file with optional CLI args, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to the Python file to run, relative to the working directory."
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                items=types.Schema(type=types.Type.STRING),
                description="Optional list of string arguments to pass to the Python file."
            )
        },
    ),
)