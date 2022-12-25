"""
Made with ♥ By Haris
"""
import pyautogui
import time
time.sleep(10)

lines = open("text.txt", 'r')
for word in lines:
    pyautogui.typewrite(word)
    pyautogui.press("enter")
