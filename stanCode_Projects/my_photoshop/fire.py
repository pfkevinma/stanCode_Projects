"""
File: fire.py
Name: Pei-Feng (Kevin) Ma
---------------------------------
This file contains a method called
highlight_fires which detects the
pixels that are recognized as fire
and highlights them for better observation
"""
from simpleimage import SimpleImage


HURDLE_FACTOR = 1.05


def highlight_fires(filename):
    """
    :param filename: str, picture filename
    :return: SimpleImage

    loop through every pixel in the picture
    find out the average of value of RGB in each pixel.
    use a if/ else statement to determine which pixel will turn full red and gray scale.
    """
    img = SimpleImage(filename)
    for pixel in img:
        avg = (pixel.red + pixel.green + pixel.blue) // 3
        if pixel.red > avg * HURDLE_FACTOR:
            pixel.red = 255
            pixel.green = 0
            pixel.blue = 0
        else:
            pixel.red = avg
            pixel.green = avg
            pixel.blue = avg
    return img


def main():
    """
    This program will
        import pictures
        highlight the fire, turn the red part of the picture into full red.
        gray scale rest of the part.
        show the result.
    """
    original_fire = SimpleImage('images/greenland-fire.png')
    original_fire.show()
    highlighted_fire = highlight_fires('images/greenland-fire.png')
    highlighted_fire.show()


if __name__ == '__main__':
    main()
