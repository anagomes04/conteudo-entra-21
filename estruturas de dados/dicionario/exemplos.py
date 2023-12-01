# dicionário são chaves com correspondência entre os elementos

dicionario = {'chave 1': 'jonas',
              'chave 2': 'adriana',
              'chave 3': 'ariadne',
              }

#as chaves podem ser texto e número também
#e os valores das podem ser de qualquer tipo

# print(dicionario)
# print(dicionario['chave 3'])
#não passa o ínidce, mas sim o nome da chave

emails = {'jonas': 'jonasreiter@hotmail.com',
          'dalva': 'dalva_das_quebradas@gmail.com',
          'juvenal': 'canetaazul@uol.com.br',
          'nestor': 'nenenestor@bol.com.br'}

print(emails['nestor'])
#acessar um item do dicionário

# print(emails['artur'])
#erro de chave (keyerror), pois a chave não existe

print(emails.get('artur', 'Não existente'))

#adicionar itens no dicionário
emails['tristan'] = 'tristinho@gmail.com'
print(emails.get('tristan', 'não existe'))

#alterar valor do dicionário, duas formas de fazer:
emails['tristan'] = 'tristinho@bol.com'
#dessa forma sobrescreve o que já existe
emails.update({'jonas': 'jonas.reiter92@gmail.com'})
print(emails)

#alterar nome da chave - método 1
emails['jonasreiter'] = emails.pop('jonas')
print(emails)
#joga a "nova chave" para o final

#alterar nome da chave - método 2
emails['jonas'] = emails['jonasreiter']
del emails['jonasreiter']
print(emails)

#imprimir todas as chaves
print(emails.keys())

#imprimir todos os valores
print(emails.values())

#percorrer todas as chaves do cicionário
for chave in emails:
    print(chave)

#percorrer todos os valores do dicionário
for valor in emails:
    print(emails[valor])

#percorrer dicionario completo
for chave, valor in emails.items():
    print(f'{chave} ------- {valor}')

#deletar uma chave, que deleta o valor junto por consequência
emails.pop('tristan')
print(emails)

#deletar só o último item
emails.popitem()
print(emails)

#verificar se uma chave existe
if 'joaquim' in emails:
    print('existe')
else:
    print('não existe')

#verificar se um valor existe
if 'canetaazul@uol.com.br' in emails.values():
    print('existe')
else:
    print('não existe')

emails2 = {'carlos': 'carlos@gmail.com',
           'sandra': 'sandrinha@gmail.com'}

emails_geral = {**emails, **emails2}
print(emails_geral)

#transformar duas listas em dicionários
lista_nomes = ['jonas', 'marcela', 'aristides', 'gilberta']
notas = [7, 8, 9, 10]

#método bruto
dicionario_novo = dict()
for i in range(len(lista_nomes)):
    dicionario_novo[lista_nomes[i]] = notas[i]
print(dicionario_novo)

#método nutella
dicionario_novo2 = dict(zip(lista_nomes, notas))
print(dicionario_novo2)