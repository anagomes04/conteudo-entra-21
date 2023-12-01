nome = input('Informe o nome do jogador: ')
qtde_partidas = int(input('Informe a quantidade de partidas jogadas: '))


informacoes = {
    'nome': nome,
    'quantidade de partidas': qtde_partidas
}

qtde_gols = []

for i in range(qtde_partidas):
    gols = int(input(f'Informe a quantidade de gols feitos na partida {i + 1}:'))
    qtde_gols.append(gols)

for i, qtde in enumerate(qtde_gols):
    informacoes[f'gols partida {i+1}'] = qtde

informacoes['total_gols'] = sum(qtde_gols)

print(informacoes)