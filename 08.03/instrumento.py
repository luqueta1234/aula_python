class Instrumento:
    def __init__(self, nome, mensagem):
        self.nome = nome
        self.mensagem = mensagem

    def tocar(self):
        print(f"{self.mensagem}")

class Guitarra:
    def __init__(self, nome, mensagem):
        Instrumento.__init__(self, nome, mensagem)

    def definirMensagem(self, mensagem):
        self.mensagem = mensagem

    def exibir(self):
        Instrumento.tocar(self)

class Bateria:
    def __init__(self, nome, mensagem):
        Instrumento.__init__(self, nome, mensagem)
        mensagem = "Sou uma bateria"

    def definirMensagem(self, mensagem):
        self.mensagem = mensagem

    def exibir(self):
        Instrumento.tocar(self)

instrumento1 = Guitarra("Guitarra elétrica", "")
instrumento2 = Bateria("Bateria", "")

instrumento1.definirMensagem("\nSou uma guitarra\n")
instrumento2.definirMensagem("\nSou uma bateria\n")
instrumento1.exibir()
instrumento2.exibir()