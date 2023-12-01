import os

path = r"C:\Users\ana.gomes11\Desktop\Ana.txt"

if os.path.exists(path):
    print('O caminho existe')
    file_name = os.path.basename(path)
    print("Nome do arquivo:", file_name)
    directory = os.path.dirname(path)
    print("Diretório:", directory)
else:
    print('O caminho não existe')