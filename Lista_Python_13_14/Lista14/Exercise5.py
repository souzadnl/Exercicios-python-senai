from bs4 import BeautifulSoup
import requests

response = requests.get("https://quotes.toscrape.com/")
soup = BeautifulSoup(response.text, "html.parser")

author = soup.find("small", "author")
parent = author.parent
print(parent.find_previous_sibling().get_text())

for line in author:
    uva = line.get_text()
    print(uva)