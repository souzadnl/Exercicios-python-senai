import os
import time

import requests
from bs4 import BeautifulSoup

"""
response = requests.get("https://www.adorocinema.com")

soup = BeautifulSoup(response.text, "html.parser")

titulo = soup.title.string
print(titulo)

paragrafos = soup.find_all('a')
for paragrafo in paragrafos:
    paragrafo = paragrafo.text.strip()
    if paragrafo != "":
        print(paragrafo)


cep = input("Insira o seu cep:\n")
url = "https://viacep.com.br/ws/" + cep + "/json/"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print("Erro ao buscar informação do CEP", response.status_code)

"""

response = requests.get("http://www.example.com/")
print(response.text)

soup = BeautifulSoup(response.text, "html.parser")
paragrafos = soup.find_all("p")
print(paragrafos,"\n")
for paragrafo in paragrafos:
    paragrafo = paragrafo.text.strip()
    if paragrafo != "":
        print(paragrafo)