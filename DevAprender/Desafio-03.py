''' Crie um programa que receba a velocidade de um veículo numa determinada rua cuja velocidade máxima seja de 80km/h, e mostre:
 Caso o veículo esteja dentro da velocidade máxima, informe que não houve multa;
 Caso o veículo esteja até 10 km/h acima da velocidade, tome multa leve;
 Caso o veículo esteja entre 11 e 20 km/h acima da velocidade, tome multa grave;
 Caso o veículo esteja acima de 20 km/h da velocidade mácima, tome multa gravíssima; '''
from random import randint
from time import sleep

print('Radar monitorando...')
sleep(3)
print('Veículo passou')
sleep(1)

v = randint(60,120)
vmax = 80
multa_leve = (vmax + 10)
multa_grave = (vmax + 20)
print(f'Velocidade de {v} km/h')

if v < vmax:
    print('Não houve multa')
elif v < multa_leve:
    print('Multa leve aplicada')
elif v > multa_leve and v < multa_grave:
    print('Multa grave aplicada')
else:
    print('Multa gravíssima aplicada')