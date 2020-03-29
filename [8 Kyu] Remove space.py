#Simple, remove the spaces from the string, then return the resultant string.

def no_space(x):
    space_removed = ""
    for index in x:
        if index != " ":
            space_removed += index
    return space_removed

x = '8 j 8   mBliB8g  imjB8B8  jl  B'

print(no_space(x))


####Answer####

def no_space(x):
    return x.replace(' ' ,'') #replace("replace this", "with this")