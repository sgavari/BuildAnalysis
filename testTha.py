# -*- coding: utf-8 -*-
"""
Created on Tue Jun  5 15:23:24 2018

@author: sgavari
"""
from tkinter.messagebox import *
import os
import pyautogui
import time 
os.startfile(r"C:\Program Files\Key Metric Software\FolderSizes 7\FolderSizes.exe")
time.sleep(4)
pyautogui.click((647, 111))

time.sleep(3)
pyautogui.click(442, 638)
pyautogui.click(424, 664)
print(pyautogui.size())
time.sleep(3)
pyautogui.click(635, 399)
pyautogui.click(719, 402)
pyautogui.typewrite("C:\Scan Folder Size\CSV\FolderSizes_Report.csv")
time.sleep(3)
pyautogui.click(653, 456)
pyautogui.click(727, 450)
pyautogui.typewrite("C:\Scan Folder Size\PDF\FolderSizes_Report.pdf")

pyautogui.click(632, 707)

pyautogui.click(795, 706)
pyautogui.typewrite("Sairaviteja.Gavari@kla-tencor.com")
pyautogui.click(900, 313)
pyautogui.click(916, 362)
pyautogui.click(988, 357)
pyautogui.click(988, 357)
pyautogui.click(988, 357)
pyautogui.click(988, 357)
pyautogui.alert('Select your Drive and press OK.')
y=pyautogui.prompt('This lets the user type in a string and press OK.')
pyautogui.alert(y)
time.sleep(5)
pyautogui.click(900, 80)