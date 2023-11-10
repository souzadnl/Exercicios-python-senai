import pandas as pd

historico_pedidos = [

    {'ID': 1, 'Nome': 'João', 'Endereço': 'Rua das Flores, 123', 'Produto': 'Camiseta', 'Quantidade': 2, 'Preço': 50, 'Data': '01/01/2023'},

    {'ID': 2, 'Nome': 'Mariana', 'Endereço': 'Avenida Central, 456', 'Produto': 'Tênis', 'Quantidade': 1, 'Preço': 120, 'Data': '02/01/2023'},

    {'ID': 3, 'Nome': 'Carlos', 'Endereço': 'Praça da Estação, 789', 'Produto': 'Mochila', 'Quantidade': 1, 'Preço': 80, 'Data': '03/01/2023'},

    {'ID': 4, 'Nome': 'Fernanda', 'Endereço': 'Alameda dos Anjos, 101', 'Produto': 'Relógio', 'Quantidade': 1, 'Preço': 150, 'Data': '04/01/2023'}

]

for row in historico_pedidos:
    print(row)

dadosExcel = pd.DataFrame(historico_pedidos)
dadosExcel.to_excel("Desafio1.xlsx")


