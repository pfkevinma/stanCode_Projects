"""
File: draw_line.py
Name: Pei-Feng (Kevin) Ma
-------------------------
This program creates lines on an instance of GWindow class.
There is a circle indicating the user’s first click. A line appears
at the condition where the circle disappears as the user clicks
on the canvas for the second time.
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked

SIZE = 5
window = GWindow(width=500, height=500, title='CLick and Draw')

dot = GOval(SIZE, SIZE)
count = 0


def main():
    onmouseclicked(dot_and_line)


def dot_and_line(event):
    """
    use a if/else statement to determine putting the dot or draw a line on window.
    this extension use lesser code than the other solution, by using a global variables
    'count'.
    """
    global dot, count
    if count % 2 == 0:
        count += 1
        window.add(dot, event.x-SIZE/2, event.y-SIZE/2)
    else:
        count += 1
        window.add(GLine(dot.x, dot.y, event.x, event.y))
        window.remove(dot)


if __name__ == "__main__":
    main()



