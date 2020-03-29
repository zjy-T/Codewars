#Your job is to return the middle character of the word. If the word's length is odd, return the middle character.
# If the word's length is even, return the middle 2 characters.

def get_middle(s):
    length = len(s)
    middle = int(length / 2)
    if length == 1 or length == 2:
        return s
    elif length % 2 == 0:
        return s[middle-1:middle+1]
    else:
        return s[middle]

s = "tests"

print(get_middle(s))

###Passed###

###Answer###
def get_middle(s):
    index, odd = divmod(len(s), 2) # divmod()
    return s[index] if odd else s[index - 1:index + 1]