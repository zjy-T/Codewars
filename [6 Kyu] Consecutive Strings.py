# You are given an array strarr of strings and an integer k.
# Your task is to return the first longest string consisting of k consecutive strings taken in the array.

strarr = "zone", "abigail", "theta", "form", "libe", "zas", "theta", "abigail"
def longest_consec(strarr, k):
    sorted_string = sorted(list(set(strarr)), key=len)
    sorted_string.reverse()

    return "".join(sorted_string[0:k])

print(longest_consec(strarr, 2))

### Failed ###

### Answer ###

def longest_consec(strarr, k):
    result = ""

    if k > 0 and len(strarr) >= k:
        for index in range(len(strarr) - k + 1):
            s = ''.join(strarr[index:index + k])
            if len(s) > len(result):
                result = s

    return result

