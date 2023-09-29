"""
Try / Except 

Tratamento de Erro Básico: Use try/except para tratar o erro no código abaixo. 

x = int(input("Enter a number: ")) #Digite uma letra. 

x = x + 10 

print(x) #A resposta precisa ser um número. 
"""

try:
    number = int(input("Enter a number: "))
    number = number + 10
    print(number)
except ValueError:
    print("The value must be a number") 
    