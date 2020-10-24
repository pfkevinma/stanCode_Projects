"""
Name: Pei-Feng (Kevin) Ma
File: caesar.py
------------------------------
This program demonstrates the idea of caesar cipher.
Users will be asked to input a number to produce shifted
ALPHABET as the cipher table. After that, any strings typed
in will be encrypted.
"""


# This constant shows the original order of alphabetic sequence
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def main():
    """
    This program will encrypt the ciphered code that input by user.
    1. getting the secret number
    2. encrypt the alphabet using secret number. Cut the old alphabet and reconnect it.
    3. loop through ciphered string find location of alphabet
    3. use the location to find word in normal alphabet
    """
    code = int(input('Secret number: '))
    new_alpha = ALPHABET[26-code:]+ALPHABET[:26-code]
    ciphered = str(input('What\'s the ciphered string? ')).upper()
    ans = ''
    for ch in ciphered:
        location = new_alpha.find(ch)
        if ch.isalpha():
            ans += ALPHABET[location]
        else:
            ans += ch
    print('The deciphered string is: '+str(ans))


#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
