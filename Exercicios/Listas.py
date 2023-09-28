""""
mensagem = "oi, python"
numero = 5
pi = 3.14

print(mensagem)
print(numero)
print(pi)

nome = input("olá")
print(f"tudo bem {nome}?")
print (pi * numero)

x = 5
y = 10

resultado = x < y
print (resultado)

idade = 25
print("idade", idade)

idade = 25
print(f"Eu tenho {idade} anos")


nome1 = "aula"
nome2 = "Python"

print(f"nome1 = {nome2}")
print(f"nome2 = {nome1}")

nome1 = "aula"
nome2 = "Python"
caixa = ""

print (nome1,nome2)

caixa = nome1
nome1 = nome2
nome2=caixa
print (nome1,nome2)


nome = "Daniel"
sobrenome = "Souza"
nomecompleto = nome +" "+ sobrenome
print(nomecompleto)



valor = 2
valorstring = (f"{valor}")
print(valorstring)

valor = 12
valorstring = str(valor)
print(valorstring)


valorinteiro = 5
valorfloat = float(valorinteiro)
print(valorfloat)

valorinteiro = input("Digite o número")
valorfloat = float(valorinteiro)
print(valorfloat)

lado = int(input("Digite o valor de uma das laterais"))
resultado = lado * 2
print(f"A área do quadrado é {resultado}")

lado1 = int(input("Digite o valor do lado 1"))
lado2 = int(input("Digite o valor do lado 2"))
resultado = lado1 * lado2
print(f"A área do Retangulo é {resultado}")



principal = "strogonoff de frango"
acompanhamento = "arroz"
salada = "alface"

print(f"Hoje vou preparar {principal} com {acompanhamento} e salada de {salada}")

prato = input("Escolha seu prato favorito")
bebida = input("O que deseja beber?")
print(f"Aqui está! {prato} e {bebida}. Bom apetite!")



print("Hoje vou fazer"+" "+principal+" "+"com"+" "+acompanhamento+" "+"e salada de"+" "+salada)


dia = int(input("Digite o dia que você nasceu "))
mes = int(input("Digite o mes que você nasceu "))
ano = int(input("Digite o ano que você nasceu "))

data = (f"{dia:02}/{mes:02}/{ano}")
print(data)

#Exercicio 1 PI
PI = 3.14159265358979323846
print (f"o valor de pi é: {PI}")

#Exercicio 2 NOME
nome = input("Digite seu nome ")
print(nome)

#Exercicio 3 NOME COMPLETO
nome = input("Insira seu primeiro nome ")
sobrenome = input("Insira seu sobrenome ")

nomeCompleto = (f"{nome} {sobrenome}")
print(nomeCompleto)

#Exercicio 4 CONVERSAO DE VARIAVEIS
a = "sopa"
b = "doce"
caixa = ""

caixa = a
a = b
b = caixa
print(a, b)

#Exercicio 5 DIVIDA
saldo = int(input("Digite seu saldo "))
divida = int(input("Digite sua divida "))

print(saldo - divida)

#Exercicios 6 NOME FSTRING
nome = input("Insira seu nome")
idade = input("Insira sua idade")
print(f"Olá {nome}, fiquei sabendo que você tem {idade} anos, é verdade?")

#DESAFIO

a = int(input("Insira o valor de A "))
b = int(input("Insira o valor de B "))

a, b = b, a
print(a, b)


frase = input("Escreva uma frase ")
caracteres = int(input("Digite a quantidade dos primeiros caracteres que deseja coletar "))

print(frase[:caracteres])

frase = input("Escreva uma frase ")
procurar = input("Digite a palavra que procura")
print(frase.split())

#CILINDRO
PI = 3.14159

raio = int(input("Insira o valor do raio "))
altura = int(input("Insira o valor da altura "))

areaBase = PI * (raio*raio)
volume = (areaBase * altura)

print(f"A área da base é: {areaBase}")
print(f"O volume é: {volume}")


frase = input("Insira uma frase ")
fraseMinuscula = (frase.lower())
print(fraseMinuscula)


frase = input("Insira uma frase ")
fraseMaiuscula = (frase.upper())
print(fraseMaiuscula)

frase = input("Insira uma frase ")
fraseStrip = (frase.strip())
print(fraseStrip)

frase = input("Insira uma frase ")
print("A frase que você digitou foi: ", frase)
palavraAntiga = input("Escreva a palavra antiga que deseja substituir ")
palavraNova = input("Insira a palavra nova para substituir ")

print(frase.replace(palavraAntiga, palavraNova))


#exercicio 1 lista 4
PI = float(input("Insira o valor de PI "))
print("O valor de PI é", PI)

#exercicio 2 lista 4
frase = input("Insira sua frase ")
print("Sua frase tem ", (len(frase)), " caracteres")

#exercicio 3 lista 4
frase = input("Insira sua frase")
ocorrencia = input("Insira o caracter que deseja substituir")
novaLetra = input("Digite a letra que deseja inserir no local")

print(frase.replace(ocorrencia, novaLetra))

#exercicio 4 lista 4
frase = "Python é uma linguagem de alto nível"
print('A letra "a" aparece ', frase.count("a"), "vezes" )

#exercicio Desafio 1 lista 4
frase = input("Insira a palavra que deseja saber se é palindromo ")
fraseInvertida = frase[::-1]
palindromo = (frase == fraseInvertida)
print(palindromo)

#exercicio Desafio 2 lista 4
frase = input("Insira sua frase ")
ocorrencia = input("Insira a letra que deseja saber quantas vezes aparece na frase inserida ")

print("A letra", ocorrencia.upper(), "aparece", frase.count(ocorrencia), "na frase inserida")

#exercicio 1 lista 5
num1 = int(input("Digite um número "))
num2 = int(input("Digite outro número "))
print("A soma desses números é", (num1 + num2))

#exercicio 2 lista 5
print("Dada a expressão (10 * 3) - (8 / 2), o resultado desta expressão é ")
print((10 * 3) - (8 / 2))

#exercicio 3 lista 5
numero = int(input("Digite um número "))
if numero % 2 == 0 :
    {
        print("O número é par ")
    }
else :
    {
        print("O número é impar ")
    }

#exercicio 5 lista 5
numero = int(input("Insira o número desejado "))
absoluto = abs(numero)

print("O valor absoluto deste número é ", abs(absoluto))



conta1 = 1 > 3
conta2 = 2 < 4

if (conta1 == True && conta2 == True)

        print("Ambas são verdadeiras")

else:
        print("Um ou ambos não são verdadeiros")

credencial = "diit"
usuario = input("Insira sua credencial")

cred = usuario.strip() and usuario.lower()
if cred == credencial:
    print("Acesso autorizado")
else:
    print("Acesso negado")


x = int(input("Insira o valor de X "))
y = int(input("Insira o valor de Y "))
z = int(input("Insira o valor de Z "))

if (x == 0) or (y == 0) or (z == 0):
    print("Pelo menos uma é verdadeira")
else:
    print("Nenhuma é verdadeira")

m = int(input("Digite o valor de M "))
n = int(input("Digite o valor de N "))

if (m % 2 == 1) or (n % 2 == 1):
    print("No mínimo um dos valores é impar")
else:
    print("Nenhum valor é ímpar")

#exercicio 6 lista 5
num1 = int(input("Insira o primeiro valor "))
num2 = int(input("Insira o segundo valor "))

if (num1 % 2 == 0) and (num2 % 2 == 0):
    print("Ambos os valores são pares")
else:
    print("Um ou ambos os valores NÃO são pares")

#exercicio 7 lista 5
x = int(input("Insira o valor de X "))
y = int(input("Insira o valor de Y "))
z = int(input("Insira o valor de Z "))

print((x + y + z) / 3)


prestacao = int(input("Insira o valor da prestação "))
prestacaoJuros = (prestacao + (prestacao * 0.1))

print("O valor da prestação com juros é de R$", prestacaoJuros)

#exercicio 8 lista 5
num1 = int(input("Insira o valor do número "))

if num1 >= 0:
    print("O valor inserido é positivo")
else:
    print("O valor inserido é negativo")

#exercicio 9 lista 5
valor1 = int(input("Insira o valor1 "))
valor2 = int(input("Insira o valor2 "))

if (valor1+15) == (valor2*3):
    print("O valor é verdadeiro")
else:
    print("O valor é falso")

#exercicio 11 lista 5
celcius = int(input("Insira o valor em Celcius"))
fahrenheit = ((celcius * 9/5) + 32)

print(fahrenheit)

##Exercício 12 lista 5
print("Descubra seu IMC")

altura = float(input("Digite sua altura: "))
peso = float(input("Digite sua peso: "))
imc = round(peso / (altura * altura), 2)

if imc > 40:
    print(f"Seu IMC é {imc}")
    print("Obesidade III")
elif imc > 35:
    print(f"Seu IMC é {imc}")
    print("Obesidade II")
elif imc > 30:
    print(f"Seu IMC é {imc}")
    print("Obesidade I")
elif imc > 18.6:
    print(f"Seu IMC é {imc}")
    print("Peso ideal")
else:
    print(f"Seu IMC é {imc}")
    print("Abaixo do peso")

#Exercicio 13 lista 5
n1 = int(input("Insira a primeira nota"))
n1ponderada = int(input("Insira o peso da primeira nota"))
n2 = int(input("Insira a segunda nota"))
n2ponderada = int(input("Insira o peso da segunda nota"))
n3 = int(input("Insira a terceiro nota"))
n3ponderada = int(input("Insira o peso da terceira nota"))

media = ((n1 * n1ponderada) + (n2 * n2ponderada) + (n3 * n3ponderada)) / (n1ponderada + n2ponderada + n3ponderada)
print("A média ponderada é:",round(media))

#Exercicio 14 lista 5

numero = int(input("Insira um valor"))
expoente = int(input("Insira um expoente"))
potencia = numero ** expoente

print("A potencia desta operação é", potencia)

idade = int(input("Insira sua idade "))

if idade >= 18:
    print("Você é maior de idade")
else:
    print("Você é menor de idade")

nota = float(input("Insira a nota do aluno "))

#Desafio 1 lista 5
numero = float(input("Insira um valor "))
potencia = numero ** (1/3)

print("A potencia desta operação é {:.2f}".format(potencia))

#Desafio 2 lista 5
capital = float(input("Insira o valor de capital "))
juros = float(input("Insira o valor de juros "))
anos = int(input("Insira a quantidade de anos "))
meses = anos * 12

compostos = (capital * (juros + 1)) * meses

print(compostos)

///////

if   nota >= 9:
    print("Excelente!")
elif nota >= 7:
    print("Boa")
elif nota >= 5:
    print("Média")
else:
    print("Insuficiente")

3) Peça um número para o usuário e imprima se ele é par ou ímpar. E se é múltiplo de 3 e se é múltiplo de 5.

numero = int(input("Insira um número "))

if (numero % 2) == 0:
    print(f"{numero} é par")
else:
    print(f"{numero} é ímpar")

if (numero % 3 == 0):
    print("O número é múltiplo de 3")
else:
    print("O número não é múltiplo de 3")

if (numero % 5 == 0):
    print("O número é múltiplo de 5")
else:
    print("O número não é múltiplo de 5")

    Peça 5 números para o usuário imprima qual o maior.



n1 = int(input("Insira o valor do número 1 "))
n2 = int(input("Insira o valor do número 2 "))
n3 = int(input("Insira o valor do número 3 "))
n4 = int(input("Insira o valor do número 4 "))
n5 = int(input("Insira o valor do número 5 "))
maior

n1 = int(input("Insira o valor do número 1 "))
n2 = int(input("Insira o valor do número 2 "))
n3 = int(input("Insira o valor do número 3 "))
n4 = int(input("Insira o valor do número 4 "))
n5 = int(input("Insira o valor do número 5 "))

lista = [n1, n2, n3, n4, n5]
print("O menor número da lista é", (min(lista)))
print("O maior número da lista é", (max(lista)))

idade= int(input("Insira sua idade : "))
if idade <=2:
    print("CLASSIFICAÇÃO: Bebê")
elif idade <13:
    print("CLASSIFICAÇÃO: Criança")
elif idade <18:
    print("CLASSIFICAÇÃO: Adolescente")
elif idade <60:
    print("CLASSIFICAÇÃO: Adulto")
else:
    print("CLASSIFICAÇÃO: Idoso")

Conversor de Unidades. Escreva um programa que permite ao usuário escolher entre converter uma temperatura de Celsius para Fahrenheit ou vice-versa. Solicite o valor e execute a conversão.

print("Escolha a opção desejada \n Caso queira converter de Celsius para Fahrenheit digite [1] \n Caso queira converter de Fhrenheit para Celsius digite [2]")
escolha = int(input("Digite a opção "))
temperatura = int(input("Insira a temperatura "))

celsiusToFarenheit = (((9 / 5) * temperatura) + 32)
fahrenheitToCelsius = ((temperatura - 32) * 5 / 9)

match escolha:
    case 1:
        print(celsiusToFarenheit)
    case 2:
        print(fahrenheitToCelsius)

Verificação de Triângulo. Crie um programa que solicita três comprimentos e determina se esses comprimentos podem formar um triângulo. Se sim, classifique-o como equilátero, isósceles ou escaleno.

largura1 = int(input("Insira o valor da primeira largura "))
largura2 = int(input("Insira o valor da segunda largura "))
largura3 = int(input("Insira o valor da terceira largura "))

if largura1 == largura2 == largura3:
    print("É um triângulo equilátero")
elif (largura1 == largura2) or (largura2 == largura3) or (largura1 == largura3):
    print("É um triângulo isósceles")
else:
    print("É um triângulo escaleno")

Crie um programa em Python para um banco que avalia a elegibilidade de empréstimos com base na idade e renda mensal dos clientes. As regras são:

Clientes com 18 anos ou mais podem pedir um empréstimo se tiverem renda mensal acima de R$1500,00.

Menores de 18 anos podem obter um empréstimo se tiverem renda mensal acima de R$ 1000.

Utilize estruturas condicionais aninhadas para implementar essa análise e exiba se o cliente é elegível e sob qual condição.

print("Descubra se você pode solicitar um empréstimo no banco Souzáro \n")
idade = int(input("Insira sua idade "))
renda = int(input("Insira o valor da sua renda mensal "))

if idade
"""
from time import sleep

