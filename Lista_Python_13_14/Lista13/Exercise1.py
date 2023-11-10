frase = input("Insira uma frase: ")

with open("aula.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write(frase+"\n")
    arquivo.writelines("Python é legal\n")
    arquivo.writelines("Aprendendo python\n")
