import threading
import asyncio
import random

from models import Item, Quest, Map, archfiend
from helpers import click
from utils import capture_packets

# Item, Quest and Map variables
quest_1_item_1 = Item(27755, 'Battleground E Opponent Defeated', 'Quest Item', 0)
quest_1 = Quest(3992, 'Level 61-75', 10000, 10000, 35, [quest_1_item_1], None)
map_1 = Map('battlegrounde')

event_loop_1 = asyncio.new_event_loop()
packet_sniffer_thread = threading.Thread(target=capture_packets, args=[event_loop_1, quest_1_item_1], daemon=True)

def main():
    global quest_1_fail_safe_thread
    
    map_1.join_map(random.randint(1000, 9999))
    
    click(940, 240, 2)
    
    click(1300, 285, 1)
    
    click(950, 720, 1)
    
    quest_1.accept_quest(5)
    
    click(940, 240, 2)
    
    packet_sniffer_thread.start()

    while True:
        if quest_1_item_1.item_count == 10:
                quest_1.turn_in_quest(1, False)
        archfiend.attack()