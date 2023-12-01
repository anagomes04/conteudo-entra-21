candidatoA = open('candidatoA', 'r').read().splitlines()
candidatoB = open('candidatoB', 'r').read().splitlines()

if len(candidatoA) > len(candidatoB):
    print('Candidato A ganhou')
elif len(candidatoB) > len(candidatoA):
    print('Candidato B ganhou')
else:
    print('Deu empate')