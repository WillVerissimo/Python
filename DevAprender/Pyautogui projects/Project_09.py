from pyautogui import locateCenterOnScreen, click

path = "DevAprender\Pyautogui projects\Screenshot_captcha.PNG"

try:
    captcha = locateCenterOnScreen(path)
except FileNotFoundError:
    print(f"Arquivo {path} não encontrado.")
    exit()

if captcha is not None:
    click(captcha[0], captcha[1], duration=2)
else:
    print('Captcha não encontrado')
