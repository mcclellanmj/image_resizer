import argparse
from PIL import Image
import os
from glob import glob

def single_mode(output):
    """
    This function is to generate another function which can be used for generating file names
    :param output:  the output location the user has passed in
    :return: A function which will generate a filename based on the output parameter
    """
    def create_path(current_file):
        if os.path.isdir(output):
            return os.path.join(output, current_file)
        else:
            return output

    return create_path

def multi_mode(output):
    """
    This function is to generate another function which can be used for generating file names
    :param output: The output location the user entered
    :return: A function which will create paths for a file based on the output directory
    """
    if not os.path.isdir(output):
        raise Exception("When passing in multiple files the destination must be an existing directory")

    def create_path(current_file):
        return os.path.join(output, current_file)

    return create_path

def expand_for_windows(files):
    """
    Do works that Windows should be doing for us, expand out the CLI wildcards
    :param files: list of files based in from Windows CLI
    :return: expanded list if any needed expansion, this function will always return 1 or more, if not we error out
    """
    expanded_files = []
    for file in files:
        expanded_files.extend(glob(file))

    if len(expanded_files) == 0:
        raise Exception("Not enough files were found, command line argument was [%s]", " ".join(files))

    return expanded_files


if __name__ == "__main__":
    argument_parser = argparse.ArgumentParser(description="Tool for resizing images")

    argument_parser.add_argument('files', nargs='+', help='Files to be resized')
    argument_parser.add_argument('destination', nargs=1, help='The location to save the resized file')
    argument_parser.add_argument('-W', '--maxwidth', type=int, default=2048, help='Maximum width')
    argument_parser.add_argument('-H', '--maxheight', type=int, default=2048, help='Maximum height')
    argument_parser.add_argument('--no-metadata', action='store_false', dest='copy_metadata')
    argument_parser.set_defaults(copy_metadata=True)

    args = argument_parser.parse_args()
    size = (args.maxwidth, args.maxheight)
    destination = args.destination[0]

    # Windows shell doesn't expand because.. well windows so we have to do it for them.  Reimplementing
    # stuff your OS should do for you is fun.
    files = args.files if not os.name == 'nt' else expand_for_windows(args.files)

    generate_output_name = single_mode(destination) if len(files) == 1 else multi_mode(destination)

    for file in files:
        image = Image.open(file)
        image.thumbnail(size, Image.ANTIALIAS)

        # **image.info tells it to pass all the existing image.info onto the thumbnail
        metadata = image.info if args.copy_metadata else {}
        image.save(generate_output_name(file), **metadata)

