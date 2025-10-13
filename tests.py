from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file
from functions.run_python_file import run_python_file


# result for current directory
# print(get_files_info("calculator","."))

# # result for pkg directory
# print(get_files_info("calculator","pkg"))

# # result for /bin directory
# print(get_files_info("calculator","bin"))

# # result for ../ directory
# print(get_files_info("calculator","../"))

# print(get_file_content("calculator","lorem.txt"))

# result for current directory
# print(get_file_content("calculator","main.py"))

# # # result for pkg directory
# print(get_file_content("calculator","pkg/calculator.py"))

# # # result for /bin directory
# print(get_file_content("calculator","/bin/cat"))

# # # result for ../ directory
# print(get_file_content("calculator","pkg/does_not_exist.py"))

# print(write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum"))
# print(write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"))
# print(write_file("calculator", "/tmp/temp.txt", "this should not be allowed"))

print(run_python_file("calculator", "main.py"))
print(run_python_file("calculator", "main.py", ["3+5"]))
print(run_python_file("calculator", "tests.py"))
print(run_python_file("calculator", "../main.py"))
print(run_python_file("calculator", "nonexistent.py"))
print(run_python_file("calculator", "lorem.txt"))
