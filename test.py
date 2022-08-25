import cv2
import time
import random
import win32api
import win32con
import win32ui
import win32gui


hwnd = win32gui.FindWindow(None, "雷电模拟器-1")
hwnd = win32gui.FindWindowEx(hwnd, None, None, None)
img0 = cv2.imread("images/xingdong0.png", 0)

def click(x, y):
    long_position = win32api.MAKELONG(x, y)  # 模拟鼠标指针 传送到指定坐标
    win32api.SendMessage(hwnd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, long_position)  # 模拟鼠标按下
    win32api.SendMessage(hwnd, win32con.WM_LBUTTONUP, win32con.MK_LBUTTON, long_position)  # 模拟鼠标弹起


def screenshot(hWnd):
    try:
        left, top, right, bot = win32gui.GetWindowRect(hWnd)
        width = right - left
        height = bot - top
        hWndDC = win32gui.GetWindowDC(hWnd)
        mfcDC = win32ui.CreateDCFromHandle(hWndDC)
        saveDC = mfcDC.CreateCompatibleDC()
        saveBitMap = win32ui.CreateBitmap()
        saveBitMap.CreateCompatibleBitmap(mfcDC,width,height)
        saveDC.SelectObject(saveBitMap)
        saveDC.BitBlt((0,0), (width,height), mfcDC, (0, 0), win32con.SRCCOPY)
        saveBitMap.SaveBitmapFile(saveDC, "screenshot.png")
        win32gui.DeleteObject(saveBitMap.GetHandle())
        saveDC.DeleteDC()
        mfcDC.DeleteDC()
        win32gui.ReleaseDC(hWnd, hWndDC)
    except:
        screenshot(hwnd)


def getposition(img, minval=0.1):
    screenshot(hwnd)
    template = cv2.imread('screenshot.png', 0)
    h, w = img.shape[:2]
    res = cv2.matchTemplate(template, img, cv2.TM_SQDIFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    print(min_val)



# while True:
#     getposition("images/tiaojian.png")



# while True:
t1=time.time()
getposition(img0)
t=time.time()-t1
print(t)
    # screenshot(hwnd)
    # time.sleep(0.01)
    # img = cv2.imread("screenshot.png",0)
    # cv2.imshow("screenshot",img)
    # if cv2.waitKey(10)& 0xFF ==27:
    #     break


