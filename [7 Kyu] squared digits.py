def squared_digits(num):
    ret = ""
    for index in str(num):
        ret += str(int(index)*int(index))
    return int(ret)

print(squared_digits(9119))