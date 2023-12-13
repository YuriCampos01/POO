class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.velocidade = 0

    def acelerar(self):
        self.velocidade += 10

    def frear(self):
        if self.velocidade >= 5:
            self.velocidade -= 5
        else:
            self.velocidade = 0

    def __str__(self):
        return f"Carro: {self.marca} {self.modelo} {self.ano}, Velocidade: {self.velocidade}"

# Criando um objeto Carro
meu_carro = Carro("Toyota", "Corolla", 2020)

# Acelerando o carro duas vezes
meu_carro.acelerar()
meu_carro.acelerar()

# Exibindo a velocidade do carro
print(meu_carro)  # Saída: Carro: Toyota Corolla 2020, Velocidade: 20

# Freando o carro
meu_carro.frear()

# Exibindo a velocidade após frear
print(meu_carro)  # Saída: Carro: Toyota Corolla 2020, Velocidade: 15
