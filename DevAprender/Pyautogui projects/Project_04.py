# Programa que, determinado uma aba de site, arrasta até uma determinada seção dela

from pyautogui import scroll, moveTo

def scroll_historia():
    moveTo(1021,338,duration=1)
    scroll(-4800)

scroll_historia()