import ctypes as c
from ctypes import wintypes as w

pid = 13796  # Minesweeper

k32 = c.WinDLL('kernel32', use_last_error=True)

OpenProcess = k32.OpenProcess
OpenProcess.argtypes = w.DWORD,w.BOOL,w.DWORD
OpenProcess.restype = w.HANDLE

ReadProcessMemory = k32.ReadProcessMemory
ReadProcessMemory.argtypes = w.HANDLE,w.LPCVOID,w.LPVOID,c.c_size_t,c.POINTER(c.c_size_t)
ReadProcessMemory.restype = w.BOOL

CloseHandle = k32.CloseHandle
CloseHandle.argtypes = [w.HANDLE]
CloseHandle.restype = w.BOOL

processHandle = OpenProcess(0x10, False, pid)

addr = 0x1AE08E051B0  # Minesweeper.exe module base address
data = c.c_ulonglong()
bytesRead = c.c_ulonglong()
result = ReadProcessMemory(processHandle, addr, c.byref(data), c.sizeof(data), c.byref(bytesRead))
e = c.get_last_error()

print('result: {}, err code: {}, bytesRead: {}'.format(result,e,bytesRead.value))
print('data: {:016X}h'.format(data.value))


CloseHandle(processHandle)