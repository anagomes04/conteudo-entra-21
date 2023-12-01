numeros = []
num_decrescente = []

while True:
    valor = float(input('Informe um valor: '))

    if valor == 0:
        break

    numeros.append(valor)
    num_decrescente.append(valor)

numeros.sort()

num_decrescente.sort(reverse=True)

print(numeros)
print(num_decrescente)
print(sum(numeros))

media = sum(numeros)/len(numeros)
print(media)