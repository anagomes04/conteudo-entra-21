candidatoA = open('candidatoA', 'r').read().splitlines()
candidatoB = open('candidatoB', 'r').read().splitlines()

candidatoA = set(candidatoA)
candidatoB = set(candidatoB)

print(f'{len(candidatoA.intersection(candidatoB))}')