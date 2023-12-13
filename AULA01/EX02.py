class Aluno:
    def __init__(self, matricula, nome, notas):
        self.matricula = matricula
        self.nome = nome
        self.notas = notas

    def get_media(self):
        if len(self.notas) == 0:
            return 0  # Se não houver notas, a média é zero
        return sum(self.notas) / len(self.notas)

    def get_situacao(self):
        media = self.get_media()
        if media >= 7:
            return "Aprovado"
        elif 5 <= media < 7:
            return "Recuperação"
        else:
            return "Reprovado"

# Criando um aluno com número de matrícula, nome e notas
aluno1 = Aluno(1234, "João", [8, 7, 9, 6])

# Calculando a média do aluno e verificando sua situação
print(f"Média: {aluno1.get_media()}")
print(f"Situação: {aluno1.get_situacao()}")

# Adicionando novas notas e verificando novamente a média e situação
aluno1.notas.append(4)
print(f"Média atualizada: {aluno1.get_media()}")
print(f"Situação atualizada: {aluno1.get_situacao()}")
