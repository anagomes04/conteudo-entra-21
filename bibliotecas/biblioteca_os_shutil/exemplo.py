import os

# sistema = os.environ
# print(sistema)
#printa um dicionário das variáveis do sistema
# print(sistema['USERNAME'])

# for sistema in os.environ:
#     print(sistema)

# os.getcwd()
# print(os.getcwd())
# novo_caminho = r'C:\Users\ana.gomes11\PycharmProjects\ana\bibliotecas\biblioteca_os_shutil'
# os.chdir(novo_caminho)
# print(novo_caminho)
# os.getcwd()

# os.mkdir('novo diretório')
#makedirs = fazer diretório

caminho = r'C:\Users\ana.gomes11\Documents'
# os.makedirs(caminho)
os.chdir(caminho)
# print(os.listdir())

# os.remove('arquivo_texto.txt')
# os.rmdir('teste')

# os.rename('arquivo_texto.txt', 'ARQUIVO_TEXTO.txt')

# os.startfile(r'C:\Users\ana.gomes11\Documents\arquivo.txt')

for root, dir, file in os.walk(r'C:\Users\ana.gomes11\Documents'):
    # print(root) #para ver a raíz
    # print(dir) #para ver o diretório
    print(file) #para ver os arquivos

