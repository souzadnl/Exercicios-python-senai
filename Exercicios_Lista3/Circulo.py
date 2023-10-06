class Circulo:
    def __init__(self, raio):
        self.raio = raio

    def get_raio(self):
        return self.raio

    def area(self):
        PI = 3.14159
        area = PI * (self.raio * self.raio)
        return area


raioUsuario = float(input("Insira o valor de raio "))
area = Circulo(raioUsuario).area()
print("A área é:",area)