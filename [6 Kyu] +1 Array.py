# Given an array of integers of any length, return an array that has 1 added to the value represented by the array.
arr = []
def up_array(arr):
    if len(arr) == 0:
        return None
    for index in arr:
        if isinstance(index, int) == False:
            return None
        elif len(str(index)) > 1:
             return None
        elif index < 0:
            return None
    number = ""
    for i in arr:
        number += str(i)
    int_number = int(number) +1
    new_list = str(int_number)
    list = []
    for index in new_list:
        list.append(int(index))
    return list

print(up_array(arr))