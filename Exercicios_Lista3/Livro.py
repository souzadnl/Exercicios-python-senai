"""
Crie uma classe Livro com atributos titulo e autor,
e um método resumo() que imprime ambos.
"""

class Livro:

    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def Resumo(self):
        resumo = f"O nome do livro é {self.titulo}, e o autor que escreveu foi {self.autor}"
        return resumo


titulo = input("Insira o titulo do livro: ")
autor = input("Insira o autor do livro: ")

print(Livro(titulo,autor).Resumo())

