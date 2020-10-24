"""
File: shrink.py
Name: Pei-Feng (Kevin) Ma
-------------------------------
Create a new "out" image half the width and height of the original.
Set pixels at x=0 1 2 3 in out , from x=0 2 4 6 in original,
and likewise in the y direction.
"""

from simpleimage import SimpleImage


def shrink(filename):
    """
    :param filename: str,
    :return img: SimpleImage
    using the concept of the checker board.
    select pixels we need and reorganize into a new image
    """
    img = SimpleImage(filename)
    after_shrink = SimpleImage.blank(img.width // 2, img.height // 2)
    for y in range(img.height):
        for x in range(img.width):
            p_org = img.get_pixel(x, y)
            if (x+y) % 2 == 0:
                if x % 2 == 0:
                    p_shrink = after_shrink.get_pixel(x//2, y//2)
                    p_shrink.red = p_org.red
                    p_shrink.green = p_org.green
                    p_shrink.blue = p_org.blue
                else:
                    p_shrink = after_shrink.get_pixel((x-1) // 2, (y-1) // 2)
                    p_shrink.red = p_org.red
                    p_shrink.green = p_org.green
                    p_shrink.blue = p_org.blue
    return after_shrink


def main():
    """
    This program will shrink the image into 1/2 original sizw.
    """
    original = SimpleImage("images/poppy.png")
    original.show()
    after_shrink = shrink("images/poppy.png")
    after_shrink.show()


if __name__ == '__main__':
    main()
