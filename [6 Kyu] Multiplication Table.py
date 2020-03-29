# Create a function that accepts dimensions, of Rows x Columns, as parameters in order to create a multiplication table sized according to the given dimensions.
# **The return value of the function must be an array, and the numbers must be Fixnums, NOT strings.

def multiplication_table(row,col):
    row_list = list(range(1,row+1))
    placeholder = int(row_list[-1])
    col_count = 1
    current_list =[]

    while col_count < col:
        current_list = list(range((placeholder + 1), (placeholder + 1 + row)))
        placeholder = current_list[-1]
        row_list.append(current_list)
        col_count += 1


    return row_list

print(multiplication_table(3,3))
