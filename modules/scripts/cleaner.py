import os
import shutil

from modules.config import folder_path


def delete_file(path: str):
    print(f"delete_file path = {path}")
    shutil.rmtree(path, ignore_errors=True)


def delete_input_images():
    print("delete_input_images start")
    path_images = folder_path["input_images"]
    items = os.listdir(path_images)
    for item in items:
        if not item.endswith(".png"):
            continue
        path = f"{path_images}/{item}"
        print(f"os.remove path = {path}")
        os.remove(path)
    print("delete_input_images end")
