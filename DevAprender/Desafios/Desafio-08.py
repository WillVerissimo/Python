# Transforme a frase1 em uma lista de palavras e guarde o resultado em uma variável chamada palavras1
# Transforme a frase2 em uma lista de palavras e guarde o resultado em uma variável chamada palavras2
# Pegue o palavras1 e transforme elas no seguinte string: "Desafio,manipulação,de,strings". Imprima o resultado no console.
# Pegue o palavras2 e transforme elas no seguinte string: frase2 = "jhonatan & rafael & carol & camilla. Imprima o resultado no console.

frase1 = 'Desafio manipulação de strings'
frase2 = 'jhonatan,rafael,carol,camilla'

palavras1 = frase1.split()
palavras2 = frase2.split(',')

print(','.join(palavras1))
print(' & '.join(palavras2))