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
