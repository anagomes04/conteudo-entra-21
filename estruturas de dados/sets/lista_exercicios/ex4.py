lista_novo = open('clientes_sistema_novo', 'r').read().splitlines()
lista_antigo = open('clientes_sistema_antigo', 'r').read().splitlines()

lista_clientes = lista_antigo + lista_novo

cnpjs_unicos = set(lista_clientes)
#quando passa pra set já tira os repetidos

print(len(cnpjs_unicos))