def run_python_file(working_directory, file_path, args=[]):
    try:
        
        abs_working = os.path.abspath(working_directory)
        # ano nga ulit ibig sabihin nung nirerepresent nung  abs_target
        abs_target = os.path.abspath(os.path.join(working_directory, file_path))
        
    except Exception as e:
        return f"Error: executing Python file: {e}"