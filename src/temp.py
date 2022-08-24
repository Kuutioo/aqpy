import asyncio, pyshark, json
from jsonstream import loads

def capture_packets(event_loop):
    last_packet = None
    
    item_id = 27756
    item_id_2 = 598
    
    asyncio.set_event_loop(event_loop)
    capture = pyshark.LiveCapture(interface='Ethernet', bpf_filter='tcp port 5588', eventloop=event_loop)
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
                        items = o.get('items').get(str(item_id))
                        if items == None:
                            continue
                        i_qty = items.get('iQty')
                        i_qty_now = items.get('iQtyNow')
                        print(i_qty)
                        print(i_qty_now)
                                   
            except json.decoder.JSONDecodeError:
                last_packet = decoded_payload
                
            
    capture.close()
       
event_loop_1 = asyncio.new_event_loop()

capture_packets(event_loop_1)