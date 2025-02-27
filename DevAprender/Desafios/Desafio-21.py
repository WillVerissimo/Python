'''
Crie um decorador que irá pegar a função que foi passado para ele e o horário atual antes de executar a função de pois imprimir o horário após ter finalizado a execução da função
'''
from datetime import datetime
from time import sleep

def decorator(funcao):
    def wrapper(*args, **kwargs):
        print(f'Início do processo às {datetime.now()}')
        funcao(*args, **kwargs)
        print(f'Fim do processo às {datetime.now()}')
    return wrapper

@decorator
def pausa(segundos):
    sleep(segundos)

# Exemplo
pausa(3)