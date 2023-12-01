# lista = []
#
# while True:
#     valor = float(input('Informe um valor: '))
#     lista.append(valor)
#     media = sum(lista)/len(lista)
#     print(f'Média = {media}')
#
#     qtde_positivo = 0
#     qtde_negativo = 0
#
#     for i in lista:
#         if i > 0:
#             qtde_positivo += 1
#         elif i < 0:
#             qtde_negativo += 1
#
#     print(f' Quantidade de números positivos = {qtde_positivo}')
#     print(f' Quantidade de números negativos = {qtde_negativo}')
#
#     percent_positivo = qtde_positivo/len(lista) * 100
#     percent_negativo = qtde_negativo/len(lista) * 100
#
#     print(f' Porcentagem de números positivos = {percent_positivo}')
#     print(f' Porcentagem de números positivos = {percent_negativo}')
#
#     maior_valor = 0
#     menor_valor = 100000000000
#
#     for i in lista:
#         if i > maior_valor:
#             maior_valor = i
#         if i < menor_valor:
#             menor_valor = i
#
#     print(f' Máximo = {maior_valor}')
#     print(f' Mínimo = {maior_valor}')

maior = 0
menor = 0
soma = 0
total = 0
qtde_positivo = 0
qtde_negativo = 0

while True:
    valor = float(input('Informe um valor: '))

    if valor == 0:
        break

    soma += valor
    total += 1

    if valor > 0:
        qtde_positivo += 1
    else:
        qtde_negativo += 1

    if total == 1:
        maior = valor
        menor = valor

    if valor > maior:
        maior = valor

    if valor < menor:
        menor = valor

print(f'Média = {soma / total}')

print(f' Quantidade de números positivos = {qtde_positivo}')
print(f' Quantidade de números negativos = {qtde_negativo}')

print(f' Porcentagem de números positivos = {(qtde_positivo / total) * 100}')
print(f' Porcentagem de números positivos = {(qtde_negativo / total) * 100}')

