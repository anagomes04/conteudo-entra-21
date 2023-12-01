nomes = ['heitor', 'hugo', 'helena', 'helena']
nomes2 = ['cássio', 'claudete', 'cirilo']
nomes3 = [1, 2, 1.5, False, True,  'carlos']

# nomes.txt.append(nomes2)
# print(len(nomes.txt))
#dá para colocar uma lista dentro da outra,
# só que vai como um outro elemento

# nomes.txt.extend(nomes2)
# print(nomes.txt)
#extend faz com que os elementos da segunda lista vire elementos
# na primeira lista

nomes += nomes3
print(nomes)
#faz o mesmo que o extend, mas só funciona para listas,
#não funciona com sets e tuplas


nomes.pop()
print(nomes)
#elimina o último item da lista

nomes.pop(0)
print(nomes)
#elimina elementos específicos da lista

nomes.remove('helena')
print(nomes)
#remove o priemiro

print(nomes3.index('carlos'))

nomes3.pop(nomes3.index('carlos'))
print(nomes3)

numeros = [5, 3, 7, 9, 11, 15]
print(sum(numeros))
#soma os valores da lista, desde que seja int ou float
numeros.sort()
print(numeros)

cidades = ['blumenau', 'idaial', 'ascurra', 'pomerde', 'blumenau']
print(cidades.count('blumenau'))
#dá quantas vezes um elemento aparece na lista,
# funciona com int e float também

cidades.sort(reverse=True)
print(cidades)
#ordena em ordem alfabética, os elementos tem que ser do mesmo tipo
#reverse =True ordena em ordem decrescente

cidades.reverse()
print(cidades)
#.reverse ordena de trás pra frente

cidades.insert(0,'rodeio')
print(cidades)
#insere na lista na posição desejada

cidades.clear()
print(cidades)
#faz com que a lista fique vazia, tira todos os elementos

letras = ['a', 'b', 'c']
palavra = ''
for letra in letras:
    palavra += letra
print(palavra)
#junta os itens de uma lista em uma coisa só

alimentos = ['café', 'macarrão', 'frango', 'camarão', 'alcatra']

#desempacotamento de lista - list unpacking
bebida, carboidrato, *proteinas, carne = alimentos
#definiu que bebida é o índice 0, carboidrato é o índice 1
# e o resto é proteína
# também pode ser usado para definir um intervalo,
# desde que tenhas os próximos índices

print(bebida)
print(carboidrato)
print(proteinas)
print(carne)

negativos = [-3, -8, -15, -35, -16, -4]
positivos = [-1 * valor for valor in negativos]
print(positivos)


# negativos = [-3, -8, -15, -35, -16, -4, 9]
# positivos = [-1 * valor for valor in negativos]
# print(positivos)

pares = [valor for valor in positivos if valor % 2 == 0]
print(pares)