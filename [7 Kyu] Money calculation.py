def calculate_years(principal, interest, tax, desired):
    year = 0
    while principal < desired:
        principal = principal + principal * interest - principal * interest * tax
        year += 1
    return year

print(calculate_years(1000, 0.05, 0.18, 1100))

###Passed###

