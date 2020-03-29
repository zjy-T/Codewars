#It's pretty straightforward. Your goal is to create a function that removes the first and last characters of a string.
#You're given one parameter, the original string. You don't have to worry with strings with less than two characters.

def remove_char(s):
    return s[1:-1] #([0:] indicates the entire array, [1:] indicates from second to last index


s = "Tony"

print(remove_char(s))