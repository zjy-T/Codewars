#Your task is to create a function that does four basic mathematical operations.
#The function should take three arguments - operation(string/char), value1(number), value2(number).
#The function should return result of numbers after applying the chosen operation.

def basic_op(operator, value1, value2):
    ans = int()
    if operator == "+":
        ans = int(value1) + int(value2)
    elif operator == "-":
        ans = int(value1) - int(value2)
    elif operator == "*":
        ans = int(value1) * int(value2)
    elif operator == "/":
        ans = int(value1) / int(value2)
    return ans

print(basic_op("+", "1", "2"))
