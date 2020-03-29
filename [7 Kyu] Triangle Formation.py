# Implement a method that accepts 3 integer values a, b, c.
# The method should return true if a triangle can be built with the sides of given length and false in any other case.

def is_triangle(a, b, c):
    if a >= b and a >= c:
        biggest = a
        small1 = b
        small2 = c
    elif b >= a and b >= c:
        biggest = b
        small1 = a
        small2 = c
    else:
        biggest = c
        small1 = a
        small2 = b

    if small1 + small2 > biggest:
        return True
    else:
        return False

print(is_triangle(1, 2, 2))