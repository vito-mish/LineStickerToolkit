import os
import uuid
from typing import List

from colored import attr, fg
from PIL import Image

from modules.config import folder_path
from modules.theme import colors

path_input = folder_path["input_images"]
path_output = folder_path["output_images"]


def create_ids(n: int) -> List[str]:
    id_list: List[str] = []
    for _ in range(n):
        while True:
            new_id = str(uuid.uuid4())
            if new_id not in id_list:
                id_list.append(new_id)
                break
        print(f"new_id = {new_id}")

    return id_list


def separate_by_path(path: str, id: str) -> None:
    image = Image.open(path)
    width, height = image.size
    half_width = int(width * 0.5)
    half_height = int(height * 0.5)
    coords = []

    def append_coord(x1, y1, x2, y2):
        coords.append([x1, y1, x2, y2])

    data = [
        [0, 0, half_width, half_height],
        [half_width, 0, width, half_height],
        [0, half_height, half_width, height],
        [half_width, half_height, width, height],
    ]

    for item in data:
        append_coord(*item)

    for index, coord in enumerate(coords):
        file_name = f"{path_output}/{id}_cropped_{index + 1}.png"
        cropped_image = image.crop((tuple(coord)))
        cropped_image.save(file_name)


def run_image_separate():
    print("run_image_separate start")
    items = os.listdir(path_input)
    id_list = create_ids(len(items))
    for index, item in enumerate(items):
        if not item.endswith(".png"):
            # print(fg(colors["error"][0]) + f"[filename: {item}] is not .png file.") # ! for debug
            continue
        print(fg(colors["success"][0]) + f"[filename: {item}] in progress......")
        separate_by_path(
            path=f"{path_input}/{item}",
            id=id_list[index],
        )
    print(attr("reset") + "\nrun_image_separate end")
