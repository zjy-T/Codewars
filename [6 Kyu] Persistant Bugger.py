# Write a function, persistence, that takes in a positive parameter num and returns its multiplicative persistence,
# which is the number of times you must multiply the digits in num until you reach a single digit.

def persistence(n):
    num_str = str(n)
    length = len(num_str)
    count = 0
    len_ans = 0
    while len(num_str) > 1:
        product = 1
        for digit in num_str:
            product *= int(digit)
        num_str = str(product)
        count += 1

    return count

n = 999
print(persistence(n))

### Failed ###

### Answer ###

def persistence(n):
    n = str(n)
    count = 0
    while len(n) > 1:
        p = 1
        for i in n:
            p *= int(i)
        n = str(p)
        count += 1
    return count