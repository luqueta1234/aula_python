class Carro:
    def __init__(self, marca, ano, tetosolar):
        self.marca = marca
        self.ano = ano
        self.tetosolar = tetosolar

    def exibir_info(self):
        print(f"Marca do carro: {self.marca}\nAno de fabricação: {self.ano}\nTem teto solar? {self.tetosolar}\n")

carro1 = Carro("Chevrolet", 2023, False)
carro2 = Carro("Toyota", 2024, False)
carro3 = Carro("Ferrari", 2026, True)

carro1.exibir_info()
carro2.exibir_info()
carro3.exibir_info()