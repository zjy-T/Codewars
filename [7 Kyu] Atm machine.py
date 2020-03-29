#ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot contain anything but exactly 4 digits or exactly 6 digits.
#If the function is passed a valid PIN string, return true, else return false.

###Attempt###
def validate_pin(pin):
    length = len(pin)
    if length < 4 or length == 5 or length > 6:
        return False #return can be used to return a boolean
    else:
        return pin.isdigit() #isdigit() checks a string to see if all index are digits and returns a boolean
print(validate_pin("a234"))

###Gave Up###

###Answer###
def validate_pin(pin):
    return len(pin) in (4, 6) and pin.isdigit()