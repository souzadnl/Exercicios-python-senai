"""
Crie uma classe Carro com um atributo velocidade e métodos para acelerar()
e frear(). O método acelerar aumenta em 10 a velocidade e
o método frear diminuiu em 10. A velocidade não pode ser < 0.
"""

class Carro:

    def __init__(self, velocidade):
        self.velocidade = velocidade

    def Acelerar(self):
        acelerar = self.velocidade + 10
        print(self.velocidade)
        return acelerar
    def Frear(self):
        frear = self.velocidade - 10
        print(self.velocidade)
        return frear

velocidade = int(input("Insira a velocidade do carro "))

while True:
    escolha = input("Você deseja acelerar ou frear?")

    match(escolha.lower()):
        case "acelerar":
            print(Carro(velocidade).Acelerar())
            break
        case "frear":
            print(Carro(velocidade).Frear())
            break