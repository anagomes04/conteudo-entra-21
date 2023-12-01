import requests

id_post = 1

url = f'https://jsonplaceholder.typicode.com/users/{id_post}'

response = requests.delete(url)

if response.status_code == 200:
    print(f'Postagem com ID {id_post} foi excluída com sucesso')