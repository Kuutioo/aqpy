import os, sys
import pyautogui
import time

import battlegrounde_farm
from utils import focus_window_hwnd, find_pid_by_name, get_hwnds_for_pid

pyautogui.FAILSAFE = True

# AQW HWND
aqw_hwnd = None

def find_aqw_hwnd():
    global aqw_hwnd
    
    print('Finding AQW HWND...')
    try:
        list_of_pids = find_pid_by_name('Artix')

        if len(list_of_pids) > 0:
            print('Process Found')
            for elem in list_of_pids:
                hwnd_list = get_hwnds_for_pid(elem['pid'])
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
    focus_window_hwnd(aqw_hwnd)

    time.sleep(3)
    print('Application Running')
    print('Press CTRL + C to exit\n\n')
    
    
# Main function of the program    
def main():    
    os.system('cls')
    
    start()
    battlegrounde_farm.start()    
          
if __name__ == "__main__":
    main()