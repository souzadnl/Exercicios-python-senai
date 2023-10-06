"""
Crie uma classe Pessoa com atributos nome e idade, e um método apresentar()
que imprime o nome e a idade.
"""

class Pessoa:
    def __init__(self, nome, idade):

        self.nome= nome
        self.idade= idade

    def Apresentar(self):

        apresentar= f"Nome: {self.nome}\nIdade: {self.idade}"
        return apresentar

nome= input("Insira seu nome : ")
idade= input("Insira sua idade  : ")


print(Pessoa(nome, idade).Apresentar())