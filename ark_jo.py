import cv2
import time
import random
import win32api
import win32con
import win32ui
import win32gui

hwnd = win32gui.FindWindow(None, "雷电模拟器-1")
hwnd = win32gui.FindWindowEx(hwnd, None, None, None)


def click(x, y):
    long_position = win32api.MAKELONG(x, y)  # 模拟鼠标指针 传送到指定坐标
    win32api.SendMessage(hwnd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, long_position)  # 模拟鼠标按下
    win32api.SendMessage(hwnd, win32con.WM_LBUTTONUP, win32con.MK_LBUTTON, long_position)  # 模拟鼠标弹起
    time.sleep(3)


def screenshot(hWnd):
    try:
        left, top, right, bot = win32gui.GetWindowRect(hWnd)
        width = right - left
        height = bot - top
        hWndDC = win32gui.GetWindowDC(hWnd)
        mfcDC = win32ui.CreateDCFromHandle(hWndDC)
        saveDC = mfcDC.CreateCompatibleDC()
        saveBitMap = win32ui.CreateBitmap()
        saveBitMap.CreateCompatibleBitmap(mfcDC, width, height)
        saveDC.SelectObject(saveBitMap)
        saveDC.BitBlt((0, 0), (width, height), mfcDC, (0, 0), win32con.SRCCOPY)
        saveBitMap.SaveBitmapFile(saveDC, "screenshot.png")
        win32gui.DeleteObject(saveBitMap.GetHandle())
        saveDC.DeleteDC()
        mfcDC.DeleteDC()
        win32gui.ReleaseDC(hWnd, hWndDC)
    except:
        screenshot()


def getposition(path, minval=0.1):
    screenshot(hwnd)
    img = cv2.imread('screenshot.png', 0)
    template = cv2.imread(path, 0)
    h, w = template.shape[:2]
    res = cv2.matchTemplate(img, template, cv2.TM_SQDIFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    # print(min_val)
    if min_val < minval:
        top_left = min_loc
        return top_left[0] + random.randint(0, w), top_left[1] + random.randint(0, h)
    else:
        return None

n1 = 0
n = 0
c = int(input())
while True:
    p0 = getposition('images/xingdong0.png', 0.0242)
    p1 = getposition('images/xingdong1.png', 0.018)
    p3 = getposition('images/queding.png', 0.000006)
    p4 = getposition('images/tiaojian.png', 0.0005)
    p5 = getposition('images/jieshu.png', 0.015)
    if p0 and n1 == 0:
        n += 1
        print(n)
        click(p0[0], p0[1])
        n1 += 1
    if p1:
        click(p1[0], p1[1])
    if p5:
        n1 = 0
        while True:
            p5 = getposition('images/jieshu.png', 0.015)
            if p5:
                click(p5[0], p5[1])
            else:
                break
        if n == c:
            print(f"{n}  break")
            break
    if p3 and p4:
        click(p3[0], p3[1])
        time.sleep(10)
