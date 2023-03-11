import platform
import subprocess


def open_folder(file_path: str) -> None:
    command = "explorer" if platform.system() == "Windows" else "open"
    subprocess.run([command, file_path])
