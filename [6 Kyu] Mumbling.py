def accum(s):
    ret = ""
    count = 1
    length = len(s)
    for index in s:
        if count == 1 and index.isupper() == True:
            ret += index + "-"
            count += 1
        elif count == 1 and index.isupper() == False:
            ret += index.upper() + "-"
            count += 1
        elif count < length and index.isupper() == True:
            ret += index + index.lower() * (count - 1) + "-"
            count += 1
        elif count < length and index.isupper() == False:
            ret += index.upper() + index.lower() * (count - 1) + "-"
            count += 1
        elif count == length and index.isupper() == True:
            ret += index + index.lower() * (count - 1)
        else:
            ret += index.upper() + index.lower() * (count - 1)
    return ret

s = "ZpglnRxqenU"

print(accum(s))

###Passed###

###Answer 1###
def accum(s):
    return '-'.join(c.upper() + c.lower() * i for i, c in enumerate(s))

###Answer 2###
def accum(s):
    i = 0
    result = ''
    for letter in s:
        result += letter.upper() + letter.lower() * i + '-'
        i += 1
    return result[:len(result)-1]
