Image Resizer
-------------
Tool to resize an image or list of images and save them back to their source.  It will work on anything that PIL can handle.  In the case of JPEGs it will save any exif data that is on the image.

Usage
-----
    python -W 1024 -H 1024 main.py image.jpg image2.jpg image3.jpg output

-W signifies the maximum allowable width, this flag is optional and will default to 2048

-H signifies the maximum allowable height, this flag is optional and will default to 2048

In the case that multiple files are passed in the output location must be an existing directory.  If only one file to be resized
is passed in the output can be a file or directory.  If it is a directory the resized file will be placed in the directory, if
it does not exist then the file will be created.

The usage is intended to mimic the copy (cp) command in linux.  On a Windows machine it will handle the glob expansion that is done automatically on Linux, so for instance 

    python main.py *.jpg resized
Will resize all files ending with .jpg and output them to the resized directory.  On linux the glob expansion of *.jpg will be automatic, and on Windows the script will handle it.

Installation
------------
Requires Python, should work on 2 or 3 but is only tested on 3

Requires the Pillow library.

Easy requirement install

    pip install -r requirements.txt
