import time
import pyautogui
from threading import Thread

        
class Class:
    def __init__(self, id: int, name: str, combo):
        self.id = id
        self.name = name
        self.combo = combo
        
        self.ability_cooldowns = list(combo.values())
        self.threads = []
        
        for index in range(len(self.ability_cooldowns)):
            self.threads.append(Thread(target=self.ability_cooldown, args=[self.ability_cooldowns[index], index], daemon=True))
        
    def attack(self):
        for index, (ability, cooldown) in enumerate(self.combo.items()):
            time.sleep(0.1)
            if self.threads[index] == None:
                self.threads[index] = Thread(target=self.ability_cooldown, args=[self.ability_cooldowns[index], index], daemon=True)
            if self.is_ability_on_cooldown(self.threads[index]):
                continue
            pyautogui.hotkey(ability)
            self.threads[index].start()
            time.sleep(0.95)
                
    def ability_cooldown(self, cooldown, thread_index):
        time.sleep(cooldown)
        self.threads[thread_index] = None       
        
    def is_ability_on_cooldown(self, thread: Thread):
        if thread.is_alive():
            return True
        return False