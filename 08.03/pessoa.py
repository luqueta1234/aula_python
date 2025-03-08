class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

class Aluno(Pessoa):
    def __init__(self, nome, idade, matricula):
        Pessoa.__init__(self, nome, idade)
        self.matricula = matricula

    def exibir(self):
        print(f"\nNome do aluno: {self.nome}\nIdade: {self.idade}\nMatricula: {self.matricula}\n")

aluno1 = Aluno("Lucas", 18, 1928398)
aluno1.exibir()