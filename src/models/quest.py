import pyautogui
import time
import sys
from typing import List

from helpers import click
from .item import Item

class Quest:
    quest_tab_line_x, quest_tab_line_y = 370, 248
    
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

        click(self.quest_tab_line_x, 830)
        time.sleep(1.5)
            
        pyautogui.hotkey('l')
        time.sleep(1)
    
    # Function to handle all of the logic required to accept a quest   
    def accept_quest(self, quest_number: int):                
        click(self.quest_tab_line_x, self.quest_tab_line_y + (37 * quest_number))
        time.sleep(1.5)
                
        click(self.quest_tab_line_x, 830)
        time.sleep(1.5)