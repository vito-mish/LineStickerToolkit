import os
import random
import shutil

from colored import attr, fg

from modules.config import folder_path
from modules.theme import colors
from modules.utils import get_current_date, open_folder

# src_file = '/path/to/source/file.txt'
# dst_folder = '/path/to/destination/folder/'
# dst_file = os.path.join(dst_folder, os.path.basename(src_file))

# shutil.move(src_file, dst_file)


def run_auto_pack(n: int = 8):
    print("run_auto_package start")
    path_output = folder_path["output"]
    path_output_images = folder_path["output_images"]
    images = os.listdir(path_output_images)
    images = list(filter(lambda x: x.endswith(".png"), images))
    if len(images) <= n:
        print(
            fg(colors["error"][0])
            + f"Error: Insufficient number of pictures. len(images) = {len(images)}"
            + attr("reset")
        )
        return
    dst_folder = f"{path_output}/{get_current_date(1)}"
    if not os.path.exists(dst_folder):
        os.makedirs(dst_folder)
    images = random.sample(images, n)
    for index, image in enumerate(images):
        src_file = f"{path_output_images}/{image}"
        # dst_file = os.path.join(dst_folder, os.path.basename(src_file))
        dst_file = os.path.join(dst_folder, "{:02d}.png".format(index + 1))
        shutil.move(src_file, dst_file)
        open_folder(dst_folder)
        print(dst_file)
    print("run_auto_package end")
