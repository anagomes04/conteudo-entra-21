import requests
from bs4 import BeautifulSoup
import pandas

site = 'https://www.havan.com.br/eletronicos/games/?cat=133&departamentosHV='

response = requests.get(site)
# print(response)

html = BeautifulSoup(response.text, 'html.parser')

produtos = []
precos = []

for produto in html.select('#categoryProductsGrid .product-item-link'):
    produtos.append(produto.text.strip())

for preco in html.select('#categoryProductsGrid .price-wrapper'):
    preco_ajustado = preco.text.replace('\n', '').replace('R$\xa0', '')
    preco_ajustado = float(preco_ajustado.replace('.','').replace(',', '.'))
    precos.append(preco_ajustado)

dados = zip(produtos, precos)
dados = pandas.DataFrame(dados)

dados.to_csv('havan.csv')