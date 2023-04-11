from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con


def click():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
    time.sleep(0.45)

while keyboard.is_pressed('c') == False:
    time.sleep(3)
    num_clicks = 1
    for i in range(num_clicks):
        pyautogui.click(700, 480)
        time.sleep(0.7)
        start = pyautogui.locateOnScreen('quick-sell.png', confidence=0.9)
        if start is not None:
            print("Sold!")
            time.sleep(0.45)
            pyautogui.moveTo(start)
            click()
    else:
        print("Can't sell!")
        time.sleep(0.5)
        num_clicks = 1
    for i in range(num_clicks):
        pyautogui.click(770, 480)
        time.sleep(0.7)
        start = pyautogui.locateOnScreen('quick-sell.png', confidence=0.9)
        if start is not None:
            print("Sold!")
            time.sleep(0.45)
            pyautogui.moveTo(start)
            click()
    else:
        print("Can't sell!")
        time.sleep(0.5)
        num_clicks = 1
    for i in range(num_clicks):
        pyautogui.click(840, 480)
        time.sleep(0.7)
        start = pyautogui.locateOnScreen('quick-sell.png', confidence=0.9)
        if start is not None:
            print("Sold!")
            time.sleep(0.45)
            pyautogui.moveTo(start)
            click()
    else:
        print("Can't sell!")
        time.sleep(0.5)
        num_clicks = 1
    for i in range(num_clicks):
        pyautogui.click(910, 480)
        time.sleep(0.7)
        start = pyautogui.locateOnScreen('quick-sell.png', confidence=0.9)
        if start is not None:
            print("Sold!")
            time.sleep(0.45)
            pyautogui.moveTo(start)
            click()
    else:
        print("Can't sell!")
        time.sleep(0.5)
        num_clicks = 1
    for i in range(num_clicks):
        pyautogui.click(980, 480)
        time.sleep(0.7)
        start = pyautogui.locateOnScreen('quick-sell.png', confidence=0.9)
        if start is not None:
            print("Sold!")
            time.sleep(0.45)
            pyautogui.moveTo(start)
            click()
    else:
        print("Can't sell!")
        time.sleep(0.5)
        num_clicks = 1
    for i in range(num_clicks):
        pyautogui.click(700, 550)
        time.sleep(0.7)
        start = pyautogui.locateOnScreen('quick-sell.png', confidence=0.9)
        if start is not None:
            print("Sold!")
            time.sleep(0.45)
            pyautogui.moveTo(start)
            click()
    else:
        print("Can't sell!")
        time.sleep(0.5)
        num_clicks = 1
    for i in range(num_clicks):
        pyautogui.click(780, 550)
        time.sleep(0.7)
        start = pyautogui.locateOnScreen('quick-sell.png', confidence=0.9)
        if start is not None:
            print("Sold!")
            time.sleep(0.45)
            pyautogui.moveTo(start)
            click()
    else:
        print("Can't sell!")
        time.sleep(0.5)
        num_clicks = 1
    for i in range(num_clicks):
        pyautogui.click(840, 550)
        time.sleep(0.7)
        start = pyautogui.locateOnScreen('quick-sell.png', confidence=0.9)
        if start is not None:
            print("Sold!")
            time.sleep(0.45)
            pyautogui.moveTo(start)
            click()
    else:
        print("Can't sell!")
        time.sleep(0.5)
        num_clicks = 1
    for i in range(num_clicks):
        pyautogui.click(910, 550)
        time.sleep(0.7)
        start = pyautogui.locateOnScreen('quick-sell.png', confidence=0.9)
        if start is not None:
            print("Sold!")
            time.sleep(0.45)
            pyautogui.moveTo(start)
            click()
    else:
        print("Can't sell!")
        time.sleep(0.5)
        num_clicks = 1
    for i in range(num_clicks):
        pyautogui.click(980, 550)
        time.sleep(0.7)
        start = pyautogui.locateOnScreen('quick-sell.png', confidence=0.9)
        if start is not None:
            print("Sold!")
            time.sleep(0.45)
            pyautogui.moveTo(start)
            click()
    else:
        print("Can't sell!")
        time.sleep(0.5)
        num_clicks = 1
    for i in range(num_clicks):
        pyautogui.click(700, 620)
        time.sleep(0.7)
        start = pyautogui.locateOnScreen('quick-sell.png', confidence=0.9)
        if start is not None:
            print("Sold!")
            time.sleep(0.45)
            pyautogui.moveTo(start)
            click()
    else:
        print("Can't sell!")
        time.sleep(0.5)
        num_clicks = 1
    for i in range(num_clicks):
        pyautogui.click(770, 620)
        time.sleep(0.7)
        start = pyautogui.locateOnScreen('quick-sell.png', confidence=0.9)
        if start is not None:
            print("Sold!")
            time.sleep(0.45)
            pyautogui.moveTo(start)
            click()
    else:
        print("Can't sell!")
        time.sleep(0.5)
        num_clicks = 1
    for i in range(num_clicks):
        pyautogui.click(840, 620)
        time.sleep(0.7)
        start = pyautogui.locateOnScreen('quick-sell.png', confidence=0.9)
        if start is not None:
            print("Sold!")
            time.sleep(0.45)
            pyautogui.moveTo(start)
            click()
    else:
        print("Can't sell!")
        time.sleep(0.5)
        num_clicks = 1
    for i in range(num_clicks):
        pyautogui.click(910, 620)
        time.sleep(0.7)
        start = pyautogui.locateOnScreen('quick-sell.png', confidence=0.9)
        if start is not None:
            print("Sold!")
            time.sleep(0.45)
            pyautogui.moveTo(start)
            click()
    else:
        print("Can't sell!")
        time.sleep(0.5)
        num_clicks = 1
    for i in range(num_clicks):
        pyautogui.click(980, 620)
        time.sleep(0.7)
        start = pyautogui.locateOnScreen('quick-sell.png', confidence=0.9)
        if start is not None:
            print("Sold!")
            time.sleep(0.45)
            pyautogui.moveTo(start)
            click()
    else:
        print("Can't sell!")
        time.sleep(0.5)
        num_clicks = 1
    for i in range(num_clicks):
        pyautogui.click(700, 690)
        time.sleep(0.7)
        start = pyautogui.locateOnScreen('quick-sell.png', confidence=0.9)
        if start is not None:
            print("Sold!")
            time.sleep(0.45)
            pyautogui.moveTo(start)
            click()
    else:
        print("Can't sell!")
        time.sleep(0.5)
        num_clicks = 1
    for i in range(num_clicks):
        pyautogui.click(770, 690)
        time.sleep(0.7)
        start = pyautogui.locateOnScreen('quick-sell.png', confidence=0.9)
        if start is not None:
            print("Sold!")
            time.sleep(0.45)
            pyautogui.moveTo(start)
            click()
    else:
        print("Can't sell!")
        time.sleep(0.5)
        num_clicks = 1
    for i in range(num_clicks):
        pyautogui.click(840, 690)
        time.sleep(0.7)
        start = pyautogui.locateOnScreen('quick-sell.png', confidence=0.9)
        if start is not None:
            print("Sold!")
            time.sleep(0.45)
            pyautogui.moveTo(start)
            click()
    else:
        print("Can't sell!")
        time.sleep(0.5)
        num_clicks = 1
    for i in range(num_clicks):
        pyautogui.click(910, 690)
        time.sleep(0.7)
        start = pyautogui.locateOnScreen('quick-sell.png', confidence=0.9)
        if start is not None:
            print("Sold!")
            time.sleep(0.45)
            pyautogui.moveTo(start)
            click()
    else:
        print("Can't sell!")
        time.sleep(0.5)
        num_clicks = 1
    for i in range(num_clicks):
        pyautogui.click(980, 690)
        time.sleep(0.7)
        start = pyautogui.locateOnScreen('quick-sell.png', confidence=0.9)
        if start is not None:
            print("Sold!")
            time.sleep(0.45)
            pyautogui.moveTo(start)
            click()
    else:
        print("Can't sell!")
        time.sleep(0.5)
        num_clicks = 1
    for i in range(num_clicks):
        pyautogui.click(700, 760)
        time.sleep(0.7)
        start = pyautogui.locateOnScreen('quick-sell.png', confidence=0.9)
        if start is not None:
            print("Sold!")
            time.sleep(0.45)
            pyautogui.moveTo(start)
            click()
    else:
        print("Can't sell!")
        time.sleep(0.5)
        num_clicks = 1
    for i in range(num_clicks):
        pyautogui.click(770, 760)
        time.sleep(0.7)
        start = pyautogui.locateOnScreen('quick-sell.png', confidence=0.9)
        if start is not None:
            print("Sold!")
            time.sleep(0.45)
            pyautogui.moveTo(start)
            click()
    else:
        print("Can't sell!")
        time.sleep(0.5)
        num_clicks = 1
    for i in range(num_clicks):
        pyautogui.click(840, 760)
        time.sleep(0.7)
        start = pyautogui.locateOnScreen('quick-sell.png', confidence=0.9)
        if start is not None:
            print("Sold!")
            time.sleep(0.45)
            pyautogui.moveTo(start)
            click()
    else:
        print("Can't sell!")
        time.sleep(0.5)
        num_clicks = 1
    for i in range(num_clicks):
        pyautogui.click(910, 760)
        time.sleep(0.7)
        start = pyautogui.locateOnScreen('quick-sell.png', confidence=0.9)
        if start is not None:
            print("Sold!")
            time.sleep(0.45)
            pyautogui.moveTo(start)
            click()
    else:
        print("Can't sell!")
        time.sleep(0.5)
        num_clicks = 1
    for i in range(num_clicks):
        pyautogui.click(980, 760)
        time.sleep(0.7)
        start = pyautogui.locateOnScreen('quick-sell.png', confidence=0.9)
        if start is not None:
            print("Sold!")
            time.sleep(0.45)
            pyautogui.moveTo(start)
            click()
    else:
        print("Can't sell!")
        time.sleep(0.5)
        num_clicks = 1
    for i in range(num_clicks):
        pyautogui.click(970, 805)
        time.sleep(0.3)
