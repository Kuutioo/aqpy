import asyncio, pyshark, json
import re

def capture_packets(event_loop):
    asyncio.set_event_loop(event_loop)
    capture = pyshark.LiveCapture(interface='Ethernet', bpf_filter='tcp port 5588', eventloop=event_loop)
    index = 0
    for packet in capture.sniff_continuously(20):
        index += 1
        if 'DATA' in str(packet.layers):
            payload = packet.tcp.payload
            payload = payload.replace(':', '')
            decoded_payload = bytes.fromhex(str(payload)).decode('utf-8')
            if '%' in decoded_payload:
                continue
            text = decoded_payload[33:80]
            print(text)
            # print(re.findall(r'\d+', text))
            
    capture.close()
    
event_loop_1 = asyncio.new_event_loop()

capture_packets(event_loop_1)