#You are given a list of arrays, the first number is positive and second number is negative
#find the sum between every array in the list

###Attempt###
def number(bus_stops):
    difference = 0
    count = 0
    for array in bus_stops:
        a = bus_stops[count]
        difference += a[0] - a[1]
        count += 1
    return difference


bus_stops = [[10, 0], [3, 5], [5, 8]]
print(number(bus_stops))

###Passed###

###Answer###
def number(bus_stops):
    return sum([stop[0] - stop[1] for stop in bus_stops])
