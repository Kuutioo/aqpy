import os, sys
import pyautogui
import time

import battlegrounde_farm
import utils.process_utils as process_utils

pyautogui.FAILSAFE = True

# AQW HWND
aqw_hwnd = None

def find_aqw_hwnd():
    global aqw_hwnd
    
    print('Finding AQW HWND...')
    try:
        list_of_pids = process_utils.find_pid_by_name('Artix')

        if len(list_of_pids) > 0:
            print('Process Found')
            for elem in list_of_pids:
                hwnd_list = process_utils.get_hwnds_for_pid(elem['pid'])
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
    process_utils.focus_window_hwnd(aqw_hwnd)

    time.sleep(3)
    print('Application Running\n\n')
    
    
# Main function of the program    
def main():    
    start()
    battlegrounde_farm.start()    
          
if __name__ == "__main__":
    os.system('cls')
    main()