import pandas as pd

link = "file:///C:/Users/53505046817/Documents/Souza/PYTHON/WebScraping/Web%20Scraping/FPOO-Formativa-WebScraping_E-commerce.html"

dfs = pd.read_html(link, encoding="utf8")

df = dfs[0]

df.to_excel('python.xlsx', index=False, sheet_name="Teste")

print(dfs)
