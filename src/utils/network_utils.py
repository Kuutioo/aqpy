import asyncio, pyshark

from models.item import Item

def capture_packets(event_loop, item: Item):
    asyncio.set_event_loop(event_loop)
    capture = pyshark.LiveCapture(interface='Ethernet 3', bpf_filter='tcp port 5588', eventloop=event_loop)
    for packet in capture.sniff_continuously():
        if 'DATA' in str(packet.layers):
            payload = packet.tcp.payload
            payload = payload.replace(':', '')
            decoded_payload = bytes.fromhex(str(payload)).decode('utf-8')
            item_command = item.add_item_command()
            if item_command in decoded_payload:
                item.add_item_count(1)
    capture.close()