"""
Funções 

Calculadora de IMC. Crie uma função que calcule o Índice de Massa Corporal (IMC) de uma pessoa. A fórmula do IMC é: 
Uma imagem contendo Interface gráfica do usuário
Descrição gerada automaticamente 
Solicite ao usuário o peso e a altura. 
Chame a função para calcular o IMC. 
Mostre o IMC calculado. 

"""

weight = int(input("Enter your weight"))
height = float(input("Enter your height"))

def function(weight, height, imc):
    imc = weight / (height * height)
    print(imc)
    return

function(weight, height)    