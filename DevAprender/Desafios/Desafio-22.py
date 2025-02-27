''' 
​# Desafios 🥇
Desafio #1 Crie uma lista que tenha os nomes dos 3 objetos que você mais usa durante o dia e imprima ele na tela
Desafio #2 Usando apenas uma linha de código, crie uma lista de 10 a 131
Desafio #3 Imprima na tela o resultado da combinação da lista do desafio 1 e desafio 2
Desafio #4 Crie uma lista de listas(matriz) que tenha os nomes dos 3 objetos
que você mais usa durante o dia, mas agora dentro de cada item você vai colocar 
uma informação extra, coloque o valor em reais desse objeto também e imprima ele 
na tela
'''

objetos = ['computador', 'bike', 'cama']

numeros = list(range(10,132))

combinacao = objetos + numeros
print(combinacao)

objetos_com_valores = [['computador', 3500], ['bike', 10000], ['cama', 800]]
print(objetos_com_valores)