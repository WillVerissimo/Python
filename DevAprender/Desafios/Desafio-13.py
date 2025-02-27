# DESAFIO 🥇

# uso expressão condicional(operador ternário) para criar a seguinte condição

# se velocidade estiver acima de 100 exibir, você foi multado, caso contrário exiba siga em frente

while True:
    velocidade = int(input('Digite a velocidade: '))
    if velocidade <= 0:
        print('Digite novamente. ')
    else:
        break
if velocidade > 100:
    print('Você foi multado')
else:
    print('Siga em frente')