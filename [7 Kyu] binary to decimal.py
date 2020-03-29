#Given an array of ones and zeroes, convert the equivalent binary value to an integer.

def binary_array_to_number(arr):
    exp = len(arr) -1
    integer = 0
    for binary in arr:
        integer += binary * 2 ** exp
        exp -= 1
    return integer

arr = [0, 0, 0, 1]

print(binary_array_to_number(arr))
