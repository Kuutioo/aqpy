import asyncio, pyshark, json

from jsonstream import loads

from models.item import Item

def capture_packets(event_loop, item_list):
    last_packet = None
    
    asyncio.set_event_loop(event_loop)
    capture = pyshark.LiveCapture(interface='Ethernet', bpf_filter='tcp port 5588', eventloop=event_loop)
    for packet in capture.sniff_continuously():
        if 'DATA' in str(packet.layers):
            payload = packet.tcp.payload
            payload = payload.replace(':', '').replace('00', '')
            decoded_payload = bytes.fromhex(payload).decode('UTF-8')
            
            if '%' in decoded_payload:
                continue
            
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
    