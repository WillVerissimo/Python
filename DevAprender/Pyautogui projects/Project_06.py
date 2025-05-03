from pyautogui import hotkey, click, moveTo

def copiar_e_colar(): # Função que copia e cola o texto
    hotkey('ctrl','a') # Seleciona todo o texto
    hotkey('ctrl','c') # Copia o texto selecionado
    hotkey('ctrl','v') # Cola o texto copiado

moveTo(1006,339,duration=1) # Move o mouse para a posição desejada

click() # Clica na posição desejada

copiar_e_colar() # Chama a função para executar o copiar e colar
# O código acima move o mouse para a posição (1006, 339), clica nessa posição e em seguida copia e cola o texto selecionado.
# O código é útil para automatizar tarefas de copiar e colar em um editor de texto ou em qualquer outro aplicativo onde o atalho Ctrl+C e Ctrl+V funcione.
# O código pode ser utilizado em diversas situações, como por exemplo, para copiar e colar informações de um site ou de um documento para outro.