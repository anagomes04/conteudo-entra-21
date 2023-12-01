lista_novo = open('clientes_sistema_novo', 'r').read().splitlines()
# print(clientes_novo)

lista_antigo = open('clientes_sistema_antigo', 'r').read().splitlines()
# print(clientes_antigo)

lista_clientes = lista_antigo + lista_novo

clientes = set()
# lista_duplicados = []
for i in lista_clientes:
    if lista_clientes.count(i) > 1:
        clientes.add(i)

clientes_novo = set(lista_novo) #já está tirando os duplicados que estavam no prórpio conjunto

clientes_antigo = set(lista_antigo)

# print(f'Intersection {cliente_antigo.intersection(clientes_novo)}')

# print(len(clientes_antigo.intersection(clientes_novo)))
print(len(clientes))