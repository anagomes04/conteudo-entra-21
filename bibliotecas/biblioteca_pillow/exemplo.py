from PIL import Image

imagem = Image.open(r"C:\Users\ana.gomes11\Downloads\dog4.jpg")
imagem.show()


#se a imagem estivesse no mesmo diretório, poderia colocar só o nome
#ai ele retornaria só o nome do arquivo
#caso contrário, retorna o caminho


print(imagem.filename)
print(imagem.format)
print(imagem.mode)
print(imagem.width)
print(imagem.height)
print(imagem.size)
# print(imagem.info)
# print(imagem.palette)

# im_flip1 = imagem.transpose(Image.FLIP_LEFT_RIGHT)
# im_flip2 = imagem.transpose(Image.FLIP_TOP_BOTTOM)
#
# im_flip1.show()
# im_flip2.show()

# tamanho = (450,225)
#
# im_menor = imagem.resize(tamanho)
# im_menor.show()

# imagem = imagem.rotate(45, expand=True).show()
# imagem.show()

imagem.save(r"C:\Users\ana.gomes11\Downloads\shishu.jpg")
imagem2 = Image.open(r"C:\Users\ana.gomes11\Downloads\shishu.jpg")
imagem2.show()