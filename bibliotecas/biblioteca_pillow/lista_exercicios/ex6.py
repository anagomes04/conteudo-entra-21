from PIL import Image, ImageEnhance

imagem = Image.open(r"C:\Users\ana.gomes11\Downloads\paisagem.jpg")
imagem.show()

im_modificada1 = ImageEnhance.Brightness(imagem)
im_modificada2 = ImageEnhance.Color(imagem)
im_modificada3 = ImageEnhance.Contrast(imagem)
im_modificada4 = ImageEnhance.Sharpness(imagem)

def criar_filtro(imagem):
    return (f'{im_modificada1.enhance(1.5).show()} '
            f'{im_modificada2.enhance(5.0).show()} '
            f'{im_modificada3.enhance(100).show()}'
            f'{im_modificada4.enhance(100).show()}')

criar_filtro(imagem)