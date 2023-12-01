import shutil
import os

# destino = r"C:\Users\ana.gomes11\Desktop\pasta"
# shutil.rmtree(destino)

caminho = r"C:\Users\ana.gomes11\Desktop"
os.chdir(caminho)
os.rmdir('nova_pasta')