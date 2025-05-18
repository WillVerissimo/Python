# This bot is able to play the game Guitar Flash, a game where you have to press the keys to play the music.

from pyautogui import press, pixelMatchesColor, moveTo, click, write, hotkey, scroll, locateCenterOnScreen
from time import sleep
from keyboard import is_pressed

hotkey('win', 'r')
write('chrome')
press('enter')
sleep(3)
write('https://www.guitarflash.com/')
press('enter')
sleep(3)
moveTo(539,560, duration=2)
click()
sleep(3)
scroll(-400)
moveTo(672, 452, duration=1)
click()
sleep(10) # Waiting for the game to load
press('a')
sleep(2)
green = locateCenterOnScreen('DevAprender\\Pyautogui projects\\Guitar_Flash_Project\\Green_tile.PNG', confidence=0.8)
red = locateCenterOnScreen('DevAprender\\Pyautogui projects\\Guitar_Flash_Project\\Red_tile.PNG', confidence=0.8)
yellow = locateCenterOnScreen('DevAprender\\Pyautogui projects\\Guitar_Flash_Project\\Yellow_tile.PNG', confidence=0.8)
# blue = locateCenterOnScreen('DevAprender\\Pyautogui projects\\Guitar_Flash_Project\\Blue_tile.PNG', confidence=0.8)
# orange = locateCenterOnScreen('DevAprender\\Pyautogui projects\\Guitar_Flash_Project\\Orange_tile.PNG', confidence=0.8)

while True:
    if pixelMatchesColor(512, 582, (0, 152, 0), tolerance=10):
        press('a')
        sleep(0.05)
    if pixelMatchesColor(601, 583, (255, 0, 0), tolerance=10):
        press('s')
        sleep(0.05)
    if pixelMatchesColor(693, 579, (244, 244, 2), tolerance=10):
        press('j')
        sleep(0.05)
#    if pixelMatchesColor(blue[0], blue[1], (0, 152, 255), tolerance=10):
#        press('k')
#        sleep(0.05)
#    if pixelMatchesColor(orange[0], orange[1], (255, 101, 0), tolerance=10):
#        press('l')
#        sleep(0.05)
    if is_pressed('esc') == True:
        break