#The first century spans from the year 1 up to and including the year 100,
# The second - from the year 101 up to and including the year 200, etc.
#Given a year, return the century it is in.

import math

def century(year):
    century = (year/100)
    return math.ceil(century) #math.ceil(num) will round num up

print(century(1705))

###Passed###