# Create a program that makes automatic likes on Instagram posts.

# 1 - Open Browser

from webbrowser import open_new_tab
from time import sleep
from pyautogui import click, write, press, moveTo, locateCenterOnScreen, move

open_new_tab('https://www.instagram.com/')
sleep(5)

# 2 - Log in (Already logged in)

# 3 - Search for a profile - I'll be searching for the profile of Cristiano Ronaldo

profile = '/cristiano'

try:
    Search_bar = locateCenterOnScreen(r'DevAprender\Pyautogui projects\Instagram_Project\Search_bar.PNG')
except FileNotFoundError:
    print(f"Arquivo Search_bar.PNG não encontrado.")
    exit()

moveTo(Search_bar[0], Search_bar[1], duration=2)
move(200, 0, duration=2)
click()
sleep(1)
click()
write(profile, interval=0.1)
sleep(0.5)
press('enter')

# 4 - Click on the first post

move(100, 400, duration=2)
click()
sleep(1)

# 5 - Try to find the heart icon and click on it, if not found, just finish the program

try:
    heart_icon = locateCenterOnScreen(r'DevAprender\Pyautogui projects\Instagram_Project\Heart_icon.PNG')
except FileNotFoundError:
    print(f"Arquivo Heart_icon.PNG não encontrado.")
    exit()

if heart_icon is not None:
    moveTo(heart_icon[0], heart_icon[1], duration=2)
    click()
else:
    print('Heart icon not found')
    exit()
