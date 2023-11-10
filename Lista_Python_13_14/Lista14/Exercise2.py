from bs4 import BeautifulSoup
import requests

response = requests.get("https://quotes.toscrape.com/")
soup = BeautifulSoup(response.text, "html.parser")

citacoes = soup.find_all("span", "text")
for line in citacoes:
    print(line)
