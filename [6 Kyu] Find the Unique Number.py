#There is an array with some numbers. All numbers are equal except for one. Try to find it!

def find_uniq(arr):
    # Sort the array
    arr.sort()
    n = len(arr)

    # Check for first element
    if arr[0] != arr[1]:
        return arr[0]

        # Check for all the elements
    # if it is different its
    # adjacent elements
    for i in range(1, n - 1):
        if (arr[i] != arr[i + 1] and
                arr[i] != arr[i - 1]):
            return arr[i]

            # Check for the last element
    if arr[n - 2] != arr[n - 1]:
        return arr[n - 1]

arr = [ 1, 1, 1, 2, 1, 1 ]

print(find_uniq(arr))

###Passed###

###Answer###

def find_uniq(arr):
    s = set(arr) #sets takes a list and creates a new list consisting of only the unique digits eg. [1,1,1,2,1,1] = [1,2]
    for e in s:
        if arr.count(e) == 1: #checks to see which of the uniques appears only once
            return e
