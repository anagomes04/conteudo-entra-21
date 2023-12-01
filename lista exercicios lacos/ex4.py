print('TABUADAS!')

lista = [0]

for i in lista:
    print('Deseja ver uma tabuada? [S ou N]')
    resposta = input('Resposta: ')

    if resposta.upper() == 'S':
        lista.append(0)
        tabuada = int(input('Tabuada de: '))

        for j in range(10):
            print(f'{tabuada} X {j+1} = {tabuada * (j+1)}')

#poderia fazer com while true, else break

#for dentro de for tem que usar outra variável além de i ex: j, k l ...