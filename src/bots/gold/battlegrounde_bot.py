import threading
import asyncio
import random

from models import Item, Quest, Map, archfiend_farm
from helpers import click
from utils import capture_packets

# Item, Quest and Map variables
quest_1_item_1 = Item(27755, 'Battleground E Opponent Defeated', 'Quest Item', 0)
quest_2_item_1 = Item(27756, 'HonorHall Opponent Defeated', 'Quest Item', 0)

quest_1 = Quest(3992, 'Level 61-75', 10000, 10000, 35, [quest_1_item_1], None)
quest_2 = Quest(3993, 'Hall of Honors', 20000, 20000, 60, [quest_2_item_1], None)

map_1 = Map('battlegrounde')
map_2 = Map('honorhall')

event_loop_1 = asyncio.new_event_loop()
packet_sniffer_thread = threading.Thread(target=capture_packets, args=[event_loop_1, [quest_2_item_1]], daemon=True)

def main():    
    map_2.join_map(random.randint(1000, 9999))
        
    click(1300, 285, 1)
    
    click(950, 720, 1)
    
    quest_2.accept_quest(6)
    
    click(940, 240, 2)
    
    packet_sniffer_thread.start()

    while True:
        if quest_2_item_1.item_count == 10:
                quest_2.turn_in_quest(1, False)
        archfiend_farm.attack()