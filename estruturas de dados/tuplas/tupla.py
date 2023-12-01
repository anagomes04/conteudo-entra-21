tupla = (10, 20)

#tuplas são imutáveis
#usa qundo quer infomrações e métodos que não podem mudar
# é uma lista que não sofre alterações

# tupla = (True, False, 1.25, 54, 'aaaa')
# #aceita qualquer tipo de dados
# print(tupla[3])

tupla = (1, 5, 10, 1)
print(tupla.index(10))
print(tupla.count(1))
print(len(tupla))
print(type(tupla))

for i in tupla:
    print(type(i))