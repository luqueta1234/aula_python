class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario
    def exibir(self):
        print(f"\nNome do funcionário: {self.nome}\nSalário: {self.salario}\n")

class Gerente (Funcionario):
    def __init__(self, nome, salario, departamento):
        Funcionario.__init__(self, nome, salario)
        self.departamento = departamento

    def qual_departamento(self):
        print(f"Departamento: {self.departamento}\n")

    def exibir(self):
        print(f"\nNome do funcionário: {self.nome}\nSalário: {self.salario}\n")

funcionario01 = Funcionario("Lucas", 2000.00)
funcionario02 = Gerente("André", 5000.00, "Administrativo")

funcionario01.exibir()

funcionario02.exibir()
funcionario02.qual_departamento()