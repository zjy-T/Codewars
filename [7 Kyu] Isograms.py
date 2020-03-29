# Implement a function that determines whether a string that contains only letters is an isogram.
# Assume the empty string is an isogram. Ignore letter case.

def is_isogram(string):
    if len(set(string.lower())) != len(string):
        return False
    else:
        return True

string = "HeLlo"

print(is_isogram(string))

### Passed ###

### Answer ###
def is_isogram(string):
    string = string.lower()
    for letter in string:
        if string.count(letter) > 1: return False
    return True
