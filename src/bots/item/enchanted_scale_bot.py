import threading
import asyncio
import random

from models import Item, Quest, Map, archfiend
from helpers import click
from utils import capture_packets

# Item, Quest and Map variables
enchanted_scale = Item(35957, 'Enchanted Scale', 'Item', 0)

quest_1_item_1 = Item(35956, 'Dracolich Slain', 'Quest Item', 0)
quest_1 = Quest(5294, 'DragonSlayer General Class', 300, 300, [quest_1_item_1], [enchanted_scale])
map_1 = Map('dragontown')

event_loop_1 = asyncio.new_event_loop()
packet_sniffer_thread = threading.Thread(target=capture_packets, args=[event_loop_1, quest_1_item_1], daemon=True)

quest_1_fail_safe_thread = threading.Thread(target=quest_1.check_if_quest_done, args=[1, 30], daemon=True)

def main():
    map_1.join_map(random.randint(1000, 9999))
    
    click(830, 355, 1)
    
    click(830, 715, 1)
    
    click(750, 715, 1)
    
    quest_1.accept_quest(1)
    
    click(1000, 470, 1.5)
    
    click(1800, 675, 2)

    packet_sniffer_thread.start()
    quest_1_fail_safe_thread.start()
    while True:
        if quest_1_item_1.item_count == 12:
                quest_1_fail_safe_thread = None
            
                quest_1.turn_in_quest(1)
                
                quest_1_fail_safe_thread = threading.Thread(target=quest_1.check_if_quest_done, args=[1, 30], daemon=True)
                quest_1_fail_safe_thread.start()
        archfiend.attack()