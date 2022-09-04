import os
import pyautogui
import bots

from bots.gold import *
from bots.items import *
from utils import find_aqw_hwnd, focus_window_hwnd
from helpers import check_user_input

pyautogui.FAILSAFE = True
 
def start():
    aqw_hwnd = find_aqw_hwnd()
    focus_window_hwnd(aqw_hwnd)

    print('Application Running')
    print('Press CTRL + C to exit or drag your mouse to any corners of the screen\n\n')
    
    
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
        
        if choice == 1:
            start()
            bots.gold.battlegrounde_bot.main() 
        elif choice == 2:
            start()
            bots.items.enchanted_scale_bot.main()
        elif choice == 3:
            while True:
                print('\n1 - Archfiend')
                print('2 - Legion Revenant')
                print('3 - Necrotic Chronomancer')
                print('4 - Auto attack Spam')
                try:
                    class_choice = int(input('\nEnter class number: '))
                except ValueError:
                    print('Please enter a number\n')
                    continue
                start()
                bots.skill.skill_rotate_bot.main(class_choice)
          
if __name__ == "__main__":
    main()