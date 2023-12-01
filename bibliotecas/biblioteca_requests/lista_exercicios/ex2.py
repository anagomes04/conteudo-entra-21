import requests

url = 'https://jsonplaceholder.typicode.com/posts'

postagem = {
    'userid':1,
    'id': 27,
    'titulo': 'nova postagem',
    'corpo': 'conteúdo'
}

# response = requests.post(url, json=postagem)
#
# print(postagem)

response = requests.post('https://jsonplaceholder.typicode.com/posts', json=postagem)