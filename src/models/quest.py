from threading import Thread, Event
import pyautogui
import time

from typing import List
from helpers import click

from .item import Item

class Quest:
    quest_tab_line_x, quest_tab_line_y = 370, 248
    
    def __init__(self, id: int, name: str, xp: int, gold: int, failsafe_time: int, required_items: List[Item], rewards: List[Item]):
        self.id = id
        self.name = name
        self.xp = xp
        self.gold = gold
        self.failsafe_time = failsafe_time
        self.required_items = required_items
        self.rewards = rewards
        self.event = Event()
        
        self.check_quest_thread = Thread(target=self.check_quest_done, args=[self.event, 1, self.failsafe_time, True], daemon=True)
        
        
    # Function to handle all of the logic required to turn in a quest
    def turn_in_quest(self, quest_number, failsafe):
        self.event.set()
        self.check_quest_thread = None
        
        pyautogui.hotkey('l')
        time.sleep(1.8)
        
        click(self.quest_tab_line_x, self.quest_tab_line_y + (37 * quest_number), 1.5)
        
        if pyautogui.locateOnScreen('images/quest_turn_in_button.png', confidence=0.8) == None and failsafe:
            print('Turn in button not found!')
            print('Trying to force complete when next failsafe triggers')
            print('If quest is not completed then, it will loop back to see if the turn in button is found')
            
            pyautogui.hotkey('l')
            time.sleep(1)
            
            self.check_quest_thread = Thread(target=self.check_quest_done, args=[self.event, 1, self.failsafe_time, False], daemon=True)
            self.check_quest_thread.start()
                        
            return
        
        for item in self.required_items:
            item.item_count = 0
            
        print(f'\nCompleted Quest: {self.name}')
            
        self.check_quest_thread = Thread(target=self.check_quest_done, args=[self.event, 1, self.failsafe_time, True], daemon=True)
        self.event.clear()
        self.check_quest_thread.start()
                    
        click(self.quest_tab_line_x, 830, 1.5)
                  
        pyautogui.hotkey('l')
        time.sleep(1)
        
    
    # Function to handle all of the logic required to accept a quest   
    def accept_quest(self, quest_number):                
        click(self.quest_tab_line_x, self.quest_tab_line_y + (37 * quest_number), 1.5)
        click(self.quest_tab_line_x, 830, 1.5)
        self.check_quest_thread.start()
        
    def check_quest_done(self, event, quest_number, when_to_check, check_with_failsafe):
        for _ in range(when_to_check):
            if event.is_set():
                return
            time.sleep(1)
        print('\nTriggering Failsafe. Most likely reason: Packet Missed')
        self.turn_in_quest(quest_number, check_with_failsafe)   