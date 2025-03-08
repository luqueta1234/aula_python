class Veiculo:
    def __init__(self, marca, ano):
        self.marca = marca
        self.ano = ano

class Carro (Veiculo):
    def __init__(self, marca, ano, em_movimento):
        Veiculo.__init__(self, marca, ano)
        self.em_movimento = em_movimento

    def exibir_info(self):
        print(f"\nMarca do carro: {self.marca}\nAno de fabricação: {self.ano}\n")

    def movimento(self):
        if self.em_movimento == True:
            print(f"O carro está em movimento.\n")
        else:
            print(f"O carro não está em movimento.\n")

carro01 = Carro("Chevrolet", 1987, True)


carro01.exibir_info()
carro01.movimento()