# DESAFIO 1 - Crie um loop while que irá contar e imprimir no console de 1 até 120

n = 1
while n <= 120:
    print(n)
    n += 1

# DESAFIO 2 - Crie um loop while que irá continuamente pedir ao usuário a senha para entrada, e só irá permitir o programa continuar caso ele digite a senha 'secreto'
from sys import exit

senha = ''
tentativas = 0
while senha != 'secreto':
    senha = str(input('Digite sua senha:'))
    if senha != 'secreto':
        tentativas += 1
        if tentativas >= 3:
            print('Acesso negado.')
            exit()
        print('Tente novamente. ')
print('Sistema acessado com sucesso')

# DESAFIO 3 - Crie um loop que conte e imprima na tela o valor em ordem descrescente de 100 para 1

for numero in range(100,-1,-1):
    print(numero)

numero = 100
while numero >= 0:
    print(numero)
    numero -=1