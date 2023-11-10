import json

with open("info.json", "w", encoding="utf-8") as arquivo:
    json.dump({"gato":"Félix", "cachorro":"Rex"}, arquivo, ensure_ascii=False)