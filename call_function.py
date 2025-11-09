from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file
from functions.run_python_file import run_python_file

def call_function(function_call_part, verbose = False):
    if verbose == True:
        print(f"Calling function: {function_call_part.name}({function_call_part.args})")
    else:
        print(f" - Calling function: {function_call_part.name}")



    
    
    # function_map = {
    # "get_files_info": get_files_info,
    # "get_file_content": get_file_content,
    # "write_file": write_file,
    # "run_python_file": run_python_file}

    # function_name = function_call_part.name

    # if function_name not in function_map:
    #     return types.Content(
    #         role="tool",
    #         parts=[
    #             types.Part.from_function_response(
    #                 name=function_name,
    #                 response={"error": f"Unknown function: {function_name}"},
    #             )
    #         ],
    #     )
    
    # kwargs = dict(function_call_part.args)
    # kwargs["working_directory"] = "./calculator"

    # fn = function_map[function_name]
    # result = fn(**kwargs)
    
    # return types.Content(
    #     role="tool",
    #     parts=[
    #         types.Part.from_function_response(
    #             name=function_name,
    #             response={"result": result},
    #         )
    #     ],
    # )