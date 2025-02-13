from PIL import ImageGrab
import numpy as np
import cv2
import time
import os
import pydirectinput
import win32api
import pyautogui
import keyboard

def button():
    while True:
        pydirectinput.keyDown('s')
        pydirectinput.keyUp('s')
        time.sleep(0.1)
        if keyboard.is_pressed('q'):
            break

button()
