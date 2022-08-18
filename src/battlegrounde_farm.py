import threading
import asyncio
import time
import pyautogui
import random

from models import Item, Quest, Map, Class
from helpers import click
from utils import capture_packets

combo = {'q': 3, 'w': 3, 'e': 25, 'r': 25}

# Item, Quest, Map and Class variables
quest_1_item_1 = Item(27755, 'Battleground E Opponent Defeated', 'Quest Item', 0)
quest_1 = Quest(3992, 'Level 61-75', 10000, 10000, None)
map_1 = Map('battlegrounde')
archfiend = Class(9405, 'ArchFiend', combo)

# Go To Arena and leave Arena coordinates
arena_x, arena_y = 940, 240

# Combo for class
class_combo = ['q', 'w', 'e', 'r']

event_loop_1 = asyncio.new_event_loop()
packet_sniffer_thread = threading.Thread(target=capture_packets, args=[event_loop_1, quest_1_item_1], daemon=True)

def main():
    map_1.join_map(random.randint(1000, 9999))
    
    click(arena_x, arena_y)
    time.sleep(3)
    
    quest_1.accept_quest(5)
    
    click(arena_x, arena_y)
    time.sleep(2)
    
    packet_sniffer_thread.start()
    while True:
        if quest_1_item_1.item_count == 10:
                quest_1_item_1.item_count = 0
                quest_1.turn_in_quest(1)
                break
        archfiend.attack()