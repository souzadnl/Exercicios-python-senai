import pandas as pd

def create():
    link = "file:///C:/Users/53505046817/Documents/Souza/PYTHON/WebScraping/Web%20Scraping/FPOO-Formativa-WebScraping_E-commerce.html"

    dfs = pd.read_html(link, encoding="utf-8")
    df = dfs[0]
    df.to_json("JSON.json", orient='records', indent=4, force_ascii=False)

def convert():
    read_file = pd.read_json('JSON.json')
    read_file.to_excel("JSON.xlsx", index=None, header=True)

create()

