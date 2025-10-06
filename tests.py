from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content


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
print(get_file_content("calculator","main.py"))

# # result for pkg directory
print(get_file_content("calculator","pkg/calculator.py"))

# # result for /bin directory
print(get_file_content("calculator","/bin/cat"))

# # result for ../ directory
print(get_file_content("calculator","pkg/does_not_exist.py"))