"""
#Exercicio 3 lista 6
quantidade = int(input("Insira a quantidade de produtos que deseja levar"))
valor = int(input("Insira o valor do produto"))
desconto_maior = (quantidade * valor) * 0.1
desconto_menor = (quantidade * valor) * 0.05

if quantidade > 100:
    print("O total da compra com desconto é", (quantidade*valor) + desconto_maior)
else:
    print("O total da compra com desconto é", (quantidade*valor) + desconto_menor)

#Exercicio 4 lista 6
print("Descubra se você está apto para votar")
idade = int(input("Insira sua idade"))

if idade < 16:
    print("Não eleitor")
elif idade < 18:
    print("Facultativo")
else:
    print("Obrigatório") 

#Exercicio 5 lista 6
idade1 = int(input("Insira a primeira idade"))
idade2 = int(input("Insira a segunda idade"))
idade3 = int(input("Insira a terceira idade"))
lista = []

lista.append(idade1)
lista.append(idade2)
lista.append(idade3)
print("A menor idade é",min(lista),"e a maior idade é", max(lista))

#Exercicio 6 lista 6
print("Que horas são?")
hora = int(input("Insira a hora"))
minutos = int(input("Insira os minutos"))
segundos = int(input("Insira os segundos"))
print(f"A hora inserida foi {hora}:{minutos}:{segundos}")

if (hora >= 0 and hora <=24) and (minutos >= 0 and minutos <= 60) and (segundos >= 0 and segundos <= 60):
    print("A hora inserida é válida")
else:
    print("Inválida")

#Exercicio 7 lista 6
nota = int(input("Insira sua nota "))

if nota < 3:
    print("Sua nota é E")
elif nota < 5:
    print("Sua nota é D")
elif nota < 7:
    print("Sua nota é C")
elif nota < 9:
    print("Sua nota é B")
else:
    print("Sua nota é A")
    
    
#Exercicio 8 lista 6
lado1 = int(input("Insira o valor do lado 1"))
lado2 = int(input("Insira o valor do lado 2"))
lado3 = int(input("Insira o valor do lado 3"))
lado4 = int(input("Insira o valor do lado 4"))

if lado1 == lado2 == lado3 == lado4:
    print("É um quadrado")
elif lado1 == lado2 == lado3 or lado2 == lado3 == lado4 or lado4 == lado1 == lado2 or lado1 == lado3 == lado4:
    print("Não é nenhum dos dois")
elif (lado1 == lado2 and lado3 == lado4) or (lado3 == lado1 and lado2 == lado4) or (lado1 == lado4 and lado2 == lado3):
    print("É um retângulo")
else:
    print("Não é nenhum dos dois")
    
#Exercicio 9 lista 6
print("Insira dois números com casas decimais, exemplo 1.99")
numero1 = float(input("Insira o primeiro número"))
numero2 = float(input("Insira o segundo número"))


print("Agora escolha a operação que deseja realizar")
print("Digite somente o caractere da operação desejada\n[+] Adição\n[-] Subtração\n[/] Divisão\n[*] Multiplicação")
escolha = input()

match escolha:
    case '+':
        print(f"O resultado da operação {numero1} + {numero2} é", numero1 + numero2)
    case '-':
        print(f"O resultado da operação {numero1} - {numero2} é", numero1 - numero2)
    case '/':
        print(f"O resultado da operação {numero1} / {numero2} é", numero1 / numero2)
    case '*':
        print(f"O resultado da operação {numero1} * {numero2} é", numero1 * numero2)

#Exercicio 10 lista 6
nota1 = int(input("Insira o valor da primeira nota"))
nota2 = int(input("Insira o valor da segunda nota"))
nota3 = int(input("Insira o valor da terceira nota"))

notas = (nota1, nota2, nota3)
menor = min(notas)
media = (((nota1 + nota2 + nota3) - menor) / 2)
print(media)

#Desafio lista 6
import random
import time


def jogo():
    print("JOGUE O JOGÃO DA ADVINHAÇÃO\nO seu objetivo é acertar o número que foi sorteado pela máquina\nVocê tem 2 chances\nO número sorteado será um número entre 1 e 10. Boa Sorte!!!")

    for i in range(3,0, -1):
        print(f"O jogo começará em {i}")
        time.sleep(1)

def sorteio():
    cpu = random.randint(1, 10)
    return cpu


def checagem():

    numeroSorteado = sorteio()
    print(numeroSorteado)
    numeroUsuario = int(input("Valendo! Chute o número sorteado"))

    if True:
        if numeroSorteado == numeroUsuario:
            print("VOCÊ ACERTOU!!")
        else:
            print("Você ERROU")
            if numeroUsuario < numeroSorteado:
                print("O número que você escolheu é menor que o número sorteado")
            else:
                print("O número que você escolheu é maior que o número sorteado")

            numeroUsuario = int(input("Chute outro número!\n"))
            if numeroUsuario == numeroSorteado:
                print("VOCÊ ACERTOU!!!")
            else:
                print("GAME OVER")
                print(f"O número sorteado foi {numeroSorteado}")

jogo()
checagem()

#Exercicio 1 lista 10
for i in range(1,11):
    print(i)

for i in range(numero + 1):
    soma = soma + i
    print(soma)

print(soma)

#Exercicio 2 lista 10
print("Descubra a soma dos primeiros números até o número escolhido")
numero = int(input("Insira um número "))
soma = 0
contador = 1

while contador < numero +1:
    soma = soma + contador
    contador = contador + 1

print(soma)

#Exercicio 5 lista 7
numero = int(input("Insira um valor "))
print(f"Esta é a tabuada do {numero}:")
for i in range(11):
    print(f"{numero} x {i} = ",(numero * i))
    
#Exercicio 6 lista 7
numero = int(input("Insira um valor "))
multiplicador = numero

while numero > 0:
    numero = numero - 1

    print(numero)

#Exercicio 7 lista 7
print("Descubra os números pares dentro de um intervalo")
numero = int(input("Insira um valor "))

for i in range(2, numero, 2):
    print(i)
"""



