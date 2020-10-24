"""
File: blur.py
Name: Pei-Feng (Kevin) Ma
-------------------------------
This file shows the original image first,
smiley-face.png, and then compare to its
blurred image. The blur algorithm uses the
average RGB values of a pixel's nearest neighbors
"""
from simpleimage import SimpleImage


def blur(img):
    """
    :param img: str
    :return: SimpleImage
    This function will blur the image by make pixels RGB value to the average value with nearby pixels.
    1. Create blank image
    2. loop the pixels original image
    3. loop the nearby pixels RGB value
    4. if the nearby pixel in the range of the picture, include into calculation.
    """
    img = img
    new_img = SimpleImage.blank(img.width, img.height)
    for x in range(img.width):
        for y in range(img.height):
            red = 0
            green = 0
            blue = 0
            num = 0
            for i in range(x-1, x+2):
                for j in range(y-1, y+2):
                    if img.width > i >= 0 and img.height > j >= 0:
                        pixel_img = img.get_pixel(i, j)
                        red += pixel_img.red
                        green += pixel_img.green
                        blue += pixel_img.blue
                        num += 1
            pixel_new = new_img.get_pixel(x, y)
            pixel_new.red = red // num
            pixel_new.green = green // num
            pixel_new.blue = blue // num
    return new_img


def main():
    """
    This program will the image 5 times blurrier.
    """
    old_img = SimpleImage("images/smiley-face.png")
    old_img.show()

    blurred_img = blur(old_img)
    for i in range(5):
        blurred_img = blur(blurred_img)

    blurred_img.show()


if __name__ == '__main__':
    main()
