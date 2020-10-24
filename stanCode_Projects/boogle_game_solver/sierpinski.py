"""
File: sierpinski.py
Name: Pei-Feng (Kevin) Ma
---------------------------
This file recursively prints the Sierpinski triangle on GWindow.
The Sierpinski triangle is a fractal described in 1915 by Waclaw Sierpinski.
It is a self similar structure that occurs at different levels of iterations.
"""

from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GLine
from campy.gui.events.timer import pause

# Constants
ORDER = 6                 # Controls the order of Sierpinski Triangle
LENGTH = 600               # The length of order 1 Sierpinski Triangle
UPPER_LEFT_X = 150		   # The upper left x coordinate of order 1 Sierpinski Triangle
UPPER_LEFT_Y = 100         # The upper left y coordinate of order 1 Sierpinski Triangle
WINDOW_WIDTH = 950         # The width of the GWindow
WINDOW_HEIGHT = 700        # The height of the GWindow

# Global Variable
window = GWindow(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)  # The canvas to draw Sierpinski Triangle


def main():
	"""
	Print the Sierpinski triangle on GWindow recursively by calling sierpinski triangle function.
	"""
	sierpinski_triangle(ORDER, LENGTH, UPPER_LEFT_X, UPPER_LEFT_Y)


def sierpinski_triangle(order, length, upper_left_x, upper_left_y):
	"""
	:param order: int, control how many time will this function call itself recursively.
	:param length: int or float, control the length of each side of triangle.
	:param upper_left_x: int or float, control x coordinate where the triangle should placed.
	:param upper_left_y: int or float, control y coordinate where the triangle should placed.
	:return:
	"""
	# base case: stop when order reaches 0.
	if order == 0:
		return

	# recursive case
	else:
		pause(5)
		# draw current layer triangle.
		line_upper = GLine(upper_left_x, upper_left_y, upper_left_x+length, upper_left_y)
		line_left = GLine(upper_left_x, upper_left_y, upper_left_x+length*0.5, upper_left_y+length*0.886)
		line_right = GLine(upper_left_x+length, upper_left_y, upper_left_x+length*0.5, upper_left_y+length*0.886)
		window.add(line_upper)
		window.add(line_left)
		window.add(line_right)
		# draw upper left triangle in next the layer.
		sierpinski_triangle(order - 1, length / 2, upper_left_x, upper_left_y)
		# draw upper right triangle in the next layer.
		sierpinski_triangle(order - 1, length / 2, upper_left_x+length*0.5, upper_left_y)
		# draw lower triangle in the next layer
		sierpinski_triangle(order - 1, length / 2, upper_left_x+length*0.5*0.5, upper_left_y+length*0.886*0.5)


if __name__ == '__main__':
	main()