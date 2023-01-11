# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import sys
import os
from PIL import Image

path = '/Users/bapnarb/Desktop/JPEG_images'
directory = '/Users/sonia/PyCharm/new_images'

if not os.path.exists(directory):
    os.makedirs(directory)

for filename in os.listdir(path):
    if os.path.isfile(path + '/' + filename):
        if filename.endswith(".jpeg"):
            img = Image.open(path + '/' + filename)
            new_filename = filename.replace(".jpeg", ".png")
            img.save(directory + '/' + new_filename, "png")
            print(f"Successfully converted {filename} to {new_filename}")