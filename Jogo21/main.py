import random

baralho = {
    "A_ouro": 1, "2_ouro": 2, "3_ouro": 3, "4_ouro": 4, "5_ouro": 5, "6_ouro": 6, "7_ouro": 7, "8_ouro": 8, "9_ouro": 9, "10_ouro": 10, "J_ouro": 10, "Q_ouro": 10, "K_ouro": 10,
    "A_espadilha": 1, "2_espadilha": 2, "3_espadilha": 3, "4_espadilha": 4, "5_espadilha": 5, "6_espadilha": 6, "7_espadilha": 7, "8_espadilha": 8, "9_espadilha": 9, "10_espadilha": 10, "J_espadilha": 10, "Q_espadilha": 10, "K_espadilha": 10,
    "A_copas": 1, "2_copas": 2, "3_copas": 3, "4_copas": 4, "5_copas": 5, "6_copas": 6, "7_copas": 7, "8_copas": 8, "9_copas": 9, "10_copas": 10, "J_copas": 10, "Q_copas": 10, "K_copas": 10,
    "A_zap": 1, "2_zap": 2, "3_zap": 3, "4_zap": 4, "5_zap": 5, "6_zap": 6, "7_zap": 7, "8_zap": 8, "9_zap": 9, "10_zap": 10, "J_zap": 10, "Q_zap": 10, "K_zap": 10
}

class Mesa:

    def sorteio_mao(self):
        # Eu to pegando duas cartas aleatórias da lista e jogando aqui pra dentro
        cartas_jogador = {}
        mao_jogador = 0
        i = 0

        while i < 2:
            carta_sorteada = random.choice(list(baralho.items()))  # Pego uma carta aleatória do baralho e chamo de carta sorteada
            mao_jogador = mao_jogador + carta_sorteada[1]  # adiciono o valor dessa carta na mao do jogador
            baralho.pop(carta_sorteada[0])  # retiro essa carta do baralho
            cartas_jogador.update({carta_sorteada})  # adiciono essa carta nas cartas do jogador
            i = i + 1

        print("Suas cartas são:")
        for i in cartas_jogador:
            print(i)
        print("\nVocê tá com",mao_jogador)


        return cartas_jogador

    def apresentacao(self):
        return "JOGUE AGORA O 21 DO SOUZA!\nO objetivo é chegar mais próximo do número 21 sem estourar\nÉ assim que se joga:\n1 - Cada jogador receberá duas cartas\n2 - O jogador escolherá se compra mais uma carta ou para\n3 - Se ambos pararem, ganha quem tiver mais próximo de 21\n4 - Se o jogador estourar ele perde\n"

    def cadastro_login(self):
        print("Você deseja logar ou cadastrar uma nova conta?(logar/cadastrar)")
        escolha = input()
        match (escolha.lower()):
            case "logar":
                Mesa.logar()
            case "cadastrar":
                Mesa.cadastrar()

    def apresentacao_pessoal(self, nome):
        return (f"Olá {nome.capitalize()}, Seja bem vindo ao 21!")

    def logar(self):

        print("Seja bem vindo a área de login")
        nome_login = "Daniel"
        email_login = "daniel@gmail.com"
        senha_login = 123

        while True:
            nome = input("Insira seu nome: ")
            email = input("Insira seu email: ")
            senha = int(input("Insira sua senha: "))

            if nome.capitalize() == nome_login and email == email_login and senha == senha_login:
                print(Mesa.apresentacao_pessoal(self,nome))
                break
            else:
                print("Login inválido\n")

    def cadastrar(self):
        print("Seja bem vindo a área de cadastro")
        while True:
            idade = int(input("Insira sua idade: "))
            if idade > 17:
                nome = input("Insira seu nome: ")
                email = input("Insira seu email: ")
                senha = int(input("Insira sua senha: "))

                jogador1 = Jogador(nome, idade, email, senha)
                print(Mesa.apresentacao_pessoal(Mesa, nome))
                break
            else:
                print("Vish! Este jogo só é permitido para maiores de 18\n")

class Jogador:

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.cartas = Mesa.sorteio_mao(self)





jogador1 = Jogador("Daniel", 19)
print(jogador1.nome)
print(jogador1.cartas)




