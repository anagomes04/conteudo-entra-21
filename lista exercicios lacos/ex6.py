valor = float(input('Digite o valor a ser financiado: '))
juros = float(input('Digite a taxa de juros mensal: '))
meses = int(input('Digite a quantidade de meses em que a compra vai ser parcelada: '))
amortizacao = input('Digite o tipo de amortização utilizada [1] PRICE [2] SAC: ')

if amortizacao == '2':
    valor_amortizacao = valor / meses
    for i in range(meses):
        valor_parcela = valor_amortizacao + (valor - (i * valor_amortizacao)) * juros/100
        saldo = valor - ((i + 1) * valor_amortizacao)
        juros_pag = valor_parcela - valor_amortizacao
        print(f'Parcela {i + 1}: {valor_parcela}, Amortização: {valor_amortizacao}, Juros: {juros_pag}, Saldo Devedor: {saldo}')
else:
    for i in range(meses):
        valor_parcela = (valor * juros/100) / (1 - 1/(1 + juros/100)**meses)
        saldo = valor - ((i + 1) * valor_parcela)
        juros_pag = pass
        valor_amortizacao = valor_parcela - juros_pag
        print(f'Parcela {i + 1}: {valor_parcela}, Amortização: {valor_amortizacao}, Juros: {juros_pag}, Saldo Devedor: {saldo}')