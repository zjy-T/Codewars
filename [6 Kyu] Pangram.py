#Given a string, detect whether or not it is a pangram. Return True if it is, False if not.
#Ignore numbers and punctuation.

import string

s = "The quick, brown fox jumps over the lazy dog!"

def is_pangram(s):
    sen = s.lower()
    sen1 = "".join(set(sen.replace(" ", "")))
    count = 0
    for index in sen1:
        if index in string.punctuation:
            count += 0
        elif index.isdigit() == True:
            count += 0
        elif index.lower() == "a":
            count += 1
        elif index.lower() == "b":
            count += 1
        elif index.lower() == "c":
            count += 1
        elif index.lower() == "d":
            count += 1
        elif index.lower() == "e":
            count += 1
        elif index.lower() == "f":
            count += 1
        elif index.lower() == "g":
            count += 1
        elif index.lower() == "h":
            count += 1
        elif index.lower() == "i":
            count += 1
        elif index.lower() == "j":
            count += 1
        elif index.lower() == "k":
            count += 1
        elif index.lower() == "l":
            count += 1
        elif index.lower() == "m":
            count += 1
        elif index.lower() == "n":
            count += 1
        elif index.lower() == "o":
            count += 1
        elif index.lower() == "p":
            count += 1
        elif index.lower() == "q":
            count += 1
        elif index.lower() == "r":
            count += 1
        elif index.lower() == "s":
            count += 1
        elif index.lower() == "t":
            count += 1
        elif index.lower() == "u":
            count += 1
        elif index.lower() == "v":
            count += 1
        elif index.lower() == "w":
            count += 1
        elif index.lower() == "x":
            count += 1
        elif index.lower() == "y":
            count += 1
        else:
            count += 1
    if count == 26:
        return True
    else:
        return False

print(is_pangram(s))

