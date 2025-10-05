# python
import os

# def inside(wd, sub):
#     abs_working = os.path.abspath(wd)
#     abs_target = os.path.abspath(os.path.join(wd,sub))
#     return abs_working, abs_target, os.path.commonpath([abs_working, abs_target])

# print(inside("calculator", "."))          # True (same dir)
# print(inside("calculator", "pkg"))        # True (child)
# print(inside("calculator", "../"))        # False (parent)
# print(inside("calculator", "/bin"))       # False (absolute outside)

# python
# import os
# wd = ".."
# print(os.path.abspath(os.path.join(wd, ".")))   # True
# print(os.path.abspath(os.path.join(wd, "pkg")))  # True
# print(os.path.abspath(os.path.join(wd, "nope")))  # False

# print(os.path.isdir(os.path.abspath(os.path.join(wd, "."))))     # True
# print(os.path.isdir(os.path.abspath(os.path.join(wd, "pkg"))))   # True
# print(os.path.isdir(os.path.abspath(os.path.join(wd, "nope"))))  # False

wd = "."
print(os.listdir(wd))