from pyautogui import moveTo, hotkey, click
from pyperclip import copy

def caracteres_especiais(frase): # Função que permite que seja utilizado UTF-8 sem erros, ao contrário do "typewrite"
    copy(frase)
    hotkey('ctrl','v')

def escrever(frase): # Função que utiliza da função acima pra poder gerar escrita através do pyautogui
    moveTo(1006,339,duration=1)
    click()
    caracteres_especiais(frase)

escrever('Automação é incrível!')