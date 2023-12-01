# nome = 'ana'
# print(nome[0])
# #printa a primeira letra (indice 0 porque começa no 0)
# print(nome[1:3])
# #do indice 1 ao 3, mas não parece o tereiro
# print(nome[:-1])
# #exclui o último caractere
# print(nome[1:])
# # exlcui o primeiro caractere

#criar um programa que pede o nome e informa se começa com vogal

nome = input('Digite seu nome: ')

print(nome.upper())

print(nome[0].upper())

# if nome[0].upper() in ['A','E','I','O','U'] ou 'AEIOU':
#     print('O nome começa com uma vogal')
# else:
#     print('O nome começa com uma consoante')

letra = nome[0].upper()

if letra == 'A' or letra == 'E' or letra == 'I' or letra == 'O' or letra == 'U' :
    print('O nome começa com uma vogal')
else:
    print('O nome começa com uma consoante')