import threading
import asyncio
import time
import pyautogui
import random

from models.item import Item
from helpers.helpers import click
from helpers.quest_helpers import *
from utils.network_utils import capture_packets

# Variable to store the Quest Item
item_27755 = Item(27755, 'Battleground E Opponent Defeated', 'Quest Item', 0)

# Go To Arena and leave Arena coordinates
arena_x, arena_y = 940, 240

# Battlegrounde join command
battlegrounde_command = '/join battlegrounde-'

# Combo for class
class_combo = ['q', 'w', 'e', 'r']

# Counter for how many quests has been completed in current session
quest_turn_in_counter = 0

# Boolean value to check if player is in the arena
in_arena = False

event_loop_1 = asyncio.new_event_loop()
packet_sniffer_thread = threading.Thread(target=capture_packets, args=[event_loop_1, item_27755])

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
    
    accept_quest(5)
    time.sleep(3)
    
    click(arena_x, arena_y)
    time.sleep(2)

    main_loop(item_27755)
    
def main_loop(item: Item):
    packet_sniffer_thread.start()
    while True:
        in_arena = True
        while in_arena:
            for ability in class_combo:
                if item.item_count == 10:
                    item.item_count = 0
                    in_arena = False
                    turn_in_quest()
                    break
                pyautogui.hotkey(ability)
                time.sleep(0.9)