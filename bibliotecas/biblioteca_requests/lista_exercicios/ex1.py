import requests

data = requests.get('https://jsonplaceholder.typicode.com/users').json()

for user in data:
    print(f'Nome:{user["username"]}')

#usar chave que já estava na api