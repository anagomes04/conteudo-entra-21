idade = int(input('Informe dua idade: '))
sangue = input('Informe seu tipo sanguíneo A+ (1), A- (2), B+ (3), B- (4), O+ (5), O- (6), AB+ (7), AB- (8): ')
pergunta = input('Quer doar (1) ou retirar (2)? ')
if pergunta == '2':
    qtde_bolsas = int(input('Informe a quantidade de bolsas que deseja retirar: '))

estoque_AP = 17
estoque_AN = 12
estoque_BP = 1
estoque_BN = 3
estoque_OP = 9
estoque_ON = 22
estoque_ABP = 23
estoque_ABN = 11

estoque_geral = estoque_AP + estoque_AN + estoque_BP + estoque_BN + estoque_OP + estoque_ON + estoque_ABP + estoque_ABN

if idade < 0:
    print('Idade não pode ser negativa')
elif idade >= 65 and pergunta == '1':
    print('Não pode doar')
elif estoque_geral >= 200 and pergunta == '1':
    print('Estoque cheio')
elif pergunta == '1' and sangue == '1':
    print('Pode doar')
    print(f'Estoque A+: {estoque_AP+1}')
elif pergunta == '1' and sangue == '2':
    print('Pode doar')
    print(f'Estoque A-: {estoque_AN+1}')
elif pergunta == '1' and sangue == '3':
    print('Pode doar')
    print(f'Estoque B+: {estoque_BP+1}')
elif pergunta == '1' and sangue == '4':
    print('Pode doar')
    print(f'Estoque B-: {estoque_BN + 1}')
elif pergunta == '1' and sangue == '5':
    print('Pode doar')
    print(f'Estoque O+: {estoque_OP + 1}')
elif pergunta == '1' and sangue == '6':
    print('Pode doar')
    print(f'Estoque O-: {estoque_ON + 1}')
elif pergunta == '1' and sangue == '7':
    print('Pode doar')
    print(f'Estoque AB+: {estoque_ABP + 1}')
elif pergunta == '1' and sangue == '8':
    print('Pode doar')
    print(f'Estoque AB-: {estoque_ABN + 1}')
elif pergunta == '2' and qtde_bolsas % 5 != 0:
    print('Quantidade de bolsas para retirar deve ser múltiplo de 5')
elif pergunta == '2' and sangue == '1' and qtde_bolsas > estoque_AP:
    print('Quantidade de bolsas insuficiente para retirar')
elif pergunta == '2' and sangue == '2' and qtde_bolsas > estoque_AN:
    print('Quantidade de bolsas insuficiente para retirar')
elif pergunta == '2' and sangue == '3' and qtde_bolsas > estoque_BP:
    print('Quantidade de bolsas insuficiente para retirar')
elif pergunta == '2' and sangue == '4' and qtde_bolsas > estoque_BN:
    print('Quantidade de bolsas insuficiente para retirar')
elif pergunta == '2' and sangue == '5' and qtde_bolsas > estoque_OP:
    print('Quantidade de bolsas insuficiente para retirar')
elif pergunta == '2' and sangue == '6' and qtde_bolsas > estoque_ON:
    print('Quantidade de bolsas insuficiente para retirar')
elif pergunta == '2' and sangue == '7' and qtde_bolsas > estoque_ABP:
    print('Quantidade de bolsas insuficiente para retirar')
elif pergunta == '2' and sangue == '8' and qtde_bolsas > estoque_ABN:
    print('Quantidade de bolsas insuficiente para retirar')
elif pergunta == '2' and sangue == '1':
    print('Pode retirar')
    print(f'Estoque A+: {estoque_AP - qtde_bolsas}')
elif pergunta == '2' and sangue == '2':
    print('Pode retirar')
    print(f'Estoque A-: {estoque_AN - qtde_bolsas}')
elif pergunta == '2' and sangue == '3':
    print('Pode retirar')
    print(f'Estoque B+: {estoque_BP - qtde_bolsas}')
elif pergunta == '2' and sangue == '4':
    print('Pode retirar')
    print(f'Estoque B-: {estoque_BN - qtde_bolsas}')
elif pergunta == '2' and sangue == '5':
    print('Pode retirar')
    print(f'Estoque O+: {estoque_OP - qtde_bolsas}')
elif pergunta == '2' and sangue == '6':
    print('Pode retirar')
    print(f'Estoque O-: {estoque_ON - qtde_bolsas}')
elif pergunta == '2' and sangue == '7':
    print('Pode retirar')
    print(f'Estoque AB+: {estoque_ABP - qtde_bolsas}')
elif pergunta == '2' and sangue == '8':
    print('Pode retirar')
    print(f'Estoque AB-: {estoque_ABN - qtde_bolsas}')
else:
    print('Operação inválida')


#fazer de novo com if dentro de if