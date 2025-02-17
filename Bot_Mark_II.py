from PIL import ImageGrab
import numpy as np
import cv2
import time
import os
import pydirectinput
import win32api
import pyautogui

color = [255, 255, 255]
count = 1

while count < 2:
    time.sleep(3)
    window = np.array(ImageGrab.grab(bbox = (100,100,1010,1020)))
    window = cv2.cvtColor(window, cv2.COLOR_BGR2RGB)
    #cv2.imshow("Bot_Vision", window)

    ###Create and analysis screenshot
    screenshot = pyautogui.screenshot()
    screenshot = cv2.cvtColor(window, cv2.COLOR_BGR2RGB)
    color_place = np.where(np.all(color == screenshot, axis = 2))
    coordinate_duo = np.column_stack((color_place))
    print(coordinate_duo)
    count = count + 1   
    

    if cv2.waitKey(1) == ord("q"):
        cv2.DestroyAllWindows()
        break
