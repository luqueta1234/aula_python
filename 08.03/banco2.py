class Banco:
    def __init__(self, saldo):
        self.__saldo = saldo

    def depositarQuantia(self, quantia):
        self.__saldo += quantia

    def sacarQuantia(self, quantia):
        if quantia <= self.__saldo:
            self.__saldo -= quantia
        else:
            print(f"Quantia de saque inválida.")

    def exibir(self):
        print(f"Saldo: {self.__saldo}")

cliente01 = Banco(0)

cliente01.depositarQuantia(5000)
cliente01.sacarQuantia(500)

cliente01.exibir()