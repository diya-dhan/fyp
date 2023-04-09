import numpy as np
from PIL import Image
import os

file_path = "/home/oem/venvdiya/fyp/fyp/test/spec_mel"

for dirpath, dirnames, filenames in os.walk(file_path):
# Load npz file
    for files in filenames:
        if files!="npz_img.py":
            data = np.load(files, allow_pickle=True)

# Get the first array in the file
            array = data[list(data.keys())[0]]

# Convert the array to an image and save it
            img = Image.fromarray(array)
            img.save(files.split(".")[0] + '.png')

