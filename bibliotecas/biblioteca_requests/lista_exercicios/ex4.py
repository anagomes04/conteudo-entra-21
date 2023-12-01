import requests

reponse = requests.get('http://shibe.online/api/shibes?count=1&urls=true&httpsUrls=true').json()

print(reponse)