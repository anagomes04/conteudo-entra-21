idade = int(input('Informe dua idade: '))
sangue = int(input('Informe seu tipo sanguíneo A+ (1), A- (2), B+ (3), B- (4), O+ (5), O- (6), AB+ (7), AB- (8): '))
pergunta = input('Quer doar (1) ou retirar (2)? ')
if pergunta == '2':
    qtde_bolsas = int(input('Informe a quantidade de bolsas que deseja retirar: '))
else:
    qtde_bolsas = 0

estoque_AP = 17
estoque_AN = 12
estoque_BP = 1
estoque_BN = 3
estoque_OP = 9
estoque_ON = 22
estoque_ABP = 23
estoque_ABN = 11

estoque_geral = estoque_AP + estoque_AN + estoque_BP + estoque_BN + estoque_OP + estoque_ON + estoque_ABP + estoque_ABN

tipos = ['A+', 'A-', 'B+', 'B-', 'O+', 'O-', 'AB+', 'AB-']

estoques = [estoque_AP, estoque_AN, estoque_BP, estoque_BN, estoque_OP, estoque_ON, estoque_ABP, estoque_ABN ]

if idade < 18 and pergunta == '1':
    print('Não pode doar, menor de idade')
elif idade >= 65 and pergunta == '1':
    print('Não pode doar, idade acima do permitido')
elif estoque_geral == 200 and pergunta == '1':
    print('Estoque cheio')
elif qtde_bolsas > estoques[sangue - 1]:
    print('Quantidade de bolsas insuficiente para esse tipo sanguíneo')
elif pergunta == '2' and qtde_bolsas % 5 != 0:
    print('Quantidade de bolsas para retirar deve ser múltiplo de 5')
else:
    for i in range(8):
        if sangue == i + 1:
            if pergunta == '1':
                print('Pode doar')
                print(f'Estoque {tipos[i]}: {estoques[i] + 1}')
            elif pergunta =='2':
                print('Pode retirar')
                print(f'Estoque: {tipos[i]}: {estoques[i] - qtde_bolsas}')