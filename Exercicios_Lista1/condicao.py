print("Verifique se pelo menos uma das condições é verdadeira")
a = int(input("Insira o primeiro valor"))
b = int(input("Insira o segundo valor"))
c = int(input("Insira o terceiro valor"))
d = int(input("Insira o quarto valor"))

if a > c or b < c:
    print("Pelo menos uma das condições são verdadeiras")
elif a > c and b < c:
    print("Ambas são verdadeiras")
else:
    print("Nenhuma condição é verdadeira")