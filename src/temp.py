import asyncio, pyshark, json
import enum
import re
from jsonstream import loads

def capture_packets(event_loop):
    asyncio.set_event_loop(event_loop)
    capture = pyshark.LiveCapture(interface='Ethernet', bpf_filter='tcp port 5588', eventloop=event_loop)
    for packet in capture.sniff_continuously(50):
        if 'DATA' in str(packet.layers):
            payload = packet.tcp.payload
            payload = payload.replace(':', '').replace('00', '')
            decoded_payload = bytes.fromhex(payload).decode('ASCII')
            
            if '%' in decoded_payload:
                continue
            it = loads(decoded_payload)
            for element in list(it):
                # element = element
                print(element)
                '''b = element['b']
                o = b['o']
                cmd = o['cmd']
                if cmd == None:
                    continue
                if cmd == 'addItems':
                    print('Command is add items')'''
                #print(cmd)
            
    capture.close()
       
event_loop_1 = asyncio.new_event_loop()

capture_packets(event_loop_1)