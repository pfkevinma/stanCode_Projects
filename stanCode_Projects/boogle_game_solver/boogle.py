"""
File: boggle.py
Name: Pei-Feng (Kevin) Ma
----------------------------------------
This program will find all the exist word in a 4*4 boogle game.
It allows user to input 4 words in 4 rows, and print out words that are
in the dictionary in the console.
"""
# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'

# global variables
dict_lst = []  # this list stores all the words in the dictionary.
results_lst = []  # this list stores all words in dictionary that we found.


def main():
    """
    This program allows user to input 4 words in 4 rows, and print out words that are
    in the dictionary in the console.
    """
    read_dictionary(FILE)

    word_lst = []  # this list contains all the alphabets the user inputs, from left to right, top to bottom.
    location_lst = []  # this list contains the location of the input alphabets with same sequence of word_lst.
    start = True  # this variable control if the recursive function could start by checking the input alphabet number
                    # is four.

    for i in range(4):
        s = input(f'{i + 1} row of letters: ')
        input_check = True  # this variable will check if the input format is correct.
        for j in range(len(s)):
            if j % 2 == 1 and s[j] != ' ':
                input_check = False
        if input_check:
            r = ''
            for ch in s:
                if ch.isalpha():
                    ch = ch.lower()
                    r += ch
                    word_lst.append(ch)
                else:
                    pass
            if len(r) != 4:
                print('Illegal input')
                start = False
                break
            for j in range(len(r)):
                location_lst.append((i, j))
        else:
            print('Illegal input')
            start = False
            break

    if start:
        find_word(location_lst, word_lst, '', [], [])
        print(f'There are {len(results_lst)} words in total.')


def find_word(location, word, current_word, found_index, current_location):
    """
    This function will find all the word in boogle game that exist in dictionary.
    :param location: list, user input alphabets location in 4*4 square.
    :param word: list, user input alphabets in 4*4 square.
    :param current_word: str, word that are searching in this layer.
    :param found_index: str, the alphabets index that were used in previous search
    :param current_location: str, the location of the alphabet that are searched in previous and current layer.
    :return:
    """

    # Base case
    if not has_prefix(current_word):
        return

    # recursive case
    else:
        # if a string match this statement means it is a new discover word that we want.
        if current_word in dict_lst and len(current_word) >= 4 and current_word not in results_lst:
            results_lst.append(current_word)
            print(f'Found \'{current_word}\'')

        # this for loop start searching from the top left corner.
        for i in range(len(location)):
            # if the alphabet has been used we will start the loop over to next one.
            if i in found_index:
                continue
            # this controls the next word we are search is connected to previous word.
            elif len(current_location) > 0:

                if location[i][0] > current_location[len(current_location) - 1][0] + 1 or \
                        location[i][0] < current_location[len(current_location) - 1][0] - 1:
                    continue
                if location[i][1] > current_location[len(current_location) - 1][1] + 1 or \
                        location[i][1] < current_location[len(current_location) - 1][1] - 1:
                    continue

            current_location.append(location[i])
            found_index.append(i)

            find_word(location, word, current_word+word[i], found_index, current_location)

            current_location.pop()
            found_index.pop()


def read_dictionary(filename):
    """
    This function reads file "dictionary.txt" stored in FILE
    and appends words in each line into a Python list.
    :param filename: a text file that contains dictionary
    """
    global dict_lst
    with open(filename, 'r') as f:
        for line in f:
            dict_lst += line.split()


def has_prefix(sub_s):
    """
    :param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
    :return: (bool) If there is any words with prefix stored in sub_s
    """
    for ele in dict_lst:
        if ele.startswith(sub_s):
            return True
    return False


if __name__ == '__main__':
    main()
