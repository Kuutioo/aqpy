import os, sys
import pyautogui
import time

import battlegrounde_farm
from helpers import parse_apybot_file
from utils import find_aqw_hwnd, focus_window_hwnd
from models import Class

pyautogui.FAILSAFE = True

combo = {'q': 3, 'w': 3, 'e': 25, 'r': 25}

archfiend = Class(9405, 'ArchFiend', combo)
 
def start():
    print('Application Starting...\n\n')
    
    aqw_hwnd = find_aqw_hwnd()
    focus_window_hwnd(aqw_hwnd)

    print('Application Running')
    print('Press CTRL + C to exit\n\n')
    
    
# Main function of the program    
def main():    
    os.system('cls')
    
    start()
    
    battlegrounde_farm.main() 
          
if __name__ == "__main__":
    # list = parse_apybot_file()
    # print(list)
    # main()
    time.sleep(3)
    while True:
        archfiend.attack()