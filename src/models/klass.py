import time
import pyautogui
import threading
import sys
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
        
        ability_cooldowns = list(combo.values())
        
        self.threads = [
            Thread(target=self.ability_cooldown, args=[ability_cooldowns[0], 0], daemon=True),
            Thread(target=self.ability_cooldown, args=[ability_cooldowns[1], 1], daemon=True),
            Thread(target=self.ability_cooldown, args=[ability_cooldowns[2], 2], daemon=True),
            Thread(target=self.ability_cooldown, args=[ability_cooldowns[3], 3], daemon=True)    
        ]
        
    def attack(self):
        for index, (ability, cooldown) in enumerate(self.combo.items()):
            print(index)
            if self.is_ability_on_cooldown(self.threads[index]): break
            pyautogui.hotkey(ability)
            self.threads[index].start()
            time.sleep(0.8)
                
    
    def ability_cooldown(self, cooldown, thread_index):
        thread = threading.currentThread()
        for _ in range(cooldown):
            time.sleep(1)
        print(f'Ability ready to use. Thread stopping')
            
        
    def is_ability_on_cooldown(self, thread: Thread):
        if thread.is_alive():
            return True
        return False