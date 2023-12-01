print('DUPLAS!')

mulheres = []

for i in range(3):
    nome = input(f'Mulher {i + 1}: ')
    mulheres.append(nome)
print(f' Mulheres: {mulheres}')

homens = []

for i in range(3):
    nome = input(f'Homem {i + 1}: ')
    homens.append(nome)
print(f' Homens: {homens}')

for i in range(3):
    print(f'Dupla: {mulheres[i]} e {homens[i]}')