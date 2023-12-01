from PIL import Image

imagem = Image.open(r"C:\Users\ana.gomes11\Downloads\paisagem.jpg")
imagem.show()

tamanho = (550, 230)

imagem_menor = imagem.resize(tamanho)
imagem_menor.show()