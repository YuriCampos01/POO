class Calculadora:
    @staticmethod
    def soma(a, b):
        return a + b

    @staticmethod
    def subtracao(a, b):
        return a - b

    @staticmethod
    def multiplicacao(a, b):
        return a * b

    @staticmethod
    def divisao(a, b):
        if b == 0:
            return "Erro: Divisão por zero"
        return a / b

# Testando os métodos da Calculadora
print("Soma:", Calculadora.soma(10, 5))  # Saída: 15
print("Subtração:", Calculadora.subtracao(10, 5))  # Saída: 5
print("Multiplicação:", Calculadora.multiplicacao(10, 5))  # Saída: 50
print("Divisão:", Calculadora.divisao(10, 5))  # Saída: 2.0
print("Divisão por zero:", Calculadora.divisao(10, 0))  # Saída: "Erro: Divisão por zero"
