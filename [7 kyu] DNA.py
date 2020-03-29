#In DNA strings, symbols "A" and "T" are complements of each other, as "C" and "G".
# You have function with one side of the DNA (string, except for Haskell); you need to get the other complementary side.
# DNA strand is never empty or there is no DNA at all (again, except for Haskell).

def DNA_strand(dna):
    ret = ""
    for amino in dna:
        if amino is "a":
            ret = ret + "t"
        elif amino is "t":
            ret = ret + "a"
        elif amino is "c":
            ret = ret + "g"
        elif amino is "g":
            ret = ret + "c"
    return ret

dna = "accggttac"

print(DNA_strand(dna))
