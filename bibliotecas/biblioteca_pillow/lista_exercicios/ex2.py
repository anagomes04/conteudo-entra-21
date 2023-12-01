from PIL import Image

imagem = Image.open(r"C:\Users\ana.gomes11\Downloads\paisagem.jpg")

print(imagem.filename)
print(imagem.format)
print(imagem.mode)
print(imagem.width)
print(imagem.height)
print(imagem.size)