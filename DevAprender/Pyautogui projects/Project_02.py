from pyautogui import click, rightClick, moveTo

def criar_pasta():
    moveTo(964,401,duration=2)
    rightClick()
    moveTo(1037,647,duration=1)
    click()
    moveTo(815,433,duration=1)
    click()
    moveTo(909,371,duration=0.5)
    click()

criar_pasta()