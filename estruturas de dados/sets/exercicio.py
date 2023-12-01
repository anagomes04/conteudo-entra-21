lista = open('numeros.txt', 'r').read().splitlines()
# r = leitura, w = escrever o arquivo
print(lista)
print(type(lista))
#sem o splitlines é uma string só