#Complete the function that accepts a string parameter, and reverses each word in the string.
#All spaces in the string should be retained.

def reverse_words(text):
    return " ".join(index[::-1] for index in text.split(" "))

text = 'double spaced words'

print(reverse_words(text))

###Failed###

###Answer###
def reverse_words(str):
    return ' '.join(s[::-1] for s in str.split(' ')) #split(" ") species the separator used