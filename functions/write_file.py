
import os

def write_file(working_directory, file_path, content):
    try:

        abs_working = os.path.abspath(working_directory)
        abs_target = os.path.abspath(os.path.join(working_directory, file_path))
        dir_path = os.path.dirname(abs_target)

        if os.path.commonpath([abs_working, abs_target]) != abs_working:
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
        
        if os.path.isdir(abs_target):
            return f'Error: "{file_path}" is a directory, not a file'
        
        if dir_path and not os.path.exists(dir_path):
            os.makedirs(dir_path, exist_ok=True)
        
        with open(abs_target,"w") as f:
            f.write(content)
            return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    
    except Exception as e:
        return f"Error: {e}"
