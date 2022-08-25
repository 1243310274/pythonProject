import cv2
import time
import random
import win32api
import win32con
import win32ui
import win32gui


hwnd = win32gui.FindWindow(None, "雷电模拟器-1")
hwnd = win32gui.FindWindowEx(hwnd, None, None, None)
left, top, right, bot = win32gui.GetWindowRect(hwnd)
width = right - left
height = bot - top

t1= time.time()
hWndDC = win32gui.GetWindowDC(hwnd)
mfcDC = win32ui.CreateDCFromHandle(hWndDC)
saveDC = mfcDC.CreateCompatibleDC()
saveBitMap = win32ui.CreateBitmap()
saveBitMap.CreateCompatibleBitmap(mfcDC,width,height)
saveDC.SelectObject(saveBitMap)
saveDC.BitBlt((0,0), (width,height), mfcDC, (0, 0), win32con.SRCCOPY)
t=time.time()-t1
print(t)
saveBitMap.SaveBitmapFile(saveDC, "screenshot.png")
win32gui.DeleteObject(saveBitMap.GetHandle())
saveDC.DeleteDC()
mfcDC.DeleteDC()
win32gui.ReleaseDC(hwnd, hWndDC)