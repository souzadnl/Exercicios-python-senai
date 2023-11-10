import random

baralho = {
    "A_ouro": 1, "2_ouro": 2, "3_ouro": 3, "4_ouro": 4, "5_ouro": 5, "6_ouro": 6, "7_ouro": 7, "8_ouro": 8, "9_ouro": 9, "10_ouro": 10, "J_ouro": 10, "Q_ouro": 10, "K_ouro": 10,
    "A_espadilha": 1, "2_espadilha": 2, "3_espadilha": 3, "4_espadilha": 4, "5_espadilha": 5, "6_espadilha": 6, "7_espadilha": 7, "8_espadilha": 8, "9_espadilha": 9, "10_espadilha": 10, "J_espadilha": 10, "Q_espadilha": 10, "K_espadilha": 10,
    "A_copas": 1, "2_copas": 2, "3_copas": 3, "4_copas": 4, "5_copas": 5, "6_copas": 6, "7_copas": 7, "8_copas": 8, "9_copas": 9, "10_copas": 10, "J_copas": 10, "Q_copas": 10, "K_copas": 10,
    "A_zap": 1, "2_zap": 2, "3_zap": 3, "4_zap": 4, "5_zap": 5, "6_zap": 6, "7_zap": 7, "8_zap": 8, "9_zap": 9, "10_zap": 10, "J_zap": 10, "Q_zap": 10, "K_zap": 10
}

def sorteio_mao(self):
    # Eu to pegando duas cartas aleatórias da lista e jogando aqui pra dentro
    cartas_jogador = {}
    mao_jogador = 0
    i = 0

    while i < 2:
        carta_sorteada = random.choice(
            list(baralho.items()))  # Pego uma carta aleatória do baralho e chamo de carta sorteada
        mao_jogador = mao_jogador + carta_sorteada[1]  # adiciono o valor dessa carta na mao do jogador
        baralho.pop(carta_sorteada[0])  # retiro essa carta do baralho
        cartas_jogador.update({carta_sorteada})  # adiciono essa carta nas cartas do jogador
        i = i + 1

    print("Suas cartas são:")
    for i in cartas_jogador:
        print(i)
    print("\nVocê tá com", mao_jogador)

    return cartas_jogador, mao_jogador

class Jogador:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.cartas = sorteio_mao(self)


jogador1 = Jogador("daniel", 19)
