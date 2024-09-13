# Crie um programa que escolha um número aleatório de 1 a 10 e peça para o usuário tentar acertar, informe se o número chutado é maior ou menor e se o usuário acertou, e permita que ele tente até acertar.
from random import randint
numero = randint(1, 10)
print('Eu escolhi um número de 1 a 10, consegue acertar?')
while True:
    chute = int(input('Qual é o número que eu escolhi?: '))
    if chute > 10 or chute < 1:
        print('Somente números de 1 a 10, tente de novo')
    elif chute > numero:
        print('Meu número é menor')
    elif chute < numero:
        print('Meu número é maior')
    else:
        print(f'Parabéns! Você acertou, eu escolhi o número {numero}.')
        break