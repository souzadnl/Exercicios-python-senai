from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

link = "file:///C:/Users/53505046817/Documents/Souza/PYTHON/WebScraping/FPOO-Aula16-WebScraping-Pedidos.html"
map = {
    "columns": {
        "xpath": "/html/body/table/thead/tr/th[$NUM$]"
    },
    "lines": {
        "xpath": "/html/body/table/tbody/tr[1]/td[$NUM$]"
    }
}

cabecalho = []
linhas = []
matriz = []

driver = webdriver.Chrome()
driver.minimize_window()
sleep(2)
driver.get(link)

k = 1
x = 1
y = 1
o = 1
linhas = []

for j in range(3):
    coluna = driver.find_element(By.XPATH, map["columns"]["xpath"].replace("$NUM$", f'{k}')).text
    cabecalho.append(coluna)
    k += 1
matriz.append(cabecalho)

for g in range(1):
    for y in range(3):
        linha = driver.find_element(By.XPATH, map["lines"]["xpath"].replace("$NUM$", f"{o}")).text
        linhas.append(linha)
        o += 1
    o = 1
    y = 1
    matriz.append(linhas)

for i in matriz:
    print(i)



