from os import kill
import time
import pyautogui
import threading
import sys
import ctypes
from threading import Thread

class Ability:
    def __init__(self, name: str, cooldown: int):
        self.name = name
        self.cooldown = cooldown
        
class Class:
    def __init__(self, id: int, name: str, combo):
        self.id = id
        self.name = name
        self.combo = combo
        
        self.ability_cooldowns = list(combo.values())
        
        self.threads = [
            Thread(target=self.ability_cooldown, args=[self.ability_cooldowns[0], 0], daemon=True),
            Thread(target=self.ability_cooldown, args=[self.ability_cooldowns[1], 1], daemon=True),
            Thread(target=self.ability_cooldown, args=[self.ability_cooldowns[2], 2], daemon=True)    
        ]
        
                
    def attack(self):
        for index, (ability, cooldown) in enumerate(self.combo.items()):
            time.sleep(0.1)
            if self.threads[index] == None:
                self.threads[index] = Thread(target=self.ability_cooldown, args=[self.ability_cooldowns[index], index], daemon=True)
            if self.is_ability_on_cooldown(self.threads[index]):
                continue
            print(f'Pressed {ability}')
            pyautogui.hotkey(ability)
            self.threads[index].start()
            time.sleep(1)
                
    
    def ability_cooldown(self, cooldown, thread_index):
        # print(f'Thread Index: {thread_index}')
        time.sleep(cooldown)
        # print(f'Ability ready to use. Thread stopping')     
        self.threads[thread_index] = None       
        
    def is_ability_on_cooldown(self, thread: Thread):
        if thread.is_alive():
            return True
        return False