import sys
import win32gui, win32con, win32process
import psutil

# Focus a window using its HWND
def focus_window_hwnd(handle):
    def callback(hwnd, list_to_append):
        list_to_append.append((hwnd, win32gui.GetWindowText(hwnd)))

    window_list = []
    win32gui.EnumWindows(callback, window_list)
    for hwnd in window_list:
        if handle == hwnd[0]:
            # IMPORTANT MIGHT ALSO BE HWND[5] IN SOME SCENARIOS
            win32gui.ShowWindow(hwnd[0], win32con.SW_MAXIMIZE)
            win32gui.SetForegroundWindow(hwnd[0])
            break

# Get HWND for ProcessID        
def get_hwnds_for_pid(pid):
    def callback(hwnd, hwnds):
        _, found_pid = win32process.GetWindowThreadProcessId(hwnd)

        if found_pid == pid:
            hwnds.append(hwnd)
        return True
    hwnds = []
    win32gui.EnumWindows(callback, hwnds)
    return hwnds 

def find_pid_by_name(process_name):
    list_of_process_objects = []
    for proc in psutil.process_iter():
       try:
           pinfo = proc.as_dict(attrs=['pid', 'name'])
           if process_name.lower() in pinfo['name'].lower() :
               list_of_process_objects.append(pinfo)
       except (psutil.NoSuchProcess, psutil.AccessDenied , psutil.ZombieProcess) :
           pass
    return list_of_process_objects


def find_aqw_hwnd():
    aqw_hwnd = None
    
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
        
    return aqw_hwnd