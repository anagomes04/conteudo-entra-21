from selenium import webdriver
from time import sleep

navegador = webdriver.Edge()
link = 'https://www.formula1.com/en/latest/all.html'
navegador.get(link)

sleep(5)
dados = (navegador.find_elements('xpath', '//*[(@id = "article-list")]//*[contains(concat( " ", @class, " " ), concat( " ", "no-margin", " " ))]'))

for i, noticia in enumerate(dados):
    print(i+1, '-', noticia.text)
