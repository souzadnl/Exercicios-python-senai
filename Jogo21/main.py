import random
import requests

cartas = {
    "A_ouro": 1, "2_ouro": 2, "3_ouro": 3, "4_ouro": 4, "5_ouro": 5, "6_ouro": 6, "7_ouro": 7, "8_ouro": 8, "9_ouro": 9, "10_ouro": 10, "J_ouro": 10, "Q_ouro": 10, "K_ouro": 10,
    "A_espadilha": 1, "2_espadilha": 2, "3_espadilha": 3, "4_espadilha": 4, "5_espadilha": 5, "6_espadilha": 6, "7_espadilha": 7, "8_espadilha": 8, "9_espadilha": 9, "10_espadilha": 10, "J_espadilha": 10, "Q_espadilha": 10, "K_espadilha": 10,
    "A_copas": 1, "2_copas": 2, "3_copas": 3, "4_copas": 4, "5_copas": 5, "6_copas": 6, "7_copas": 7, "8_copas": 8, "9_copas": 9, "10_copas": 10, "J_copas": 10, "Q_copas": 10, "K_copas": 10,
    "A_zap": 1, "2_zap": 2, "3_zap": 3, "4_zap": 4, "5_zap": 5, "6_zap": 6, "7_zap": 7, "8_zap": 8, "9_zap": 9, "10_zap": 10, "J_zap": 10, "Q_zap": 10, "K_zap": 10
}

response = requests.get("https://deckofcardsapi.com/api/deck/new/draw/?count=52")

if response.status_code == 200:
    data = response.json()
    print(data)
    for i in data:
        print(i)
else:
    print("Erro ao buscar informação do CEP", response.status_code)

print(response.text)
continua = True

carta_sorteada = random.choice(list(cartas.items()))
print(carta_sorteada)