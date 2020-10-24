"""
Name: Pei-Feng (Kevin) Ma
File: hangman.py
-----------------------------
This program plays hangman game.
Users sees a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
to try in order to win this game.
"""

import random

# This constant controls the number of guess the player has
N_TURNS = 7


def main():
    """
    create a variable for the answer from random word
    create a variable for '-'
    create a variable for life
    create a variable for guess(input)
    we'll have a answer, an answer only show '-', life, and guess
    if the guess is correct, life won't change and the word show on str '-'.
    if wrong, life minus 1 and no word will be shown.
    Stop condition:
        if guess all the word before life == 0, win.
        if life reach 0, lose.
    """
    life = N_TURNS
    ans = random_word()
    dashed_ans = ''

    for i in range(len(ans)):
        dashed_ans += '-'

    # the loop will stop either life == 0 or ans being solved.
    while life > 0 and ans != dashed_ans:
        print('The word looks like: ' + str(dashed_ans))
        print('You have ' + str(life) + ' guesses left.')
        guess = str(input('Your guess: ')).upper()
        # Illegal format.
        while guess.isalpha() is not True or len(guess) > 1:
            print('Illegal format')
            guess = str(input('Your guess: ')).upper()
        # Wrong
        if ans.find(str(guess)) == -1:
            life -= 1
            print('There is no ' + str(guess) + '\'s in the word.')
            if life <= 0:
                print('You are completely hung : (\nThe word was: ' + str(ans))

        # Correct
        else:
            dashed_ans = show_answer(ans, dashed_ans, guess)
            if ans == dashed_ans:
                print('You win!!\nThe word was: ' + str(ans))


def show_answer(ans, s, guess):
    """
    this function will switch answer word on dash string.
    :param ans: str, answer word
    :param s: str, dash string
    :param guess: str, user guess word
    :return:
    """
    for i in range(len(ans)):
        if ans[i] == guess:
            s = s[:i] + guess + s[i + 1:]
    return s


def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()

