from PIL import Image, ImageDraw

imagem = Image.new('RGB', (750,460), 0)

draw = ImageDraw.Draw(imagem)
draw.line()