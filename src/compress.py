from PIL import Image
import glob
import re

files = glob.glob('../pic/input/*.JPG')


def compress_image(target_url):
    '''compress single image
    '''

    image = Image.open(target_url)
    width, height = image.size
    resized_image = image.resize((width//2, height//2), Image.LANCZOS)
    return resized_image


def compress_multiple_images():
    '''compress images that is in ../pic/input/
    '''

    for pic in files:
        print(pic)
        file_name = re.findall('input/(.*).JPG', pic)[0]
        resized_image = compress_image(pic)
        resized_image.save(f"../pic/output/{file_name}_resized.JPG")


