"""
7)	Crie uma função chamada maior_n() que recebe um número inteiro como argumento e retorna o maior número entre
os n números digitados pelo usuário.
"""

# Maior function, this functions the return the biggest number
def maior_n():
    print("The biggest number in the list is:",max(lista))


lista = []
count = 0

while count < 5:
    number = int(input("Enter a number: "))
    lista.append(number)
    count += 1

maior_n()

