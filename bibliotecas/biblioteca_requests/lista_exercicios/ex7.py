import requests

while True:
    response = requests.get('https://api.chucknorris.io/jokes/random?category={category}')
    joke = response['value']
    if 'dollars' in joke:
        print(joke)
        break

#ver api

