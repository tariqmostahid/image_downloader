#!/usr/bin/python3

import sys
import os
import urllib.request
from pathlib import Path


image_directory = './images/'
def download_image(url):
    # removing trailing \n from urls
    url = url.rstrip("\n")
    try:
        # creating images directory if not exists
        os.makedirs(image_directory)
    except FileExistsError:
        # directory already exists
        pass
    # starting Download
    urllib.request.urlretrieve(url, "./images/" + os.path.basename(url))
    return 0

def read_file(filepath):
    if Path(filepath).exists():
        # open and read file 
        with open(filepath, "r") as urls:
            for url in urls:
                download_image(url)
        return 0
    else:
        return 1

if __name__ == '__main__':
    read_file("input_images.txt")