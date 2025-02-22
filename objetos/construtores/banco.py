class Banco:
    def __init__(self, saldo):
        self.saldo = saldo

    def depositar(self, depositarQuantia):
        self.saldo += depositarQuantia

    def sacar(self, sacarQuantia):
        if (self.saldo > 0):
            self.saldo -= sacarQuantia
        else:
            print("Saque inválido.")

    def mostrar_saldo(self):
        return self.saldo
    
usuario1 = Banco(0)

usuario1.depositar(500)
usuario1.sacar(270)

print(f"Saldo da sua conta bancária: {usuario1.mostrar_saldo()}")