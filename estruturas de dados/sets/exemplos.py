#sets não permite dado duplicado dentro dele

lista = list(range(5, 11))
lista2 = list(range(8))
# print(lista)
# print(lista2)

# lista3 = lista + lista2
# print(lista3)

set1 = set(lista+lista2)
print(set1)
# #removeu os elementos duplicados
print(type(set1))

#adicionar itens ao set
set1.add(15)
print(set1)
#não é garantido que o elemento adicionaddo vai ficar sempre no final
#justamente porque os sets não são ordenados

lista3 = [22, 65, 18, 92]
set1.update(lista3)
print(set1)

# set1.remove(92)
# print(set1)

set1.discard(92)
print(set1)

# set1.discard(91)
# print(set1)

#remove e disacrd para eliminar elementos de um set.
#caso não encontrado, o discard ignora e o remove retorna KeyError

set1.pop()
print(set1)
#remove o primerio item

#lista é um item mutável, set também mas não permite duplicados e é desrodenado

set1.clear()
print(set1)
#fica um set vazio

