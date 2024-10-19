'''
Itere sobre a lista a abaixo exibindo o número do índice + nome da fruta. Porém quando o índice for 3 exiba 'Nº índice + nome da fruta EM PROMOÇÃO
'''

frutas = ['Maçã', 'Laranja', 'Morango', 'Limão']

for indice, fruta in enumerate(frutas, 0):
    if indice == 3:
        print(f'Nº {indice} - {fruta} EM PROMOÇÃO')
    else:
        print(f'Nº {indice} - {fruta}')
