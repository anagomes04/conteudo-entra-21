import requests

site = 'https://api2023--aleticiabg.repl.co/24-04-200'
signo = requests.get(site).json()

print(signo)