from PIL import Image, ImageFilter
import glob
import re

files = glob.glob('../pic/input/*.JPG')

for pic in files:
    print(pic)
    image = Image.open(pic)
    width, height = image.size
    file_name = re.findall('input/(.*).JPG', pic)[0]

    resized_image = image.resize((width//2, height//2), Image.LANCZOS)
    resized_image.save(f"../pic/output/{file_name}_resized.JPG")