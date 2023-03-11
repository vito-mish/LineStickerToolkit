from colored import attr, bg, fg

from modules.init import init_folder_path
from modules.merge import merge_command
from modules.png_separator import run_image_separate
from modules.theme import colors

options = [
    "1. 合併 Midjourney command",
    "2. 分離 Midjourney 圖片 (1 to 4)",
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
