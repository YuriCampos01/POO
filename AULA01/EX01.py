class Pessoa:
    def __init__(self):
        self.__nome = ""
        self.__telefone = ""

    def set_nome(self, nome):
        self.__nome = nome

    def get_nome(self):
        return self.__nome

    def set_telefone(self, telefone):
        self.__telefone = telefone

    def get_telefone(self):
        return self.__telefone

# Criando um objeto da classe Pessoa
pessoa = Pessoa()

# Definindo nome e telefone usando os métodos
pessoa.set_nome("João")
pessoa.set_telefone("123456789")

# Obtendo e exibindo o nome e telefone
print("Nome:", pessoa.get_nome())
print("Telefone:", pessoa.get_telefone())
