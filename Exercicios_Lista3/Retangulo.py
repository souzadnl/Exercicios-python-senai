"""
Crie uma classe Retangulo com atributos
altura e largura, e um método perimetro() para calcular o perímetro.
"""
class Retangulo:

    def __init__(self, altura, largura):
        self.altura = altura
        self.largura = largura

    def Perimetro(self):
        perimetro = (self.altura * 2) + (self.largura * 2)
        return perimetro


altura = int(input("Insira a altura: "))
largura = int(input("Insira a largura: "))
perimetro=Retangulo(altura,largura).Perimetro()
print(perimetro)
