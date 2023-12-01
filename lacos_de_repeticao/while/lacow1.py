#no for já sabemos quantas iterações o laço vai ter
#no while não sabemos essa informação

# nota = -1
# while nota < 0 or nota > 10:
#     nota = float(input('Digite um número: '))

#no while a variavel já tem que estar declarada antes do laçõ,
# no for isso não é necessário

# while True:
#     nota = float(input('Digite um número: '))
#     if nota >= 0 or nota <= 10:
#         break

numero = 0
while numero <= 10:
    numero += 1
    if numero == 5:
        continue
    print(numero)

#continue faz voltar pro while

#while true tem que ter break