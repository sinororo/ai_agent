import os


functions = os.path.abspath("functions")
calculator = os.path.abspath("calculator")
print(os.path.commonpath([functions,calculator]))