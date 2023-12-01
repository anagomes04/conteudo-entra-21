candidatoA = open('candidatoA', 'r').read().splitlines()
candidatoB = open('candidatoB', 'r').read().splitlines()

candidatoA = set(candidatoA)
candidatoB = set(candidatoB)

votos_anulados = candidatoA.intersection(candidatoB)

votos_reais_a = candidatoA.difference(votos_anulados)
votos_reais_b = candidatoB.difference(votos_anulados)

if len(votos_reais_a) > len(votos_reais_b):
    print('Candidato A ganhou')
elif len(votos_reais_b) > len(votos_reais_a):
    print('Candidato B ganhou')
else:
    print('Deu empate')