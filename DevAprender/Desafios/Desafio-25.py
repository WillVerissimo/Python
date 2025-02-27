# Ordene a lista de produtos abaixo pelo preço em ordem crescente

from operator import itemgetter

produtos = [
    {'nome': 'Celular',
     'preco': 1500
     },
    {'nome': 'Monitor',
     'preco': 500
     },
    {'nome': 'Microfone',
     'preco': 300
     }
]

produtos.sort(key=itemgetter('preco'))
print(produtos)

# Ordene em ordem descrescente a lista de equipamento_filmagem por valor do equipamento
equipamento_filmagem = [
    ('Tripé', 300),
    ('Câmera', 1700),
    ('Iluminação', 200),
]

equipamento_filmagem.sort(key=itemgetter(1), reverse = True)
print(equipamento_filmagem)

# Ordene em ordem crescente a cotacao_moedas com base no valor da moeda

cotacao_moedas = [['usd', 5.25], ['brl', 1.56], ['eur', 6.47]]

cotacao_moedas.sort(key=itemgetter(1))
print(cotacao_moedas)