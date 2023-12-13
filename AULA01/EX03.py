class Pessoa:
    def __init__(self, nome, idade, telefone):
        self.nome = nome
        self.idade = idade
        self.telefone = telefone

class Agenda:
    def __init__(self):
        self.pessoas = []

    def adicionar_pessoa(self, pessoa):
        if len(self.pessoas) < 10:
            self.pessoas.append(pessoa)
            print(f"{pessoa.nome} foi adicionado à agenda.")
        else:
            print("A agenda está cheia, não é possível adicionar mais pessoas.")

    def remover_pessoa(self, nome):
        for pessoa in self.pessoas:
            if pessoa.nome == nome:
                self.pessoas.remove(pessoa)
                print(f"{nome} foi removido da agenda.")
                return
        print(f"{nome} não encontrado na agenda.")

    def buscar_pessoa(self, nome):
        for pessoa in self.pessoas:
            if pessoa.nome == nome:
                print(f"Informações de {nome}:")
                print(f"Nome: {pessoa.nome}")
                print(f"Idade: {pessoa.idade}")
                print(f"Telefone: {pessoa.telefone}")
                return
        print(f"{nome} não encontrado na agenda.")

    def listar_pessoas(self):
        print("Lista de Pessoas na Agenda:")
        for pessoa in self.pessoas:
            print(f"Nome: {pessoa.nome}, Idade: {pessoa.idade}, Telefone: {pessoa.telefone}")


# Criando objetos Pessoa
pessoa1 = Pessoa("João", 30, "123456789")
pessoa2 = Pessoa("Maria", 25, "987654321")
pessoa3 = Pessoa("Carlos", 40, "555555555")

# Criando a agenda e adicionando pessoas
agenda = Agenda()
agenda.adicionar_pessoa(pessoa1)
agenda.adicionar_pessoa(pessoa2)
agenda.adicionar_pessoa(pessoa3)

# Listando pessoas na agenda
agenda.listar_pessoas()

# Buscando uma pessoa na agenda
agenda.buscar_pessoa("João")

# Removendo uma pessoa da agenda
agenda.remover_pessoa("Maria")

# Listando pessoas após a remoção
agenda.listar_pessoas()
