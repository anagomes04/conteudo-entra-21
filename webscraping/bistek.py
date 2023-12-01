import requests
from bs4 import BeautifulSoup
import pandas
import arrow


site = 'https://loja17.bistek.com.br/carnes.html?cat=1037'

data = arrow.now().format('YYYY-MM-DD')

response = requests.get(site)

# print(response)
#response = 200 -> que deu certo o acesso

# print(response.text)
#printa o html da página


html = BeautifulSoup(response.text, 'html.parser')
#objeto de uma classe = instância

produtos = []
precos = []

for produto in html.select('.product-item-link'):
    produtos.append(produto.text.strip())

for preco in html.select('.weee'):
    preco_ajustado = preco.text.replace('\n', '').replace('R$\xa0', '')
    preco_ajustado = float(preco_ajustado.replace(',', '.'))
    precos.append(preco_ajustado)

dados = zip(produtos, precos)
dados = pandas.DataFrame(dados)

# dados.to_csv('bistek.csv')

# dados.to_excel('dados bistex.xlsx', header=False, index=False)
dados.to_excel(f'dados bistex{data}.xlsx', header=False, index=False)
