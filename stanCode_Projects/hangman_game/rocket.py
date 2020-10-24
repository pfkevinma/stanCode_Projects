"""
Name: Pei-Feng (Kevin) Ma
File: rocket.py
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
    """
    I am building a rocket in the console.
    The rocket is constructed by six separated parts with four different functions.
    The constant SIZE with control the size of the rocket.
    :return:
    """
    head(SIZE)
    belt(SIZE)
    upper(SIZE)
    lower(SIZE)
    belt(SIZE)
    head(SIZE)


def upper(n):
    '''
    both end contain '|'
    both end contain n-i-1 of '.'
    from left to right, each row always start with slash and follow with a backslash
    the width is 2 * i+1
    when j is even, its a slash
              odd, its a backslash
    :param n: int, SIZE
    :return: print out the 'upper'
    '''
    for i in range(n):
        print('|', end='')
        for j in range(n - i - 1):
            print('.', end='')
            
        for j in range((i + 1) * 2):
            if j % 2 == 0:
                print('/', end='')
            else:
                print('\\', end='')
        for j in range(n - i - 1):
            print('.', end='')
        print('|')


def lower(n):
    '''
    both end contain '|'
    both end contain i of '.'
    from left to right, each row always start with bachkslash and follow with a slasgh
    the width is 2 * n-i
    when j is even, its a backslash
              odd, its a slash
    :param n: int, SIZE
    :return: print out the 'lower'
    '''
    for i in range(n):
        print('|', end='')
        for j in range(i):
            print('.', end='')
        for j in range((n - i) * 2):
            if j % 2 == 0:
                print('\\', end='')
            else:
                print('/', end='')
        for j in range(i):
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
