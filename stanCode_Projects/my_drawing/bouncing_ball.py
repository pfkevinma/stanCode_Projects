"""
File: bouncing_ball.py
Name: Name: Pei-Feng (Kevin) Ma
-------------------------
This program simulates a bouncing ball at (START_X, START_Y)
that has VX as x velocity and 0 as y velocity. Each bounce reduces
y velocity to REDUCE of itself.
"""

from campy.graphics.gobjects import GOval, GLabel
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

# Constants
VX = 5
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 100

# Global Variables
window = GWindow(800, 500, title='bouncing_ball.py') # This is the canvas.
count = 0  # This controls the time the ball bounce out of the window and repeat.
switch = 0  # This protect the animation affect from mouse clicks after animation started.
ball = GOval(10, 10)


def main():
    """
    """
    ball.filled = True
    ball.fill_color = 'black'
    window.add(ball, START_X - SIZE / 2, START_Y - SIZE / 2)
    onmouseclicked(start)


def start(event):
    """
    This function will start playing the bouncing ball animation 3 times after the first click
    and will not be interrupted until it finishes.
    I add a replay option as a extension at the end of the code.
    """
    global count, ball, switch

    # using a if statement and global variable "switch" to block other click when the function starts.
    if switch == 0:
        switch = 1
    # a bouncing ball formula V = V0+at
        vy = 0
        # the while loop controls repeat time of the animation.
        while count < 3:
            vy += GRAVITY
            ball.move(VX, vy)
            # this if statement will change th V0 when ball touches the ground.
            if ball.y >= window.height - SIZE/2:
                vy *= -0.9
            # this if statement will add the ball back to starting point after leaving the window.
            if ball.x > window.width:
                window.add(ball, START_X - SIZE / 2, START_Y - SIZE / 2)
                break
            pause(DELAY)
        # reset switch and count will achieve playing the animation by clicking it again.
        switch = 0
        count += 1


if __name__ == "__main__":
    main()
