moeda_retirada = int(input('Informe qual moeda você quer comprar (1 - Dólar, 2 - Real, 3 - Euro, 4 - Libra esterlina): '))
moeda_entrada = int(input('Informe qual moeda você quer dar em troca (1 - Dólar, 2 - Real, 3 - Euro, 4 - Libra esterlina): '))
valor = float(input('Informe o valor desejado para compra: '))

# a moeda da frente é sempre a que está valendo 1. ex 1 dólar vale 4.97 reais

cotacao = [
    [1, 4.97, 0.92, 0.78], #dolar_to
    [0.2, 1, 0.18, 0.16], #real_to
    [1.09, 5.41, 1, 0.85], #euro_to
    [1.27, 6.34, 1.17, 1], #libra_to
]

print(f'Valor necessário: {valor * cotacao[moeda_retirada-1][moeda_entrada-1]}')
