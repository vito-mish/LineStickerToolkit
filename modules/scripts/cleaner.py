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
    items = list(filter(lambda x: x.endswith(".png"), items))
    for item in items:
        path = f"{path_images}/{item}"
        print(f"os.remove path = {path}")
        os.remove(path)
    print("delete_input_images end")
