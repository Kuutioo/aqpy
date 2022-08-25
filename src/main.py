import os
import pyautogui
import bots

from bots.gold import *
from bots.item import *
from utils import find_aqw_hwnd, focus_window_hwnd
from helpers import check_user_input

pyautogui.FAILSAFE = True
 
def start():
    aqw_hwnd = find_aqw_hwnd()
    focus_window_hwnd(aqw_hwnd)

    print('Application Running')
    print('Press CTRL + C to exit\n\n')
    
    
# Main function of the program    
def main():    
    os.system('cls')
    print('Application Starting...\n\n')
    
    while True:
        print('1 - Battlegrounde Gold Farm')
        print('2 - Enchanted Scale')
        print('3 - Skill Rotate')
        try:
            choice = int(input('\nEnter bot number: '))
        except ValueError:
            print('Please enter a number\n')
            continue
        
        start()
        if choice == 1:
            bots.gold.battlegrounde_bot.main() 
        elif choice == 2:
            bots.item.enchanted_scale_bot.main()
        elif choice == 3:
            bots.skill.skill_rotate_bot.main()
          
if __name__ == "__main__":
    main()