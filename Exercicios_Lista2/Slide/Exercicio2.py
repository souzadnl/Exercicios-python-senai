try:
    lista = open ("Lista.txt", "r", encoding="utf-8")
    linhas = lista.readline()
    print(linhas)
except FileNotFoundError:
    print("O arquivo não foi encontrado")