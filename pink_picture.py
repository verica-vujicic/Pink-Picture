"""
File: pink_picture.py
You have to have the a Pillow module 
installed on your machine to get this
program working.
"""

from simpleimage import SimpleImage

DEFAULT_FILE = 'quad.jpg'

def main():
    # Get file and load image
    filename = get_file()

    original_image = SimpleImage(filename)
    original_image.show()

    pink_image = pinker(filename)
    pink_image.show()

def pinker(filename):
    # Apply the filter
    image = SimpleImage(filename)
    for pixel in image:
        pixel.red *= 1.5
        pixel.green *= 0.7
        pixel.blue *= 1.5
    return image

def get_file():
    # Read image file path from user, or use the default file
    filename = input('Enter image file (or press enter for default): ')
    if filename == '':
        filename = DEFAULT_FILE
    return filename


if __name__ == '__main__':
    main()
