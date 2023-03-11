from colored import attr, bg, fg

from modules.config import folder_path
from modules.init import init_folder_path
from modules.scripts.cleaner import delete_file, delete_input_images
from modules.scripts.merge import merge_command
from modules.scripts.png_separator import run_image_separate
from modules.theme import colors

options = [
    "[1] 合併 Midjourney command",
    "[2] 分離 Midjourney 圖片 (1 to 4)",
    "[d1] 清除 assets/outputs/images",
    "[d2] 清除 assets/outputs",
    "[d3] 清除 assets/inputs/*.png",
    "(enter 'q' to exit)",
]


def print_options():
    option_text = ""
    for option in options:
        option_text += f"{option}\n"
    print(fg(colors["primary"][0]) + f"\n{option_text}" + attr("reset"))
    print(fg(colors["gray"][5]) + "請選擇要執行的腳本：" + attr("reset"), end="")


def switch_script_by_id(id):
    if id == "1":
        merge_command()
    elif id == "2":
        run_image_separate()
    elif id == "d1":
        delete_file(folder_path["output_images"])
    elif id == "d2":
        delete_file(folder_path["output"])
    elif id == "d3":
        delete_input_images()
    elif id in ["q", "Q"]:
        pass
    else:
        print(fg(colors["error"][0]) + "Command not found" + attr("reset"))


if __name__ == "__main__":
    init_folder_path()
    print_options()
    id = input()
    print(bg(colors["success"][0]) + f"開始執行腳本：{id}" + attr("reset"), end="\n\n")
    switch_script_by_id(id)
    print("\n--exit--")
