# Desafio 1
# Usando a lista compreheension, crie a seguinte lista:
# [2, 4, 6, 8, 10]
def is_it_even(number):
    if number % 2 == 0:
        return True

print([n for n in range(11) if is_it_even(n)])

# Desafio 2
# Use a seguinte lista como base:
cores = ['vermelho','azul','verde','amarelo','rosa','preto']
# Para criar a lista a seguir:
# ['1 - vermelho','2 - azul','3 - verde','4 - amarelo','5 - rose','6 - preto']

print([str(n+1) + ' - ' + cor for n, cor in enumerate(cores)])

# Desafio 3 
# Usando a lista a seguir como base:
participantes = ['joel','jessica','maria','cris','Larissa','rafael','marcus','john']
pagamento_realizado = ['joel','jessica','maria','cris']
# Concatene(adicione) a palavra 'PAGO' aos nomes da lista 'participantes' usando condicionais somente nos casos onde seu nome esteja na lista 'pagamento_realizado'. O resultado final deve ser como a lista a seguir:
# ['joel PAGO','jessica PAGO','maria PAGO','cris PAGO','Larissa','rafael','marcus','john']

# print([participante + ' PAGO' for participante in participantes if participante in pagamento_realizado else participante + 'DEVENDO' for participante in participantes])

print([participante + ' PAGO' if participante in pagamento_realizado else participante for participante in participantes])
