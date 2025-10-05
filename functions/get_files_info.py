import os
def get_files_info(working_directory, directory="."):
    try:

         # 1) Build the absolute target path from working_directory + directory
        abs_working = os.path.abspath(working_directory)
        abs_target = os.path.abspath(os.path.join(working_directory, directory))

        # 2) Ensure target_path stays within working_directory (compare absolute paths)
        if os.path.commonpath([abs_working, abs_target]) != abs_working:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

        # 3) Ensure target_path is a directory
        if not os.path.isdir(abs_target):
            return f'Error: "{directory}" is not a directory'

        # 4) List entries and build lines: "- NAME: file_size=### bytes, is_dir=Bool"
        lines = []
        for name in os.listdir(abs_target):
            entry = os.path.join(abs_target, name)
            is_dir = os.path.isdir(entry)
            size = os.path.getsize(entry) # size for both files and dirs is fine per instructions
            lines.append(f'- {name}: file_size={size} bytes, is_dir={is_dir}')

        # 5) Join lines into a single string
        return "\n".join(lines)
        
    except Exception as e:
        return f"Error: {e}"