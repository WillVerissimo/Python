from datetime import datetime

# Coleta a data de aniversário
dia_aniversario = int(input('Digite o dia do seu aniversário: '))
mes_aniversario = int(input('Digite o mês do seu aniversário: '))

# Data atual
data_atual = datetime.now()

# Define o próximo aniversário
aniversario_atual = datetime(data_atual.year, mes_aniversario, dia_aniversario)

# Se o aniversário já passou neste ano, considera o próximo ano
if aniversario_atual < data_atual:
    aniversario_atual = datetime(data_atual.year + 1, mes_aniversario, dia_aniversario)

# Calcula a diferença em dias
diferenca = aniversario_atual - data_atual

# Resultado
print(data_atual.strftime('%d/%m/%Y'))
print(f'Faltam {diferenca.days} dias para o seu próximo aniversário.')
