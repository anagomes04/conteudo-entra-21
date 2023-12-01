nomes = []

while True:
    nome = input('Digite seu nome: ')

    if nome == 'z':
        break

    nomes.append(nome)

nomes.sort()
print(nomes)

nomes.sort(reverse=True)
print(nomes)

print(len(nomes))

print(nomes.count('carlos'))