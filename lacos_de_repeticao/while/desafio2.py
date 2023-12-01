#jokenpô - melhor de 3.

import random
import math

vitorias_usuario = 0
vitoria_maquina = 0

while True:
    jogada_usuario = int(input('Faça sua jogada: \n'
                               '1. Pedra \n'
                               '2. Papel \n'
                               '3. Tesoura \n'))

    jogada_maquina = math.ceil(random.random() * 3)
    print(jogada_maquina)

    if jogada_usuario == jogada_maquina:
        print('Empate.')
        continue

# 1 - pedra
# 2 - papel
# 3 - tesoura
#
# pedra < papel < tesoura (1 < 2 < 3)
# exceto que pedra ganha de tesoura (tesoura < pedra)

    elif jogada_maquina < jogada_usuario:
        if jogada_maquina == 1 and jogada_usuario == 3:
            vitoria_maquina += 1
            print('Máquina ganhou.')
        else:
            vitorias_usuario += 1
            print('Usuário ganhou.')

    elif jogada_usuario < jogada_maquina:
        if jogada_usuario == 1 and jogada_maquina == 3:
            vitorias_usuario += 1
            print('Usuário ganhou.')
        else:
            vitoria_maquina += 1
            print('Máquina ganhou.')

    if vitorias_usuario == 2:
        print('Vencedor: usuário.')
        break

    elif vitoria_maquina == 2:
        print('Vencedor: máquina.')
        break