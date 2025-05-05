from pyautogui import locateCenterOnScreen, click

path = 'Screenshot_captcha.png'
captcha = locateCenterOnScreen(path)

if captcha is not None:
    click(captcha[0], captcha[1], duration=2)
else:
    print('Captcha não encontrado')
