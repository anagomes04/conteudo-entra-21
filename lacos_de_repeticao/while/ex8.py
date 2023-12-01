lista = []

while True:
    ano = int(input('Informe um ano: '))
    lista.append(ano)

    pares = 0
    impares = 0
    bissexto = 0
    futuro = 0
    passado = 0

    for i in lista:

        if i % 2 == 0:
            pares += 1
            print(f'Quantidade de anos pares = {pares}')

        if i % 2 != 0:
            impares += 1
            print(f'Quantidade de anos ímpares = {impares}')

        if i > 2023:
            futuro += 1
            print(f'Quantidade de anos futuros = {futuro}')

        if i <= 2023:
            passado += 1
            print(f'Quantidade de anos passados = {passado}')

        if i % 400 == 0 or (i % 4 == 0 and i % 100 != 0):
            bissexto += 1
            print(f'Quantidade de anos bissexto = {bissexto}')