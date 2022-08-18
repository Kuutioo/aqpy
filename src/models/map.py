import time
import pyautogui

class Map:    
    def __init__(self, name: str):
        self.name = name
        
    def join_map(self, room_number):
        pyautogui.hotkey('enter')
        time.sleep(0.5)
        
        pyautogui.write(f'/join {self.name}-{room_number}')
        time.sleep(0.5)
        
        pyautogui.hotkey('enter')
        time.sleep(3)