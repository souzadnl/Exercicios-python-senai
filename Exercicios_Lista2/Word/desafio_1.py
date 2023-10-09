"""
Contagem Regressiva. Crie uma função chamada contagem_regressiva que receba um número inteiro n. A função deve imprimir
uma contagem regressiva a partir de n até 1 usando recursividade. Após a contagem, imprima “Fim”.
Observação: pesquisa sobre funções recursivas.
"""
import time

number_user = int(input("Enter an integer number: "))

def contagem_regressiva(number):

    if number > 0:
        print(number)
        number_user = number - 1
        time.sleep(1)
        contagem_regressiva(number_user)

contagem_regressiva(number_user)