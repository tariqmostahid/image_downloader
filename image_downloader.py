#!/usr/bin/python3

import sys
import os
from pathlib import Path
import requests

image_directory = './images/'


def download_image(url):
    if url is not "":
        # removing trailing \n from urls
        url = url.rstrip("\n")
        try:
            # creating images directory if not exists
            os.makedirs(image_directory)
        except FileExistsError:
            # directory already exists
            pass
        # starting Download
        req = requests.get(url, allow_redirects=True)
        open("./images/" + os.path.basename(url) + '.jpg', 'wb').write(req.content)

        return True
    else:
        return False


def read_file(filepath):
    if Path(filepath).exists() and filepath != "":
        # open and read file
        with open(filepath, "r") as urls:
            for url in urls:
                download_image(url)
        return True
    else:
        return False


if __name__ == '__main__':
    read_file("input_images.txt")
