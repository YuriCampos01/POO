class Ponto2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @staticmethod
    def tem_eixo_comum(ponto_a, ponto_b):
        if ponto_a.x == ponto_b.x or ponto_a.y == ponto_b.y:
            return True
        return False

# Criando pontos
ponto1 = Ponto2D(3, 5)
ponto2 = Ponto2D(3, 8)
ponto3 = Ponto2D(7, 5)

# Verificando se os pontos têm algum eixo em comum
print("Ponto1 e Ponto2 têm eixo comum?", Ponto2D.tem_eixo_comum(ponto1, ponto2))  # True
print("Ponto1 e Ponto3 têm eixo comum?", Ponto2D.tem_eixo_comum(ponto1, ponto3))  # True
print("Ponto2 e Ponto3 têm eixo comum?", Ponto2D.tem_eixo_comum(ponto2, ponto3))  # False
