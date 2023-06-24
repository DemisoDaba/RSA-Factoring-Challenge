#!/usr/bin/python3
def factorize(n):
    i = 3
    factors = []
    while n > 1:
        if n % i == 0:
            factors.append(i)
            n //= i
        else:
            i += 2
    return factors

n = 2388506527
factors = factorize(n)
print(f"{n}={'*'.join(map(str, factors))}")
