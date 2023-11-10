from bs4 import BeautifulSoup
import requests

response = requests.get("https://quotes.toscrape.com/")
soup = BeautifulSoup(response.text, "html.parser")

title = soup.title.string
print(title)