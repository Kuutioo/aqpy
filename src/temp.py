import asyncio, pyshark, json
from jsonstream import loads
from models import Item

def capture_packets(event_loop, item_list):
    last_packet = None
    
    asyncio.set_event_loop(event_loop)
    capture = pyshark.LiveCapture(interface='Ethernet 3', bpf_filter='tcp port 5588', eventloop=event_loop)
    for packet in capture.sniff_continuously():
        if 'DATA' in str(packet.layers):
            payload = packet.tcp.payload
            payload = payload.replace(':', '').replace('00', '')
            decoded_payload = bytes.fromhex(payload).decode('UTF-8')
            
            if '%' in decoded_payload:
                continue
            
            # print(decoded_payload)
            try:
                if last_packet != None:
                    decoded_payload = last_packet + decoded_payload
                    last_packet = None
                it = loads(decoded_payload)
                for element in list(it):
                    o = element['b']['o']
                    command = o['cmd']
                    if command == 'addItems':
                        for item in item_list:
                            items = o.get('items').get(str(item.id))
                            if items == None:
                                continue
                            i_qty = items.get('iQty')
                            if item.category == 'Quest Item':
                                item.add_item_count(int(i_qty))
                            elif item.category == 'Item':
                                i_qty_now = items.get('iQtyNow')
                                item.display_count(int(i_qty_now))
                    if command == 'dropItem':
                        for item in item_list:
                            items = o.get('items').get(str(item.id))
                            if items == None:
                                continue
                            if item.category == 'Item':
                                item.alert_drop()
            except json.decoder.JSONDecodeError:
                last_packet = decoded_payload
                
            
    capture.close()
       
test_item = Item(35998, 'Slayer Helm', 'Item', 0)
       
event_loop_1 = asyncio.new_event_loop()

capture_packets(event_loop_1, [test_item])