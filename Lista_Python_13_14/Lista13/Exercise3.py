import csv

with open("alunos.csv", "w", newline="", encoding="utf-8") as arquivo:
    writer = csv.writer(arquivo)
    writer.writerow(["João","20 anos"])
    writer.writerow(["Maria", "22 anos"])