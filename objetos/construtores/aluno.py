class Aluno:
    def __init__(self, nome, nota):
        self.nome = nome
        self.nota = nota
    
    def media(self):
        if self.nota >= 6 and self.nota > 0:
            print(f"Aluno aprovado. Nota: {self.nota}")
        elif self.nota <= 5 and self.nota > 0:
            print(f"Aluno reprovado. Nota: {self.nota}")
        else:
            print("Nota inserida inválida.")

aluno1 = Aluno("João", 8)

aluno1.media()