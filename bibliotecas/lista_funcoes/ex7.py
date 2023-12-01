valor = float(input('Informe um valor: '))

def maior_valor(valor):
    lista = []
    maior = 0

    while True:
        lista.append(valor)

        if valor == 0:
            break

        for i in lista:

            if i > maior:
                maior = i
                return True

print(maior_valor(valor))