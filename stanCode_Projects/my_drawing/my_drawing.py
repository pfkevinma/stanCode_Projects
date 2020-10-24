"""
File: my_draw.py
Name: Pei-Feng (Kevin) Ma
----------------------
I recently watched tutorials about data science on Youtube, and learn a acronym called 'GIGO'.
When I was doing this assignment, the word just came across my mind with no reason.
So I decided to draw picture about it...
"""

from campy.graphics.gobjects import GOval, GRect, GLine, GLabel
from campy.graphics.gwindow import GWindow


def main():
    """
    """
    # create a window.
    window = GWindow(width=1000, height=700, title='work station')

    # draw the screen side of my laptop.
    top_case = GRect(300, 200, x=350, y=100)
    top_case.filled = True
    top_case.fill_color = 'black'
    window.add(top_case)

    screen = GRect(280, 175, x=360, y=110)
    screen.filled = True
    screen.fill_color = 'silver'
    window.add(screen)

    # drawing keyboard and trackpad side of my laptop.
    c__side_left = GLine(350, 300, 250, 460)
    window.add(c__side_left)
    c_side_right = GLine(650, 300, 750, 460)
    window.add(c_side_right)
    c_side_bottom = GLine(250, 460, 750, 460)
    window.add(c_side_bottom)

    keyboard_left = GLine(360, 310, 317, 380)
    window.add(keyboard_left)
    keyboard_right = GLine(640, 310, 682, 380)
    window.add(keyboard_right)
    keyboard_up = GLine(360, 310, 640, 310)
    window.add(keyboard_up)
    keyboard_down = GLine(317, 380, 682, 380)
    window.add(keyboard_down)

    keyboard = GRect(280, 70)
    keyboard.filled = True
    keyboard.fill_color = 'black'
    window.add(keyboard, 360, 310)

    # making my keyboard look like a garbage can :)
    for i in range(360, 640, 31):
        grid_verti = GLine(i, 310, i, 380)
        grid_verti.color = 'silver'
        window.add(grid_verti)

    for i in range(310, 380, 15):
        grid_hori = GLine(360, i, 640, i)
        grid_hori.color = 'silver'
        window.add(grid_hori)

    #  drawing track pad.
    pad_up = GLine(430, 390, 571, 390)
    pad_down = GLine(392, 450, 608, 450)
    pad_left = GLine(430, 390, 392, 450)
    pad_right = GLine(571, 390, 608, 450)
    window.add(pad_up)
    window.add(pad_down)
    window.add(pad_left)
    window.add(pad_right)

    # adding thickness to my laptop.
    edge_bottom = GRect(500, 10, x=250, y=460)
    edge_bottom.filled = True
    edge_bottom.fill_color = 'silver'
    window.add(edge_bottom)

    # put on mackbook pro logo.
    mbplogo = GLabel('MacBook Pro')
    mbplogo.font = '-10'
    mbplogo.color = 'silver'
    window.add(mbplogo, 465, 298)

    # create labels.
    GI = GLabel('Garbage In')
    GO = GLabel('Garbage Out')
    GI.font = '-50'
    GO.font = '-50'
    window.add(GI, 50, 320)
    window.add(GO, 700, 320)

    # draw 5 circles symbolize garbage
    Garbage_1 = GOval(20, 20)
    Garbage_1.filled = True
    Garbage_1.fill_color = 'red'
    window.add(Garbage_1, 320, 270)

    Garbage_2 = GOval(20, 20)
    Garbage_2.filled = True
    Garbage_2.fill_color = 'green'
    window.add(Garbage_2, 400, 320)

    Garbage_3 = GOval(20, 20)
    Garbage_3.filled = True
    Garbage_3.fill_color = 'blue'
    window.add(Garbage_3, 670, 270)

    Garbage_4 = GOval(20, 20)
    Garbage_4.filled = True
    Garbage_4.fill_color = 'yellow'
    window.add(Garbage_4, 585, 300)

    Garbage_5 = GOval(20, 20)
    Garbage_5.filled = True
    Garbage_5.fill_color = 'magenta'
    window.add(Garbage_5, 510, 340)


if __name__ == '__main__':
    main()
