# Calcule quantos dias faltam até o seu aniversário

from datetime import datetime

data_atual = datetime.now()
aniversario = datetime.strptime(input('Qual a data do seu próximo aniversário? (dia/mês/ano): '), '%d/%m/%Y')
dias_restantes = aniversario - data_atual
print(f'Faltam exatamente {dias_restantes.days} dias para o seu aniversário.')