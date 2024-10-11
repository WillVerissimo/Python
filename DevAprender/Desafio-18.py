'''

# Desafio 🥇

### Desafio 1 

Monte um mini-game turtle, que possibilite que o usuário controle para qual direção a tartaruga deve andar(frente/trás) e qual ângulo deverá ser tomado a cada nova movimentação

### Desafio 2 

Usando o mini-game, desenha um quadrado passando instruções para a turtle, totalmente através do input do usuário

#### Dicas Iniciais

* Crie uma nova turtle primeiro

* Coloca seu programa em loop 

* Faça perguntas ao usuário para decidir se a tartaruga deve movimentar para frente ou para trás

* Após decidir se ele deve movimentar para frente ou para trás, receba do usuário quantos pixels devem ser percorridos

* Faça perguntas ao usuário para decidir se a tartaruga deve rotacionar para esquerda ou direta

* Após decidir se ele deve rotacionar para esquerda ou direita, receba do usuário quantos pixels devem ser rotacionados

* Ao executar essa ação pergunte ao usuário "Continuar andando?", e reaga de acordo com a resposta do usuário.

#### Dicas Adicionais

* Não esqueça de converter o input do usuário para o tipo apropriado

* Resolva um problema de cada vez e lembre de seguir a seguinte lógica: 

Pergunte -> Processe resposta -> A

'''
from turtle import Turtle

move = Turtle()

move.speed(1)

condicao = 'S'

print('--------Movimentando a seta--------')
print('Movimente a seta de acordo com as instruções:')

condicao = 'S'

while condicao in 'Ss':
    while True:
        try:
            resposta = int(input('Digite 1 para seguir em frente\nDigite 2 para virar para a direita\nDigite 3 para virar para a esquerda\nDigite 4 para virar para trás\nSua resposta: '))
            if resposta == 1:
                break
            elif resposta == 2:
                angulo = float(input('Quantos graus a seta deve virar?\nSua resposta: '))
                move.right(angulo)
                break
            elif resposta == 3:
                angulo = float(input('Quantos graus a seta deve virar?\nSua resposta: '))
                move.left(angulo)
                break
            elif resposta == 4:
                move.right(180)
                break
            else:
                print('Comando inválido.')
        except ValueError:
            print('Por favor, digite um número válido. ')

    while True:
        try:
            pixels = int(input('Quantos pixels a seta deve andar?\nSua resposta: '))
            move.forward(pixels)
            break
        except ValueError:
            print('Por favor, digite um número válido.')
            
    while True:
        condicao = input('Deseja continuar a movimentar a seta? (S/N): ').strip().upper()
        if condicao not in 'SN':
            print('Comando inválido, tente novamente.')
        else:
            if condicao == 'S':
                print('Continuando a movimentar a seta...')
            else:
                print('Movimentação da seta encerrada.')
            break
