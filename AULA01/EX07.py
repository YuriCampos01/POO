class Universidade:
    total_estudantes = 0
    total_professores = 0

    @staticmethod
    def matricular_estudante():
        Universidade.total_estudantes += 1

    @staticmethod
    def contratar_professor():
        Universidade.total_professores += 1

    @staticmethod
    def obter_total_pessoas():
        return Universidade.total_estudantes + Universidade.total_professores

# Testando a classe Universidade
Universidade.matricular_estudante()
Universidade.matricular_estudante()
Universidade.contratar_professor()

# Obtendo o total de pessoas na universidade
total_pessoas = Universidade.obter_total_pessoas()
print("Total de estudantes e professores:", total_pessoas)  # Saída: 3
