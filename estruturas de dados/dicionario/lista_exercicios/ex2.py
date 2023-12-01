import random
import math

jogadas = {
    'Jogador_1': math.ceil(random.random() * 6),
    'Jogador_2': math.ceil(random.random() * 6),
    'Jogador_3': math.ceil(random.random() * 6),
    'Jogador_4': math.ceil(random.random() * 6)
}

# print(jogadas)

maior_jogada = sorted(jogadas.values())
jogadas_ordenadas = {}

for i in maior_jogada:
    for k in jogadas.keys():
        if jogadas[k] == i:
            jogadas_ordenadas[k] = jogadas[k]
            break

print(jogadas_ordenadas)