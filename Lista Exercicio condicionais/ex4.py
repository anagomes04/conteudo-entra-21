preco = float(input('Digite o preço: '))
pagamento = input('Digite a forma de pagamento (1 - À vista em dinheiro ou cheque, 2 - À vista no cartão; 3 - Em duas vezes sem juros, 4 - Em duas vezes com juros: ')


if pagamento == '1':
    print(f'Total a pagar: {preco - 0.1 * preco}')
elif pagamento == '2':
    print(f'Total a pagar: {preco - 0.15 * preco}')
elif pagamento == '3':
    print(f'Duas parcelas de: {preco / 2}')
elif pagamento == '4':
    print(f'Duas parcelas de: {preco*1.1/2:.2f}') #para arredondar duas casas depois da virgula
else:
    print('Forma de pagamento não informada')