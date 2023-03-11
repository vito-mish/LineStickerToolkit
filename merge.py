from typing import List


path_input = "assets/inputs/command"
path_output = "assets/outputs"


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
