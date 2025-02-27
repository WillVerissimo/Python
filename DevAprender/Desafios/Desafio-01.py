# Faça um programa que leia uma entrada de um número inteiro e devolva o seu resultado em fatorial

while True:
    n1 = int(input('Digite um número para ver o seu fatorial: '))
    if type(n1) is int and n1 > 0:
        fatorial = 1
        for numero in range(n1,0,-1):
            fatorial *= numero
        print(f'O fatorial de {n1} é {fatorial}')
        break
    else:
        print('Comando inválido, tente novamente. ')