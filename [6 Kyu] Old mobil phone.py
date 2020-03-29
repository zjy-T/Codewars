# For this assignment, write a module that can calculate the amount of button presses required for any phrase.

def presses(phrase):
    dict = {
        "a": 1,
        "b": 2,
        "c": 3,
        "d": 1,
        "e": 2,
        "f": 3,
        "g": 1,
        "h": 2,
        "i": 3,
        "j": 1,
        "k": 2,
        "l": 3,
        "m": 1,
        "n": 2,
        "o": 3,
        "p": 1,
        "q": 2,
        "r": 3,
        "s": 4,
        "t": 1,
        "u": 2,
        "v": 3,
        "w": 1,
        "x": 2,
        "y": 3,
        "z": 4,
        "1": 1,
        "2": 4,
        "3": 4,
        "4": 4,
        "5": 4,
        "6": 4,
        "7": 5,
        "8": 4,
        "9": 5,
        "0": 2,
        " ": 1
    }

    count = 0
    for index in phrase.lower():
        count += dict[index]
    return count

print(presses("LOL"))

### Passed ###

### Answer ###
def presses(phrase):
    x = 0
    for letter in phrase:
        if letter.lower() in list('1*#adgjmptw '): x+= 1
        elif letter.lower() in list('0behknqux'): x+= 2
        elif letter.lower() in list('cfilorvy'): x+= 3
        elif letter.lower() in list('234568sz'): x+= 4
        elif letter.lower() in list('79'): x+= 5
    return x