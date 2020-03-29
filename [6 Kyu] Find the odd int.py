# Given an array, find the integer that appears an odd number of times.

# There will always be only one integer that appears an odd number of times.

def find_it(seq):
    for number in seq:
        holder = seq.count(number)
        if holder % 2 == 0:
            pass
        else:
            return number


seq = [1,1,2,-2,5,2,4,4,-1,-2,5]

print(find_it(seq))