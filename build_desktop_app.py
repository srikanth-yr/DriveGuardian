"""
Build helper for packaging the desktop app with PyInstaller.
"""

import importlib.util
import subprocess
import sys
from pathlib import Path


PROJECT_ROOT = Path(__file__).parent.resolve()


def add_data_args(path_name):
    """Return a PyInstaller --add-data pair for a directory if it exists."""
    path = PROJECT_ROOT / path_name
    if not path.exists():
        return []
    return ["--add-data", f"{path}{';'}{path_name}"]


def main():
    """Build the desktop executable when PyInstaller is installed."""
    if importlib.util.find_spec("PyInstaller") is None:
        print("PyInstaller is not installed.")
        print("Install it with: python -m pip install pyinstaller")
        return 1

    command = [
        sys.executable,
        "-m",
        "PyInstaller",
        "--noconfirm",
        "--clean",
        "--windowed",
        "--name",
        "AI_Driver_Safety_App",
        "--hidden-import",
        "PIL._tkinter_finder",
    ]

    for directory in ["templates", "static", "dashboard", "sounds", "models"]:
        command.extend(add_data_args(directory))

    command.append(str(PROJECT_ROOT / "desktop_app.py"))

    print("Running:", " ".join(str(part) for part in command))
    subprocess.check_call(command, cwd=PROJECT_ROOT)
    print("Build complete. Check the dist/AI_Driver_Safety_App folder.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
