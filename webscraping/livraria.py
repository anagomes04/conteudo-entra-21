import requests
from bs4 import BeautifulSoup
import pandas

site = 'https://www.livrariascuritiba.com.br/senhor%20dos%20aneis'

response = requests.get(site)
# print(response)

html = BeautifulSoup(response.text, 'html.parser')

produtos = []
precos = []

for produto in html.select('.box-name'):
    produtos.append(produto.text.strip())

for preco in html.select('.bestPrice'):
    preco_ajustado = preco.text.replace('\n', '').replace('R$', '')
    preco_ajustado = float(preco_ajustado.replace(',', '.'))
    precos.append(preco_ajustado)

dados = zip(produtos, precos)
dados = pandas.DataFrame(dados)

dados.to_csv('livraria.csv')