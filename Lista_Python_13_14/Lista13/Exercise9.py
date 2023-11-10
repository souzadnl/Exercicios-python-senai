import pandas as pd

dados = ({
    "Aluno":["Aluno1", "Aluno2"],
    "Matemática": [10, 6],
    "Português": [8, 9]
})

dadosExcel = pd.DataFrame(dados)
dadosExcel.to_excel("notas.xlsx")
print(dados)

