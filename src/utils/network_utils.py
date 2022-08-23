import asyncio, pyshark

from jsonstream import loads

from models.item import Item

def capture_packets(event_loop, item: Item):
    asyncio.set_event_loop(event_loop)
    capture = pyshark.LiveCapture(interface='Ethernet', bpf_filter='tcp port 5588', eventloop=event_loop)
    for packet in capture.sniff_continuously():
        if 'DATA' in str(packet.layers):
            payload = packet.tcp.payload
            payload = payload.replace(':', '')
            decoded_payload = bytes.fromhex(str(payload)).decode('ASCII')
            
            if '%' in decoded_payload:
                continue
            
            it = loads(decoded_payload)
            for element in list(it):
                print(element)
                if item.add_item_command() in element:
                    item.add_item_count(1)
                
    capture.close()
    