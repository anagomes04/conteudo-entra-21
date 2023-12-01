print('CADASTRO DE PRODUTOS!')

print('Quantos produtos você deseja cadastrar?')
resposta = int(input('Resposta: '))

produtos = []
precos = []

for i in range(resposta):
    produto = input(f'Produto {i + 1}: ')
    preco = float(input('Preço: '))
    produtos.append(produto)
    precos.append(preco)

for i in range(resposta):
    print(f'Produto: {produtos[i]} - Preço: R$ {precos[i]}')