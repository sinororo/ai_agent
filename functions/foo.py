import os

def demo_safe(file_path):
    dir_path = os.path.dirname(file_path)
    print(f"file_path={file_path!r}, dir_path={dir_path!r}")

    if dir_path and not os.path.exists(dir_path):
        print("Trying to make dirs WITH guard...")
        os.makedirs(dir_path, exist_ok=True)

    print("Done\n")

demo_safe("notes.txt")
demo_safe("docs/readme.md")
demo_safe("data/reports/out.txt")