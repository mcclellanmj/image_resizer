Image Resizer
-------------
Tool to resize an image or list of images and save them back to their source.  Requires Python and the Pillow library.  It will also preserve any of the exif data on the image.

Usage
-----
python [-W 1024] [-H 1024] main.py image.jpg image2.jpg

-W signifies the maximum allowable width
-H siginifies the maximum allowable height

Warning
-------
This will overwrite the existing image with the resized image (by intention).  Make a copy of your originals if you want to keep them at that size. 