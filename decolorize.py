import math
from PIL import Image


def decolorize_image(input_path, output_path):
    im = Image.open(input_path)
    width = im.width
    height = im.height
    px = im.load()

    for h in range(0, height):
        for w in range(0, width):
            coordinate = w, h
            rgb = im.getpixel(coordinate)

            avg = math.ceil((min(rgb[0], rgb[1], rgb[2]) + max(rgb[0], rgb[1], rgb[2])) / 2)
            px[w, h] = (avg, avg, avg)

    im.save(output_path)
