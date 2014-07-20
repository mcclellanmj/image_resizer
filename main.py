import argparse
from PIL import Image

if __name__ == "__main__":
    argument_parser = argparse.ArgumentParser()

    argument_parser.add_argument('files', metavar='file', default='.', nargs='+')
    argument_parser.add_argument('-W', '--maxwidth', type=int, default=2048, help='Maximum width')
    argument_parser.add_argument('-H', '--maxheight', type=int, default=2048, help='Maximum height')

    args = argument_parser.parse_args()
    size = (args.maxwidth, args.maxheight)

    for file in args.files:
        image = Image.open(file)
        image.thumbnail(size, Image.ANTIALIAS)
        exif = image.info['exif']
        image.save(file, exif=exif)

