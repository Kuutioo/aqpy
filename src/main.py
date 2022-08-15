import os, sys
import random
import pyautogui
import time
import threading
import asyncio
import win32api, win32con
import asyncio
import pyshark

import utils


pyautogui.FAILSAFE = True

event_loop_1 = asyncio.new_event_loop()

item_27755 = 0

item_command = '"addItems","items":{"27755"'

# Go To Arena and leave Arena coordinates
arena_x, arena_y = 940, 240

# Line of the quest in Available Quests tab
quest_line_x, quest_line_y = 440, 290

# Battlegrounde join command
battlegrounde_command = '/join battlegrounde-'

# Combo for class
class_combo = ['q', 'w', 'e', 'r']

# Counter for how many quests has been completed in current session
quest_turn_in_counter = 0

# Boolean value to check if player is in the arena
in_arena = False

# AQW HWND
aqw_hwnd = None

# Click function
def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
    
def quest_item_counter():
    global item_27755
    item_27755 += 1
    print(f'Added 1 quest item. Total count {item_27755}')

def capture_packets(event_loop):
    asyncio.set_event_loop(event_loop)
    capture = pyshark.LiveCapture(interface='Ethernet 3', bpf_filter='tcp port 5588', eventloop=event_loop)
    for packet in capture.sniff_continuously():
        if 'DATA' in str(packet.layers):
            payload = packet.tcp.payload
            payload = payload.replace(':', '')
            decoded_payload = bytes.fromhex(str(payload)).decode('utf-8')
            if item_command in decoded_payload:
                quest_item_counter()
    capture.close()

thread_1 = threading.Thread(target=capture_packets, args=[event_loop_1])

def find_aqw_hwnd():
    global aqw_hwnd
    
    print('Finding AQW HWND...')
    try:
        list_of_pids = utils.find_pid_by_name('Artix')

        if len(list_of_pids) > 0:
            print('Process Found')
            for elem in list_of_pids:
                hwnd_list = utils.get_hwnds_for_pid(elem['pid'])
                pid = elem['pid']
                if len(hwnd_list) > 8:
                    aqw_hwnd = hwnd_list[0]
                    print(f'Found AQW HWND: {aqw_hwnd} from PID: {pid}\n\n')
        else:
            print('No Running Process found with given text')
            sys.exit()
    except:
        print('An error has occurred. Try restarting the application or AQW\n')
        sys.exit()

def start():
    print('Application Starting...\n\n')
    
    find_aqw_hwnd()
    utils.focus_window_hwnd(aqw_hwnd)

    time.sleep(3)
    print('Application Running\n\n')
    
# Function to handle all of the logic required to turn in a quest
def turn_in_quest():
    global quest_turn_in_counter
    
    click(arena_x, arena_y)
    time.sleep(2)
    
    pyautogui.hotkey('l')
    time.sleep(1.5)
    
    click(quest_line_x, quest_line_y)
    time.sleep(1.5)
    
    turn_in_button = pyautogui.locateOnScreen('images/quest_turn_in_button.png')
    
    if turn_in_button != None:
        turn_in_button_x, turn_in_button_y = pyautogui.center(turn_in_button)
        click(turn_in_button_x, turn_in_button_y)
        
        quest_turn_in_counter += 1
        print(f'Quest turned in {quest_turn_in_counter} times\n')
        
        time.sleep(2)

def join_map(map_command, room_number):
    pyautogui.hotkey('enter')
    time.sleep(0.5)
    
    pyautogui.write(map_command + str(room_number))
    time.sleep(0.5)
    
    pyautogui.hotkey('enter')
    time.sleep(3)

def accept_quest(quest_number):
    exclamation_mark = pyautogui.locateOnScreen('images/exclamation_mark.png')
    if exclamation_mark != None:
        exclamation_mark_x, exclamation_mark_y = pyautogui.center(exclamation_mark)
        click(exclamation_mark_x, exclamation_mark_y)
        
        time.sleep(2)
        
        quests_button = pyautogui.locateOnScreen('images/quests_button.png')
        if quests_button != None:
            quests_button_x, quests_button_y = pyautogui.center(quests_button)
            click(quests_button_x, quests_button_y)
            time.sleep(2)
            
            click(300, 248 + (37 * quest_number))
            time.sleep(2)
            
            accept_button = pyautogui.locateOnScreen('images/quest_accept_button.png')
            if accept_button != None:
                accept_button_x, accept_button_y = pyautogui.center(accept_button)
                click(accept_button_x, accept_button_y)
    
# Main loop function of the program    
def main():
    global item_27755
    
    start()
    
    join_map(battlegrounde_command, random.randint(1000, 9999))
    
    click(arena_x, arena_y)
    time.sleep(3)
    
    accept_quest(5)
    time.sleep(3)

    thread_1.start()
    while True:
        click(arena_x, arena_y)
        in_arena = True
        while in_arena:
            for i in class_combo:
                if item_27755 == 10:
                    item_27755 = 0
                    print('Quest Completed')
                    in_arena = False
                    turn_in_quest()
                    break
                pyautogui.hotkey(i)
                time.sleep(1)
                
if __name__ == "__main__":
    os.system('cls')
    main()