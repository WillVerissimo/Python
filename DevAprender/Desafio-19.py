# DESAFIO 1 - Crie uma função chamada gerar_nome_completo que recebe como parâmetro o nome e sobrenome de alguém e dá boas vindas para essa pessoa
# DESAFIO 2 - # Crie uma função chamada calcular_valores que recebe 2 parâmetros o primeiro o preco de um produto e o segundo parâmetro é a quantidade, porém a quantidade deve haver um valor padrão de 1. Sua função deve exibir o resultado do preço do produto, multiplicado a quantidade escolhida.

def gerar_nome_completo(nome, sobrenome):
    print(f'Seja bem vindo, {nome} {sobrenome}!')

gerar_nome_completo('Willian', 'Veríssimo')

def calcular_valores(produto, quantidade = 1):
    resultado = produto * quantidade
    print(resultado)

calcular_valores(3)