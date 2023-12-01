matriz = [
    [' ', ' ',' '],
    [' ', ' ',' '],
    [' ', ' ',' ']
]

jogador_atual = 'X'

jogo_acabou = False

while not jogo_acabou:

    print(f'{matriz[0][0]}|{matriz[0][1]}|{matriz[0][2]}\n'
          '-----\n'
          f'{matriz[1][0]}|{matriz[1][1]}|{matriz[1][2]}\n'
          '-----\n'
          f'{matriz[2][0]}|{matriz[2][1]}|{matriz[2][2]}')

    linha = int(input('Informe a linha que quer jogar: '))

    coluna = int(input('Informe a coluna que quer jogar: '))

    if matriz[linha - 1][coluna - 1] == ' ':
        matriz[linha - 1][coluna - 1] = jogador_atual
    else:
        print('Campo ocupado')
        continue

    for linha in matriz:
        if linha[0] == linha[1] == linha[2] and linha[0] != ' ':
            print(f'Jogador {jogador_atual} ganhou.')
            jogo_acabou = True
            break

    for coluna in range(3):
        if matriz[0][coluna] == matriz[1][coluna] == matriz[2][coluna] and matriz[0][coluna] != ' ':
            print(f'Jogador {jogador_atual} ganhou.')
            jogo_acabou = True
            break

    if matriz[0][0] == matriz[1][1] == matriz[2][2] and matriz[0][0] != ' ':
        print(f'Jogador {jogador_atual} ganhou.')
        jogo_acabou = True
        break

    elif matriz[0][2] == matriz[1][1] == matriz[2][0] and matriz[0][2] != ' ':
        print(f'Jogador {jogador_atual} ganhou.')
        jogo_acabou = True
        break

    empate = True

    for linha in matriz:
        for i in linha:
            if i == ' ':
                empate = False
                break

    if empate:
        print('Empate.')
        jogo_acabou = True
        break

    if jogador_atual == 'X':
        jogador_atual = 'O'
    else:
        jogador_atual = 'X'

print(f'{matriz[0][0]}|{matriz[0][1]}|{matriz[0][2]}\n'
          '-----\n'
          f'{matriz[1][0]}|{matriz[1][1]}|{matriz[1][2]}\n'
          '-----\n'
          f'{matriz[2][0]}|{matriz[2][1]}|{matriz[2][2]}')

#fazer com uma lista (matriz) de 1 a 9 que seriam as posições do tabuleiro,
#ai só informar a posição na hora de fazer a jogada