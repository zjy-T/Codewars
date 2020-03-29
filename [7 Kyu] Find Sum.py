#Upto and including n, this function will return the sum of all multiples of 3 and 5.

def find(n):
    count = 1
    list = []
    ret = 0
    while count <= n:
        list.append(count)
        count += 1
    for index in list:
        if index % 3 == 0 or index % 5 == 0:
            ret += index
    return ret

print(find(10))

### Passed ###

### Answer ###
def find(n):
    return sum(e for e in range(1, n+1) if e % 3 == 0 or e % 5 == 0)
