#given starting population (p0), growth rate(percent), change in popularion (aug) and target population,
#caluculate the number of years required for the population to surpass the target

###Attempt###
def nb_year(p0, percent, aug, p):
    year = 1
    pop = p0 + p0 * (percent / 100) + aug
    while pop < p:
        pop = pop + pop * (percent/100) + aug
        year += 1
    return year

print(nb_year(1000, 2, 50, 1200))

###Passed###

###Answer###
def nb_year(population, percent, aug, target):
    year = 0
    while population < target:
        population += population * percent / 100. + aug
        year += 1
    return year