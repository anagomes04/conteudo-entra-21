from PIL import Image, ImageEnhance

imagem = Image.open(r"C:\Users\ana.gomes11\Downloads\dog4.jpg")
imagem.show()

# im_modificada = ImageEnhance.Brightness(imagem)
# im_modificada.enhance(1.5).show()
# im_modificada.enhance(0.5).show()

# im_modificada = ImageEnhance.Color(imagem)
# im_modificada.enhance(5.0).show()

# im_modificada = ImageEnhance.Contrast(imagem)
# im_modificada.enhance(100).show()

im_modificada = ImageEnhance.Sharpness(imagem)
im_modificada.enhance(100).show()
im_modificada.enhance(-100).show()