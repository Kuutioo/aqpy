import threading
import asyncio
import time
import pyautogui
import random

from models import Item, Quest
from helpers import click
from utils import capture_packets

# Item and Quest variables
quest_1_item_1 = Item(27755, 'Battleground E Opponent Defeated', 'Quest Item', 0)
quest_1 = Quest(3992, 'Level 61-75', 10000, 10000, None)

# Go To Arena and leave Arena coordinates
arena_x, arena_y = 940, 240

# Battlegrounde join command
battlegrounde_command = '/join battlegrounde-'

# Combo for class
class_combo = ['q', 'w', 'e', 'r']

event_loop_1 = asyncio.new_event_loop()
packet_sniffer_thread = threading.Thread(target=capture_packets, args=[event_loop_1, quest_1_item_1])

def join_map(map_command, room_number):
    pyautogui.hotkey('enter')
    time.sleep(0.5)
    
    pyautogui.write(map_command + str(room_number))
    time.sleep(0.5)
    
    pyautogui.hotkey('enter')
    time.sleep(3)
    
def start():
    join_map(battlegrounde_command, random.randint(1000, 9999))
    
    click(arena_x, arena_y)
    time.sleep(3)
    
    quest_1.accept_quest(5)
    
    click(arena_x, arena_y)
    time.sleep(2)

    main_loop(quest_1_item_1)
    
def main_loop(item: Item):
    packet_sniffer_thread.start()
    while True:
        for ability in class_combo:
            if item.item_count == 10:
                item.item_count = 0
                quest_1.turn_in_quest(1)
                break
            pyautogui.hotkey(ability)
            time.sleep(0.9)