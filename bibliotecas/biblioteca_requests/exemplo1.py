# import requests
# data = '24-04-2000'
# signo = requests.get(f'https://minha-api-entra-21.jonasreiter.repl.co/{data}').json()
#
# print(signo)

# instalar requests no terminal usando pip
# pip install requests

# importar requests
import requests

# usuário informa quantidade e quais meda será convertida
moeda_local = input('Qual moeda você tem? (responda somente com a abreviação)\n'
                    'real - BRL\n'
                    'euro - EUR\n'
                    'dolar - USD\n'
                    'dólar canadense - CAD\n'
                    'peso chileno - CLP\n').upper()
quantidade = int(input('Quanto você quer converter?\n'))
moeda_destino = input('Para qual moeda você quer converter? (responda somente com a abreviação)\n').upper()

# url será formada com base nas informações passadas
part_url = 'http://economia.awesomeapi.com.br/json/last/'
url = part_url + moeda_local + '-' + moeda_destino
res = requests.get(url).json()

# da informação recebida, precisaremos apenas da cotação para a conversão da moeda
moeda = (res[moeda_local + moeda_destino]['bid'])

# Converção de valores para unidade certa e calculando a conversão
conversao = float(moeda)
valor_final = quantidade * conversao

# print final com informação desejada
print(f'Você terá R${quantidade * conversao:.2f} {moeda_destino}')

#ndpoint => algo que você pode mudar na url