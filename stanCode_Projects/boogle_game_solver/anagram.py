"""
File: anagram.py
Name: Pei-Feng (Kevin) Ma
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop

# Global variables
dict_lst = []  # this list stores all the words in the dictionary.
#found_anagrams_lst = []  # this list stores all the anagrams that we found.


def main():
    """
    This program allows user input words and it will find all the
    anagrams of it.
    """

    read_dictionary(FILE)

    print('Welcome to stanCode "Anagram Generator" (or -1 to quit)')
    s = input('Find anagrams for: ')
    if s != EXIT:
        print('searching...')
        find_anagrams(s)
        while True:
            s = input('Find anagrams for: ')
            if s != EXIT:
                print('searching...')
                find_anagrams(s)
            else:
                break


def read_dictionary(filename):
    """
    This function will read the dictionary file and store it in a
    list called dict_lst as a list data type.
    :param filename: a text file that contains dictionary
    """
    global dict_lst
    with open(filename, 'r') as f:
        for line in f:
            dict_lst += line.split()


def find_anagrams(s):
    """
    This function will call a helper function to find anagrams recursively.
    :param s: str, the word that user inputs.
    """
    find_anagrams_helper(s, '', [], [])


def find_anagrams_helper(s, current_word, found_index, found_anagrams_lst):
    """
    This function will find all the anagrams recursively and print it our at the
    console.
    :param found_anagrams_lst:
    :param s: string, the word that user inputs.
    :param current_word: string, a string that stores current word searching in current layer.
    :param found_index: list, a list that we been search in current and previous layer.
    """
    # Base Case. If the length of current word == len(s), check if it is the word exist in dictionary.
    if len(s) == len(current_word):
        if current_word in dict_lst and current_word not in found_anagrams_lst:
            found_anagrams_lst.append(current_word)
            print(current_word)
            print('searching...')
        else:
            print(f'{len(found_anagrams_lst)} anagrams: {found_anagrams_lst}')
            return
    # Recursive case
    else:
        if not has_prefix(current_word):
            return
        for i in range(len(s)):
            if i in found_index:
                continue
            else:
                found_index.append(i)
                find_anagrams_helper(s, current_word + s[i], found_index, found_anagrams_lst)
                found_index.pop()


def has_prefix(sub_s):
    """
    This function will search it a part of string matches with words in the dictionary.
    :param sub_s: str, a part of string which is the current word
    :return: boolean, tells if a sub string matches words in the dictionary.
    """
    for word in dict_lst:
        if word.startswith(sub_s):
            return True
    return False


if __name__ == '__main__':
    main()
