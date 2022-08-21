import pyautogui
import time

from typing import List
from helpers import click

from .item import Item

class Quest:
    quest_tab_line_x, quest_tab_line_y = 370, 248
    
    def __init__(self, id: int, name: str, xp: int, gold: int, required_items: List[Item], rewards: List[Item]):
        self.id = id
        self.name = name
        self.xp = xp
        self.gold = gold
        self.required_items = required_items
        self.rewards = rewards
        
    # Function to handle all of the logic required to turn in a quest
    def turn_in_quest(self, quest_number):
        pyautogui.hotkey('l')
        time.sleep(1.5)
        
        click(self.quest_tab_line_x, self.quest_tab_line_y + (37 * quest_number), 1.5)

        print(f'Completed Quest: {self.name}\n')
        for item in self.required_items:
            item.item_count = 0
        click(self.quest_tab_line_x, 830, 1.5)
            
        pyautogui.hotkey('l')
        time.sleep(1)
    
    # Function to handle all of the logic required to accept a quest   
    def accept_quest(self, quest_number):                
        click(self.quest_tab_line_x, self.quest_tab_line_y + (37 * quest_number), 1.5)
        click(self.quest_tab_line_x, 830, 1.5)
        
    def check_if_quest_done(self, quest_number, fail_safe_time):
        time.sleep(fail_safe_time)
        self.required_items[0].item_count = 0
        self.turn_in_quest(quest_number)   