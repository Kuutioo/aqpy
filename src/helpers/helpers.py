import win32api, win32con
import time
import re

def click(x, y, wait_time):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
    time.sleep(wait_time)
    
def check_user_input(input):
    if input.isdigit():
        return True
    return False
    
def parse_apybot_file():
    commands = ['CLICK', 'JOIN']

    with open('battlegrounde.apybot') as f:
        list = []
        lines = [line.split() for line in f]
        for line in lines:
            for command in commands:
                if re.search(command, line[0]):
                    arguments = line[1:]
                    list.append(line[0])
                    list.append(arguments)
    return list
                    