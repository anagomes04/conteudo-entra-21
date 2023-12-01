numero = int(input('Informe um número: '))

def calcular_fatorial(numero):
    contador = 1
    fatorial = 1

    if numero < 0:
        return f'Número não pode ser negativo'

    elif numero == 0 or numero == 1:
        return f'Fatorial = 1'

    else:
        while contador <= numero:
            fatorial = contador * fatorial
            contador += 1
        return f'{fatorial}'
print(calcular_fatorial(numero))