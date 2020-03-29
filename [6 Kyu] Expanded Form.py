# You will be given a number and you will need to return it as a string in Expanded Form.

def expanded_form(num):
    string = str(num)
    count = 1
    length = len(string)
    ret = ""
    #if string[-1] == "0":

    for index in string:
        if index == "0":
            count += 1
            length -= 1
        elif count < len(string):
            ret += str(int(index) * 10 ** (length - 1)) + " " + "+" + " "
            count += 1
            length -= 1
        else:
            ret += str(int(index) * 10 ** (length - 1))
            count += 1
            length -= 1
    if ret[-1] == " ":
        ret = ret[:-2]
    return ret


print(expanded_form(1010))