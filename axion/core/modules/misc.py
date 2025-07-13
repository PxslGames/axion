import os
import sys
import time

def clear():
    os.system("cls")

def settitle(title):
    os.system(f"title {title}")

def axionquit():
    print("exiting...")
    time.sleep(1)
    sys.exit()