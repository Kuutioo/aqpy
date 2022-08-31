import threading
import asyncio
import random

from models import Item, Quest, Map, archfiend_farm
from helpers import click
from utils import capture_packets

event_loop_1 = asyncio.new_event_loop()
packet_sniffer_thread = threading.Thread(target=capture_packets, args=[event_loop_1], daemon=True)

def main():
    packet_sniffer_thread.start()
    
    while True:
        archfiend_farm.attack()