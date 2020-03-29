#the returned string should only contain lowercase letters

def kebabize(string):
    ret = ''
    count = 0
    for index in string:
        if count == 0 and index.isalpha() and index.isupper:
            ret += index.lower()
            count += 1
        elif index.isupper():
            ret += "-" + index.lower()
        elif index.isdigit():
            pass
        else:
            ret += index
    return ret

string = '42'

print(kebabize(string))

### Passed ###

### Answer ###

def kebabize(string):
    result = ""

    for c in string:
        if c.isupper():
            if result is not "":
                result += "-{}".format(c.lower()) # .format() inserts the specified value or string in place of the placeholder
            else:
                result += c.lower()
        if c.islower():
            result += c

    return result
