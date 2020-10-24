"""
File: green_screen.py
Name: Pei-Feng (Kevin) Ma
-------------------------------
This file creates a new image that uses
MillenniumFalcon.png as background and
replace the green pixels in ReyGreenScreen.png
"""

from simpleimage import SimpleImage


def combine(background_img, figure_img):
    """
    :param background_img: str
    :param figure_img: str,
    :return: SimpleImage
    This function will find out the green screen area in the figure image,
    and replace it by background image.
    1. loop the pixel in figure image
    2. if the pixel matches the definition of a green screen, assign background image pixel.
    """
    back = background_img
    fig = figure_img

    for x in range(fig.width):
        for y in range(fig.height):
            pixel_fig = fig.get_pixel(x, y)
            pixel_back = back.get_pixel(x, y)

            bigger = max(pixel_fig.red, pixel_fig.blue)
            if pixel_fig.green <= 2 * bigger:
                pixel_back.red = pixel_fig.red
                pixel_back.green = pixel_fig.green
                pixel_back.blue = pixel_fig.blue
    return back


def main():
    """
    this program will put the background image into figure's green screen.
    """
    space_ship = SimpleImage("images/MillenniumFalcon.png")
    figure = SimpleImage("images/ReyGreenScreen.png")
    result = combine(space_ship, figure)
    result.show()


if __name__ == '__main__':
    main()
