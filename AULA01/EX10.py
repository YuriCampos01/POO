class Triangulo:
    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def verificar_tipo(self):
        if self.lado1 == self.lado2 == self.lado3:
            return "Equilátero"
        elif self.lado1 == self.lado2 or self.lado1 == self.lado3 or self.lado2 == self.lado3:
            return "Isósceles"
        else:
            return "Escaleno"

# Testando a classe Triangulo
triangulo1 = Triangulo(5, 5, 5)  # Equilátero
triangulo2 = Triangulo(3, 4, 4)  # Isósceles
triangulo3 = Triangulo(7, 4, 9)  # Escaleno

# Verificando e exibindo os tipos dos triângulos
print("Triângulo 1:", triangulo1.verificar_tipo())  # Saída: Equilátero
print("Triângulo 2:", triangulo2.verificar_tipo())  # Saída: Isósceles
print("Triângulo 3:", triangulo3.verificar_tipo())  # Saída: Escaleno
