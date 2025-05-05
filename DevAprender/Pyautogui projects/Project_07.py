# Crie um programa que pede o usuário e senha e, na sequência, copia e cola o usuário e senha dentro de um bloco de notas.

from pyautogui import hotkey, password, prompt, write, press
from pyperclip import copy
from time import sleep

def abrir_bloco_de_notas():
    hotkey('win', 'r') # Abre o executar do Windows
    write('notepad') # Digita "notepad" no executar
    press('enter') # Pressiona "Enter" para abrir o bloco de notas

def caracteres_especiais(frase): # Função que permite que seja utilizado UTF-8 sem erros, ao contrário do "typewrite"
    copy(frase)
    hotkey('ctrl','v')

def escrever():
    caracteres_especiais(usuario) # Escreve o usuário no bloco de notas
    press('enter') # Pressiona "Enter" para pular uma linha
    caracteres_especiais(senha) # Escreve a senha no bloco de notas
    press('enter') # Pressiona "Enter" para pular uma linha

usuario = prompt(text='Digite seu usuário:', title='Login' )
senha = password(text='Digite sua senha:', title='Login', mask='*')

abrir_bloco_de_notas()
sleep(2)
escrever()
