nomes = open('nomes.txt.txt', 'r').read().splitlines()
emails = open('emails.txt', 'r').read().splitlines()

# print(nomes.txt)
# print(emails)

geral = dict(zip(nomes, emails))
print(geral)

ordem_alfabetica = sorted(geral.items())
print(ordem_alfabetica)
#ordem dos nomes.txt