from pyautogui import moveTo, hotkey, click
from pyperclip import copy

def caracteres_especiais(frase):
    copy(frase)
    hotkey('ctrl','v')

def escrever(frase):
    moveTo(1006,339,duration=1)
    click()
    caracteres_especiais(frase)

escrever('Automação é incrível!')