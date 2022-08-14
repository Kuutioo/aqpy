import psutil
import win32process
import win32gui
import time

import utils

'''
time.sleep(2)

window = win32gui.GetForegroundWindow()
tid, pid = win32process.GetWindowThreadProcessId(window)
active_window_path = psutil.Process(pid).exe()

print(window)
print(tid, pid)
print(active_window_path)
'''

list_of_pids = utils.find_pid_by_name('Artix')

if len(list_of_pids) > 0:
    print('Process Exists | PID and other details are')
    for elem in list_of_pids:
        # print((elem['pid'], elem['name']))
        pid = elem['pid']
        hwnd_list = utils.get_hwnds_for_pid(elem['pid'])
        print(hwnd_list)
        if len(hwnd_list) > 8:
            if win32gui.IsWindow(hwnd_list[2]) and win32gui.IsWindowEnabled(hwnd_list[2]):
                print('Is window')
                
            # IMPORTANT MIGHT ALSO BE hwnd_list[5]
            print(f'Found AQW HWND: {hwnd_list[0]} from PID: {pid}\n\n')
else:
    print('No Running Process found with given text')
    