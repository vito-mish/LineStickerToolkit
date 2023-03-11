import os

from colored import attr, fg
from PIL import Image

from modules.config import folder_path
from modules.theme import colors

path_input = folder_path["input_images"]
path_output = folder_path["output_images"]


def separate_by_path(path: str) -> None:
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
        file_name = f"{path_output}/cropped_{index + 1}.png"
        cropped_image = image.crop((tuple(coord)))
        cropped_image.save(file_name)


def run_image_separate():
    print("run_image_separate start")
    items = os.listdir(path_input)
    for item in items:
        if not item.endswith(".png"):
            # print(fg(colors["error"][0]) + f"[filename: {item}] is not .png file.") # ! for debug
            continue
        print(fg(colors["success"][0]) + f"[filename: {item}] in progress......")
        separate_by_path(f"{path_input}/{item}")
    print(attr("reset") + "\nrun_image_separate end")
