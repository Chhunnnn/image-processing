import os

from colorize import colorize_image
from decolorize import decolorize_image

ORIGINAL_DIR = 'original'
GRAYSCALE_DIR = 'grayscale'
RECOLOR_DIR = 'recolor'

PROCESSABLE_EXTENSION = ['.jpg', '.jpeg', '.png']

if __name__ == '__main__':
    current_dir = os.getcwd()
    original_dir = "{}/{}".format(current_dir, ORIGINAL_DIR)
    grayscale_dir = "{}/{}".format(current_dir, GRAYSCALE_DIR)
    recolor_dir = "{}/{}".format(current_dir, RECOLOR_DIR)

    images = []
    for (directory_path, _, file_names) in os.walk(original_dir):
        for file_name in file_names:
            file_name_and_ext = os.path.splitext(file_name)
            if file_name_and_ext[1] in PROCESSABLE_EXTENSION:
                images.append(file_name)
        break

    for img in images:
        original_path = "{}/{}".format(original_dir, img)
        grayscale_path = "{}/{}".format(grayscale_dir, img)
        recolor_path = "{}/{}".format(recolor_dir, img)

        decolorize_image(original_path, grayscale_path)
        colorize_image(grayscale_path, recolor_path)
