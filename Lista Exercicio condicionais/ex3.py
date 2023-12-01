altura = float(input('Digite sua altura: '))
genero = input('Digite seu genero: [1] feminino [2] masculino')

if genero == '1':
    print(f'Seu peso ideal é {40*altura} kg')
elif genero == '2':
    print(f'Seu peso ideal é {50*altura} kg')
else:
    print('Algo não foi informado')