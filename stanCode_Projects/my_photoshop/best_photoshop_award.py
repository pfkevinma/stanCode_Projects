"""
File: best_photoshop_award.py
Name: Pei-Feng (Kevin) Ma
----------------------------------
This file creates a photoshopped image
that is going to compete for the 2020 Best
Photoshop Award for SC101P.
Please put all the images you use in image_contest folder
and make sure to choose which award you are aiming at
"""
from simpleimage import SimpleImage


THRESHOLD = 1.17  # Controls the threshold of detecting green screen pixel.
BLACK_PIXEL = 120  # Controls the upper bound for black pixel.


def suit_up(figure, suit):
    """
    This program will use kevin's jacket as a green screen and replace it with astronaut suit.
    : param figure: SimpleImage, picture of Kevin
    : param suit: SimpleImage, picture of a spacesuit
    : return: SimpleImage, picture of Kevin in a spacesuit
    """
    for y in range(figure.height):
        for x in range(figure.width):
            pixel_fig = figure.get_pixel(x, y)
            if pixel_fig.blue > 0 and pixel_fig.red < 65 and pixel_fig.green < 65:
                if y > 1135:
                    pixel_suit = suit.get_pixel(x, y)
                    pixel_fig.red = pixel_suit.red
                    pixel_fig.blue = pixel_suit.blue
                    pixel_fig.green = pixel_suit.green

    return figure


def into_space(figure, background):
    """
    This program will put the background into the green screen and other redundant part of the image.
    : param figure: SimpleImage, picture of Kevin in a spacesuit
    : param background: SimpleImage, picture of the space
    : return: SimpleImage, picture of Kevin with a spacesuit in the space.
    """
    me = figure
    back = background
    for y in range(back.height):
        for x in range(back.width):
            pixel_me = me.get_pixel(x, y)
            avg = (pixel_me.red + pixel_me.blue + pixel_me.green) // 3
            total = pixel_me.red + pixel_me.blue + pixel_me.green
            pixel_bg = back.get_pixel(x, y)

            # put the background into the green screen.
            if pixel_me.green > avg * THRESHOLD and total > BLACK_PIXEL:
                pixel_me.red = pixel_bg.red
                pixel_me.blue = pixel_bg.blue
                pixel_me.green = pixel_bg.green

            # put the back ground into the gray part in the suit image.
            if y > 1135:  # we do not want to touch the head therefore set a range on height.
                if 50 > pixel_me.red and pixel_me.green and pixel_me.blue >= 0:
                    pixel_me.red = pixel_bg.red
                    pixel_me.blue = pixel_bg.blue
                    pixel_me.green = pixel_bg.green

            # remove the hands and let it blend into the space.
            if y > 2840:
                if pixel_me.red > avg * 1.1:
                    pixel_me.red = pixel_bg.red
                    pixel_me.blue = pixel_bg.blue
                    pixel_me.green = pixel_bg.green
    return me


def main():
    """
    Being a astronaut is a dream that lives in everyone's childhood, and now, it finally came true...
    This program will make Kevin a astronaut by combining three layers image into one.
    """
    figure = SimpleImage('image_contest/IMG_2267.jpeg')
    background = SimpleImage('image_contest/universe.jpeg')
    suit = SimpleImage('image_contest/space suit.jpeg')
    background.make_as_big_as(figure)
    suit.make_as_big_as(figure)

    dressed_up = suit_up(figure, suit)
    result = into_space(dressed_up, background)
    result.show()


if __name__ == '__main__':
    main()
