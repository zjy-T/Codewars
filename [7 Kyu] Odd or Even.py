#Given a list of numbers, determine whether the sum of its elements is odd or even.

def odd_or_even(arr):
    ret = 0
    for index in arr:
        ret += index
    if ret % 2 == 0:
        return "even"
    else:
        return "odd"

    ### Passed ###

    ### Answer ###
    def oddOrEven(arr):
        return 'even' if sum(arr) % 2 == 0 else 'odd'
