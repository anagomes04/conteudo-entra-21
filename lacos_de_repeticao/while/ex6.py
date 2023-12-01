lista = []

while True:
    valor = float(input('Informe um valor: '))

    if valor < 0:
        break

    lista.append(valor)

    intervalo1 = 0
    intervalo2 = 0
    intervalo3 = 0
    intervalo4 = 0

    for i in lista:

        if i in range(0, 26):
            intervalo1 += 1

        elif i in range(26, 51):
            intervalo2 += 1

        elif i in range(51, 76):
            intervalo3 += 1

        elif i in range(76, 101):
            intervalo4 += 1

    print(intervalo1)
    print(intervalo2)
    print(intervalo3)
    print(intervalo4)