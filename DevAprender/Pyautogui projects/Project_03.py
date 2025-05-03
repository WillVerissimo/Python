# Programa que arrasta documentos automaticamente de acordo com a necessidade

from pyautogui import dragTo, moveTo

def arrastar_documentos():
    moveTo(960,508,duration=1)
    dragTo(991,221,duration=1)

total_de_documentos = 10 # Insira aqui o número total de documentos a serem transferidos

for documento in range(total_de_documentos):
    arrastar_documentos()