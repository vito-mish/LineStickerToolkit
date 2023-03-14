from colored import attr, bg, fg

from modules.config import folder_path
from modules.init import init_folder_path
from modules.scripts.cleaner import delete_file, delete_input_images
from modules.scripts.merge import merge_command
from modules.scripts.png_auto_pack import run_auto_pack
from modules.scripts.png_separator import run_image_separate
from modules.theme import colors
from modules.utils import open_folder

options = [
    "[0] 打開 assets/inputs",
    "[1] 合併 Midjourney command",
    "[2] 分離 Midjourney 圖片 (1 to 4)",
    "\n",
    "[p1] 自動挑選：隨機挑選 8 張",
    "[p2] 自動挑選：隨機挑選 16 張",
    "[p3] 自動挑選：隨機挑選 24 張",
    "\n",
    "[d1] 刪除 assets/outputs/images",
    "[d2] 刪除 assets/outputs",
    "[d3] 刪除 assets/inputs/*.png",
    "\n",
    "(enter 'q' to exit)",
]


def print_options():
    option_text = ""
    for option in options:
        option_text += f"{option}\n"
    print(fg(colors["primary"][0]) + f"\n{option_text}" + attr("reset"))
    print(fg(colors["gray"][5]) + "請選擇要執行的腳本：" + attr("reset"), end="")


def switch_script_by_id(id):
    if id == "0":
        open_folder(folder_path["input_images"])
    elif id == "1":
        merge_command()
    elif id == "2":
        run_image_separate()
    elif id == "p1":
        run_auto_pack()
    elif id == "p2":
        run_auto_pack(16)
    elif id == "p3":
        run_auto_pack(24)
    elif id == "d1":
        delete_file(folder_path["output_images"])
    elif id == "d2":
        delete_file(folder_path["output"])
    elif id == "d3":
        delete_input_images()
    elif id in ["q", "Q"]:
        pass
    else:
        print(fg(colors["error"][0]) + "Error: Command not found" + attr("reset"))


def start():
    init_folder_path()
    print_options()
    id = input()
    print(bg(colors["success"][0]) + f"開始執行腳本：{id}" + attr("reset"), end="\n\n")
    switch_script_by_id(id)
    return id


if __name__ == "__main__":
    id = None
    while id not in ["q", "Q"]:
        id = start()
    print("\n--exit--")
