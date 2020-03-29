#Create a function (or write a script in Shell) that takes an integer as an argument and returns
# "Even" for even numbers or "Odd" for odd numbers.

###Attempt###
def even_or_odd(number):
    if number % 2 == 0:
        return True
    else:
        return False

print(even_or_odd(3))

###Passed###

###Answer###
def even_or_odd(number):
    return 'Odd' if number % 2 else 'Even'
