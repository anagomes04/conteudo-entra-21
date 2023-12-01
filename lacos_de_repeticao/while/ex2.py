numero = int(input('Informe um número: '))
contador = 1
fatorial = 1

if numero < 0:
    print('Número não pode ser negativo')

elif numero == 0 or numero == 1:
    print('Fatorial = 1')

else:
    while contador <= numero:
        fatorial = contador * fatorial
        contador += 1
    print(fatorial)