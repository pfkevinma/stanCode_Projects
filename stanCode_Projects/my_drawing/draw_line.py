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

# Constants
SIZE = 5  # This is the diameter of the ball

# Global variables
window = GWindow(width=500, height=500, title='CLick and Draw')  # This is the canvas.
# create 2 global variables to record the location of the dot.
first_dot_x = 0  # create a x global variables to record the x location of the dot.
first_dot_y = 0  # create a y global variables to record the y location of the dot.


def main():
    """
    """
    onmouseclicked(draw_line)


def draw_line(event):
    """
    use a if/else statement to determine putting the dot or draw a line on window.
    :param event: every click on window.
    """
    global first_dot_x, first_dot_y

    if first_dot_x == 0 and first_dot_y == 0:
        dot = GOval(SIZE, SIZE)
        window.add(dot, event.x - SIZE / 2, event.y - SIZE / 2)
        first_dot_x = event.x
        first_dot_y = event.y

    else:
        window.remove(window.get_object_at(first_dot_x, first_dot_y))
        line = GLine(first_dot_x, first_dot_y, event.x, event.y)
        window.add(line)
        first_dot_x = 0
        first_dot_y = 0


if __name__ == "__main__":
    main()
