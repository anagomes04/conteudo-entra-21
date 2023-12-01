import requests

site = 'https://apiex--aleticiabg.repl.co/8driv'
casa = requests.get(site).json()

print(casa)