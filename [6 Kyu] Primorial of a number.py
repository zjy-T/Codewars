# Is similar to factorial of a number, In primorial, not all the natural numbers get multiplied,
# only prime numbers are multiplied to calculate the primorial of a number. It's denoted with P#.

n=785
def num_primorial(count):
    primes = []
    ret = 1
    n = 2
    while len(primes) != count:
        for i in range(2, n // 2 + 1):
            if n % i == 0:
                break
        else:
            primes.append(n)
        n += 1
    for j in primes:
        ret *= j
    return ret

print(num_primorial(n))

### Passed ###
