from PIL import Image, ImageDraw, ImageFont

imagem = Image.open(r"C:\Users\ana.gomes11\Downloads\dog4.jpg")

draw = ImageDraw.Draw(imagem)
font = ImageFont.truetype("AGENCYB.TTF", 100)

draw.text((250,70), 'Shishu', font=font, fill=(218,165,32))
imagem.show()