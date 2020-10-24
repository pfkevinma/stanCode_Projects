"""
File: mirror_lake.py
Name: Pei-Feng (Kevin) Ma
----------------------------------
This file reads in mt-rainier.jpg and
makes a new image that creates a mirror
lake vibe by placing the inverse image of
mt-rainier.jpg below the original one
"""
from simpleimage import SimpleImage


def reflect(filename):
    """
    :param filename: str, image's filename
    :return: SimpleImage

    This function will create a blank image with 2 times higher than input image.
    Then, loop through pixel in the input image and assign two mirror coordinates
    in blank image.
    Return the blank image after assigned pixels.
    """
    img = SimpleImage(filename)
    img_blank = SimpleImage.blank(img.width, img.height * 2)
    for x in range(img.width):
        for y in range(img.height):
            pixel = img.get_pixel(x, y)
            p1 = img_blank.get_pixel(x, y)
            p2 = img_blank.get_pixel(x, img_blank.height - 1 - y)
            p1.red = pixel.red
            p1.green = pixel.green
            p1.blue = pixel.blue
            p2.red = pixel.red
            p2.green = pixel.green
            p2.blue = pixel.blue
    return img_blank


def main():
    """
    This program will make a mirror image along the x-axis, converting with the original image.
    """
    original_mt = SimpleImage('images/mt-rainier.jpg')
    original_mt.show()
    reflected = reflect('images/mt-rainier.jpg')
    reflected.show()


if __name__ == '__main__':
    main()
