# FOR - para
# WHILE - enquanto

# for i in range(10): #range(10) =  intervalo de 0 a 9
#     print(i)
#vai imprimir todos os valores do intervalo, até acabar. Iterações

# for i in range(1, 11): #range(10) =  intervalo de 1 a 10
#     print(i)

# for i in range(5):
#     print('ana')

# for i in 'ana':
#     print(i)

# for i in range(1, 11):
#     if i % 2 == 0:
#         print(f'{i} - Par')
#     else:
#         print(f'{i} - Ímpar')

nome = 'arazra'
letra = 'a'
letra_saida = 'z'

total = 0
for i in nome:
    if i == letra:
        total += 1
    if i == letra_saida:
        break
print(total)

