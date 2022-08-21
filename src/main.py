import os, sys
import pyautogui
import time

import battlegrounde_farm
from utils import find_aqw_hwnd, focus_window_hwnd

pyautogui.FAILSAFE = True
 
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
    main()