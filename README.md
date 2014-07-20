Image Resizer
-------------
Tool to resize an image or list of images and save them back to their source.  Will save any exif data that is on the image.

Usage
-----
    python -W 1024 -H 1024 main.py image.jpg image2.jpg

-W signifies the maximum allowable width, this flag is optional and will default to 2048
-H siginifies the maximum allowable height, this flag is optional and will default to 2048

Installation
------------
Requires Python, should work on 2 or 3 but is only tested on 3
Requires the Pillow library.

Easy requirement install
    pip install -r requirements.txt

Warning
-------
This will overwrite the existing image with the resized image (by intention).  Make a copy of your originals if you want to keep them at that size. 