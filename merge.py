from typing import List

body_list: List[str] = []
prefix: str = ''
suffix: str = ''

with open('body.txt', 'r') as file:
    body_list = file.readlines()
    body_list = [s.replace('\n', '') for s in body_list]

with open('prefix.txt', 'r') as file:
    prefix = file.read()

with open('suffix.txt', 'r') as file:
    suffix = file.read()

with open('full-command.txt', 'w') as file:
    for body in body_list:
        file.write(f"{prefix} {body}{suffix}\n")
