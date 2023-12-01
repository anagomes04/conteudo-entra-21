from selenium import webdriver
from time import sleep

navegador = webdriver.Edge()
link = 'https://www.formula1.com'
navegador.get(link)

sleep(5)
dados = (navegador.find_elements('xpath', '//*[contains(concat( " ", @class, " " ), concat( " ", "f1--s", " " ))]'))

for noticia in dados:
    print(noticia.text)
