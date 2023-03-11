import os

from modules.config import folder_path


def init_folder_path():
    targets = [folder_path["output"], folder_path["output_images"]]
    for item in targets:
        if not os.path.exists(item):
            os.makedirs(item)
