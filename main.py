from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

import win32gui

from WindowManager import WindowManager

def click(x: int, y: int):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.05)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

def clickMessageBox(currentWindow):
    # Copied with modifications from https://stackoverflow.com/questions/7142342/get-window-position-size-with-python
    rect = win32gui.GetWindowRect(currentWindow)
    x = rect[0]
    y = rect[1]
    width = rect[2] - x
    height = rect[3] - y

    desired_x = x + int(width / 2)
    desired_y = y + int(height * 0.94)

    click(desired_x, desired_y)

iterations = 0

def messageLogic():
    time.sleep(interval)

    if addMessageSuffix:
        if useRandomSuffix:
            random_bits = hex(random.getrandbits(128))[2:-1]
            keyboard.write(f"{phrase} {random_bits}")
        else:
            keyboard.write(f"{phrase} {iterations + 1} / {maxIterations}")
    else:
        keyboard.write(phrase)

    time.sleep(0.05)
    pyautogui.press("enter")

intervalLimit = 0.4

def messageFunction():
    if interval < intervalLimit:
        print(f"WARNING: interval of {intervalLimit} seconds or less used. Please note Discord may prompt you to enter the chill zone, and some messages may not be sent.")

    if isAutomatic:
        print("Message function started. Automatically sending messages...")

        windowManager.find_window_wildcard(".* - Discord")
        windowManager.set_foreground()

        time.sleep(0.05)

        clickMessageBox(windowManager._handle)

        time.sleep(0.05)

        while True:
            if keyboard.is_pressed("esc") | iterations >= maxIterations:
                exit()
            else:
                messageLogic()
                
                iterations += 1
    else:
        print("Message function started. Press the Insert button to start sending messages.")
        while True:
            if keyboard.is_pressed("esc"):
                exit()
            elif keyboard.is_pressed("insert"):
                messageLogic()



phrase = "test"
interval = 0.1

maxIterations = 20
addMessageSuffix = True
useRandomSuffix = True

isAutomatic = False # the above two depend on this one



windowManager = WindowManager()

if isAutomatic:
    print("- -- --- ---- ----- ---- --- -- -")
    print("NOTE: Hold the Esc key to exit the script.")
    print("- -- --- ---- ----- ---- --- -- -")

    for i in range(3):
        print(f"Message function beginning in {3 - i}...")
        time.sleep(1)

messageFunction()

# For a list of keyboard keys, uncomment the line below and Ctrl + Left Click on the rightmost name:
# keyboard._canonical_names.canonical_names