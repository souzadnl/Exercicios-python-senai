"""
#Exercicio 9 lista 7
numero = int(input("Insira um valor "))
soma = 0
for i in range(numero + 1):
    soma = soma + i
    print(soma)
print(f"O resultado da soma dos números de 0 a {numero} é",soma)

# Digits of an integer number
chosen_number = input("Enter an integer number to see how many digits does it have!\n")
counter = 0
digits = 0
while(counter<len(chosen_number)):
    digits+=1
    counter+=1
print(f"The number {chosen_number} have {digits} digits.")"""

"""
#Exercicio 9 lista 7
numero = input("Insira um valor ")
digitos = 0
while digitos < len(numero):
    digitos = digitos + 1
print(f"este número tem {digitos} digitos")

#Exercicio 8 lista 7
numero = int(input("Insira um valor "))

resultado = 1
contador = 1

while contador <= numero:
    resultado = resultado * contador
    contador = contador + 1

print(f"O resultado é da fatorial de {numero} é",resultado)

#Exercicio 8 lista 7
print("Insira 5 números e exibiremos o maior e menor")
lista = []
contador = 0

while contador < :
    numero = int(input("Insira um valor "))
    lista.append(numero)
    print(lista)
    contador += 1

print("O menor número é o", min(lista))
print("O maior número é o", max(lista))

#Exercicio 3 lista 7
enesimo = int(input("Insira um valor "))
a1 = 0
a2 = 1
resultado = 0

for i in range(enesimo): #Pra cada numero até o enesimo
    print(resultado)
    resultado = a1 + a2 #Atribuo o resultado desta conta ao resultado
    a1 = a2 #Digo que agora o a1 é o valor do a2, então o a1 agora é agora vale 1
    a2 = resultado #Agora o a2 pega o valor do resultado, que era de 1, e vai recebendo os próximos valores
"""

import random

numero_secreto = random.randint(1, 10)

tentativa1 = int(input("Tente adivinhar o número entre 1 e 10: "))

if tentativa1 == numero_secreto:
    print("Parabéns! Você acertou o número.")
else:
    if tentativa1 < numero_secreto:
        print("Tente novamente. O número é maior.")
    else:
        print("Tente novamente. O número é menor.")

    tentativa2 = int(input("Tente adivinhar novamente: "))

    if tentativa2 == numero_secreto:
        print("Parabéns! Você acertou o número.")
    else:
        print(f"Você errou. O número correto era {numero_secreto}.")

