# Simular uma moeda de cara ou coroa e exibir o resultado na tela
from random import choices, randint

print('Cara ou coroa?')
while True:
    escolha = str(input('Digite sua escolha: '))
    if escolha == 'cara' or escolha == 'coroa':
        break
    else:
        print('Tente novamente. ')
jogar_moeda = ['cara', 'coroa']
resultado = choices(jogar_moeda)
if resultado[0] == escolha:
    print(f'Você escolheu {escolha} e o resultado deu {resultado[0]}, você venceu!')
else:
    print(f'Você escolheu {escolha} e o resultado deu {resultado[0]}, você perdeu!')

# Crie uma lista com cinco nomes e sorteie um, exiba o valor na tela

lista = ['Aderbal', 'Bolsonaro', 'Clovis', 'Adalberto', 'Mauro']
nome_escolhido = choices(lista)
print(nome_escolhido[0])

# Escolha aleatoriamente um número de 10 a 100 e imprima o resultado na tela

numero = randint(10,100)
print(numero)