import pandas as pd

def create():
    link = "file:///C:/Users/53505046817/Documents/Souza/PYTHON/WebScraping/Web%20Scraping/FPOO-Formativa-WebScraping_E-commerce.html"

    dfs = pd.read_html(link, encoding="utf8")
    df = dfs[0]
    df.to_csv('CSV.csv')
    print(dfs)

def convert():
    read_file = pd.read_csv("CSV.csv")
    read_file.to_excel("CSV.xlsx", index=None, header=True)

create()

