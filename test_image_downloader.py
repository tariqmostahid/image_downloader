#!/usr/bin/python3
import pytest
from image_downloader import read_file, download_image

def test_read_file_without_filepath():
    filepath = ""
    assert read_file(filepath) == 0

def test_read_file_filepath_does_not_exists():
    filepath = "path/to/filepath"
    assert read_file(filepath) == 0

def test_read_file_filepath_exists():
    assert read_file("input_images.txt") == 0

def test_download_image_existing_url():
    url = "https://images.unsplash.com/photo-1504610926078-a1611febcad3"
    assert download_image(url) == 0

def test_download_image_without_url():
    url = ""
    assert download_image(url) == 1
