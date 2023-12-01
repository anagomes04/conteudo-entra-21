set1 = {1, 2, 3, 4, 5, 6}
#set é dentro de chaves
set2 = {4, 5, 6, 7, 8, 9, 22}

#unir dois sets

print(f'Union{set1.union(set2)}')
print(f'Union{set2.union(set1)}')
#ordem não importa, retorna o mesmo resultado

#interseção

print(f'Intersection {set1.intersection(set2)}')

#diferenças

print(f'Difference {set2.difference(set1)}')
print(f'Difference {set1.difference(set2)}')
#nesse caso a ordem diferente retorna resultados diferentes
#já que faz referência ao está em um conjunto e não está no outro

print(f'Symetric Difference {set1.symmetric_difference(set2)}')
#junta num cnjunto só as duas diferenças => união - intersecção
#printa tudo que não está na intersecção, mas está nos dois conjuntos

if 22 in set2:
    print('achou')