# ​🥇 DESAFIO Manipulação de Arquivos🥇

# Primeiro crie 3 listas

# * Uma lista que contem 5 frutas
import os
quebra_linha = os.linesep

frutas = ['maçã', 'pera', 'banana', 'melão', 'abacaxi']

#  * Uma lista que contem 5 cores
cores = ['azul', 'amarelo', 'verde', 'roxo', 'rosa'] 

#  * Uma lista que contem 5 linguagens de programação
linguagens_programacao = ['python', 'javascript', 'java', 'C#', 'php']

# Desafio 1 - Crie um novo arquivo chamado frutas.txt e insira dentro dele todos as 5 frutas que estão na lista de frutas
with open('frutas.txt', 'w', newline='') as arquivo_frutas_escrever:
    for fruta in frutas:
        arquivo_frutas_escrever.write(str(fruta + quebra_linha))

# Desafio 2 - Imprima na tela todas as linhas que estao dentro do arquivo frutas.txt
with open('frutas.txt', 'r', newline='') as arquivo_frutas_leitura:
    for linha in arquivo_frutas_leitura:
        print(linha)

# Desafio 3 - Sem apagar os dados que já estão dentro de frutas.txt, adicione todas as cores que estão dentro da sua lista de cores ao arquivos frutas.txt
with open('frutas.txt', 'a', newline='') as arquivo_frutas_adicionar:
    for cor in cores:
        arquivo_frutas_adicionar.write(str(cor + quebra_linha))

# Desafio 4 - Crie um novo arquivo chamado 'Top 5 Linguagens.txt' e popule o arquivo, de forma com que cada linguagem ocupe apenas uma linha.
with open('Top 5 Linguagens.txt', 'w', newline='') as arquivo_linguagens:
    for linguagem in linguagens_programacao:
        arquivo_linguagens.write(str(linguagem + quebra_linha))

# BONUS - Como você poderia criar vários arquivos diferentes usando um laço for e strings dinâmicos(f'{}'), e também não escrever nada dentro deles?
arquivos = ['musica.mp3', 'nomes.txt', 'telefones.pdf', 'videos.mp4', 'desenhos.jpg']
for arquivo in arquivos:
    with open(arquivo, 'w', newline='') as novo_arquivo:
        pass
