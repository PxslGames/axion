import os
import time
from modules.misc import *
from utils.menus import *
from pystyle import Colorate, Colors
from colorama import init, Fore, Style

init(autoreset=True)

class Axion:
    def __init__(self):
        self.mainmenu_grad = Colorate.Vertical(Colors.purple_to_blue, mainmenutxt)
        self.configmenu_grad = Colorate.Vertical(Colors.purple_to_blue, configmenutxt)
        self.banner_grad = Colorate.Vertical(Colors.purple_to_blue, banner)
        self.launch()
    
    def launch(self):
        clear()
        self.banner()
        self.mainmenu()
    
    def banner(self):
        print(self.banner_grad)
    
    def mainmenu(self):
        while True:
            settitle("axion")
            clear()
            self.banner()
            print(self.mainmenu_grad)
            colorinput = Colorate.Color(Colors.purple, "[@HOME] > ")
            inp = input(colorinput)

            if inp == "1":
                self.configmenu()
            elif inp == "9":
                axionquit()
            else:
                print("[-] Invalid Option, Please Try Again!")
                time.sleep(1)
                self.mainmenu()
    
    def configmenu(self):
        while True:
            settitle("axion")
            clear()
            self.banner()
            print(self.configmenu_grad)
            colorinput = Colorate.Color(Colors.purple, "[@CONFIG] > ")
            inp = input(colorinput)

            if inp == "1":
                self.mainmenu()
            else:                
                print("[-] Invalid Option, Please Try Again!")
                time.sleep(1)
                self.mainmenu()

if __name__ == "__main__":
    axion = Axion()