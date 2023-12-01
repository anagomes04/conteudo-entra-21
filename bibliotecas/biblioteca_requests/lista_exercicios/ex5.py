import requests

url = requests.get('http://shibe.online/api/shibes?count=[1-100]&urls=[true/false]&httpsUrls=[true/false]')

response_code = url.status_code

if response_code == 200:
    print('Página localizada com sucesso')
elif response_code == 404:
    print('Página não encontrada')
elif response_code == 500:
    print('Erro de servidor')

