import pyautogui
from time import sleep

pyautogui.moveTo(971,324,duration=1.5)

for n in range(150):
    sleep(0.3)
    pyautogui.click()