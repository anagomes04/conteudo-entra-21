from PIL import Image

imagem = Image.open(r"C:\Users\ana.gomes11\Downloads\paisagem.jpg")
imagem.show()

# imagem.transpose(Image.FLIP_TOP_BOTTOM).show()
# imagem.transpose(Image.FLIP_LEFT_RIGHT).show()
# imagem.transpose(Image.ROTATE_90).show()
# imagem.transpose(Image.ROTATE_180).show()
# imagem.transpose(Image.ROTATE_270).show()
# imagem.transpose(Image.TRANSVERSE).show()

imagem.save(r"C:\Users\ana.gomes11\Downloads\paisagem_modificada.jpg")
imagem2 = Image.open(r"C:\Users\ana.gomes11\Downloads\paisagem_modificada.jpg")
imagem2.show()