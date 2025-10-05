from functions.get_files_info import get_files_info

# result for current directory
print(get_files_info("calculator","."))

# result for pkg directory
print(get_files_info("calculator","pkg"))

# result for /bin directory
print(get_files_info("calculator","bin"))

# result for ../ directory
print(get_files_info("calculator","../"))