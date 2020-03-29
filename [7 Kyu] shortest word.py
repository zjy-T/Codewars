#Simple, given a string of words, return the length of the shortest word(s).
#String will never be empty and you do not need to account for different data types.

def find_short(s):
    word = s.split() #split() splits a string into a list of words
    ans = min(word, key=len) #min() returns the the smallest word based on specified length "key=len"
    return len(ans)

s = "bitcoin take over the world maybe who knows perhaps"

print(find_short(s))