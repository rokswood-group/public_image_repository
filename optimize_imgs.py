#!/usr/bin/env python3
"""
Optimize a list of images in specified paths (in argv) using
PIL.Image class.
"""
import os
from sys import argv, exit
from PIL import Image

if len(argv) < 2:
    print("Usage: {} <dir-1> <dir-2> ...".format(argv[0]))
    exit(-1)
else:
    argv.pop(0)

image_formats = ["jpeg", "jpg", "png", "bmp",
                 "gif", "tiff", "tif", "webp", "ico"]


for path in argv:
    if not all([os.path.exists(path), os.path.isdir(path)]):
        continue
    file_list = os.listdir(path)
    for file in file_list:
        file_path = '/'.join([path, file])
        image_format = file_path.split('.')[-1]
        if not all([
            os.path.isfile(file_path),  # is file
            image_format in image_formats  # format is supported
        ]):
            print('[*] Skipped... {}'.format(file))
            continue
        Image.open(file_path).convert('RGB').save(
            file_path.replace(image_format, 'jpg'), format='JPEG', optimized=True)
        print('[*] Optimized... {}'.format(file))
        # os.remove(file_path)
