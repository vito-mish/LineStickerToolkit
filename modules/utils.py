import platform
import subprocess
from datetime import datetime
from typing import Literal


def open_folder(file_path: str) -> None:
    command = "explorer" if platform.system() == "Windows" else "open"
    subprocess.run([command, file_path])


def get_current_date(type: Literal[0, 1] = 0):
    time = datetime.now()
    if type == 1:
        result = time.strftime("%Y-%m-%d_%H-%M-%S")
    else:
        result = time.strftime("%Y-%m-%d %H:%M:%S")
    return result
