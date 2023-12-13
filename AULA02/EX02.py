import math

class FormaGeometrica:
    def calcular_area(self):
        pass

    def calcular_perimetro(self):
        pass

class Circulo(FormaGeometrica):
    def __init__(self, raio):
        self.raio = raio

    def calcular_area(self):
        return math.pi * self.raio**2

    def calcular_perimetro(self):
        return 2 * math.pi * self.raio

class Retangulo(FormaGeometrica):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura

    def calcular_perimetro(self):
        return 2 * (self.base + self.altura)

class Triangulo(FormaGeometrica):
    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def calcular_area(self):
        # Fórmula de Heron para área de um triângulo com lados conhecidos
        s = (self.lado1 + self.lado2 + self.lado3) / 2
        area = math.sqrt(s * (s - self.lado1) * (s - self.lado2) * (s - self.lado3))
        return area

    def calcular_perimetro(self):
        return self.lado1 + self.lado2 + self.lado3

# Exemplos de uso
circulo = Circulo(5)
print("Círculo - Área:", circulo.calcular_area(), "- Perímetro:", circulo.calcular_perimetro())

retangulo = Retangulo(4, 6)
print("Retângulo - Área:", retangulo.calcular_area(), "- Perímetro:", retangulo.calcular_perimetro())

triangulo = Triangulo(3, 4, 5)
print("Triângulo - Área:", triangulo.calcular_area(), "- Perímetro:", triangulo.calcular_perimetro())
