from typing import List

from modules.config import folder_path
from modules.utils import open_folder

path_input = folder_path["input_command"]
path_output = folder_path["output"]


def merge_command():
    print("merge_command start")
    body_list: List[str] = []
    prefix: str = ""
    suffix: str = ""

    with open(f"{path_input}/body.txt", "r") as file:
        body_list = file.readlines()
        body_list = [s.replace("\n", "") for s in body_list]

    with open(f"{path_input}/prefix.txt", "r") as file:
        prefix = file.read()

    with open(f"{path_input}/suffix.txt", "r") as file:
        suffix = file.read()

    with open(f"{path_output}/full-command.txt", "w") as file:
        for body in body_list:
            file.write(f"{prefix} {body}{suffix}\n")
    print("merge_command end")
    open_folder(path_output)
