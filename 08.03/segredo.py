class Segredo:
    def __init__(self, segredo):
        self.__segredo = segredo

    def exibir(self):
        print(f"\nO segredo é... {self.__segredo}")

segredo1 = Segredo("\nHoje é sábado\n")
segredo1.exibir()