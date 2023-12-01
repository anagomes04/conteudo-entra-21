moeda_retirada = input('Informe qual moeda você quer comprar (1 - Dólar, 2 - Real, 3 - Euro, 4 - Libra esterlina): ')
moeda_entrada = input('Informe qual moeda você quer dar em troca (1 - Dólar, 2 - Real, 3 - Euro, 4 - Libra esterlina): ')
valor = float(input('Informe o valor desejado para compra: '))

# a moeda da frente é sempre a que está valendo 1. ex 1 dólar vale 4.97 reais

dolar_to_real = 4.97
real_to_dolar = 0.2
euro_to_real = 5.41
real_to_euro = 0.18
libra_to_real = 6.34
real_to_libra = 0.16
dolar_to_euro = 0.92
euro_to_dolar = 1.09
euro_to_libra = 0.85
libra_to_euro = 1.17
dolar_to_libra = 0.78
libra_to_dolar = 1.27

if moeda_retirada == '1' and moeda_entrada == '2':
    print(f'Valor necessário: {valor*dolar_to_real}')
elif moeda_retirada == '1' and moeda_entrada == '3':
    print(f'Valor necessário: {valor * dolar_to_euro}')
elif moeda_retirada == '1' and moeda_entrada == '4':
    print(f'Valor necessário: {valor * dolar_to_libra}')
elif moeda_retirada == '2' and moeda_entrada == '1':
    print(f'Valor necessário: {valor * real_to_dolar}')
elif moeda_retirada == '2' and moeda_entrada == '3':
    print(f'Valor necessário: {valor * real_to_euro}')
elif moeda_retirada == '2' and moeda_entrada == '4':
    print(f'Valor necessário: {valor * real_to_libra}')
elif moeda_retirada == '3' and moeda_entrada == '1':
    print(f'Valor necessário: {valor * euro_to_dolar}')
elif moeda_retirada == '3' and moeda_entrada == '2':
    print(f'Valor necessário: {valor * euro_to_real}')
elif moeda_retirada == '3' and moeda_entrada == '4':
    print(f'Valor necessário: {valor * euro_to_libra}')
elif moeda_retirada == '4' and moeda_entrada == '1':
    print(f'Valor necessário: {valor * libra_to_dolar}')
elif moeda_retirada == '4' and moeda_entrada == '2':
    print(f'Valor necessário: {valor * libra_to_real}')
elif moeda_retirada == '4' and moeda_entrada == '3':
    print(f'Valor necessário: {valor * libra_to_euro}')
else:
    print('Alguma informação está errada ou faltando')

