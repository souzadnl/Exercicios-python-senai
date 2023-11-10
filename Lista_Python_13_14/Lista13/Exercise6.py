import json

with open("info.json", "r", encoding="utf-8") as arquivo:
    reader = json.load(arquivo)
    print(reader)