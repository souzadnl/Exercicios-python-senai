from bs4 import BeautifulSoup
import requests

response = requests.get("https://quotes.toscrape.com/")
soup = BeautifulSoup(response.text, "html.parser")

author = soup.find_all("small", "author")
for line in author:
    print(line.get_text())