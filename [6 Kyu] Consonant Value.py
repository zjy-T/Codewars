# Given a lowercase string that has alphabetic characters only and no spaces, return the highest value of consonant substrings.
s = "strength"
import re
def solve(s):

    dict = {
        "a": 1,
        "b": 2,
        "c": 3,
        "d": 4,
        "e": 5,
        "f": 6,
        "g": 7,
        "h": 8,
        "i": 9,
        "j": 10,
        "k": 11,
        "l": 12,
        "m": 13,
        "n": 14,
        "o": 15,
        "p": 16,
        "q": 17,
        "r": 18,
        "s": 19,
        "t": 20,
        "u": 21,
        "v": 22,
        "w": 23,
        "x": 24,
        "y": 25,
        "z": 26,
        " ": 0
    }
    s.lower()
    cons = ""
    ret = []
    sum = 0
    counter = 0
    for index in s:
        if index in "aeiou":
            cons += " "
        else:
            cons += index
    for m in cons:
        if m.isalpha() and counter < len(cons):
            sum += dict[m]
            counter += 1
        elif m.isspace() and counter < len(cons):
            ret.append(sum)
            sum = 0
            counter += 1
    ret.append(sum)
    maximum = max(ret)
    return maximum

print(solve(s))


### Passed ###

