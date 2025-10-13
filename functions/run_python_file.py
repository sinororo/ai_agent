def run_python_file(working_directory, file_path, args=[]):
    try:
        
        abs_working = os.path.abspath(working_directory)
        abs_target = os.path.abspath(os.path.join(working_directory, file_path))

        if os.path.commonpath([abs_working, abs_target]) != abs_working:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        
        if not os.path.exists(abs_target):
            return f'Error: File "{file_path}" not found.'
        
        if not file_path.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file.'
        
    except Exception as e:
        return f"Error: executing Python file: {e}"