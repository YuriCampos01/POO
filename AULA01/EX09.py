class Pessoa:
    __total_pessoas = 0

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        Pessoa.__total_pessoas += 1

    @staticmethod
    def get_total_pessoas():
        return Pessoa.__total_pessoas

# Testando a classe Pessoa
pessoa1 = Pessoa("João", 30)
pessoa2 = Pessoa("Maria", 25)

# Obtendo o total de instâncias da classe Pessoa
total_pessoas = Pessoa.get_total_pessoas()
print("Total de pessoas:", total_pessoas)  # Saída: 2
