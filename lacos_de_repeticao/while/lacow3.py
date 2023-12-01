#programa que só termina quando é informado um numero primo

while True:
    numero = int(input('Informe um numero: '))

    if numero <= 1:
        print('Não é primo')
        continue

    for i in range(2, numero//2+1):
        if numero % i == 0:
            print(f'não é primo')
            break
    else:
        print('é primo')
        break

# while True:
#     numero = int(input('Informe um numero: '))
#
#     if numero <= 1:
#         print('Não é primo')
#     else:
#         for i in range(2, numero//2+1):
#             if numero % i == 0:
#                 print(f'não é primo')
#                 break
#         else:
#             print('é primo')
#             break