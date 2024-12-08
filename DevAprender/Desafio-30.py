'''
Crie uma classe abstrata chamada Monitor, que irá ter 2 métodos abstratos:

aumentar_claridade e reduzir_claridade.

Os métodos irão receber um número que representa o quanto de claridade deve ser aumentado ou diminuido ao chamar eles.

Após ter criado a classe abstrata, crie uma nova classe chamada de MonitorFullHD e coloque a implementação dos métodos aumentar_claridade e reduzir_claridade dentro deles.
'''

from abc import ABC, abstractmethod

class Monitor(ABC):
    @abstractmethod
    def aumentar_claridade(self, valor):
        pass
    @abstractmethod
    def reduzir_claridade(self, valor):
        pass

class MonitorFullHD(Monitor):
    def aumentar_claridade(self, valor):
        print(F'Aumentando a claridade em {valor} pontos')
    def reduzir_claridade(self, valor):
        print(f'Reduzindo a claridade em {valor} pontos')

monitor = MonitorFullHD()
monitor.aumentar_claridade(10)
monitor.reduzir_claridade(10)