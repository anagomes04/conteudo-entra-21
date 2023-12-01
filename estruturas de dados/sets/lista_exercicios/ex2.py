lista_novo = open('clientes_sistema_novo', 'r').read().splitlines()
lista_antigo = open('clientes_sistema_antigo', 'r').read().splitlines()

lista_clientes = lista_antigo + lista_novo

clientes = set()
lista_repetidos = []
for i in lista_clientes:
    if i in clientes:
        lista_repetidos.append(i)
    else:
        clientes.add(i)
print(len(lista_repetidos))