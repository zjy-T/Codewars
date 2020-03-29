#Consider an array/list of sheep where some sheep may be missing from their place.
#We need a function that counts the number of sheep present in the array (true means present).

###Attempt###
def count_sheeps(sheep):
    count = 0
    for number in sheep:
        if number == True:
            count += 1
    return count

sheep = [True,  True,  True,  False,
          True,  True,  True,  True ,
          True,  False, True,  False,
          True,  False, False, True ,
          True,  True,  True,  True ,
          False, False, True,  True ]

print(count_sheeps(sheep))

###Passed###

###Answer###
def count_sheeps(arrayOfSheeps):
  return arrayOfSheeps.count(True)
