from PIL import Image
from rembg import remove

input_path = r"C:\Users\ana.gomes11\Downloads\dog4.jpg"
output_path = 'dog1.png'
input = Image.open(input_path)
output = remove(input)
output.save(output_path)