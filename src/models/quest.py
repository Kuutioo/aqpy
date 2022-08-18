import pyautogui
import time
import sys
from typing import List

from helpers import click
from .item import Item

class Quest:
    quest_tab_line_x, quest_tab_line_y = 300, 248
    
    def __init__(self, id: int, name: str, xp: int, gold: int, rewards: List[Item]):
        self.id = id
        self.name = name
        self.xp = xp
        self.gold = gold
        self.rewards = rewards
        
    # Function to handle all of the logic required to turn in a quest
    def turn_in_quest(self, quest_number: int):
        print(f'Completed Quest: {self.name}\n')
        
        pyautogui.hotkey('l')
        time.sleep(1.5)
        
        click(self.quest_tab_line_x, self.quest_tab_line_y + (37 * quest_number))
        time.sleep(1.5)
        
        turn_in_button = pyautogui.locateOnScreen('images/quest_turn_in_button.png')
        
        if turn_in_button == None:
            print(f'Could not find Turn In Button. Make sure you have graphics set to Low')
            sys.exit()
            
        turn_in_button_x, turn_in_button_y = pyautogui.center(turn_in_button)
        click(turn_in_button_x, turn_in_button_y)
        time.sleep(2)
            
        pyautogui.hotkey('l')
        time.sleep(2)
    
    # Function to handle all of the logic required to accept a quest   
    def accept_quest(self, quest_number: int):
        exclamation_mark = pyautogui.locateOnScreen('images/exclamation_mark.png')
        if exclamation_mark == None:
            print('Could nto find the Exclamation Mark to accept quest')
            sys.exit()
            
        exclamation_mark_x, exclamation_mark_y = pyautogui.center(exclamation_mark)
        click(exclamation_mark_x, exclamation_mark_y)  
        time.sleep(2)
            
        quests_button = pyautogui.locateOnScreen('images/quests_button.png')
        if quests_button == None:
            print('Could not find the Quests Button from the NPC')
            sys.exit()
                
        quests_button_x, quests_button_y = pyautogui.center(quests_button)
        click(quests_button_x, quests_button_y)
        time.sleep(2)
                
        click(self.quest_tab_line_x, self.quest_tab_line_y + (37 * quest_number))
        time.sleep(2)
                
        accept_button = pyautogui.locateOnScreen('images/quest_accept_button.png')
        if accept_button != None:
            accept_button_x, accept_button_y = pyautogui.center(accept_button)
            click(accept_button_x, accept_button_y)
            
        time.sleep(1.5)