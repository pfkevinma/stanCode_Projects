"""
Name: Pei-Feng (Kevin) Ma
File: rocket_ext.py
-----------------------
This program should implement a console program
that draws ASCII art - a rocket.
The size of rocket is determined by a constant
defined as SIZE at top of the file.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""
SIZE = 6  # Control the scale of the rocket.


def main():
    head(SIZE)
    belt(SIZE)
    square(SIZE)
    belt(SIZE)
    head(SIZE)


def square(n):
    """
    This function will build upper and lower parts at the same time.
    In this function, we see it as a big square, a rectangle of width n and length 2n
    and see (i, j) as (x, y) coordinates.
    places that fits in to the if statement will print slash or back slash.
    others will print '.'
    :param n: str, SIZE
    :return:
    """
    for i in range(2 * n):
        print('|', end='')
        for j in range(2 * n):

            # determine where to put slash and backslash
            if (i < n and j < n and (i + j) >= (n - 1)) \
                    or (i < n and j >= n and (i + n) >= j) \
                    or (i >= n and j < n and i <= (j + n)) \
                    or (i >= n and j >= n and i + j < 3 * n):
                # places to put '/' and '\\' will be opposite when n is odd or even.
                if n % 2 == 0:
                    if (i + j) % 2 == 0:
                        print('\\', end='')
                    else:
                        print('/', end='')
                else:
                    if (i + j) % 2 == 0:
                        print('/', end='')
                    else:
                        print('\\', end='')
            else:
                print('.', end='')
        print('|')


def belt(n):
    """
    This function build the belt of the rocket. The belt contain one '+' on each side, and 2 * n of '='
    in the middle.
    1. create a blank string 'the_belt'
    2. add a '+' to the string
    3. create a for loop runs 2 * n times that print '='
    4. add a '+' to the string
    5. print out the_belt
    :param n:
    :return:
    """
    the_belt = ''
    the_belt += '+'
    for i in range(2*n):
        the_belt += '='
    the_belt += '+'
    print(the_belt)


def head(n):
    """
    This is the head of the rocket which is a triangle pointing north, with a base of 2 * n and height of n.
    The for loop i represent the height of the triangle, which is 'n'.
    The for loop j and y represent the blank in each row, which relates to i. when i increases, j and y decreases,
    therefore j and y should run 'n - i' times in each row.
    The for loop k and x represent the slash and backslash, which increase with i. However i start with zero,
    so range in k and x should run 'i + 1' times.
    :param n: int, size of the head.
    :return:
    """
    for i in range(n):
        for j in range(n - i):
            print(' ', end='')
        for j in range(i + 1):
            print('/', end='')
        for j in range(i + 1):
            print('\\', end='')
        for j in range(n - i):
            print(' ', end='')
        print('')


###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
    main()
