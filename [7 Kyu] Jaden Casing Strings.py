#given a string, capitalize the first letter of each word

###Attempt###
def to_jaden_case(string):
    word = string.split()
    first = string[0:1]
    ret = ""
    for index in word:
        if index[0] == first:
            ret = ret + index.capitalize()
        else:
            ret = ret + " " + index.capitalize()
    return ret

string = "How can mirrors be real if our eyes aren't real"

print(to_jaden_case(string))

###Answer 1###
import string #imports the module "string"

def toJadenCase(NonJadenStrings):
    return string.capwords(NonJadenStrings)


###Answer 2###
def toJadenCase(string):
    return " ".join(w.capitalize() for w in string.split())