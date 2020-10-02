import os
from PIL import Image

import utils

def resize_image(image_path):
    image = Image.open(image_path, 'r')
    
    width = image.size[0]
    height = image.size[1]
    bigside = width if width > height else height

    background = Image.new('RGBA', (bigside, bigside), (255, 0, 0, 0))
    offset = (int(round(((bigside - width) / 2), 0)), int(round(((bigside - height) / 2),0)))

    background.paste(image, offset)
    background.save(image_path)

def resize(working_folder, download_folder):
    dir = working_folder + os.sep + download_folder
    pngs = utils.get_png(dir)
    for p in pngs:
        print(p)
        resize_image(p)
