"""
Name: Pei-Feng (Kevin) Ma
File: similarity.py
----------------------------
This program compares short dna sequence, s2,
with sub sequences of a long dna sequence, s1
The way of approaching this task is the same as
what people are doing in the bio industry.
"""


def main():
    """
    This program will compare the short sequence to sub sequence in the long sequence,
    and find out the sequence that has the highest match rate.
    1. user input long sequence DNA, a string.
    2. user input short sequence DNA, a string.
    3. make both string case insensitive
    4. create function to find out highest match rate sequence.

    ext:
    give top three matches
    give match percentage
    if same match rate, find out>.
    """
    long_sequence = str(input('Please give me a DNA sequence to search: '))
    short_sequence = str(input('What DNA sequence do you like to match: '))
    long_sequence = long_sequence.upper()
    short_sequence = short_sequence.upper()
    match(long_sequence, short_sequence)


def match(long_sequence, short_sequence):
    """
    This function will loop through the long sequence matching with short sequence.
    :param long_sequence: str,
    :param short_sequence: str,
    :return: str, sub sequence in long sequence that has highest match rate.
    """
    best_match = ''
    match_num = 0
    for i in range(len(long_sequence)-len(short_sequence)+1):
        s = long_sequence[i:i+len(short_sequence)]
        a = 0
        for j in range(len(short_sequence)):
            if s[j] == short_sequence[j]:
                a += 1
        if match_num <= a:
            match_num = a
            best_match = s
    match_rate = match_num / len(short_sequence) * 100
    print('The best match is: '+str(best_match))
    print('The match rate is: '+str(match_rate)+'%')



###### DO NOT EDIT CODE BELOW THIS LINE ######
if __name__ == '__main__':
    main()
