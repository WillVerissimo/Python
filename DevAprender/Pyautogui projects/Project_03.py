from pyautogui import dragTo, moveTo

def arrastar_documentos():
    moveTo(960,508,duration=1)
    dragTo(991,221,duration=1)

total_documentos = 10

for documento in range(total_documentos):
    arrastar_documentos()