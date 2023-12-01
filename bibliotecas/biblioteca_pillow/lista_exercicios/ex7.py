from PIL import Image
from rembg import remove

input_path = r"C:\Users\ana.gomes11\Downloads\cavalo.jpg"
output_path = 'cavalo.png'
input = Image.open(input_path)
output = remove(input)
output.save(output_path)