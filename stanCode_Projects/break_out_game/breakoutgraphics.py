"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao
Filename: breakoutgraphics.py
Name: Pei-Feng (Kevin) Ma
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random


# Constants
BRICK_SPACING = 5  # Space between bricks (in pixels). This space is used for horizontal and vertical spacing.
BRICK_WIDTH = 40  # Height of a brick (in pixels).
BRICK_HEIGHT = 15  # Height of a brick (in pixels).
BRICK_ROWS = 10  # Number of rows of bricks.
BRICK_COLS = 10  # Number of columns of bricks.
BRICK_OFFSET = 50  # Vertical offset of the topmost brick from the window top (in pixels).
BALL_RADIUS = 10  # Radius of the ball (in pixels).
PADDLE_WIDTH = 100  # Width of the paddle (in pixels).
PADDLE_HEIGHT = 15  # Height of the paddle (in pixels).
PADDLE_OFFSET = 50  # Vertical offset of the paddle from the window bottom (in pixels).

INITIAL_Y_SPEED = 7.0  # Initial vertical speed for the ball.
MAX_X_SPEED = 5  # Maximum initial horizontal speed for the ball.


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH,
                 paddle_height=PADDLE_HEIGHT, paddle_offset=PADDLE_OFFSET,
                 brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS,
                 brick_width=BRICK_WIDTH, brick_height=BRICK_HEIGHT,
                 brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING,
                 title='Breakout', life=10):

        # Create a graphical window, with some extra space.
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing # 450
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing) # 635
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle.
        self.paddle = GRect(paddle_width, paddle_height)
        self.paddle.filled = True
        self.paddle.fill_color = 'black'
        self.window.add(self.paddle, (window_width - paddle_width) / 2, window_height - paddle_offset - paddle_height)

        # Center a filled ball in the graphical window.
        self.ball = GOval(ball_radius*2, ball_radius*2)
        self.ball.filled = True
        self.ball.fill_color = 'black'
        self.window.add(self.ball, window_width / 2, window_height / 2)

        # Default initial velocity for the ball.
        self.__dx = random.randint(1, MAX_X_SPEED)
        if random.random() > 0.5:
            self.__dx = - self.__dx
        self.__dy = INITIAL_Y_SPEED

        # Initialize our mouse listeners.
        onmouseclicked(self.start)
        onmousemoved(self.paddle_move)

        # switch protect game affected by mouse clicks after started.
        self.start1 = False

        # Total amount of bricks.
        self.bricks_num = brick_cols*brick_rows

        # Draw bricks.
        count = 0
        for j in range(brick_offset, brick_offset + brick_rows * (brick_height + brick_spacing),
                       brick_height + brick_spacing):
            count += 1
            for i in range(0, brick_cols * (brick_width + brick_spacing), brick_width + brick_spacing):
                self.bricks = GRect(brick_width, brick_height)
                self.bricks.filled = True
                if count <= 2:
                    self.bricks.fill_color = '#66CCFF'
                elif 2 < count <= 4:
                    self.bricks.fill_color = '#006699'
                elif 4 < count <= 6:
                    self.bricks.fill_color = '#006666'
                elif 6 < count <= 8:
                    self.bricks.fill_color = '#9999CC'
                else:
                    self.bricks.fill_color = '#333666'
                self.window.add(self.bricks, i, j)

        # Score board.
        self.num = 0
        self.score = GLabel('SCORE: '+str(self.num))
        self.score.font = '-20'
        self.window.add(self.score, 5, self.score.height+5)

        # life
        self.life = life
        self.label_life = GLabel('Life: ' + str(life))
        self.label_life.font = '-20'
        self.window.add(self.label_life, self.window.width - self.label_life.width - 5, self.label_life.height + 5)

    def start(self, event):
        """
        This method will change self.start from False to True, working as a switch controls the game will start
        after the first click.
        :param event: this variable stores mouse info.
        """
        self.start1 = True

    def paddle_move(self, event):
        """
        This method allows the paddle control by mouse movement. The paddle is only allowed to move side ways
        rather than up and down in the range of self.window.
        :param event: this variable stores mouse info.
        """
        if event.x - self.paddle.width / 2 > self.window.width - self.paddle.width / 2:
            self.paddle.x = self.window.width - self.paddle.width
        elif event.x - self.paddle.width / 2 < self.paddle.width / 2:
            self.paddle.x = 0
        else:
            self.paddle.x = event.x - self.paddle.width / 2

    def check_hit_wall(self):
        """
        This method will check if the ball hit the wall at top, left, or right,
        and make the ball bounce at opposite direction.
        """
        if 0 >= self.ball.x or self.ball.x + self.ball.width >= self.window.width:
            self.__dx = -self.__dx
        if 0 >= self.ball.y:
            self.__dy = -self.__dy

    def check_hit_object(self):
        """
        This method will check if the ball hits object other than wall, which might be bricks, the paddle, or nothing.
        By using coordinates of 4 corners around the ball.
        :return: object that hits by a ball or None
        """
        obj_1 = self.window.get_object_at(self.ball.x, self.ball.y)
        obj_2 = self.window.get_object_at(self.ball.x, self.ball.y + self.ball.width)
        obj_3 = self.window.get_object_at(self.ball.x + self.ball.width, self.ball.y)
        obj_4 = self.window.get_object_at(self.ball.x + self.ball.width, self.ball.y + self.ball.width)

        if obj_1 is None:
            if obj_2 is None:
                if obj_3 is None:
                    if obj_4 is None:
                        return None
                    else:
                        self.dif_object(obj_4)
                else:
                    self.dif_object(obj_3)
            else:
                self.dif_object(obj_2)
        else:
            self.dif_object(obj_1)

    def dif_object(self, obj):
        """
        This method will differentiate the object that pass method "check_hit_object".
        If the ball hits the paddle, it will bounce the opposite way of INITIAL_Y_SPEED.
        If the ball hits bricks, it will bounce away on y axis and remove the brick that hit by the ball.
        self.brick_num will - 1 to record how many bricks left.
        :param obj: object, it might be the paddle, brick or score board.
        """

        if obj is self.paddle:
            self.__dy = -INITIAL_Y_SPEED
        elif obj is self.score:
            pass
        elif obj is self.label_life:
            pass
        elif obj is not None:
            print(3)
            self.window.remove(obj)
            self.bricks_num -= 1
            self.__dy = -self.__dy
            self.score_plus()

    def score_plus(self):
        self.num += 1
        self.window.remove(self.score)
        self.score = GLabel('SCORE: '+str(self.num))
        self.score.font = '-20'
        self.window.add(self.score, 5, self.score.height + 5)

    def reset(self):
        """
        This method will reset the ball to it's initial position and assigning new speed,
        allows the game can start again after the ball get out of the window at bottom.
        """
        self.window.add(self.ball, self.window.width / 2, self.window.height / 2)
        self.start1 = False
        self.__dx = random.randint(1, MAX_X_SPEED)
        if random.random() > 0.5:
            self.__dx = - self.__dx
        self.__dy = INITIAL_Y_SPEED

        self.window.remove(self.label_life)
        self.life -= 1
        self.label_life = GLabel('Life: ' + str(self.life))
        self.label_life.font = '-20'
        self.window.add(self.label_life, self.window.width - self.label_life.width - 5, self.label_life.height + 5)

    def get_dx(self):
        """
        Getter of private variable self.__dx
        :return: int, speed of the ball on x axis.
        """
        return self.__dx

    def get_dy(self):
        """
        Getter of private variable self.__dy
        :return: int, speed of the ball on y axis.
        """
        return self.__dy

    def set_dx(self, new_dx):
        """
        Setter of private variable self.__dx
        :param new_dx: int, new speed of the ball on x axis.
        """
        self.__dx = new_dx

    def set_dy(self, new_dy):
        """
        Setter of private variable self.__dy
        :param new_dy: int, new speed of the ball on y axis.
        """
        self.__dy = new_dy




