import csv

with open("alunos.csv", "r", encoding="utf-8") as arquivo:
    reader = csv.reader(arquivo)
    for row in reader:
        print(row)