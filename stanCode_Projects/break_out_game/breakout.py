"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao

Filename: breakout.py
Name: Pei-Feng (Kevin) Ma
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics
from campy.graphics.gobjects import GOval, GRect, GLabel


# Constants
FRAME_RATE = 1000 / 500  # 120 frames per second.
NUM_LIVES = 5  # how many times can the ball get out of window at bottom.


def main():
    graphics = BreakoutGraphics()
    graphics.life = NUM_LIVES
    for i in range(NUM_LIVES):
        # How many live does the player have.
        while True:  # switch that control game start after a click.
            if graphics.start1:
                graphics.ball.move(graphics.get_dx(), graphics.get_dy())
                graphics.check_hit_wall()
                graphics.check_hit_object()
                if graphics.ball.y >= graphics.window.height:
                    # ball fall off the bottom.
                    graphics.reset()
                    break
                elif graphics.bricks_num == 0:
                    # clear all the bricks!
                    graphics.window.remove(graphics.ball)
                    break
            pause(FRAME_RATE)
    # Game Over
    gameover = GLabel('GAME OVER!')
    gameover.font = 'Garamond-60'
    gameover.color = 'magenta'
    graphics.window.add(gameover, (graphics.window.width-gameover.width)/2, graphics.window.height/2)

if __name__ == '__main__':
    main()
