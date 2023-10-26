def criar_conta(numero, titular, saldo, limite):
    conta = {
        "numero": numero,
        "titular": titular,
        "saldo": saldo,
        "limite": limite
    }
    return conta

def depositar(conta, valor):
    conta["saldo"] += valor
def sacar(conta, valor):
    conta["saldo"] -= valor
def imprimir_extrato(conta):
    print("Seu saldo é de {}".format(conta["saldo"]))

conta_1 = {
    "numero": 123,
    "titular": "Clebinho",
    "saldo": -10000,
    "limite": 100
}
conta_2 = {
    "numero": 456,
    "titular": "Beltrana",
    "saldo": 9999,
    "limite": 1000
}
conta_3 = criar_conta(789, "Ciclana", 5000, 10000)
print("conta 1: ", conta_1)
print("conta 2: ", conta_2)
print("conta 3: ", conta_3)

depositar(conta_3, 1000) #antes: 5000 depois: 6000
print(conta_3["saldo"])
sacar(conta_3, 2000) #antes: 6000 depois: 4000
print(conta_3["saldo"])
imprimir_extrato(conta_3)

class Conta:
    #funcao construtora
    def __init__(self, numero, titular, saldo, limite):
        print("Construindo um Objeto...")
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
    def imprimir_extrato(self):
        print("Saldo {} do titular {}.".format(self.__saldo, self.__titular))
    def depositar(self, valor):
        self.__saldo += valor
    def sacar(self, valor):
        self.__saldo -= valor

    def get_saldo(self):
        return self.__saldo
    def get_limite(self):
        return self.__limite
    def get_titular(self):
        return self.__titular
    def set_limite(self):
        return self.__limite
    def transferir(self, destino, valor):
        self.sacar(valor)
        destino.depositar(valor)

conta_clebinho = Conta(123, "Clebinho", -10000, 100)
conta_beltrana = Conta(456, "Beltrana", 5000, 1000)
conta_clebinho.depositar(10000) #antes: -10000, depois: 0
conta_clebinho.imprimir_extrato()
conta_beltrana.sacar(1000) #antse: 5000, depois: 4000
conta_beltrana.imprimir_extrato()

conta_clebinho.transferir(conta_beltrana, 1000)
conta_clebinho.imprimir_extrato() #antes: 0, depois: -1000
conta_beltrana.imprimir_extrato() #antes: 4000, depois: 5000

#conta_clebinho._Conta__saldo = 1000
#print(conta_clebinho._Conta__saldo)




