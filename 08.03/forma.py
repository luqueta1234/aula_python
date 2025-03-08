class Forma:
    def area(self):
        pass

class Quadrado:
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado * self.lado

class Circulo:
    def __init__(self, raio, pi):
        self.raio = raio
        self.pi = pi

    def area(self):
        return self.raio * self.pi

forma01 = Quadrado(10.00)
forma02 = Circulo(5.00, 3.14)

forma01.area()

forma02.area()
