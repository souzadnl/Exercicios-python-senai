# forca
tentativas = 6
tentativasUsuario = []
ganhou = False

palavraUsuario = input("Insira uma palavra para ser adivinhada: ").lower()

while True:
    palavraRevelada = ""

    for letra in palavraUsuario:
        if letra in tentativasUsuario:
            palavraRevelada += letra
        else:
            palavraRevelada += "_"

    print("\nPalavra a ser adivinhada:", palavraRevelada)
    print("Tentativas restantes:", tentativas)

    if ganhou or tentativas == 0:
        break

    tentativa = input("Chute uma letra: ").lower()

    if tentativa in tentativasUsuario:
        print("Você já tentou essa letra. Tente novamente.")
        continue

    tentativasUsuario.append(tentativa)

    if tentativa not in palavraUsuario:
        tentativas -= 1

    ganhou = all(letra in tentativasUsuario for letra in palavraUsuario)

    if ganhou:
        print("\nParabéns! Você venceu. A palavra era:", palavraUsuario)
    elif tentativas == 0:
        print("\nFim de jogo! Você perdeu. A palavra era:", palavraUsuario)


taxa_reproducao = float(input("Taxa de reprodução (porcentagem): ")) / 100
taxa_mortalidade = float(input("Taxa de mortalidade (porcentagem): ")) / 100
populacao = int(input("Número inicial de coelhos: "))
geracoes = int(input("Número de gerações a simular: "))

for geracao in range(geracoes):
    novos_coelhos = populacao * taxa_reproducao
    mortes = populacao * taxa_mortalidade
    populacao = populacao + novos_coelhos - mortes
    print(f"Geração {geracao + 1}: {populacao:.0f} coelhos")

print(f"População após {geracoes} gerações: {populacao:.0f} coelhos")

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