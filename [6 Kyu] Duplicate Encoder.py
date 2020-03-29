# The goal of this exercise is to convert a string to a new string where each character in the new string is "("
# if that character appears only once in the original string, or ")" if that character appears more than once in the original string.
# Ignore capitalization when determining if a character is a duplicate.
word = "din"
def duplicate_encode(word):
    ret = ""
    for index in word.lower():
        count = (word.lower()).count(index)
        if count > 1:
            ret += ")"
        else:
            ret += "("
    return ret

print(duplicate_encode(word))

### Passed ###
