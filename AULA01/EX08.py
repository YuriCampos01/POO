from abc import ABC, abstractmethod
import datetime

class Veiculo(ABC):
    def __init__(self, marca, ano, valor_base):
        self.marca = marca
        self.ano = ano
        self.valor_base = valor_base

    @abstractmethod
    def calcular_imposto(self):
        ano_atual = datetime.datetime.now().year
        anos_depreciacao = ano_atual - self.ano
        valor_depreciado = self.valor_base * (1 - (0.05 * anos_depreciacao))
        imposto = valor_depreciado * 0.02
        return imposto

# Exemplo de uma classe derivada de Veiculo (Carro)
class Carro(Veiculo):
    def calcular_imposto(self):
        return super().calcular_imposto()  # Utilizando o método da classe base

# Testando a classe Carro
carro = Carro("Toyota", 2019, 25000.0)
imposto_carro = carro.calcular_imposto()
print(f"Imposto a ser pago pelo carro: R${imposto_carro:.2f}")
