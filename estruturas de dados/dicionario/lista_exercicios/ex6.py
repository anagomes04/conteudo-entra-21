usuarios = open('usuarios.txt', 'r').read().splitlines()

espacos = dict()

for item in usuarios:
    chave = str(item[:15]).replace(' ','')
    valor = int(item[16:])
    espacos.update({chave:valor})
print(espacos)

valores_ordenados = sorted(espacos.keys())
# usuarios_ordenados = {}
#
# for i in valores_ordenados:
#     for k in espacos.keys():
#         if espacos[k] == i:
#             usuarios_ordenados[k] = espacos[k]
#             break
# print(usuarios_ordenados)
