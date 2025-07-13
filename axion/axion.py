import os
import sys
import time
import subprocess
from core.utils.menus import *
from core.modules.misc import *

PURPLE = "\033[95m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
RESET = "\033[0m"

try:
    from pystyle import Colorate, Colors
    banner_display = Colorate.Vertical(Colors.purple_to_blue, banner)
except ImportError:
    banner_display = PURPLE + banner + RESET

def log(msg, color=RESET):
    print(f"{color}[Axion Loader] {msg}{RESET}")

def install_requirements():
    req_path = "core/requirements.txt"
    if not os.path.exists(req_path):
        log("No requirements.txt found. Skipping dependency install.", YELLOW)
        return

    log("Installing dependencies...", PURPLE)
    result = subprocess.call([sys.executable, "-m", "pip", "install", "-r", req_path])
    if result == 0:
        log("Dependencies installed successfully.", GREEN)
    else:
        log("pip exited with a non-zero status. This may be fine if packages were already installed.", YELLOW)

def launch_main():
    main_path = "core/main.py"
    if not os.path.exists(main_path):
        log("core/main.py not found. Cannot launch Axion.", RED)
        sys.exit(1)

    log("Launching Axion...", PURPLE)
    time.sleep(1)
    subprocess.call([sys.executable, main_path])

def main():
    clear()
    print(banner_display)
    log("Axion Loader started.", GREEN)
    time.sleep(1)

    install_requirements()
    launch_main()

if __name__ == "__main__":
    main()