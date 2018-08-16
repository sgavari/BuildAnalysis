# -*- coding: utf-8 -*-
"""
Created on Tue Jun  5 15:23:24 2018

@author: sgavari
"""
from tkinter.messagebox import *

import os
import pyautogui
import time

#os.startfile(r"C:\Program Files\Key Metric Software\FolderSizes 7\FolderSizes.exe")
time.sleep(5)
#click on foldersizes icon in taskbar
pyautogui.click(817, 1177)
#click on first drive
pyautogui.click(545, 277)
y=pyautogui.prompt('This lets the user type in a path')
pyautogui.click(141, 148)
pyautogui.typewrite(y)
pyautogui.hotkey('ctrl','a')
pyautogui.hotkey('enter')
#print(pyautogui.position())

im2 = pyautogui.screenshot('my_screenshot.png')
